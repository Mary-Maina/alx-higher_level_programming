#!/usr/bin/python3
"""Defines the class square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square"""
    def __init__(self, size):
        """
        Initializes size
        Args:
        size: The size of a square, which is to be positive
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
