#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """defines a square

    This class defines a square

    Attributes:
        size (int): size of the square
    """

    def __init__(self, size):
        """__init__ method

        Is the first method to be called when an object is
        instatiated

        Args:
            size (int): the size of the square
        """
        self.__size = size
