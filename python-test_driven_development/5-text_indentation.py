#!/usr/bin/python3
"""Task 5"""


def text_indentation(text):
    """ Idents a text """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    matches = [".", "?", ":"]
    i = 0

    while i < len(text):
        if text[i] in matches:
            print("{}\n\n".format(text[i]), end="")
            i += 1
            while text[i] == " ":
                i += 1
        else:
            print("{}".format(text[i]), end="")
            i += 1
