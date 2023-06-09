#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    lengthA = len(tuple_a)
    lengthB = len(tuple_b)

    if lengthA == 0 and lengthB == 0:
        return (0, 0)

    if lengthA == 0 and lengthB > 0:
        return tuple_b
    elif lengthB == 0 and lengthA > 0:
        return tuple_a

    auxA = 0 if lengthA < 2 else tuple_a[1]
    auxB = 0 if lengthB < 2 else tuple_b[1]

    tuple = (tuple_a[0] + tuple_b[0], auxA + auxB)
    return tuple
