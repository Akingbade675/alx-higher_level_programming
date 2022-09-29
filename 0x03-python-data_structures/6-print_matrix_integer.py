#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        lent = len(row)
        for i in range(lent):
            print("{:d}".format(row[i]), end="" if i == (lent - 1) else " ")
        print("")
