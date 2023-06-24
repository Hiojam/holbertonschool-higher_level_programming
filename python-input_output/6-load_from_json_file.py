#!/usr/bin/python3
""" Task 6 """
import json


def load_from_json_file(filename):
    """Creates an Object from a "Json File"

    Args:
        filename (string): Name of the file
    """
    with open(filename, "r") as f:
        return json.load(f)
