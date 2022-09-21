#!/usr/bin/python3
"""module with a single class with restricted dynamic attribure"""


class LockedClass:
    """Class with only single dynamic attribute allowed """

    __slots__ = ['first_name']
