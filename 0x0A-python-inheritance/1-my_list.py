#!/usr/bin/python3
""" custom list sorting """


class MyList(list):
    """class to represent custom list
    Attributes
    ----------
    Methods
    -------
    print_sorted():
        prints sorted list (ascending order)
    """
    def print_sorted(self):
        """prints sorted list"""
        sorted_lis = sorted(self)
        print(sorted_lis)
        return sorted_lis
