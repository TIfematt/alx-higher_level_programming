#!/usr/bin/python3
"""Check if for similar classes
"""


def is_same_class(obj, a_class):
    """
    function that returns true if classes are same
    :param obj: class to be compared
    :param a_class: class to compare with
    :return: True
    """

    if type(obj) == a_class:
        return True
    else:
        return False
