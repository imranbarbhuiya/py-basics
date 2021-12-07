import math


def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x


def isFibonacci(n):
    return isPerfectSquare(5 * n * n + 4) or isPerfectSquare(5 * n * n - 4)


list = input().split(",")
# list = [5,3,2,55,4,21,36]
output = []
for i in list:
    if isFibonacci(int(i)):
        output.append(i)
print(len(output))
