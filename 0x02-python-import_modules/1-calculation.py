#!/usr/bin/python3
if __name__ == "__main__":
    a = 10
    b = 5
    from calculator_1 import add, sub, mul, div
    res = add(a, b)
    print("{} + {} = {}".format(a, b, res))
    x = sub(a, b)
    print("{} - {} = {}".format(a, b, x))
    y = mul(a, b)
    print("{} * {} = {}".format(a, b, y))
    i = div(a, b)
    print("{} / {} = {}".format(a, b, i))
