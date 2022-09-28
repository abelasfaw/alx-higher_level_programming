#!/usr/bin/python3
"""
    Methods
    -------
    append_write(filename, text)
    -------
"""


def append_write(filename="", text=""):
    """appends a string at the end of a text file and return number
    of characters added"""

    if(filename is not None):
        with open(filename, 'a', encoding="utf-8") as f:
            return f.write(text)
