#!/usr/bin/python3

def new_in_list(my_list, i, element):
    leng = len(my_list)
    if not my_list or i < 0 or i >= leng:
        return my_list

    new_list = my_list.copy()
    new_list[i] = element
    return new_list
