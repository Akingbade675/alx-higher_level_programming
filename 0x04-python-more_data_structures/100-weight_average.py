#!/usr/bin/python3
def weight_average(my_list=[]):

    if type(my_list) != list or len(my_list) == 0:
        return 0

    num = 0
    weight = 0

    for tuples in my_list:
        num += (tuples[0] * tuples[1])
        weight += tuples[1]

    return num / weight
