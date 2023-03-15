#!/usr/bin/python3
""" a class Square that defines a square by: (based on 5-square.py)

Private instance attribute: size:
    property def size(self): to retrieve it
    property setter def size(self, value): to set it:
        size must be an integer, otherwise raise a TypeError exception with
        the message size must be an integer
        if size is less than 0, raise a ValueError exception with the message
        size must be >= 0
        Private instance attribute: position:
            property def position(self): to retrieve it
            property setter def position(self, value): to set it:
                position must be a tuple of 2 positive integers, otherwise
                raise a TypeError exception with the message position must be
                a tuple of 2 positive integers
                Instantiation with optional size and optional position:
                def __init__(self, size=0, position=(0, 0)):
                    Public instance method: def area(self): that
                    returns the current square area
                    Public instance method: def my_print(self):
                    that prints in stdout the square with the character #:
                    if size is equal to 0, print an empty line
                    position should be use by using space - Don’t fill line
                    s by spaces when position[1] > 0
"""


class Square:
    """Represents a square class
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size to a value."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieves the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position to a value."""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints to stdout the square with the character #,
        at the position given by the position attribute.
        """
        if self.__size == 0:
            print()
            return
        for y in range(0, self.__position[1]):
            print()
        for i in range(0, self.__size):
            for x in range(0, self.__position[0]):
                print(" ", end="")
            for j in range(0, self.__size):
                print("#", end="")
            print()
