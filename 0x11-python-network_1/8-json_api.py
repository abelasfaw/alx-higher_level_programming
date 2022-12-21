#!/usr/bin/python3
"""takes in a letter and sends POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.If the response body is properly JSON formatted
and not empty, display the id and name.Else, Display Not a valid JSON if the
JSON is invalid, Display No result if the JSON is empty"""


import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    params = {"q": letter}
    response = requests.post(url, data=params)
    try:
        response = response.json()
        _id, name = response.get('id'), response.get('name')
        if len(response) == 0 or not _id or not name:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid json")
