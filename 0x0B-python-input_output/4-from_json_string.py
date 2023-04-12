#!/usr/bin/python3
"""
Module 4-from_json_string
"""
import json


def from_json_string(my_str):
    """
    a function that returns an object (Python data structure) represented
    by a JSON string

    Args:
        my_str (str):

    Return:
        returns an object (Python data structure) represented by a JSON
        string
    """
    return json.loads(my_str)
