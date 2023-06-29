#!/usr/bin/python3
"""Rectangle.py"""
from models.base import Base


class Rectangle(Base):
    """ Initialize an instance """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Private instance attributes,
        Return width of the Rectangle as a property.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets the width of the Rectangle. """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Private instance attributes,
        Return height of the Rectangle as a property.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets the height of the Rectangle. """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Private instance attributes,
        Return x of the Rectangle as a property.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """ Sets x of the Rectangle. """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Private instance attributes,
        Return x of the Rectangle as a property.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Private instance attributes,
        Return y of the Rectangle as a property.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ Return the area of the rectangle """
        return self.width * self.height

    def display(self):
        """ Display in stdout the Rectangle instance with the character #"""
        for lines in range(self.y):
            print()
        for element in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """ Print [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        aux = f"{self.width}/{self.height}"
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {aux}")

    def update(self, *args, **kwargs):
        """
            Assigns an argument to each attribute.
        """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.width = args[1]
        if len(args) >= 3:
            self.height = args[2]
        if len(args) >= 4:
            self.x = args[3]
        if len(args) >= 5:
            self.y = args[4]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Return a represent of dictionario of Rectangle """
        rectangle_dict = {
            'y': self.y,
            'x': self.x,
            'id': self.id,
            'width': self.width,
            'height': self.height
        }
        return rectangle_dict
