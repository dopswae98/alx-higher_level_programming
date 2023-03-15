#!/usr/bin/python3
"""This module demostrates addition function and test it
a and b must be integers or floats, otherwise raise a TypeError exception
with the message a must be an integer or b must be an integer
a and b must be first casted to integers if they are float
Returns an integer: the addition of a and b"""

def add_integer(a, b=98):
    """It adds two integers
    Arguments: a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    else:
        return int(a + b)
