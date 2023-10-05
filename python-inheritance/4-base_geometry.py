#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """this class represents a base geometry"""

    def __dir__(self):
        """Includes the default attributes and methods and the 'area' method."""
        return dir(type(self)) + ['area']

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
