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
        """Includes only the desired attributes and methods."""
        desired_attrs = [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
            'area', 'integer_validator'
        ]
        return [attr for attr in desired_attrs if attr != '__init_subclass__']

    def __init_subclass__(cls):
        pass
