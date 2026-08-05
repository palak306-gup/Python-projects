# Number Guessing Game

import random

def start_game():
    secret_number = random.randint(1, 20)
    attempts = 0
    max_attempts = 5

    print("Welcome to the Number Guessing Game!")
    print("I have picked a number between 1 and 20. Can you guess it?")

    while attempts < max_attempts:
        guess = int(input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: "))
        attempts += 1

        if guess == secret_number:
            print(f"Congratulations! You guessed it in {attempts} attempts.")
            return
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        else:
            print("Too high! Try a lower number.")

    print(f"Game over! The secret number was {secret_number}.")

if __name__ == "__main__":
    start_game()
