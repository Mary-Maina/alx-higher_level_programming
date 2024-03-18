#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length > 0:
        s = sentence[0]
    else:
        s = "None"

    return (length, s)
