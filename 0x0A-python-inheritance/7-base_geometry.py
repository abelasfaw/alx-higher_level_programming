#!/usr/bin/python3
"""Base module for geometry type"""


class BaseGeometry:
    """Class to represen Base Geometry
    ...
    Methods
    -------
    area():
        raises an Exception with custome message
    integer_validator(name, value):
        -checks if value is integer: if not raises a
        TypeError exception
        -checks if value is greater than 0: if not raises a
        ValueError exception
    """

    def area(self):
        """ raises an Exception with area() is not
        implemented message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates if number is an integer and
        greater than 0, if not raises an exception
        with custom message"""
        if(type(value) != int):
            raise TypeError("{} must be an integer".format(name))
        if(value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
