#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry."""

class BaseGeometry:
    """This class represents a base geometry."""

    def area(self):
        """Method not implemented yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.
        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class CustomDirMeta(type):
    def __dir__(cls):
        """Includes only the desired attributes and methods."""
        desired_attrs = [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__',
            'area', 'integer_validator'
        ]
        return desired_attrs

class Rectangle(BaseGeometry):
    """This class represents a rectangle."""

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with a given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height

        """ Validate width and height as positive integers """
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)

""" Explicitly set the metaclass for the Rectangle class """
Rectangle = CustomDirMeta("Rectangle", (Rectangle,), {})
