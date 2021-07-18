"""
Make a random dictionary & ask user to enter a word.
Tell him the meaning of word according to your dictionary.
"""

fruit = {"Apple": "a red fruit source of iron",
         "Mango": "My favourite",
         "Pineapple": "Very sour",
         "Orange": "Khatta Meetha"}

a = input("Enter a value :- ")
b = a.lower()
c = b.capitalize()
print(a, " = ", fruit[c])
