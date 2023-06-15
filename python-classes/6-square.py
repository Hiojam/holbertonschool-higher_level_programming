#!/usr/bin/python3
""" Task 5 """


class Square:
    """A class representing a square."""

    __poserr = ValueError("position must be a tuple of 2 positive integers")

    def __init__(self, size=0, pos=(0, 0)):
        self.size = size
        self.position = pos

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

    @property
    def position(self):
        """ Get the position of the square

        Returns:
            tuple: Two positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ Sets the position of the Square """
        if not (isinstance(value, tuple)):
            raise self.__poserr

        try:
            if (isinstance(value[0], int) and isinstance(value[1], int)):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise self.__poserr
            else:
                raise self.__poserr
        except IndexError:
            raise self.__poserr

    def my_print(self):
        """ Print the area Square. """
        if (self.__size == 0):
            print("")
        else:
            for x in range(self.__position[1]):
                print("")

            for z in range(0, self.__size):
                for y in range(0, self.__position[0]):
                    print(" ", end="")
                for i in range(0, self.__size):
                    print("#", end="")
                print(" ")

    pass
