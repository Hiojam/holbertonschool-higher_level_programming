#!/usr/bin/python3
""" Task 9 """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initialization of attributes """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a JSON representation of a dictionary of Student class"""
        return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
        }
