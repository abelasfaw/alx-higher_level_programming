#!/usr/bin/python3
"""
    Classes:
        Rectangle
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class to represent a Rectangle and is a subclass
    of BaseGeometry
    Attributes
    ----------
    width: int
        width of rectangle
    height: height
        height of rectangle
    """
    def __init__(self, width, height):
        """initializes a rectangle object with height and width"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """calculates area of rectangle (area = width * height)"""
        return self.__height * self.__width

    def __str__(self):
        """String representation of Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def __repr__(self):
        """String representaion of Rectangle instance"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
