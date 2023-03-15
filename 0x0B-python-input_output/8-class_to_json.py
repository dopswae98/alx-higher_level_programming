#!/usr/bin/python3
"""
Module 8-class_to_json
"""


def class_to_json(obj):
    """
    a function that returns the dictionary description with simple
    data structure (list, dictionary, string, integer and boolean) for
    JSON serialization of an object

    Args:
        obj (object): object

    Return:
        that returns the dictionary description with simple data
        structure
    """
    jsonstr = obj.__dict__
    return jsonstr
