#!/usr/bin/python3
""" Task 3 """
import json


def to_json_string(my_obj):
    """Converts an object into a JSON string

    Args:
        my_obj (object): The object to be converted
    """
    return json.dumps(my_obj)
