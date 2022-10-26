#!/usr/bin/python3
"""
check for inheritance
"""


def inherits_from(obj, a_class):
    """function that returns True
    if the object is an instance of a class
    that inherited (directly or indirectly)
    from the specified class ; otherwise False.

    :param obj: class to be compared
    :param a_class: class to compare with
    :return: True
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
