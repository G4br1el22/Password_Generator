import random
import string


# Random String
def create_password(length, chars):
    return "".join(random.choice(chars) for _ in range(length))


# Choosing characters
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


# Building password
def build_part(base_password, position):
    length = int(input(f"{position} length: "))
    chars = charset()
# Chars != ""
    if chars == "":
        print("You must select at least one option!")
        return base_password

    random_part = create_password(length, chars)

    return random_part + base_password if position == "Prefix" \
        else base_password + random_part


# Input Password
password = input("Password: ")

# Prefix/Sufix
if input("Prefix? y/n: ").lower() == "y":
    password = build_part(password, "Prefix")
if input("Sufix? y/n: ").lower() == "y":
    password = build_part(password, "Sufix")

# Final password
print(f"Final password: {password}")
