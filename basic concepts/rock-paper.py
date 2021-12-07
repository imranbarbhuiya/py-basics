import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
symbol = [rock, paper, scissors]
player = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))

if player != 0 and player != 1 and player != 2:
    print("You have entered invalid number,you lose!")
else:
    print(f"You Choose: \n {symbol[player]}")

    computer = random.randint(0, 2)

    print(f"Computer choose: \n {symbol[computer]}")

    if player == 0 and computer == 2:
        print("You win!")
    elif computer == 0 and player == 2:
        print("You lose")
    elif player > computer:
        print("You win!")
    elif player == computer:
        print("It's a draw")
    else:
        print("You lose")
