#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    count = 0
    while (i < x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except IndexError:
            raise
        except BaseException:
            i += 1
        else:
            count += 1
            i += 1
    print()
    return count
