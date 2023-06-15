#!/usr/bin/python3
""" Task 5 """


class Square:
    """A class representing a square."""

    def __init__(self, size=0, pos=(0, 0)):
        if (type(size) != int):
            raise TypeError("size must be an integer")
        
        if (size < 0):
            raise ValueError("size must be >= 0")
        
        self.__size = size
        self.__position = pos

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
            raise TypeError("position must be a tuple of 2 positive integers")
        
        try:
            if (isinstance(value[0], int) and isinstance(value[1], int)):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                else:
                    raise ValueError("position must be a tuple of 2 positive integers")
            else:
                raise TypeError("position must be a tuple of 2 positive integers")
        except IndexError:
            print("position must be a tuple of 2 positive integers")
                
    pass
