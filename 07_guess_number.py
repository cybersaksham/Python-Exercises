"""
let n = 18
Ask user to guess a number.
If he guess greater than 18 than tell to reduce his guess
If he guess smaller than 18 than tell to grow up his guess
If he entered 18 then he wins game
Max no of guesses are 9
If he can't guess 18 either in 9 guesses then he lose the game
Print no of guesses left at each term
"""

n = 18
guess_num = 1

while guess_num < 10:
    guess = int(input("Guess a number :- "))
    if guess == 18:
        print("Wow!! You guess the number only in", guess_num, "guesses")
        break
    elif guess <= 10:
        print("Enter a big number")
        print("No of guesses left =", 9 - guess_num)
        guess_num = guess_num + 1
        continue
    elif guess < 18:
        print("You are very close!!\nEnter a little big number")
        print("No of guesses left =", 9 - guess_num)
        guess_num = guess_num + 1
        continue
    elif guess < 25:
        print("You are very close!!\nEnter a little short number")
        print("No of guesses left =", 9 - guess_num)
        guess_num = guess_num + 1
        continue
    else:
        print("Enter a short number")
        print("No of guesses left =", 9 - guess_num)
        guess_num = guess_num + 1

if guess_num == 10:
    print("Alas!! You have spent all your turns!!\nGAME OVER")
