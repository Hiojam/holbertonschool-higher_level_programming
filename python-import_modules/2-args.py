#!/usr/bin/python3
import sys

if __name__ != "__main__": exit

len = len(sys.argv) - 1
element = 0

if len != 1:
    print("{} arguments.".format(len))
else:
    print("{} argument:".format(len))

if (len > element):
    for element in range(1, len + 1):
        print("{0}: {1}".format(element, sys.argv[element]))
