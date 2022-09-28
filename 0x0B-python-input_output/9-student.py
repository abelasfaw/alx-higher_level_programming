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

    def to_json(self):
        """returns dictionary representation of instance"""
        return self.__dict__
