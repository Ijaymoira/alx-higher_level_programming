#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        if idx < 0:
            return None
        elif idx > my_list[-1]:
            return None
        elif idx in my_list:
            return my_list[idx]
