#!/usr/bin/python3
""" Task 0 """


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout.

    Args:
        filename (str, optional): Name of the file. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(line, end='')
        print("")
