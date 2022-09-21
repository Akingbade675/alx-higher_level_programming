#!/usr/bin/python3
def uppercase(str):
    for i in str:
        char = ord(i)
        _islower = char > 96 and char < 123
        print("{}".format(chr(char - 32) if _islower else i), end="")
    print()
