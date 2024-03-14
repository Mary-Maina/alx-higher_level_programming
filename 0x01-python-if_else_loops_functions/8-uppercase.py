#!/usr/bin/python3
def uppercase(str):
    j = ""
    for i in range(len(str)):
        x = ord(str[i])
        if (x < 97 or x > 122):
            j += chr(x)
        else:
            j += chr(x - 32)
    print("{}".format(j))
