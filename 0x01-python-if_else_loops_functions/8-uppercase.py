#!/usr/bin/python3
def uppercase(str_input):
    for i in range(0, len(str_input)):
        if(ord(str_input[i]) >= 97 and ord(str_input[i]) <= 122):
            print(chr(ord(str_input[i]) - 32), end="")
        else:
            print(str_input[i], end="")
    print()
