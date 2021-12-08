import random
from os import system

from art import logo, vs
from game_data import data


def get_random_account():
    """get a random account from the list"""
    return random.choice(data)


def format_data(account):
    """format the account data"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"


def check_answer(guess, a_foolower, b_follower):

    if a_foolower > b_follower:
        return guess == "a"
    else:
        return guess == "b"


def game():
    """play the game"""
    system("cls")
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        print(format_data(account_a))
        print(vs)
        print(format_data(account_b))

        guess = input("Who has more followers? (a/b) ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        system("cls")
        print(logo)

        if is_correct:
            score += 1
            print(f"You are correct! Your current score is: {score}")
        else:
            print(f"You are wrong! Your final score is: {score}")
            game_should_continue = False


game()

while True:
    print("\n")
    play_again = input("Would you like to play again? (y/n) ").lower()
    if play_again == "y":
        game()
    else:
        print("Thanks for playing!")
        break
