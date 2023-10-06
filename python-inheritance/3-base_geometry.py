#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""

class BaseGeometry:
    """This class represents a base geometry."""

    def __dir__(self):
        """Includes only the desired attributes and methods."""
        desired_attrs = [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
        ]
        return [attr for attr in desired_attrs if attr != '__init_subclass__']
