"""
Take two numbers a & b as input.
Then swap their values & print.
"""

print("Enter number a = ", end="")
a = input()

print("Enter number b = ", end="")
b = input()

a, b = b, a
print("After swapping")
print("a = " + str(a))
print("b = " + str(b))
