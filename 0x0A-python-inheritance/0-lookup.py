#!/usr/bin/python3
"""returns the attributes and methods of an object"""


def lookup(obj):
    """ returns att and methods
    arg:
    obj: object
    returns:
    List
    """
    return dir(obj)
