# Password checker
een programma waar je je wachtwoord kunt invullen en dan kijkt of het veilig genoeg is.

## Wat het doet:
Je vult je wachtwoord in. Daarna telt de code hoeveel tekens, nummers en bijzondere tekens erin zitten. Ook kijkt hij hoe lang je wachtwoord is:
```
numbers = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - numbers - letters - spaces
lengte = len(s) - spaces
```

Dan komen er een aantal funcies. Elke functie heeft als opdracht om aan het aantal tekens een score toe te voegen. Hier is een voorbeeld van de bijzondere letters:
```
def others_calc(others):
    oth_rate = 0
    if others == 0:
        oth_rate += 0
    elif 1 <= others <= 3:
        oth_rate += 6
    else:
        oth_rate += 10
    return oth_rate
```
hij kijkt hoeveel erin zitten en geeft daarmee een score.

Dan krijg je nog de laatste funcie die de uitijndelijke score berekend:
```
def rating_system(rate_number):
    if rate_number < 3:
        rating = "Supper Slecht"
    elif rate_number >= 30:
        rating = "Onbreekbaar"
    elif 20 <= rate_number <= 30:
        rating = "Goed"
    elif 4 <= rate_number <= 10:
        rating = "Erg matig"
    elif 11 <=rate_number <= 19:
        rating = "goed zat"
    return rating
```
