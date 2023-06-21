#!/usr/bin/python3
""" Task 2 """


def is_same_class(obj, a_class):
    """True if the object is exactly an instance of class, otherwise False"""
    if obj is None:
        return False
    if not type(obj) is a_class:
        return False
    return True
