"""
Design a faulty calculator which will correctly solve all problems.
Except the following ones :-
45*3 = 555, 56+9=77, 56/6 = 4
Your program should take operator & 2 numbers as input from user.
Then return the result
"""

operator = input("Write an operator :- ")
opr1 = float(input("Enter first operand = "))
opr2 = float(input("Enter second operand = "))

if (((opr1 == 45) & (opr2 == 3)) | ((opr1 == 3) & (opr2 == 45))) & (operator == "*"):
    print(opr1, operator, opr2, "= 455")
elif (((opr1 == 56) & (opr2 == 9)) | ((opr1 == 9) & (opr2 == 56))) & (operator == "+"):
    print(opr1, operator, opr2, "= 77")
elif ((opr1 == 56) & (opr2 == 6)) & (operator == "/"):
    print(opr1, operator, opr2, "= 4")
else:
    if operator == "+":
        print(opr1, "+", opr2, "=", opr1 + opr2)
    elif operator == "*":
        print(opr1, "*", opr2, "=", opr1 * opr2)
    elif operator == "-":
        print(opr1, "-", opr2, "=", opr1 - opr2)
    elif operator == "/":
        print(opr1, "/", opr2, "=", opr1 / opr2)
    else:
        print("You have entered incorrect operator")
