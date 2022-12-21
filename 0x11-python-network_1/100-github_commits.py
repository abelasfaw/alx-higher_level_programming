#!/usr/bin/python3
""" takes GitHub credentials (username and access token) and uses the GitHub
API to display user id"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[1],
                                                              sys.argv[2])
    req_data = {"per_page": 10, "page": 1}
    response = requests.get(url, req_data)
    data = response.json()
    for commit in data:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').
                              get('author').get('name')))
