#!/usr/bin/python3
"""
    Methods
    -------
    save_to_json_file(my_obj, filename)
    -------
"""


import json


def save_to_json_file(my_obj, filename):
    """writes json representation of an object to file"""
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
