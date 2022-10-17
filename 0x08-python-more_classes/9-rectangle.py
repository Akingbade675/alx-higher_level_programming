#!/usr/bin/python3

"""A Rectangle class."""


class Rectangle:
    """Defines a Rectangle.

    Attributes:
        number_of_instances (int): The number of intances of Rectangle.
        print_symbol (any): The symbol used for string representation.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle object

        Args:
            width (int): The width of the new Rectangle object
            height (int): The height of the new Rectangle object
        """
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @classmethod
    def square(cls, size=0):
        """Returns a new Rectangle instance

        Args:
            size (int): width == height == size
        """
        return (cls(size, size))

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
            for w in range(0, self.__width):
                string.append(str(self.print_symbol))
            if h != self.__height - 1:
                string.append("\n")
        return ("".join(string))

    def __repr__(self):
        """Returns the string representation of te rectangle"""
        rect = "Rectangle(" + str(self.width) + ", " + str(self.height) + ")"
        return (rect)

    def __del__(self):
        """Prints a message when an instance of Rectangle is deleted."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area.
        Args:
            rect_1 (Rectangle): The first Rectangle.
            rect_2 (Rectangle): The second Rectangle.
        Raises:
            TypeError: If either of rect_1 or rect_2 is not a Rectangle.
        """
        if type(rect1) != Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect2) != Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect1.area() >= rect.area():
            return (rect1)
        return (rect2)
