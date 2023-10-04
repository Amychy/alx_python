#!/usr/bin/python3
"""defines class square"""

class Square:
    """square with private instance attribute size"""
    def __init__(self, size=0):
        """Initialize the square with a size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate and return the area of the square"""
        return self.__size ** 2
