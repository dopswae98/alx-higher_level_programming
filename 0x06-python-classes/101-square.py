#!/usr/bin/python3
 """a class Square that defines a square by: (based on 6-square.py)

 Private instance attribute: size:
 property def size(self): to retrieve it
 property setter def size(self, value): to set it:
 size must be an integer, otherwise raise a TypeError exception with the
 message size must be an integer
 if size is less than 0, raise a ValueError exception with the message size
 must be >= 0
 Private instance attribute: position:
 property def position(self): to retrieve it
 property setter def position(self, value): to set it:
 position must be a tuple of 2 positive integers, otherwise raise a TypeError
 exception with the message position must be a tuple of 2 positive integer
 Instantiation with optional size and optional position:
 def __init__(self, size=0, position=(0, 0)):
 Public instance method: def area(self): that returns the current square area
 Public instance method: def my_print(self): that prints in stdout the square
 with the character #:
 if size is equal to 0, print an empty line
 position should be use by using space
 Printing a Square instance should have the same behavior as my_print()
 """


class Square:
    """Represents a square.
    Private instance attribute: size:
        - property def size(self)
        - property setter def size(self, value)
    Private instance attribute: position:
        - property def position(self)
        - property setter def position(self, value)
    Instantiation with optional size and optional position.
    Public instance method: def area(self).
    Public instance method: def my_print(self).
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes the data."""
        self.__size = size
        self.__position = position

    def __str__(self):
        """Str method for print from main module."""
        my_str = ""
        if self.__size == 0:
            return ''
        else:
            my_str += '\n' * self.__position[1]
            for i in range(0, self.__size):
                my_str += ' ' * self.__position[0]
                my_str += '#' * self.__size
                my_str += '\n'
            return my_str[:-1]

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
        else:
            for y in range(0, self.__position[1]):
                print()
            for i in range(0, self.__size):
                for x in range(0, self.__position[0]):
                    print(" ", end="")
                for j in range(0, self.__size):
                    print("#", end="")
                print()
            return ''
