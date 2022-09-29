#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    prev = 0
    cur = 0
    if type(roman_string) != str or not roman_string:
        return num

    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    for i in roman_string:
        cur = romans[i]
        num += (cur - prev - prev) if cur > prev else cur

        prev = cur

    return num
