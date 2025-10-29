import random
import string

def generate_password(min_length, uppercase=True, numbers=True, special_chars=True):
    letters = string.ascii_lowercase
    if uppercase:
        letters += string.ascii_uppercase
    
    digits = string.digits
    punctuations = string.punctuation   

    # Start building character pool
    characters = letters
    if numbers:
        characters += digits
    if special_chars:
        characters += punctuations

    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_specials = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_numbers = True
        elif new_char in punctuations:
            has_specials = True

        # Check criteria
        meets_criteria = True
        if numbers:
            meets_criteria = has_numbers
        if special_chars:
            meets_criteria = meets_criteria and has_specials

    return pwd


# ----- User inputs -----
min_length = int(input("Enter minimum password length (default 8): ") or 8)
has_number = input("Do you want to have numbers (y/n)? ").lower() == "y"
has_specials = input("Do you want to have special characters (y/n)? ").lower() == "y"

pwd = generate_password(min_length, numbers=has_number, special_chars=has_specials)
print("The password is:", pwd)
