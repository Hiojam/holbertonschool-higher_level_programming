#!/usr/bin/python3
""" Task 2 """


class Rectangle:
    """Representation for Rectangle."""

    def __init__(self, width=0, height=0):
        """Initializate the rectangle."""

        self.height = height
        self.width = width

    @property
    def width(self):
        """Return the width of the Rectangle."""
        return self.__width

    @property
    def height(self):
        """Return the height of the Rectangle."""
        return self.__height

    @width.setter
    def width(self, value):
        """Set the width of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Set the height of the Rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if (self.__width == 0 or self.__height == 0):
            return 0
        return 2 * (self.__width + self.__height)
