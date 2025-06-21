import random
import string

def password_generator(length, want_numbers=True, want_letters=True, want_symbols=True):
    """generate password by arranging strings randomly"""
    characters = ""

    if want_numbers:
        characters += string.digits
    if want_letters:
        characters += string.ascii_letters
    if want_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def check_strength(password):
    """how strong is your password?"""
    score = 0

    if len(password) > 5:
        score += 1
    if any(c.islower() for c in password) and any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score < 2:
        return "Too weak!"
    elif score == 3 or score == 4:
        return "Moderate, can improve."
    else:
        return "STRONG!"

if __name__ == "__main__":
    print("\n------ Welcome to the Password Generator ------")

    while True:
        try:
            length = int(input("\nEnter the length of the password: "))
        except ValueError:
            print("Enter a valid integer!")
            continue

        want_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        want_letters = input("Include letters? (y/n): ").lower() == 'y'
        want_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        password = password_generator(length, want_numbers, want_letters, want_symbols)

        print(f"\nYour password is: {password}")
        print("\nStrength check:", check_strength(password))

        again = input("\nGenerate another password? (y/n): ").lower()
        if again != 'y':
            print("Goodbye!")
            break
