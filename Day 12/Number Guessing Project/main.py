from random import randint
from art import logo


EASY_LIVES = 10
HARD_LIVES = 5

def set_difficulty():
    difficulty = input("Choose a difficulty (easy/hard): ").lower()
    if difficulty == "easy":
        return EASY_LIVES
    elif difficulty == "hard":
        return HARD_LIVES
    else:
        print("Invalid choice, defaulting to easy.")
        return EASY_LIVES

def guessing():
    random_number = randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    if logo:
        print(logo)
    print("I'm thinking of a number between 1 and 100!")

    lives = set_difficulty()

    while lives > 0:
        guess = int(input("Guess a number: "))

        if guess == random_number:
            print("You guessed the number!")
            return
        elif guess > random_number:
            print("Too high!")
        elif guess < random_number:
            print("Too low!")

        lives -= 1

        if lives == 0:
            print("All out of lives, you lose!")
        else:
            print(f"You have {lives} lives left.")

guessing()