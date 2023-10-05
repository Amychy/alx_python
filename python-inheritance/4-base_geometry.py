#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """this class represents a base geometry"""

    def __dir__(self):
        """Includes only the attributes and methods explicitly defined in the class."""
        return [attr for attr in self.__dict__.keys() if not callable(getattr(self, attr))]

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
