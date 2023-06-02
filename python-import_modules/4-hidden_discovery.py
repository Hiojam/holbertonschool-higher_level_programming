#!/usr/bin/python3
import hidden_4

if __name__ != "__main__":
    exit

for e in dir(hidden_4):
    if e.startswith("__"):
        continue
    print(e)
