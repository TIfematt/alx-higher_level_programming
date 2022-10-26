#!/usr/bin/python3
"""
Lookup function
"""


def lookup(obj):
    """
    A function that returns the list of
    available attributes and methods of an object.
    :param obj: the object to be returned
    :return: list
    """
    return dir(obj)
