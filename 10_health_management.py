"""
Input 1 --> Ask for enter name among 3 given names.
Input 2 --> Ask for enter exercise or diet
Input 3 --> Ask for log the work or retrieve the work.
Work accordingly.
"""

import datetime


def getdate():
    return datetime.datetime.now()


def log(cleint, work):
    add = input("Enter the item you want to add = ")
    if cleint == 1:
        if work == 1:
            with open("E10 saksham_exer.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
        elif work == 2:
            with open("E10 saksham_diet.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
    elif cleint == 2:
        if work == 1:
            with open("E10 harry_exer.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
        elif work == 2:
            with open("E10 harry_diet.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
    elif cleint == 3:
        if work == 1:
            with open("E10 shubham_exer.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
        elif work == 2:
            with open("E10 shubham_diet.txt", "a") as post:
                post.write("added at :- " + str(getdate()) + "\t" + add + "\n")
    print("Item added successfully")


def retreive(cleint, work):
    if cleint == 1:
        if work == 1:
            with open("E10 saksham_exer.txt") as post:
                print(post.readlines())
        elif work == 2:
            with open("E10 saksham_diet.txt") as post:
                print(post.readlines())
    elif cleint == 2:
        if work == 1:
            with open("E10 harry_exer.txt") as post:
                print(post.readlines())
        elif work == 2:
            with open("E10 harry_diet.txt") as post:
                print(post.readlines())
    elif cleint == 3:
        if work == 1:
            with open("E10 shubham_exer.txt") as post:
                print(post.readlines())
        elif work == 2:
            with open("E10 shubham_diet.txt") as post:
                print(post.readlines())
    else:
        print("Could not retrieve. Please add some item to retreive them.")


while (1):
    print("Press 0 in client to quit")
    cleint = int(input("Enter 1 for saksham, 2 for harry, 3 for shubham = "))
    if cleint == 0:
        break
    work = int(input("Enter 1 for exercise, 2 for diet = "))
    type = int(input("Enter 1 for log, 2 for retreive = "))

    if (cleint == 1 or cleint == 2 or cleint == 3) and (work == 1 or work == 2):
        if type == 1:
            log(cleint, work)
        elif type == 2:
            retreive(cleint, work)
        else:
            print("Entered invalid values!!!")
    else:
        print("Entered invalid values!!!")
