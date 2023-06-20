#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        if idx == my_list.index(x):
            return my_list[idx]
        if idx < 0:
            return None
        if idx == 0 and len(my_list) == 1:
            return my_list[idx]
        if idx == 1 and len(my_list) == 1:
            return None
        if idx > len(my_list):
            return None
