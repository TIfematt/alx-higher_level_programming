#!/usr/bin/python3
"""AppendFile
"""


def append_write(filename="", text=""):
    """A  function that appends a string
    at the end of a text file (UTF8)
    and returns the number of characters added"""
    with open(filename, mode='a', encoding='UTF8') as appendFile:
        return appendFile.write(text)
