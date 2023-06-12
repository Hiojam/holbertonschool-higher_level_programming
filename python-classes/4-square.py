#!/usr/bin/python3
""" Task 4 """


class Square:
    """A class representing a square."""

    def __init__(self, size=0):
        if (type(size) == int):
            if (size < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            float: The area of the Square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Retrieves the size value

        Returns:
            int: The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ Sets the size of the Square. """
        if (type(value) == int):
            if (value < 0):
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")
    pass
