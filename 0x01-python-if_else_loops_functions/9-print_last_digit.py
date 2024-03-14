#!/usr/bin/python3
def print_last_digit(number):
    num = abs(number)
    x = num % 10
    print(x, end='')
    return x
