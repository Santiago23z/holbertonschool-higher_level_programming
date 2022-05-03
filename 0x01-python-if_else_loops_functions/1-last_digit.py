#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of"
if (number < 0):
    u = (abs(number) % 10) * -1
else:
    u = number % 10
if (u > 5):
    print(f"{str} {number} is {u} and is greater than 5")
elif (u == 0):
    print(f"{str} {number} is {u} and is 0")
elif (u < 6 and u != 0):
    print(f"{str} {number} is {u} and is less than 6 and not 0")
