#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if len(my_list) == 0 or my_list == []:
        return []

    # comprehension checklist - iterates on element.
    multiply = [True if element % 2 == 0 else False for element in my_list]
    return multiply
