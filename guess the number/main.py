import random
from os import system

from art import logo


def play():
    print(logo)
    print("\nWelcome to the game 'Guess the number'!")
    print("\nI'm thinking of a number between 1 and 100.")
    print("Try to guess it in as few attempts as possible.\n")

    difficulty = input("Choose a difficulty: easy, medium or hard: ")
    if difficulty == "easy":
        max_try = 10
    elif difficulty == "medium":
        max_try = 5
    elif difficulty == "hard":
        max_try = 2
    else:
        print("\nPlease choose a valid difficulty.")
        return

    print(f"\nYou have {max_try} tries to guess the number.\n")

    number = random.randint(1, 100)
    tries = 1
    while tries <= max_try:
        print(f"\nYou've {max_try-tries+1} tries left.\n")
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("\nPlease enter a valid number.")
            continue
        if guess < 1 or guess > 100:
            print("\nThe number must be between 1 and 100.")
            continue
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            break
        tries += 1

    if guess == number:
        print(f"\nGood job! You guessed my number in {tries} tries.")
    else:
        print(f"\nNope. The number I was thinking of was {number}.")


play()

while input("\nDo you want to play again? (y/n): ") == "y":
    system("cls")
    play()
