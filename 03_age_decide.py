"""
Take age from user.
Tell him that he can drive or not according to his age.
"""

age = int(input("Enter your age - "))

if (age > 6) & (age < 101):
    if age < 18:
        print("You cannot drive")
    elif age == 18:
        print("We will think about you")
    else:
        print("You can drive")
else:
    print("Your age is not valid for this program")
