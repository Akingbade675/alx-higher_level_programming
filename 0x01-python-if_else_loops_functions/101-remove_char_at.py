#!/usr/bin/python3
def remove_char_at(str, n):
    strin = ""
    for i in range(0, len(str)):
        if i != n:
            strin = strin + str[i]
    return strin
