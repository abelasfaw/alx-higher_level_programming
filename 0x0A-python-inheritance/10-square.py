#!/usr/bin/python3
"""
    Classes
    -------
    Square
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Class to represent a Square
    ---------------------------
    Attributes
    ----------
    size: int
    ----------
    Methods
    -------
    area()
    -------
    """
    def __init__(self, size):
        """initializes Square object"""
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates area of a square"""
        return self.__size * self.__size
