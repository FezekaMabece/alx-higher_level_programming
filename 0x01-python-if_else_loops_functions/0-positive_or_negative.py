#!/usr/bin/python3
import random
number = random.randint(-10, 10)
number = int(input("Write a number between -10 to 10 "))
if number >= 0:
    print(f"{number} is positive")
elif number == 0:
    print(f"{number} is zero")
elif number <=0:
    print(f"{number} is negative")
