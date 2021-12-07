yourName = input("What is your Name\n").lower()
yourLovedOne = input("What is your Lover's Name\n").lower()

name = yourName + yourLovedOne

t = name.count("t")
r = name.count("r")
u = name.count("u")
e = name.count("e")

true = t + r + u + e

l = name.count("l")
o = name.count("o")
v = name.count("v")
e = name.count("e")

love = l + o + v + e

loveCount = int(str(true) + str(love))

if loveCount < 10 or loveCount > 90:
    print(f"Your Love Score is {loveCount}%, You go together like coke and mentos")
elif loveCount > 40 and loveCount < 50:
    print(f"Your Love Score is {loveCount}%, You are alright together")
else:
    print(f"Your Love Score is {loveCount}%")
