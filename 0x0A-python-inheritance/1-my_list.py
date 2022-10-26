#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """
    A class that inherits list
    """

    def print_sorted(self):
        """
        method to sort and print a list
        :return: None
        """

        print(sorted(self))
