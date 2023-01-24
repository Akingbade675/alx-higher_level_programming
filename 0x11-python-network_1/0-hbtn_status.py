#!/usr/bin/python3
"""A script that fetches https://alx-intranet.hbtn.io/status
using urllib module.
"""

if __name__ == "__main__":
    import urllib.request as req

    with req.urlopen("https://intranet.hbtn.io/status") as res:
        content = res.read()
        print("Body response:\n\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
