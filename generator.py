# Importing libraries
import random
import string


# Randomizing function
def create_password(length, chars):
    return "".join(random.choice(chars) for _ in range(length))


# Creating charset
def charset():
    print("Choose your character types:")
    chars = ""

    if input("Letters? y/n: ").lower() == "y":
        chars += string.ascii_letters
    if input("Digits? y/n: ").lower() == "y":
        chars += string.digits
    if input("Symbols? y/n: ").lower() == "y":
        chars += string.punctuation

    return chars


# Creating password
def generate_password():
    length = int(input("Type your password lenght: "))
    chars = charset()

    if chars == "":
        print("You must select at least one option!")
        return

    print("Generated password: ")
    print(create_password(length, chars))


# Generating password
generate_password()
