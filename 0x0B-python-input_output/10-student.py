#!/usr/bin/python3
"""
    Classes
    -------
    Student
    -------
    Attributes
    ----------
    first_name
    last_name
    age
    ---------
    Methods
    -------
    to_json()
"""


class Student:
    """class to represent student"""

    def __init__(self, first_name, last_name, age):
        """initializes a student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictionary representation of instance"""
        if(attrs is not None):
            for element in attrs:
                if(type(element) != str):
                    return self.__dict__
            return dict((key, self.__dict__[key]) for key in attrs
                        if key in self.__dict__)
        return self.__dict__
