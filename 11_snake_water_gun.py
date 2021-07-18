"""
Make a program to choose sanke, water or gun.
Display score of you & computer after every turn.
Play 10 times.
At last whose score is highest he wins
"""

import random


def printing():
    print("Enter 1 for snake")
    print("Enter 2 for water")
    print("Enter 3 for gun")


sc_you = 0
sc_comp = 0


def score(you, comp):
    choices = ["Snake", "Water", "Gun"]
    global sc_you
    global sc_comp
    if you == 1 and comp == 2:
        sc_you = sc_you + 1
    elif you == 1 and comp == 3:
        sc_comp = sc_comp + 1
    elif you == 2 and comp == 3:
        sc_you = sc_you + 1
    elif you == 2 and comp == 1:
        sc_comp = sc_comp + 1
    elif you == 3 and comp == 1:
        sc_you = sc_you + 1
    elif you == 3 and comp == 2:
        sc_comp = sc_comp + 1
    else:
        sc_you = sc_you
        sc_comp = sc_comp
    print("Your's choice =", choices[you - 1])
    print("Comp's choice =", choices[comp - 1])
    print("Score of yours =", sc_you)
    print("Score of computer =", sc_comp, "\n")


def win(sc_you, sc_comp):
    if sc_you > sc_comp:
        print("Congrats!!You won")
    elif sc_you < sc_comp:
        print("Alas!!You lost")
    else:
        print("Fine!!Game Tied")


i = 1

print("\nYou have 10 turns")
while i < 11:
    print("Turn no.", i)
    printing()
    you = int(input())
    comp = random.randint(1, 3)

    if you == 1 or you == 2 or you == 3:
        score(you, comp)
        i = i + 1
    else:
        print("Enter correct value")

win(sc_you, sc_comp)
