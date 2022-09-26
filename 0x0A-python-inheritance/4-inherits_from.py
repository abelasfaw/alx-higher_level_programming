#!/usr/bin/python3
""" check if an object inherited from a class"""


def inherits_from(obj, a_class):
    """checks if obj is a subclass of a_class"""
    if(type(obj) == a_class):
        return False
    return issubclass(type(obj), a_class)
