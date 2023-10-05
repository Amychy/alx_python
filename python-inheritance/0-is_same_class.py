#!/usr/bin/python3
""" module 2-is_same_class contains function is_same_class """


def is_same_class(obj, a_class):
    """ returns True if object is an instance of the specified class """
    return type(obj) == a_class
