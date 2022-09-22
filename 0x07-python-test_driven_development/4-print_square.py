#!/usr/bin/python3
"""module to print a square of given size usng #"""


def print_square(size):
    """function for printing square of size, using #"""
    if(not(isinstance(size, int))):
        raise TypeError("size must be an integer")
    if(size < 0):
        raise ValueError("size must be >= 0")
    for i in range(0, size):
        for j in range(0, size):
            print("#", end="")
        print()
