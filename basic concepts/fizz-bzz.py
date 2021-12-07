# Rules of fizz-buzz
# * When counting numbers the number divisible by 3 should be replaced with fizz
# ? and number divisible by 5 should be replaced with buzz
# ! and number divisible by both 3 and 5 should be replaced with fizz-buzz

for n in range(1, 101):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)
