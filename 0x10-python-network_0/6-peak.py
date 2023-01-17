#!/usr/bin/python3
"""Define a function `find_peak`."""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    ints = sorted(list_of_integers)
    return str(ints[-1]) if ints else "None"
