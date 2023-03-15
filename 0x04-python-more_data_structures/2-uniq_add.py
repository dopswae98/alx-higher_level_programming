#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_list1 = list(set(my_list))
    for i in range (len(my_list1)):
        sum += my_list1[i]
    return sum
