#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    n_args = len(argv) - 1
    if n_args == 0:
        print("0 arguments.")
    else:
        r = "s" if n_args > 1 else ""
        print(f"{n_args} argument{r}:")
        for i, arg in enumerate(argv[1:], start=1):
            print(f"{i}: {arg}")
