#!/usr/bin/python3
def weight_average(my_list=[]):
    total = 0
    weight = 0
    if len(my_list) == 0:
        return 0
    for element in my_list:
        total += element[0] * element[1]
        weight += element[1]
    return total / weight
