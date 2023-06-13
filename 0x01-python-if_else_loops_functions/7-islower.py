#!/usr/bin/python3
def islower(c):
    j = ord(c)
    if j >= 97 and j <= 122:
        return True
    if j >= 67 and j <= 93:
        return False
