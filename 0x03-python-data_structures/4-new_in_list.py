#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    my_new_list = my_list.copy()
    length = len(my_new_list)
    if idx > length - 1 or idx < 0:
        return my_new_list
    else:
        my_new_list[idx] = element
        return my_new_list
