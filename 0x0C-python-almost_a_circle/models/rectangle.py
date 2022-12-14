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
        if(type(value) != int):
            raise TypeError("width must be an integer")
        if(value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets height to given value"""
        if(type(value) != int):
            raise TypeError("height must be an integer")
        if(value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns x property"""
        return self.__x

    @x.setter
    def x(self, value):
        """sets x to given value"""
        if(type(value) != int):
            raise TypeError("x must be an integer")
        if(value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """sets y to given value"""
        if(type(value) != int):
            raise TypeError("y must be an integer")
        if(value < 0):
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns area of a circle"""
        return self.__width * self.__height

    def display(self):
        """prints rectangle with #character"""
        for x in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for y in range(0, self.__x):
                print(" ", end='')
            for j in range(0, self.__width):
                print("#", end='')
            if(i != self.__height):
                print()

    def __str__(self):
        """string representation of instance"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if(args is not None and len(args) != 0):
            index = 0
            for arg in args:
                if(index == 0):
                    self.id = arg
                elif(index == 1):
                    self.width = arg
                elif(index == 2):
                    self.height = arg
                elif(index == 3):
                    self.x = arg
                elif(index == 4):
                    self.y = arg
                index += 1
        else:
            if("width" in kwargs):
                self.width = kwargs["width"]
            if("height" in kwargs):
                self.height = kwargs["height"]
            if("x" in kwargs):
                self.x = kwargs["x"]
            if("y" in kwargs):
                self.y = kwargs["y"]
            if("id" in kwargs):
                self.id = kwargs["id"]

    def to_dictionary(self):
        """dictionary represntation of instance"""
        keys = ["id", "width", "height", "x", "y"]
        index = 0
        result = dict()
        for key, value in self.__dict__.items():
            result[keys[index]] = value
            index += 1
        return result
