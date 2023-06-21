#!/usr/bin/python3
""" Task 1 """


class MyList(list):
    """ Prints the list, but sorted in ascending sort """

    def print_sorted(self):
        if hasattr(self, '__str__'):
            print(sorted(self))
            return (sorted(self))
