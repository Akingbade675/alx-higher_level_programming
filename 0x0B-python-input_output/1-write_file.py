#!/usr/bin/python3
"""Defines a function write_file."""


def write_file(filename="", text=""):
    with open(filename, "w", encoding="utf-8") as a_file:
        return a_file.write(text)
