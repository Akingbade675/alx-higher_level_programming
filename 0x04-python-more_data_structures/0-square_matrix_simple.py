#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squares = [[]]
    for row in matrix:
        squares.append(list(map(lambda x: x ** 2, row)))
    return squares


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
