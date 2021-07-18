"""
Take input for a string & n.
Then find all possible words of length n consisting letters of string only once.
"""

import random
from textblob import TextBlob  # pip install textblob
from englisttohindi.englisttohindi import EngtoHindi  # pip install englisttohindi


def factorial(n):
    i = 1
    fact = 1
    while i != n + 1:
        fact *= i
        i += 1
    return fact


def permutations(n, r):
    res = 1
    for i in range(r):
        res *= (n - i)
    return res


def choosing(length, list1):
    indexes = []
    i = 0
    while i < length:
        a = random.randint(0, len(list1) - 1)
        if a not in indexes:
            indexes.append(a)
            i += 1
    return indexes


def all_indexes(length, list1):
    totals = permutations(len(list1), length)
    index_list = []
    i = 0
    while i < totals:
        choice_now = choosing(length, list1)
        if choice_now not in index_list:
            index_list.append(choice_now)
            i += 1
    return index_list


def words(length, list1):
    ret_list = []
    for item in all_indexes(length, list1):
        final = []
        for items in item:
            final.append(list1[items])
        final_str = "".join(final)
        ret_list.append(final_str)
    ret_list.sort()
    fin_list = []
    for i in ret_list:
        if i not in fin_list:
            if TextBlob(i) == TextBlob(i).correct():
                fin_list.append(i)
    for keys in fin_list:
        print(f"{keys} - {EngtoHindi(keys).convert}")
    print(f"Total words found are {len(fin_list)}")


if __name__ == '__main__':
    print("Enter word containing all letters :")
    inp_str = input()
    l1 = [i for i in inp_str]
    length = int(input("Enter length of word = "))
    words(length, l1)
