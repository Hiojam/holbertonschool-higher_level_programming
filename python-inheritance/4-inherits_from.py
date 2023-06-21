#!/usr/bin/python3
""" Task 4 """


def inherits_from(obj, a_class):
    """Return true if obj inherits from a_class (subclass)"""
    if type(obj) == a_class:
        return False
    if issubclass(type(obj), a_class):
        return True
    return False
