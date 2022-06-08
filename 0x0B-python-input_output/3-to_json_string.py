#!/usr/bin/python3
from json import dumps
"""
contains json functions import
"""


def to_json_string(my_obj):
    """Write a function that returns the JSON 
    representation of an object (string):"""
    return dumps(my_obj)
