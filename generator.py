# Importing libraries
import random
import string


# Randomizing function
def create_password(len, char):
    random_string = ""
    for i in range(len):
        random_string += random.choice(char)
    return random_string


lenght = int(input("Type your password lenght: "))
characters = ""

print("Choose character types that are going to be in your password:")
letters = str(input("Letters y/n: "))
digits = str(input("Digits y/n: "))
symbols = str(input("Symbols y/n: "))

# Letters

if letters == "y":
    characters += string.ascii_letters
elif letters == "n":
    pass
else:
    print("Please select a valid option")

# Digits

if digits == "y":
    characters += string.digits
elif digits == "n":
    pass
else:
    print("Please select a valid option")

# Symbols

if symbols == "y":
    characters += string.punctuation
elif symbols == "n":
    pass
else:
    print("Please select a valid option")


# Printing password
print(create_password(lenght, characters))
