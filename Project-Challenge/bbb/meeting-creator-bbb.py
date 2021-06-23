import requests
import xml.etree.ElementTree as ET
import random
import string
import configparser

serverList = ['https://bbb1.proftaak.duckdns.org/bigbluebutton/api/', 'https://bbb2.proftaak.duckdns.org/bigbluebutton/api/', 'https://bbb3.proftaak.duckdns.org/bigbluebutton/api/', 'https://meet.proftaak.duckdns.org/bigbluebutton/api/']

def getSharedSecret():
    config = configparser.ConfigParser()
    config.read(r'C:\Users\larsi\OneDrive\bbb key\config.ini')
    secret = config['secret']['key']
    return secret
# Het lezen van de config file voor de MySQL database
def config_read():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    return config
def inputReturn(item):
    print("Enter here your: ", item)
    userInput = input()
    return userInput

def createMeetingStringGenerator():
    global meetingName
    global meetingId
    global modPassword
    global atendeePass
    meetingName = inputReturn('Meeting name')
    meetingId = inputReturn('Meeting Id')
    sharedSecret = getSharedSecret()
    modPassword = inputReturn('Moderator Password')
    atendeePass = inputReturn('Attendee Password')

    global sha1GenString
    global apiCallString

    sha1GenString = 'createname=' + meetingName + '&meetingID=' + meetingId + '&attendeePW=' + atendeePass + '&moderatorPW=' + modPassword + sharedSecret
    apiCallString = 'create?name=' + meetingName + '&meetingID=' + meetingId + '&attendeePW=' + atendeePass + '&moderatorPW=' + modPassword
    
    apiLink = apiCallString + "&checksum=" + sha1LinkMaker(sha1GenString)
    return apiLink

def joinMeetingStringGenerator():
    userName = inputReturn('User Name')
    joinApiSha1String = 'joinmeetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName + getSharedSecret()
    joinApiJoinSring = 'join?meetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName
    joinApiJoinLink = joinApiJoinSring + '&checksum=' + sha1LinkMaker(joinApiSha1String)
    return joinApiJoinLink

def getMeetings():
    sha1Link = 'getMeetings' + getSharedSecret()
    apiLink = 'getMeetings'
    fullLink = apiLink + "?checksum=" + sha1LinkMaker(sha1Link)
    httpLink = createJoinLink(serverStringGlobal, fullLink)
    data = requests.get(httpLink)
    root = ET.fromstring(data.text)
    if data.text.find("noMeetings") != -1:
        return "There are curently no active meetings"
    else:
        count = 0
        id_list = []
        while True:
            id_list.append(root[1][count][1].text)
            count += 1
            if count == len(root[1]):
                break
        return id_list

def getMeetingsPerServer():
    sha1Link = 'getMeetings' + getSharedSecret()
    apiLink = 'getMeetings'
    fullLink = apiLink + "?checksum=" + sha1LinkMaker(sha1Link)
    count = 0
    coolList = []
    print('Getting meetings......\n')
    while True:
        httpLink = serverList[count] + fullLink
        data = requests.get(httpLink)
        root = ET.fromstring(data.text)
        if data.text.find("noMeetings") != -1:
            coolList.append([serverList[count], 0])
        else:
            lenght = len(root[1])
            coolList.append([serverList[count], lenght])
        count += 1
        if count == len(serverList):
            break
    return coolList


def getMeetingPassword():
    sha1Link = 'getMeetings' + getSharedSecret()
    apiLink = 'getMeetings'
    fullLink = apiLink + "?checksum=" + sha1LinkMaker(sha1Link)
    httpLink = createJoinLink(serverStringGlobal, fullLink)
    data = requests.get(httpLink)
    root = ET.fromstring(data.text)
    if data.text.find("noMeetings") != -1:
        return "There are curently no active meetings"
    else:
        count = 0
        password_list = []
        while True:
            password_list.append(root[1][count][8].text)
            count += 1
            if count == len(root[1]):
                break
        return password_list

def getRecordings():
    sha1Link = 'getRecordings' + getSharedSecret()
    apiLink = 'getRecordings'
    fullLink = apiLink + '?checksum=' + sha1LinkMaker(sha1Link)
    return fullLink

def getVideoLinkRecording():
    data = requests.get(createJoinLink(serverSelecter(), getRecordings()))
    root = ET.fromstring(data.text)
    count = 0
    linkList = []
    while True:
        linkList.append(root[1][count][13][0][1].text)
        count += 1
        if count == len(root[1]):
            break
    return linkList

## Sha1 Generator ##
def sha1LinkMaker(sha1link):
    from hashlib import sha1
    m = sha1(sha1link.encode('utf-8'))
    global checksumString
    checksumString = m.hexdigest()
    return checksumString

