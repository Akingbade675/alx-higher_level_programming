#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a Square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square

        Args:
            size (int): the size of the square
            position (int, int): the position of the Square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter and Setter method for instance variable size."""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value

    @property
    def position(self):
        """Getter and Setter methods for the position attribute"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (type(value) != tuple or
                len(value) != 2 or
                all(type(i) != int for i in value) or
                all(i < 0 for i in value)):
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value

    def area(self):
        """Returns the current square area"""
        return (self.size * self.size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.size == 0:
            print("")
            return

        [print("") for i in range(0, self.position[1])]
        for i in range(0, self.size):
            [print(" ", end="") for k in range(0, self.position[0])]
            [print("#", end="") for j in range(0, self.size)]
            print("")
