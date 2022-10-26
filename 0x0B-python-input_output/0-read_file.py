#!/usr/bin/python3
"""Defines a function read_file."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding="utf-8") as a_file:
        for a_line in a_file:
            print(a_line, end="")
