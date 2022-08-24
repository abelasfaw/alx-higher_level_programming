#!/usr/bin/python3
def pow(a, b):
    if (b == 0):
        return 1
    else:
        result = 1
        for i in range(0, b):
            result *= a
    return result
