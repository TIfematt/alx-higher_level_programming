#!/usr/bin/python3
"""Write_file
"""


def write_file(filename="", text=""):
    """A function that writes a string to a text file (UTF8)
    and returns the number of characters written"""
    with open(filename, mode='w', encoding='UTF8') as writeFile:
        return writeFile.write(text)
