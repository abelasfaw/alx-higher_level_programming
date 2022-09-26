#!/usr/bin/python3
"""check instance type"""


def is_kind_of_class(obj, a_class):
    """checks if obj is instance of a_class or base class \
            of a class"""
    return isinstance(obj, a_class)
