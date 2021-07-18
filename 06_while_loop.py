"""
Take a number from user.
If number is less than 100 then take again & again.
But if number is not less than 100 then stop program
"""

print("Enter a number not less than 100 to break program")

while (1):
    i = int(input("Enter a number = "))
    if i < 100:
        print("you have entered less than 100 so enter again!!")
        continue
    if i >= 100:
        print("you have entered not less than 100 so we will close this program!!")
        break
