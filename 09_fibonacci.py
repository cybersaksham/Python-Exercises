"""
Fibonacci Series --> 0, 1, 1, 2, 3, 5, 8, 13, ........
First two elements are 0 & 1
Then we find Nth element by adding (N-1)th & (N-2)th elements.
"""

def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib_rec(n - 1) + fib_rec(n - 2)


while (1):
    number = int(input("Enter a number = "))
    print("Fibonacci of", number, "is", fib_rec(number))
