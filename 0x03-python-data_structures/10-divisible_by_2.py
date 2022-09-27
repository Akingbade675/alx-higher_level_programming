#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    div_list = []
    for i in range(len(my_list)):
        div_list.append(True if not my_list[i] % 2 else False)
    return div_list
