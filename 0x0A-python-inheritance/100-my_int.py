#!/usr/bin/python3
"""Defines clas MyInt which inherits from int"""


class MyInt(int):
    """My int converts "==" to "!=" and vice verse
    in other words, returns the invert


    consider __eq__: a method that checks if int are equal
    consider __ne__: method to check int are not equal
    """
    def __eq__(self, other):
        """override the eq and return the opposite"""
        return super().__ne__(other)

    def __ne__(self, other):
        """override the not equal to"""
        return super().__eq__(other)
