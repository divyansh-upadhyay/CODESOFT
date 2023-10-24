import random
import string


# Function to generate a random password
def generate_password(length, complexity):
    characters = ''

    if 'upper' in complexity:
        characters += string.ascii_uppercase
    if 'lower' in complexity:
        characters += string.ascii_lowercase
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type (upper, lower, digits, special).")
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Main program
while True:
    length = input("Enter the desired password length: ")

    if not length.isdigit():
        print("Please enter a valid number for the password length.")
        continue

    length = int(length)

    complexity = input("Enter the desired complexity (e.g., 'upper lower digits special' or 'lower digits'): ").split()

    password = generate_password(length, complexity)

    if password:
        print("Generated Password:", password)

    another = input("Generate another password? (yes/no): ").lower()
    if another != 'yes':
        print('THANK YOU')
    else:
        print('SURE')
