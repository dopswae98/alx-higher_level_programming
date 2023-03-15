#!/usr/bin/python3
"""
Module 2-append_write
"""


def append_write(filename="", text=""):
    """
    a function that appends a string at the end of a text file (UTF8) and
    returns the number of characters added

    Args:
        filename (): name of file
        text (str): text to be appended

    Returns:
        returns the number of characters added
    """
    with open(filename, mode='a', encoding='UTF8') as my_file:
        my_file.write(text)
        return len(text)
