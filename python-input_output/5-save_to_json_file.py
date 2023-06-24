#!/usr/bin/python3
""" Task 5 """
import json


def save_to_json_file(my_obj, filename):
    """Save a serialized object in JSON to a file

    Args:
        my_obj (object): Object to be serialized
        filename (string): Name of the file to write to
    """
    jsonstr = json.dumps(my_obj)
    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(jsonstr)
