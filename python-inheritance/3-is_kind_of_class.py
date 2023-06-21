#!/usr/bin/python3
""" Task 3 """


def is_kind_of_class(obj, a_class):
    """
        returns True if the object is an instance,
        or if the object is an instance of a class
        that inherited from
    """
    if isinstance(obj, a_class):
        return True
    return False
