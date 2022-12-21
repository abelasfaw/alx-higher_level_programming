#!/usr/bin/python3
""" takes GitHub credentials (username and access token) and uses the GitHub
API to display user id"""


import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    token = sys.argv[2]
    response = requests.get(url, auth=(username, token))
    print(response.json().get('id'))
