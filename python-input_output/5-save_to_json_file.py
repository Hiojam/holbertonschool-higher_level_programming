#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    """Save a serialized object in JSON to a file

    Args:
        my_obj (object): Object to be serialized
        filename (string): Name of the file to write to
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
