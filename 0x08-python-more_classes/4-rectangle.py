#!/usr/bin/python3

"""A Rectangle class."""


class Rectangle:
    """Defines a Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object

        Args:
            width (int): The width of the new Rectangle object
            height (int): The height of the new Rectangle object
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/Set the width of a Rectangle object."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")

        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """Get/Set the height of a Rectangle object."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")

        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return (self.__height * self.__width)

    def perimeter(self):
        """Returns the perimeter of the Rectangle."""
        if self.height == 0 or self.width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        if self.__height == 0 or self.__width == 0:
            return ("")
        string = []
        for h in range(0, self.__height):
            [string.append("#") for w in range(0, self.__width)]
            if h != self.__height - 1:
                string.append("\n")
        return ("".join(string))

    def __repr__(self):
        """Returns the string representation of te rectangle"""
        rect = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (rect)
