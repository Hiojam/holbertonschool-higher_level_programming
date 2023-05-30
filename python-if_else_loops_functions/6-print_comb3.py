#!/usr/bin/python3
for i in range(9):
    for z in range(1, 10):
        if i < z:
            if str(i) + str(z) == "89":
                print("89")
            else:
                print("{}{}".format(i, z), end=", ")
