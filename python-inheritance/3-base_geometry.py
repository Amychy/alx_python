#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """This class represents a base geometry."""

    def __dir__(self):
        """Includes only the desired attributes and methods."""
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

    def area(self):
        """Method not implemented yet."""
        raise Exception("area() is not implemented")
