#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square."""

    def __init__(self, size=0):
        """Initialize a Square

        Args:
            size (int): the size of the square
        """
        self.size = size

    @property
    def size(self):
        """Getter and Setter method for instance variable size.

        Returns:
            int: the value of size
        """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return (self.size * self.size)

    def my_print(self):
        """prints in stdout the square with the character #"""

        for i in range(0, self.size):
            for j in range(0, self.size):
                print("#", end="")
            print("")

        if self.size == 0:
            print("")
