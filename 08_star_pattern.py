"""
Take input for no of rows.
Take input for type of pattern.
Then print star pattern accordingly.
"""

def forward(row):
    i = 1
    while i < row + 1:
        j = 1
        while j < i + 1:
            print("*", end="")
            j = j + 1
        print()
        i = i + 1


def backward(row):
    i = 1
    while i < row + 1:
        j = row - i + 1
        while j > 0:
            print("*", end="")
            j = j - 1
        print()
        i = i + 1


def for_back(row):
    i = 1
    while i < row + 1:
        j = 1
        while j < i + 1:
            print("*", end="")
            j = j + 1
        print()
        i = i + 1
    k = 1
    while k < row:
        l = row - k
        while l > 0:
            print("*", end="")
            l = l - 1
        print()
        k = k + 1


def back_for(row):
    k = 1
    while k < row:
        l = row - k + 1
        while l > 0:
            print("*", end="")
            l = l - 1
        print()
        k = k + 1
    i = 1
    while i < row + 1:
        j = 1
        while j < i + 1:
            print("*", end="")
            j = j + 1
        print()
        i = i + 1


while (1):
    rows = int(input("\nEnter no of rows in star pattern = "))
    type = int(input("Enter 1 for forward\nEnter 2 for backward\nEnter 3 for for-back\nEnter 4 for back-for\n"))
    if type == 1:
        forward(rows)
    elif type == 2:
        backward(rows)
    elif type == 3:
        for_back(rows)
    elif type == 4:
        back_for(rows)
    else:
        print("Please enter correct number")
