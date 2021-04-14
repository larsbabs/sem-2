
s = input("Vul hier uw wachtwoord in om te laten controlleren: ")
lengte_rating = ""
others_rating = ""
numbers_rating = ""
rating = ""
numbers = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - numbers - letters - spaces
lengte = len(s) - spaces
#print("Er zitten: " + str(numbers) + " nummers in uw wachtwoord.")
#print("Er zitten: " + str(letters) + " letters in uw wachtwoord.")
#print("Er zitten: " + str(spaces) + " spaties in uw wachtwoord.")
#print("Er zitten: " + str(others) + " tekens in uw wachtwoord.")
#print("Er zitten: " + str(lengte) + " babs in uw wachtwoord.")
"babs"


def lengte_calc(lengte):
    len_rate = 0
    if lengte < 6:
        len_rate += 1
    elif 6 <= lengte <= 10:
        len_rate += 7
    else:
        len_rate += 15
    return len_rate
def others_calc(others):
    oth_rate = 0
    if others == 0:
        oth_rate += 0
    elif 1 <= others <= 3:
        oth_rate += 6
    else:
        oth_rate += 10
    return oth_rate

def numbers_calc(numbers):
    num_rate = 0
    if numbers == 0:
        num_rate += 0
    elif 1 <= numbers <= 3:
        num_rate += 5
    else:
        num_rate += 10
    return num_rate


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
#print("De lengte van uw wachtwoord is: " + lengte_calc(lengte))
#print("De lengte van uw wachtwoord is: " + numbers_calc(numbers))
#print("De lengte van uw wachtwoord is: " + others_calc(others))



rate_number = lengte_calc(lengte) + others_calc(others) + numbers_calc(numbers)
print(rate_number)
print(rating_system(rate_number)) 