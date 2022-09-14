#!/usr/bin/python3
"""module with single square class"""


class Square:
    """Square class with size property, area calculating method
    ,setter and getter"""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if(not(isinstance(value, int))):
            raise TypeError("size must be an integer")
        if(value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if(not(isinstance(value, tuple))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(not(isinstance(value[0], int)) or not(isinstance(value[1], int))):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(not(value[0] >= 0) or not(value[1] >= 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if(self.__size == 0):
            print()
        else:
            if(self.__position[1] != 0):
                for x in range(0, self.__position[1]):
                    print()
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()

    def __str__(self):
        result = ""
        if(self.__size == 0):
            return result
        else:
            if(self.__position[1] != 0):
                for x in range(0, self.__position[1]):
                    result += '\n'
            for i in range(0, self.__size):
                for k in range(0, self.__position[0]):
                    result += " "
                for j in range(0, self.__size):
                    result += "#"
                if(i != (self.__size - 1)):
                    result += '\n'
            return result
