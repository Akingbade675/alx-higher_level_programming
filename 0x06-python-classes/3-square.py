#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represents a Square"""

    def __init__(self, size=0):
        """Initialize a Square

        Args:
            size (int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """Calculates the Area of the Square

        Returns:
            int: the current square area

        """
        return (self.__size * self.__size)
