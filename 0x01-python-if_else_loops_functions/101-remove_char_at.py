#!/usr/bin/python3
def remove_char_at(str_input, n):
    new_string = ""
    for i in range(0, len(str_input)):
        if (i != n):
            new_string = new_string + (str_input[i])
    return new_string
