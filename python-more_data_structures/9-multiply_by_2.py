#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_list = a_dictionary.copy()
    for index, element in new_list.items():
        multiply = element * 2
        new_list[index] = multiply
    return new_list
