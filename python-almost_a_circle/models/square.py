#!/usr/bin/python3
"""Square.py"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Initialize the instance """
    def __init__(self, size, x=0, y=0, id=None):
        """ inherit from rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ Print [Square] (<id>) <x>/<y> - <size> """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    """ getter """
    @property
    def size(self):
        """
        Private instance attributes,
        Return width of the Rectangle as a property.
        """
        return self.width

    """ setter """
    @size.setter
    def size(self, value):
        """Sets the width of the Square."""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Assigns an argument to each attribute """
        if len(args) >= 1:
            self.id = args[0]
        if len(args) >= 2:
            self.size = args[1]
        if len(args) >= 3:
            self.x = args[2]
        if len(args) >= 4:
            self.y = args[3]
        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """ Return a represent of dictionario of Square (json :-) -) """
        square_dict = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
        return square_dict
