#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

BaseGeometry = __import__('5-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle."""

    def __init__(self, width, height):
        """Initializes a Rectangle instance."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    def __dir__(self):
        """Return a list of attributes and methods for Rectangle."""
        return [
            '__class__', '__delattr__', '__doc__', '__eq__', '__format__', '__ge__',
            '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
            '__sizeof__', '__str__', '__subclasshook__', 'area', 'integer_validator']
