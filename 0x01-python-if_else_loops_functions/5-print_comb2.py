#!/usr/bin/python3
for x in range(0, 100):
    if x < 99:
        print("{:02d}".format(x), end=", ")
    if x > 98:
        print("{:d}".format(x))
