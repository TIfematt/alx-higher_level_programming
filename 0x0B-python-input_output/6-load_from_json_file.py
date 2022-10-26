#!/usr/bin/python3
"""create object from json
"""


def load_from_json_file(filename):
    """A function that creates an Object from a “JSON file”
    """
    import json
    with open(filename, mode='r', encoding='UTF8') as file:
        return json.load(file)
