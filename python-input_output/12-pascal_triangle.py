#!/usr/bin/python3
""" Task 12 """


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row

    for i in range(1, n):
        row = [1]  # First element of each row is always 1
        for j in range(1, i):
            # Calculate the sum of the two numbers above
            sum_above = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(sum_above)
        row.append(1)  # Last element of each row is always 1
        triangle.append(row)

    return triangle
