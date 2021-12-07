import random

from hangman_art import logo, stages
from hangman_word import word_list

chosen_word = random.choice(word_list)

print(logo)

# print(f"Solution is {chosen_word}")

lives = 6
display = []
word_len = len(chosen_word)
for _ in range(word_len):
    display.append("_")
print(f"{' '.join(display)}")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You have already guessed the letter {guess}")

    for position in range(word_len):
        if chosen_word[position] == guess:
            display[position] = guess

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You loose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You loose.")

    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You won")

    print(stages[lives])
