# Python-Password-Generator
Een simpele wachtwoord generator in Python

Met deze Generator kan in in Python een wachtwoord genereren!

Je hebt 3 verschillende keuzes:
- letters
- cijfers
- tekens

## Hoe het werkt:

Je vult als eerst de gewenste lengte van het wachtwoord in.
Hierbij heb ik een while loop gemaakt zodat het programma niet crached als je ipv een nummer bijvoorbeeld letters invult.

De loop is erg makkelijk. Ik ben begonnen met een eindelose loop waar je uiteindelijk uitgaat met **break**. Dan kijkt hij met een if statement of wat je invult een digit/int is, zo ja: ga verder.
Als het geen cijfer is geeft hij een uitleg en begind de loop opnieuw.
```Python
    while True:
        print("Vul hier de lengte van uw wachtwoord in ("+ str(min_length) + " tot" , str(max_length) + "):")
        pass_lenght_str = input()
        
        if pass_lenght_str.strip().isdigit():
            pass_length = int(pass_lenght_str)
            
            if pass_length > max_length:
                print("Het moeten tussen", str(min_length), " en", str(max_length), "tekens zijn!")
                
            elif pass_length < min_length:
                print("Het moeten tussen", str(min_length), " en", str(max_length), "tekens zijn!")
                
            else: break
            
        else:
            print("Het MOET een nummer zijn!")
```
Ook zie je dat er een minimale en een maximale lengte is. Deze 2 veriabelen zijn makkelijk aan te passen bovenaan de code. Als je die 2 aanpast veranderd het overal in de code.

Nadat je een juiste lengte hebt ingevoert vraagt de code of je nummers en/of tekens erin wilt hebben:
Cijfers voorbeeld:
```Python
    while True:
        numbers = input("Wilt u cijfers in uw wachtwoord? (y/n): ")
        if numbers.strip().isdigit():
            print("Het moet y/n zijn en geen cijfer")
        elif numbers != "y" and numbers != "n":
            print("Het moet y/n zijn!")
        else: break
```
Hier gebruik ik weer een oneindige loop om te voorkomen dat het crasht.

Als laatst kijk ik in wat if statements wat de gebruiker allemaal heeft ingevult en genereer dan het wachtwoord met de random library:

2 voorbeelden van de 4 statements:
```Python
    if numbers == "y" and tekens == "y":
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)
    if numbers == "n" and tekens == "n":
        characters = string.ascii_letters
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)
```
