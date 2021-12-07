# * This is a strong password generators
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the iPass password generator!")

choice = input(
    "Do you wants to enter how many numbers of password you wants? ans in y for yes or n for no    "
)
if choice == "y":
    # if we wants the user to enter the number of digit they wants
    nr_letters = int(input("How many letters would you like in your password? \n"))
    nr_symbols = int(input("How many symbols would you like? \n"))
    nr_numbers = int(input("How many numbers would you like? \n"))
else:
    # we are giving a hard coded number of characters
    nr_letters = random.randint(6, 8)
    nr_symbols = random.randint(2, 3)
    nr_numbers = random.randint(3, 5)

password_list = []
password = ""

for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f"Here is your password: {password}")
