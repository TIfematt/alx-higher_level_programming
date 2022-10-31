#!/usr/bin/python3
"""
A class Base
"""


class Base:
    """
    A base class for futher tests
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        A method that assign public instance attribute id
        with argument value:

        Return: None

        """

        if self.id is not None:
            self.id = id
        else:
            Base. __nb_objects += 1
            self.id = Base.__nb_objects
