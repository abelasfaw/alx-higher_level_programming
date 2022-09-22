#!/usr/bin/python3
"""Rectangle module"""


class Rectangle:
    """Rectangle class with private width and height attributes"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if(not isinstance(value, int)):
            raise TypeError("width must be an integer")
        if(value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if(not isinstance(value, int)):
            raise TypeError("height must be an integer")
        if(value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if(self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        res = ""
        if (self.width == 0 or self.height == 0):
            return res
        for i in range(0, self.height):
            for j in range(0, self.width):
                if(self.print_symbol is not None):
                    if(not(isinstance(self.print_symbol, str))):
                        res += repr(self.print_symbol)
                    else:
                        res += self.print_symbol
                else:
                    if(not(isinstance(type(self).print_symbol, str))):
                        res += repr(type(self).print_symbol)
                    else:
                        res += type(self).print_symbol
            if (i != (self.height - 1)):
                res += '\n'
        return res

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
