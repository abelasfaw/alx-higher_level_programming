#!/usr/bin/python3
"""takes in a URL and an email address, sends a POST request to the
passed URL with the email as a parameter, and displays the
body of the response"""


import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    req_data = {"email": sys.argv[2]}
    response = requests.post(url, data=req_data)
    print(response.text)
