#!/usr/bin/python3
"""save obj to json file
"""


def save_to_json_file(my_obj, filename):
    """A function that writes an Object
    to a text file, using a JSON representation"""
    import json
    with open(filename, mode='w', encoding='UTF8') as file:
        json.dump(my_obj, file, indent=4)
