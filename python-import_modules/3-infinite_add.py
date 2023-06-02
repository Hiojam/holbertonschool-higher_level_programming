#!/usr/bin/python3
import sys

if __name__ != "__main__":
    exit

args = sys.argv[1:]
sum = 0

for i in args:
    sum += int(i)

print(sum)
