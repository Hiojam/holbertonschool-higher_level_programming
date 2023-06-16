#!/usr/bin/python3
"""Task 2"""


def matrix_divided(matrix, div):
    """Divide a matrix."""
    error = "matrix must be a matrix (list of lists) of integers/floats"
    size_error = "Each row of the matrix must have the same size"

    if (not isinstance(matrix, list) or
            not all(isinstance(element, list) for element in matrix)):
        raise TypeError(error)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    buffer_row = []
    len_original_row = len(matrix[0])

    for row in matrix:
        if len_original_row != len(row):
            raise TypeError(size_error)
        for element in row:
            if isinstance(element, (int, float)):
                buffer_row.append(round(element / div, 2))
            else:
                raise TypeError(error)
        new_matrix.append(buffer_row)
        buffer_row = []
    return new_matrix
