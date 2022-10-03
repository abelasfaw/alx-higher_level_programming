#!/usr/bin/python3
"""Contains a class that defines Square type"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines Square type"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
