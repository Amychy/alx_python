#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """this class represents a base geometry"""

    def __dir__(self):
        """Excludes the 'area' method from the list of attributes."""
        return [attribute for attribute in super().__dir__() if attribute != 'area']

    def area(self):
        """method not implemented yet"""
        raise Exception("area() is not implemented")
