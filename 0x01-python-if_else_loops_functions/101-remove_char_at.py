#!/usr/bin/python3
def remove_char_at(str, n):
    if len(str) <= n or n < 0:
        return (str)
    j = ""
    for i in range(len(str)):
        if i != n:
            j += str[i]
    return (j)
