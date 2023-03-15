#!/usr/bin/python3
def element_at(my_list, idx):
    length_my_list = len(my_list)
    if idx > length_my_list - 1 or idx < 0:
        return "None"
    else:
        return my_list[idx]
