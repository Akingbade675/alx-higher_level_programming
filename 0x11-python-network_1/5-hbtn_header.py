#!/usr/bin/python3
"""A script that takes in a URL, 
- sends a request to the URL and 
- displays the value of the variable X-Request-Id in the response header
"""

if __name__ == "__main__":

    import sys
    import requests

    res = requests.get(sys.argv[1])
    print(res.headers.get("X-Request-Id"))
