#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    total = list(a_dictionary.keys())
    for i in total:
        count += 1
    return count
