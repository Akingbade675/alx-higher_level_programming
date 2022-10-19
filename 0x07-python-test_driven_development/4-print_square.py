#!/usr/bin/python3
"""Defines a function print_square(size)."""


def print_square(size):
    """
    Prints a square with the character '#'.

    Args:
        size (int): the size of the square to be printed

    Raises:
        TypeError: If size is not an integer
        ValueError: If size is less than 0
    """
    if type(size) != int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        [print("#", end="") for j in range(size)]
        print("")
