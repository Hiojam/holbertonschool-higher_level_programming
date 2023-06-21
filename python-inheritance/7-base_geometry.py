#!/usr/bin/python3
""" Task 7 """


class BaseGeometry:
    """ Creation of classes for future tasks """
    def area(self):
        """ Return Exception area is not implemented """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
