#!/usr/bin/python3
"""A script that
- lists the 10 most recent commits on a given GitHub repository.
"""

if __name__ == "__main__":

    import sys
    import requests

    repo = sys.argv[1]
    owner = sys.argv[2]

    passwd = "github_pat_11AZQH3YA037jHwR3NERGY_vied30J1eWdX\
8NegSKm8E2DfeAaOFTYGlN65DSwpAyPEV5EMK6Gw3RVIrWr"
    url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)

    headers = {"Accept": "application/vnd.github+json"}

    res = requests.get(url, headers=headers, auth=(owner, passwd))
    commits = res.json()

    try:
        for i in range(10):
            print("{}: {}".format(
                commits[i].get('sha'),
                commits[i].get('commit').get('author').get('name')))
    except IndexError:
        pass
