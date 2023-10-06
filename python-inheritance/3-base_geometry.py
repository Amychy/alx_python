#!/usr/bin/python3
"""Defines an empty class BaseGeometry."""

class CustomDirMeta(type):
    def __dir__(cls):
        """Includes only the desired attributes and methods."""
        desired_attrs = [
            '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
            '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__',
            '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__',
            '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__'
        ]
        return desired_attrs

class BaseGeometry(metaclass=CustomDirMeta):
    """Represent base geometry."""
    pass
