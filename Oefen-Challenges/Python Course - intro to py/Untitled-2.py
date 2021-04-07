print("Vul hier uw wachtwoord in om te laten controlleren:")
s = input()

numbers = sum(c.isdigit() for c in s)
letters = sum(c.isalpha() for c in s)
spaces  = sum(c.isspace() for c in s)
others  = len(s) - numbers - letters - spaces

print("Er zitten: " + str(numbers) + " nummers in uw wachtwoord.")
print("Er zitten: " + str(letters) + " letters in uw wachtwoord.")
print("Er zitten: " + str(spaces) + " spaties in uw wachtwoord.")
print("Er zitten: " + str(others) + " tekens in uw wachtwoord.")