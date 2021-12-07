def reverse(n):
    r = 0
    while n != 0:
        d = n % 10
        r = r * 10 + d
        n //= 10
    return r


def num_palin(n):
    r = reverse(n)
    print(r)
    if n == r:
        return True
    else:
        return False


def fibo_series(n):
    a, b = 0, 1
    print(a)
    print(b)
    if n == 1:
        print(a)
    else:
        for i in range(2, n):
            add = a + b
            print(add)
            a = b
            b = add


# drivers code
c = 1
while c:
    print("\n")
    print("1. To display n Fibonacci series")
    print("2. To check if a number is a palindrome")
    print("0. To Exit")
    c = int(input("Enter your choice"))
    if c == 1:
        x = int(input("Enter number of terms:"))
        print("The fibonacci series are:")
        fibo_series(x)

    elif c == 2:
        x = int(input("Enter a number"))
        if num_palin(x):
            print(x, "is a palindrome")
        else:
            print(x, "is not a palindrome")
    elif c == 0:
        break
    else:
        print("Enter a valid choice")
