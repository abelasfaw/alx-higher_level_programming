#!/usr/bin/python3
def uniq_add(my_list=[]):
    used_elements = []
    result = 0
    for num in my_list:
        if not(num in used_elements):
            result += num
            used_elements.append(num)
    return result
