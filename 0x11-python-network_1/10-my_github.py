#!/usr/bin/python3
"""A script that 
- takes my GitHub credentials (username and password) 
- and uses the GitHub API to display your id.
"""

if __name__ == "__main__":

    import sys
    import requests

    user = sys.argv[1]
    passwd = sys.argv[2]
    res = requests.get("https://api.github.com/user", auth=(user, passwd))
    print(res.json().get('id'))
