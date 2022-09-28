#!/usr/bin/python3
"""
    Methods
    -------
    read_file(filename)
    -------
"""


def read_file(filename=""):
    """read a text file and prints to stdout"""

    with open(filename, encoding="utf-8") as f:
        print(f.read())
