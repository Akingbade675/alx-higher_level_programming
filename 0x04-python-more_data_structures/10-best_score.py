#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    key = ""
    num = 0
    for i in list(a_dictionary):
        if a_dictionary[i] > num:
            key = i
            num = a_dictionary[i]

    return key
