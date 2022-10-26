#!/usr/bin/python3
"""ReadFile
"""


def read_file(filename=""):
    """A function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, mode='r', encoding="UTF8") as readFile:
        print(readFile.read(), end='')
