#!/usr/bin/python3
"""checks if obj is an instance of class or base class"""


def is_kind_of_class(obj, a_class):
    """
    checks if obj is an instance of class or base class

    Args:
    obj: object
    a_class: The class

    Return:
    True if it belongs to class
    ortherwise false
    """
    return (isinstance(obj, a_class))
