#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        ch = ord(str[i])
        if ch >= 97 and ch <= 122:
            ch = ch - 32
        print("{}".format(chr(ch)), end="")
    print("")
