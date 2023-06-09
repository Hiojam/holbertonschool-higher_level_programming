#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    separator = " "

    if not matrix:
        return

    for row in matrix:
        print(separator.join("{:d}".format(element) for element in row))
