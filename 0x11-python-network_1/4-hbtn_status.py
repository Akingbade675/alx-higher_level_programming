#!/usr/bin/python3
""" A script that
- fetches https://alx-intranet.hbtn.io/status
- using `requests` package.
"""

if __name__ == "__main__":

    import sys
    import requests

    res = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:\n\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
