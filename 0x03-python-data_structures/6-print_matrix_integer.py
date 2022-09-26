def print_matrix_integer(matrix=[[]]):
    if len(matrix) == 0:
        print("Empty")
        return
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="\n" if i == len(row) - 1 else " ")
