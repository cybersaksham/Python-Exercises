"""
Make a list & print numbers greater than 6 present in list
"""

list = ["saksham", True, 11, 5, 2, 25, 0, 8]

print("Items greater than 6 are :-")

for item in list:
    if str(item).isnumeric() and item > 6:
        print(item)
