import requests

def getSharedSecret():
    secret = '1efdb9136482acd5b02962e2dcf040887269f0953bb5db7351ef6abe794ff293'
    return secret

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
    return sha1GenString, apiCallString

def joinMeetingStringGen():
    userName = inputReturn('User Name')
    global joinApiSha1String
    global joinApiJoinLink
    joinApiSha1String = 'joinmeetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName + getSharedSecret()
    joinApiJoinSring = 'join?meetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName
    joinApiJoinLink = sha1LinkMaker(joinApiSha1String, joinApiJoinSring)


def sha1LinkMaker(sha1link, apilink):
    from hashlib import sha1
    m = sha1(sha1link.encode('utf-8'))
    global checksumString
    checksumString = m.hexdigest()
    sha1_link = apilink + '&checksum=' + checksumString
    return sha1_link

def serverSelecter():
    print('Enter the Server-Number: \n 1: bbb1 \n 2: bbb2 \n 3: bbb3 \n 4: meet')
    global serverLink
    while True:
        serverNumber = input()
        if serverNumber == '1':
            serverLink = 'https://bbb1.proftaak.duckdns.org/bigbluebutton/api/'
            break
        elif serverNumber == '2':
            serverLink = 'https://bbb2.proftaak.duckdns.org/bigbluebutton/api/'
            break
        elif serverNumber == '3':
            serverLink = 'https://bbb3.proftaak.duckdns.org/bigbluebutton/api/'
            break
        elif serverNumber == '4':
            serverLink = 'https://meet.proftaak.duckdns.org/bigbluebutton/api/'
            break
        else:
            print('Enter a correct number.')
            print('Enter the Server-Number: \n 1: bbb1 \n 2: bbb2 \n 3: bbb3')
    return serverLink

def createMeetingLink():
    apiLink = str(serverLink) + str(sha1LinkMaker(sha1GenString, apiCallString))
    return apiLink


def createJoinLink():
    joinUrl = serverLink + joinApiJoinLink
    return joinUrl

def createStrings():
    serverSelecter()
    createMeetingStringGenerator()
    joinMeetingStringGen()




createStrings()
print(createMeetingLink())
print(createJoinLink())