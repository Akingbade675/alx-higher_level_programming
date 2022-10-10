#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    try:
        arg = list(args)
        return fct(*arg)
    except Exception as err:
        print("Exception: {}".format(err), file=stderr)
        return None
