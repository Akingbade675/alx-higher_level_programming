#!/usr/bin/python3

"""Defines a function add_integer"""


def add_integer(a, b=98):
    """add 2 integers.

    Returns: the addition of a and b

    Raises:
        TypeError: If either a and b are not integer or float
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
