# API Controller BBB - Python
Mijn BBB servers hebben allemaal een ingebouwde API. Deze api kan je gebruiken om meetings te maken, verwijderen, monitoren en joinen. 

De API heeft meerdere veiligheids maatreleen waarmee je moet rekeninghouden.

## Code
De code is opgebouwd in 20 functies. Alle functies hebben een unieke functie. 
Een funcitie die altijd word gebruikt is de Sha1 code generator. Deze is nodig om een valide call te doen naar de API.

```Python
def sha1LinkMaker(sha1link):
    from hashlib import sha1
    m = sha1(sha1link.encode('utf-8'))
    global checksumString
    checksumString = m.hexdigest()
    return checksumString
```
Om deze funtie re gebruiken heb je een ``sha1link`` nodig. Deze moet je genereren met een Secret key. Deze moet je veilig bewaren en NIET in je code zetten.
Deze ``sha1link`` kan je generen als je weet wat je wilt doen:

```Python
def joinMeetingStringGenerator():
    userName = inputReturn('User Name')
    joinApiSha1String = 'joinmeetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName + getSharedSecret()
    joinApiJoinSring = 'join?meetingID=' + meetingId + '&password=' + atendeePass + '&fullName=' + userName
    joinApiJoinLink = joinApiJoinSring + '&checksum=' + sha1LinkMaker(joinApiSha1String)
    return joinApiJoinLink
```
Hier kan je zien dat de sha1LinkMaker functie word aangeroepen met ``joinApiSha1String`` als variabele. Deze string word dus gebruikt om een Checksum te krijgen. Deze Checksum moet je dan aan het einde van de API Call zetten: ``&checksum=`` 

Met de combinatie van de 20 functies kan je bijna alles doen wat je met de BBB meetings te doen valt.

Deze lijst krijg je op het begin te zien:
```
Choose a function:
1: Create a Join and Session link.
2: Get list of all recordings.
3: Get a list of all ongoing calls.
4: Generate random meetings.
5: End all ongoing meetings.
6: Get all meetings per Server.
```
