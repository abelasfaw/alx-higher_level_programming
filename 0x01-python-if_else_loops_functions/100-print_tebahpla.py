#!/usr/bin/python3
if __name__ == "__main__":
    for i in range(122, 96, -2):
        print("{}{}".format(chr(i), chr(i - 33)), end="")
