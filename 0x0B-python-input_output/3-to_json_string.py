#!/usr/bin/python3
import json
"""
    Methods
    -------
    to_json_string(my_obj)
    -------
"""


def to_json_string(my_obj):
    """returns json representation of an object"""

    return json.dumps(my_obj)
