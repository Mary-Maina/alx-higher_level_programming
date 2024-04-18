#!/usr/bin/python3
"""srts a list in ascendin order"""


class MyList(list):
    """
    defines class MyList
    """
    def print_sorted(self):
        """
        print_sorted sorts a list in ascending order
        """
        print(sorted(self))
