#!/usr/bin/python3
def uppercase(str):
    for x in str:
        j = ord(x)
        if j >= 97 and j<= 122:
            j  = j - 32
            print("{:s}".format(chr(j)), end="")
        else:
            print("{:s}".format(chr(j)), end="")
