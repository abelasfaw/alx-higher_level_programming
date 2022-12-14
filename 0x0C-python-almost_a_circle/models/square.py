#!/usr/bin/python3
"""Contains a class that defines Square type"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square type"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of instance"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """returns size of square"""
        return self.width

    @size.setter
    def size(self, value):
        """sets width and height to given value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """updates values of attributes"""
        if(args is not None and len(args) != 0):
            index = 0
            for arg in args:
                if(index == 0):
                    self.id = arg
                elif(index == 1):
                    self.size = arg
                elif(index == 2):
                    self.x = arg
                elif(index == 3):
                    self.y = arg
                index += 1
        else:
            if("id" in kwargs):
                self.id = kwargs["id"]
            if("size" in kwargs):
                self.size = kwargs["size"]
            if("x" in kwargs):
                self.x = kwargs["x"]
            if("y" in kwargs):
                self.y = kwargs["y"]

    def to_dictionary(self):
        """dictionary representation of instance"""
        result = dict()
        keys = ["id", "size", "size", "x", "y"]
        index = 0
        for key, value in self.__dict__.items():
            result[keys[index]] = value
            index += 1
        return result
