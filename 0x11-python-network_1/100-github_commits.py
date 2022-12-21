#!/usr/bin/python3
""" takes GitHub credentials (username and access token) and uses the GitHub
API to display user id"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(sys.argv[2],
                                                              sys.argv[1])
    response = requests.get(url)
    data = response.json()
    for commit in data[:10]:
        print("{}: {}".format(commit.get('sha'), commit.get('commit').
                              get('author').get('name')))
