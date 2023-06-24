#!/usr/bin/python3
""" Task 1 """


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".

    Returns:
        int: Chars written
    """
    with open(filename, "w+", encoding="utf-8") as f:
        return f.write(text)
