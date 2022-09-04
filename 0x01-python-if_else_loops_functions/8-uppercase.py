#!/usr/bin/python3
def uppercase(str_input):
    for i in range(0, len(str_input)):
        islower = False
        if(ord(str_input[i]) >= 97 and ord(str_input[i]) <= 122):
            islower = True
        if islower:
            ch = chr(ord(str_input[i]) - 32)
        else:
            ch = str_input[i]
        print("{}".format(ch), end="")
    print()
