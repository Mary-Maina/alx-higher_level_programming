#!/usr/bin/python3
"Creates a rectangle class and gives attributes"


class Rectangle:
    "It is empty"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        "returns the width of a rectangle"
        return self.__width

    @width.setter
    def width(self, value):
        """gives width a value
        if the width is bot int we have typeerror
        and if it is less than 0 we have valueerror"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        "returns height of a rectangle"
        return self.__height

    @height.setter
    def height(self, value):
        "Assigns height value if it is not less than 0 or not int"
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
