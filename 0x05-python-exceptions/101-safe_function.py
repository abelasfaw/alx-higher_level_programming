#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        if(len(args) == 0):
            arg1 = arg2 = None
        if(len(args) == 1):
            arg1 = args[0]
            arg2 = None
        elif(len(args) == 2):
            arg1 = args[0]
            arg2 = args[1]
        return (fct(arg1, arg2))
    except BaseException as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return None
