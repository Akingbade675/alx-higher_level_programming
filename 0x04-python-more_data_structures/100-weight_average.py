#!/usr/bin/python3
def weight_average(my_list=[]):

    num = 0
    weight = 0

    for tuples in my_list:
        num += tuples[0] * tuples[1]
        weight += tuples[1]

    return num / weight
