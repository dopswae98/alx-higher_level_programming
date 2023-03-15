#!/usr/bin/python3
"""
Module rectangle
"""
from models.base import Base


class Rectangle(Base):
    """
    class Rectangle that inherits from Base

    Class Rectangle inherits from Base
    Private instance attributes, each with its own public getter and setter:
    __width -> width
    __height -> height
    __x -> x
    __y -> y
    Class constructor: def __init__(self, width, height, x=0, y=0, id=None):
    Call the super class with id - this super call with use the logic of the
    __init__ of the Base class
    Assign each argument width, height, x and y to the right attribute
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        method to initialise the attributes
        """
        super(Rectangle, self).__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        getter method for width
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        setter method for width
        :param width:
        :return:
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = width

    @property
    def height(self):
        """
        getter method for height
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        setter method for height
        :param height:
        :return:
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = height

    @property
    def x(self):
        """
        getter method for x
        :return: x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        setter method for x
        :param x:
        :return:
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = x

    @property
    def y(self):
        """
        getter method for y
        :return: y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        setter method for y
        :param y:
        :return:
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = y

    def area(self):
        """
        method for returning area of a rectangle

        Returns:
            area
        """
        return self.__width * self.__height

    def display(self):
        """
        method that returns area with number of #
        """
        for i in range(self.__height):
            for j in range(self.__width):
                print("#", end='')
            print()

    def __str__(self):
        """
        method that overides Base __str__

        Returns:

        """
        return "[Rectangle] ({}) {}/{} - {}/{}".\
            format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        method that updates dimensions
        """
        length = len(args)

        if length > 0:
            if length == 0:
                pass
            elif length == 1:
                self.id = args[0]
            elif length == 2:
                self.id = args[0]
                self.__width = args[1]
            elif length == 3:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
            elif length == 4:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
            elif length == 5:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
        elif length == 0:
            if "width" in kwargs:
                self.__width = kwargs.get("width")
            if "height" in kwargs:
                self.__height = kwargs.get("height")
            if "x" in kwargs:
                self.__x = kwargs.get("x")
            if "y" in kwargs:
                self.__y = kwargs.get("y")
            if "id" in kwargs:
                self.id = kwargs.get("id")

