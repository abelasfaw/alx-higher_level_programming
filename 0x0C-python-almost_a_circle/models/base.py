#!/usr/bin/python3
"""module containing Base class, this class will be used
by other modules in these package"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation of input"""
        if(list_dictionaries is None or len(list_dictionaries) == 0):
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json representation of input to file"""
        filename = str(cls.__name__) + ".json"
        dicts = []
        if(list_objs is None):
            with open(filename, 'w') as file:
                file.write(str(dicts))
            return
        for obj in list_objs:
            dicts.append(obj.to_dictionary())
        filename = str(cls.__name__) + ".json"
        js = Base.to_json_string(dicts)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(js)

    @staticmethod
    def from_json_string(json_string):
        """reutrns list of json string representation"""
        result = []
        if(json_string is None or len(json_string) == 0):
            return result
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns a new instance with provided attribute values"""
        if(cls.__name__ == "Rectangle"):
            new_instance = cls(1, 1, 0, 0)
        else:
            new_instance = cls(1)
        new_instance.update(**dictionary)
        return new_instance
