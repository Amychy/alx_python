#!/usr/bin/python3
""" module 4-inherits_from contains function inherits_from """

def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited (directly or indirectly) from a_class; otherwise False."""
    return issubclass(type(obj), a_class) and type(obj) != a_class
