#!/usr/bin/python3
"""Checks of object is of a specificed class"""


def is_same_class(obj, a_class):
    """
    Checks if object belongs to a class

    Args:
    obj: Object
    a_class: class

    Returns:
    True if it belongs to the class, otherwise false
    """
    x = type(obj)
    if x == a_class:
        return True
    else:
        return False
