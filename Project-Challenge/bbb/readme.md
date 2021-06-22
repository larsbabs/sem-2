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
Om deze funtie re gebruiken heb je een ``sha1link`` nodig
