#!/usr/bin/python3
"""load python object
"""


def from_json_string(my_str):
    """unction that returns an object (Python data structure)
    represented by a JSON string
    """
    import json
    return json.loads(my_str)
