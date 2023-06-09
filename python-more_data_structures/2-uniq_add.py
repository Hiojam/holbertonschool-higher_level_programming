#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list == []:
        return 0

    acc = 0
    new_list = []

    for element in my_list:
        if element not in new_list:
            new_list.append(element)

    for item in new_list:
        acc = acc + item

    return acc
