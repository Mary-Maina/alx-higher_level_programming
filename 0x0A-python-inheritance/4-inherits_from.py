#!/usr/bin/python3
"""Returns true if obj is from an inherited class"""


def inherits_from(obj, a_class):
    """
    Returns true if obj is from an inherited class

    Args:
    obj: Object
    a_class: Class

    Returns:
    True if it is fro an inherited class,
    otherwise false
    """
    x = type(obj)
    if issubclass(x, a_class) and x != a_class:
        return True
    else:
        return False
