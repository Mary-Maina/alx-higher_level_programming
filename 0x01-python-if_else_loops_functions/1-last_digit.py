#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num = abs(number)
x = num % 10
if number < 0:
    x = -x

if x > 5:
    print(f"Last digit of {number:d} is {x:d} and is greater than {5}")
elif x == 0:
    print(f"Last digit of {number:d} is {x:d} and is {0}")
else:
    print(f"Last digit of {number:d} is {x:d} and is less than {6} and not 0")
