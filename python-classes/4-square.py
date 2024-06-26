#!/usr/bin/python3

"""Contains a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes the Square instance."""
        self.__size = size

    @property
    def size(self):
        return self.__size

    """ that returns the current square area """

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
