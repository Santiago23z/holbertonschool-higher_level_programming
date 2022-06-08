#!/usr/bin/python3
import json
"""
contains Object to a text file, using a JSON
"""


def save_to_json_file(my_obj, filename):
    """function open"""
    with open(filename, mode="w") as f:
        json.dump(my_obj, f)
