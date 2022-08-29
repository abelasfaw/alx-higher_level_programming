#!/usr/bin/python3
def no_c(my_string):
    new_string = []
    for i in range(0, len(my_string)):
        if my_string[i] == 'c' or my_string[i] == 'C':
            continue
        new_string.append(my_string[i])
    return ' '.join(new_string)
