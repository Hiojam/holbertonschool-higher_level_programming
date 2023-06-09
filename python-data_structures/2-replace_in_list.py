#!/usr/bin/python3

def replace_in_list(my_list, i, element):
    leng = len(my_list)

    if i < 0 or i >= leng:
        return my_list

    my_list[i] = element
    return my_list
