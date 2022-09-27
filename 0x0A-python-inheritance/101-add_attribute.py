#!/usr/bin/python3
"""
    Methods
    -------
    add_attribute(obj, attr, value)
    -------
"""


def add_attribute(obj, attr, value):
    """sets attribute to an object"""

    if(obj is not None):
        if(not(hasattr(obj, '__dict__'))):
            raise TypeError("can't add new attribute")
        for key in obj.__dict__:
            if(key == attr):
                raise TypeError("can't add new attribute")
        setattr(obj, attr, value)
