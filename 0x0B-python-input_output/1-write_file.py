#!/usr/bin/python3
"""
    Methods
    -------
    write_file(filename, text)
    -------
"""


def write_file(filename="", text=""):
    """writes a string to a text file and return number
    of characters written"""

    if(filename is not None):
        with open(filename, 'w', encoding="utf-8") as f:
            return f.write(text)
