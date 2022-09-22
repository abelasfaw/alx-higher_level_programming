#!/usr/bin/python3
"""adds two integers a and b where a and be are integers or floats,
raises a TypeError if a or b are of different types"""


def add_integer(a, b=98):
    """returns sum of a and b"""

    if (not(isinstance(a, int)) and not(isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not(isinstance(b, int)) and not(isinstance(b, float))):
        raise TypeError("b must be an integer")
    if(isinstance(a, float)):
        a = int(a)
    if(isinstance(b, float)):
        b = int(b)
    return a + b
