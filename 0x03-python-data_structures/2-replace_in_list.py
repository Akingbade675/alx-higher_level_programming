def replace_in_list(my_list, idx, element):
    lent = len(my_list)
    if idx < 0 or idx > lent - 1:
        return my_list
    my_list[idx] = element
    return my_list
