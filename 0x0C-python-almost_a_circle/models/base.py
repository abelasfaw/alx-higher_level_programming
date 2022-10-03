#!/usr/bin/python3
"""module containing Base class, this class will be used
by other modules in these package"""


class Base:
    """Base class with private class attribute
    _nb_objects"""

    _nb_objects = 0

    def __init__(self, id=None):
        """initializes instance based on id value passed"""

        if(id is not None):
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base._nb_objects
