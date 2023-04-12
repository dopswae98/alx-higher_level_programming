#!/usr/bin/python3
"""
Module 6-load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    a function that creates an Object from a “JSON file”

    Args:
        filename:

    Return:

    """
    with open(filename, mode='r', encoding='UTF8') as my_file:
        data = json.load(my_file)
        return data
