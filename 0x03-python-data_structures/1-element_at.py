#!/usr/bin/python3
def element_at(my_list, idx):
    for x in my_list:
        length = len(my_list)
        if idx == 0:
            return my_list[idx]
        elif idx < len(my_list):
            return None
        elif idx == 1 and len(my_list) > 1:
            return my_list[idx]
        elif idx == 1 and len(my_list) == 1:
            return None
        else:
            return my_list[idx]
