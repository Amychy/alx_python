#!/usr/bin/python3
"""defines class square """

class Square:
    """ square with size attribute """
    def __init__(self, size):
        self.__size = size

my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)
