#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    for x in my_list:
        if idx  == my_list.index(x):
            my_list[x-1] = element
            return my_list
        if idx == 0 and len(my_list) == 1:
            my_list[x-1] = element
            return my_list
        if idx <  0:
            return my_list
        if idx == 1 and len(my_list) == 1:
            return my_list
        if idx > len(my_list):
            return my_list
