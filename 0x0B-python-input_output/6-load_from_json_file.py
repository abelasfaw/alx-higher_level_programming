#!/usr/bin/python3
"""
    Methods
    -------
    load_from_json_file(filename)
    -------
"""


import json


def load_from_json_file(filename):
    """creates an Object from JSON file"""
    if(filename is not None):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
