#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    total = 0
    n_arg = len(argv) - 1
    for i in range(n_arg):
        total += int(argv[i + 1])
    print(total)
