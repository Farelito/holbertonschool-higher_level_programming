#!/usr/bin/python3

"""Contain a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize the Square instance."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """ Public instance method size ** 2"""

    def area(self):
        return self.__size ** 2
