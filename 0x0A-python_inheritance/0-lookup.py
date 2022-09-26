#!/usr/bin/python3
def lookup(obj):
    """ returns list of attributes and methods of an object"""
    if(obj is not None):
        return dir(obj)
    return None
