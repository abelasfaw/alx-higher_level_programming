#!/usr/bin/python3
"""
    Methods
    -------
    save_arguments()
    -------
"""


import json
import os
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


if __name__ == "__main__":
    filename = "add_item.json"
    if(os.path.isfile(filename)):
        arg_list = load_from_json_file(filename)
        if(len(sys.argv) != 1):
            for i in range(1, len(sys.argv)):
                arg_list.append(sys.argv[i])
        save_to_json_file(arg_list, filename)
    else:
        arg_list = []
        if(len(sys.argv) != 1):
            for i in range(1, len(sys.argv)):
                arg_list.append(sys.argv[i])
        save_to_json_file(arg_list, filename)
