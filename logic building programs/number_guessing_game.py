from random import randint 

print("\n\t------WELCOME TO NUMBER GUESSING GAME------")
print("\nI have picked a random number between 1 and 10.")
print("You have 3 attempts to guess it correctly.\n")

secret_number = randint(1,10)
attempts = 0
total_attempts = 3

while attempts < total_attempts:
    try:
        guess = int(input(f"-> attempt {attempts + 1}:\nGuess a number(1-10): "))
        attempts += 1


        if guess == secret_number:
            print(f"\n\t🎉Congratulations, you won the game in {attempts} attempt(s)!! ")
            break
        elif guess < secret_number:
            print(f"Too low, try again.\n")
        elif guess > secret_number:
            print(f"Too high, try again.\n")

        if attempts < total_attempts:
            print(f"You have {total_attempts - attempts} attempt(s) left.\n")
        
    except ValueError:
        print("\nEnter a valid integer.")

if guess != secret_number:
    print(f"\nYou've used all your attempts. The secret number was {secret_number}.")
    print("\n\tBetter luck next time!👍")




    