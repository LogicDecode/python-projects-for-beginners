# Import Modules
import random
import string

# Welcome message
print("\n\nWelcome to Random Password Generator!")

# Get the length of the password from the user
length = int(input("Enter the length of the password: "))
use_symbols = input("Do you want to use symbols? (y/n): ")

# print the characters that can be used in the password
print("\n\n-------------------\n\n")
print("The following characters can be used in the password:")
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

if use_symbols.lower() == "y":
    print(string.punctuation)
    all_characters = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits + string.punctuation
else:
    all_characters = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits

print("All characters:", all_characters)
print("\n\n-------------------\n\n")


# Generate the password of the specified length
pass_chars = random.sample(all_characters, length)
print("Selected characters:", pass_chars)

password = "".join(pass_chars)
print("Your password is:", password)
