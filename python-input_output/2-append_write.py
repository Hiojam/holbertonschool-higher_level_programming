#!/usr/bin/python3
""" Task 2 """


def append_write(filename="", text=""):
    """Appends a string to a text file

    Args:
        filename (str, optional): Name of the file. Defaults to "".
        text (str, optional): Text to be written. Defaults to "".

    Returns:
        int: Chars appended
    """
    with open(filename, "a+", encoding="utf-8") as f:
        return f.write(text)
