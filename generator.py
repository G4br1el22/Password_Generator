# Importing libraries
import random
import string


# Randomizing function
def create_password(length, char):
    random_string = ""
    for i in range(length):
        random_string += random.choice(char)
    return random_string


# Password length

length = int(input("Type your password lenght: "))

# Setting and building characters

characters = ""

print("Choose character types that are going to be in your password:")
letters = str(input("Letters y/n: ")).lower()
digits = str(input("Digits y/n: ")).lower()
symbols = str(input("Symbols y/n: ")).lower()

# Letters
if letters == "y":
    characters += string.ascii_letters

# Digits
if digits == "y":
    characters += string.digits

# Symbols
if symbols == "y":
    characters += string.punctuation

# Validation

if characters == "":
    print("You must select at least one option!")
else:
    # Printing password
    print(create_password(length, characters))
