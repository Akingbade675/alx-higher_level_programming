#!/usr/bin/python3
"""Defines a function say_my_name()."""


def say_my_name(first_name, last_name=""):
    """
    Prints my name.

    Args:
        first_name (str): first name
        last_name (str): last name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")

    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
