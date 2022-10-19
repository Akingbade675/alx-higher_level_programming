#!/usr/bin/python3

"""Implements a function matrix_divided()."""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Args:
        matrix (list): A list of lists of integers or floats
        div (int/float): Divisor

    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If each row of different size
        TypeError: If div is not a number
        ZeroDivisionError: If div is equals to 0

    Returns: A new matrix with all matrix elements divided by div
    """
    new = []
    row_size = len(matrix[0])

    if type(matrix) != list or matrix == []:
        raise TypeError("matrix must be matrix \
                (list of lists) of integers/floats")

    for row in matrix:
        if (type(row) != list or
                all((type(item) != int and type(item) != float)
                    for item in row)):
            raise TypeError("matrix must be a matrix \
                    (list of lists) of integers/floats")

        if row_size != len(row):
            raise TypeError("Each row of the matrix must have the same size")

        if type(div) != int and type(div) != float:
            raise TypeError("div must be a number")

        if div == 0:
            raise ZeroDivisionError("division by zero")

        new.append([round((item / div), 2) for item in row])

    return (new)