def serverSelecter():
    print(serverListPrinter())
    global serverStringGlobal
    count = 0
    while True:
        count += 1
        serverNumber = input()
        if serverNumber.isnumeric() and (int(serverNumber) >= 0 and int(serverNumber) <= len(serverList)):
            serverStringGlobal = serverList[int(serverNumber) - 1]
            break
        else:
            print('Enter a correct number.')
            print(serverListPrinter())
            count = 1
    return serverStringGlobal

def serverListPrinter():
    count = 0
    initial = "Enter the Server-Number: "
    while True:
        initial += "\n " + (str(count + 1)) + ": " + serverList[count]
        count += 1
        if count == len(serverList):
            break
    return initial

def createMeetingLink():
    apiLink = str(serverSelecter()) + str(sha1LinkMaker(sha1GenString, apiCallString))
    return apiLink


def createJoinLink(serverUrl, apiLink):
    joinUrl = serverUrl + apiLink
    return joinUrl

def randomMeetingGenerator(adminPassRandom, attendeePassRandom, amount):
    letters = string.ascii_lowercase
    numbers = string.digits
    server = serverSelecter()
    count = 0
    print("Creating Meetings, this can take a while....")
    while True:
        meetingNameRandom = ''.join(random.choice(letters) for i in range(10))
        meetingIdRandom = ''.join(random.choice(numbers) for i in range(10))
        sha1link = sha1LinkMaker(('createname=' + meetingNameRandom + '&meetingID=' + meetingIdRandom + '&attendeePW=' + attendeePassRandom + '&moderatorPW=' + adminPassRandom + getSharedSecret()))
        callLink = server + 'create?name=' + meetingNameRandom + '&meetingID=' + meetingIdRandom + '&attendeePW=' + attendeePassRandom + '&moderatorPW=' + adminPassRandom + '&checksum=' + sha1link
        requests.get(callLink).text
        count += 1
        print("Created Meeting: ", count, ' Meeting Id: ', meetingNameRandom)
        if count == amount:
            break


def endAllMeetings():
    server = serverSelecter()
    meetingList = getMeetings()
    password = getMeetingPassword()
    count = 0
    if meetingList == "There are curently no active meetings":
        return meetingList
    else:
        while True:
            checksum = sha1LinkMaker(('endmeetingID=' + meetingList[count] + '&password=' + password[count] + getSharedSecret()))
            callLink = server + 'end?meetingID=' + meetingList[count] + '&password=' + password[count] + '&checksum=' + checksum
            requests.get(callLink).text
            print('Ended meeting with meeting id: ', meetingList[count])
            count += 1
            if count == len(meetingList):
                break
    return  "The meetings have been terminated"


def createStrings():
    serverSelecter()
    createMeetingStringGenerator()
    joinMeetingStringGenerator()

def ask_user(question):
    check = str(input(question)).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
            return ask_user()
    except Exception as error:
        print("Please enter valid inputs")
        print(error)
        return ask_user()


def choice():
    userInput = input(
"""
Choose a function: 
1: Create a Join and Session link.
2: Get list of all recordings.
3: Get a list of all ongoing calls.
4: Generate random meetings.
5: End all ongoing meetings.
6: Get all meetings per Server.
"""
                    )
    if userInput == "1":
        print(chr(27) + "[2J")
        link = createJoinLink(serverSelecter(), createMeetingStringGenerator())
        if ask_user("Do you want the generate the meetings automatically?(y/n)\n"):
            print("Join Link: " + serverStringGlobal + joinMeetingStringGenerator())
            print(requests.get(link))
        else:
            print("Join Link: " + serverStringGlobal + joinMeetingStringGenerator())
            print("Create Link: " + link)
    elif userInput == '2':
        print(chr(27) + "[2J")
        print(createJoinLink(serverSelecter(), getRecordings()))
    elif userInput == '3':
        print(chr(27) + "[2J")
        serverSelecter()
        meetings = getMeetings()
        if isinstance(meetings, list):
            print("List of running Meeting ID's:" , *meetings, sep = "\n")
        else:
            print(meetings)
    elif userInput == '4':
        adminPassword = input("Enter the Admin-Password for the meetings:\n")
        userPassword = input("Enter the Attendee-Password for the meetings:\n")
        while True:
            amount = input("Enter the amount of meetings you want to generate:\n")
            try:
                val = int(amount)
                break
            except ValueError:
                print("That's not an valid input")
        if int(amount) <= 51:
            randomMeetingGenerator(adminPassword, userPassword, int(amount))
        else:
            print('The amount must be lower or equal to 50')
    elif userInput == '5':
        print(endAllMeetings())
    elif userInput == '6':
        count = 0
        meetingsList = getMeetingsPerServer()
        while True:
            print('Server: ' + meetingsList[count][0] + '\nMeetings: ' + str(meetingsList[count][1]) + '\n')
            count += 1
            if count == len(meetingsList):
                break
    else:
        print(chr(27) + "[2J")
        print("Enter a valid input:")
        choice()


choice()
