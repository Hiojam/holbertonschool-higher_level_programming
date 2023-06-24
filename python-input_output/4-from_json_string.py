#!/usr/bin/python3
""" Task 4 """
import json


def from_json_string(my_str):
    """Turns a JSON string into an Object

    Args:
        my_str (string): Json serialized string
    """
    return json.loads(my_str)
