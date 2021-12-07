import random
from os import system

from art import logo


def deal_card():
    """Returns a random card"""
    cards = [11, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    """Returns the total score of the given cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    """Returns the winner of the game"""
    if user_score == computer_score:
        return "It's a tie!"
    elif computer_score == 0:
        return "You loose, opponent has blackjack"
    elif user_score == 0:
        return "You win, you have blackjack"
    elif user_score > 21:
        return "You loose, you have more than 21"
    elif computer_score > 21:
        return "You win, opponent has more than 21"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You loose"


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'hit' to get a card, 'stand' to pass\n")
            if user_should_deal == "hit":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print("\n")
    print(f"    Your cards: {user_cards}, score: {user_score}")
    print(f"    Computer's cards: {computer_cards}, score: {computer_score}")
    print(compare(user_score, computer_score))


play_game()
while input("Type 'y' to play again\n") == "y":
    system("cls")
    play_game()
