def divisible_by_2(my_list=[]):
    div_list = []
    for i in range(len(my_list)):
        div_list[i] = True if my_list[i] % 2 else False
    return div_list
