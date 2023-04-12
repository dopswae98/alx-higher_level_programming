#!/usr/bin/python3
"""
Module 0-read_file
"""


def read_file(filename=""):
    """
    a function that reads a text file (UTF8) and prints it to stdout

    Args:
        filename (): name or path of a file

    Returns:
        prints text to stdout
    """
    with open(filename, mode='r', encoding='UTF8') as my_file:
        print(my_file.read())
