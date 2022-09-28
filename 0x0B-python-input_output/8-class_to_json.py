#!/usr/bin/python3
"""
    Methods
    -------
    class_to_json(obj)
"""


def class_to_json(obj):
    """returns dictionary discription of an object"""
    return obj.__dict__
