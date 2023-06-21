#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    for x in new_list:
        if idx == new_list.index(x):
            new_list[x-1] = element
            return new_list
        if idx == 0 and len(new_list) == 1:
            new_list[x-1] = element
            return new_list
        if idx < 0:
            return new_list
        if idx == 1 and len(new_list) == 1:
            return new_list
        if idx >= len(new_list):
            return new_list
