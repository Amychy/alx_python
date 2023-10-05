#!/usr/bin/python3
""" module 3-is_kind_of_class contains function is_kind_of_class """

def is_kind_of_class(obj, a_class):
    """ returns True if object is an instance of the
    class or of a class that class inherited from """
    return isinstance(obj, a_class)
