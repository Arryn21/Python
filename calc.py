
print("You are inside the calculator now.\n"
      "what do you want to calculate.")
print("1. Add\n"
      "2. Sub\n"
      "3. Mult")

p = int(input("1st number: "))
q = int(input("2nd number: "))


def add():
    return p+q


def sub():
    return p-q


def mult():
    return p*q


def switch_demo(y):
    switcher = {
        1: add,
        2: sub,
        3: mult
    }
    func = switcher.get(y, lambda: "Invalid Input")
    print(func())


choice = int(input("Select: "))
print(switch_demo(choice))
"""
from tkinter import*
"""