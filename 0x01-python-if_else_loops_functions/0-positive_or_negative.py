#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    print(f"{number} is zero")
elif number in range(0, 11):
    print(f"{number} is positive")
else:
    print(f"{number} is negative")
