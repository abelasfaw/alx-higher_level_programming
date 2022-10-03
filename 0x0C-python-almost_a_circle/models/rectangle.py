#!/usr/bin/python3
"""Defines a Rectangle type that inherits from
Base class"""


from models.base import Base


class Rectangle(Base):
    """Defines Rectangle type with width, height, x and y
    attributes"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes rectangle instance"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """returns width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets width to given value"""
        self.__width = value

    @property
    def height(self):
        """returns height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to given value"""
        self.__height = value

    @property
    def x(self):
        """returns x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x to given value"""
        self.__x = value

    @property
    def y(self):
        """returns y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y to given value"""
        self.__y = value
