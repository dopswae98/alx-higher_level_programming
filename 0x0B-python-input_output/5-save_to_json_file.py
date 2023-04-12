#!/usr/bin/python3
"""
Module 5-save_to_json_file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    a function that writes an Object to a text file, using a JSON
    representation

    Args:
        my_obj (object): object
        filename (str): name of file

    Return:

    """
    json_object = json.dumps(my_obj)
    with open(filename, mode='w', encoding='UTF8') as my_file:
        my_file.write(json_object)
