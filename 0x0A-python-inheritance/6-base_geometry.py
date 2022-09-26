#!/usr/bin/python3
"""Base module for geometry type"""


class BaseGeometry:
    """Class to represen Base Geometry
    ...
    Methods
    -------
    area():
        raises an Exception with custome message
    """

    def area(self):
        """ raises an Exception with area() is not
        implemented message"""
        raise Exception("area() is not implemented")
