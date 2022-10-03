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
