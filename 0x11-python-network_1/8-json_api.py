#!/usr/bin/python3
"""A script that 
- takes in a letter and 
- sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""

if __name__ == "__main__":

    import sys
    import requests

    data = { "q": sys.argv[1] if len(sys.argv) > 1 else "" }

    res = requests.post("http://0.0.0.0:5000/search_user", params=data)
    try:
        json = r.json()
        if json != {}:
            print("[{}] [{}]".format(json['id'], json['name']))
        else:
            print("No result")
    except requests.exceptions.JSONDecodeError as err:
        print("Not a valid JSON")
