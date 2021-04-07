import string
import random
def generator():
    max_length = 100
    min_length = 5
    print("Dit is de Wachtwoord generator, hiermee kan je een random wachtwoord aanmaken.")
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

    #  Dit heb ik gevonden op een website:
    #  def check_of_cijfer(input_str):
    #    if input_str.strip().isdigit():
    #        print("Het moet y/n zijn")
    # dit is een git test, babs

    while True:
        numbers = input("Wilt u cijfers in uw wachtwoord? (y/n): ")
        if numbers.strip().isdigit():
            print("Het moet y/n zijn en geen cijfer")
        elif numbers != "y" and numbers != "n":
            print("Het moet y/n zijn!")
        else: break

    while True:
        tekens = input("Wilt u Apparte Tekens in uw wachtwoord? (y/n): ")
        if tekens.strip().isdigit():
            print("Het moet y/n zijn en geen cijfer")
        elif tekens != "y" and tekens != "n":
            print("Het moet y/n zijn!")
        else: break

    ### Hier staan de random nummer generators:

    #Eerst maak ik met de library "String" een string met letters punctuations of digits
    #dan maak je daar een random string van met de library "Random"

    if numbers == "y" and tekens == "y":
        characters = string.ascii_letters + string.punctuation  + string.digits
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)
    if numbers == "n" and tekens == "n":
        characters = string.ascii_letters
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)
    if numbers == "y" and tekens == "n":
        characters = string.ascii_letters + string.digits + string.digits
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)
    if numbers == "n" and tekens == "y":
        characters = string.ascii_letters + string.punctuation + string.punctuation
        password =  "".join(random.choice(characters) for x in range(pass_length))
        print(password)

    while True:
        print("Wilt u een nieuw wachtwoord maken? (y/n):")
        new = input()
        if numbers.strip().isdigit():
            print("Het moet y/n zijn en geen cijfer")
        elif numbers != "y" and numbers != "n":
            print("Het moet y/n zijn!")
        else: break
    if new == "y":
        generator()
generator()