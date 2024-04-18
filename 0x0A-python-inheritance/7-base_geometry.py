#!/usr/bin/python3
"""Inputs method area in BaseGeometry"""


class BaseGeometry():
    """
    Looks at the method area
    Raises an Exception
    """
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value
        Args:
            name = name of obj
            value = value of obj
        Raises:
            TypeError: when not int
            ValueError: when int is less or equal to 0"""

        self.name = name
        self.value = value

        if type(value) != int:
            raise TypeError("{} must be an integer".format(self.name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
