#!/usr/bin/python3
"""
    Classes
    -------
    MyInt
    -------
    Methods
    __eq__(obj)
    __new__(obj
    --------
"""


class MyInt(int):
    """MyInt class that inherits from int"""

    def __eq__(self, obj):
        """compares instance with obj and returns True
        if they are different, else return False"""

        if(isinstance(obj, int)):
            if(self > obj or self < obj):
                return True
            else:
                return False
        else:
            return True

    def __ne__(self, obj):
        """compares instance with obj and returns True
        if they are the same, else returns False"""

        return not (self.__eq__(obj))
