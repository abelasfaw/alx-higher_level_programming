#!/usr/bin/python3
"""find peak from unsorted list of integers"""


def find_peak(list_of_integers):
    """Return a peak from a list of unsorted integers"""
    if list_of_integers == []:
        return None
    size = len(list_of_integers)
    if (size == 1):
        return list_of_integers[0]
    elif (size == 2):
        return max(list_of_integers)

    start = 0
    mid = list_of_integers[start+1]
    if (mid > list_of_integers[start] and mid > list_of_integers[start+2]):
        return mid
    else:
        return find_peak(list_of_integers[start+1:])
