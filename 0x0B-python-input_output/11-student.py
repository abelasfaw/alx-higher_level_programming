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
    reload_from_json(json)
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

    def reload_from_json(self, json):
        """replace all attributes of instance with elements in json"""
        if(len(json)):
            for key in json:
                self.key = json[key]
        else:
            for key in self.__dict__:
                self.key = None
        self.__dict__ = json
