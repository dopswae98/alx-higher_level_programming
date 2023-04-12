#!/usr/bin/python3
"""
Module 1-write_file
"""


def write_file(filename="", text=""):
    """
    a function that writes a string to a text file (UTF8) and returns the
    number of characters written

    Args:
         filename ():name of file
         text (str): text to be written

    Returns:
        returns the number of characters written
    """
    with open(filename, mode='w', encoding='UTF8') as my_file:
        my_file.write(text)
        return len(text)
