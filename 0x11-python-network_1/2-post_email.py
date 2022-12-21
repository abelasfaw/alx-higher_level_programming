#!/usr/bin/python3
"""takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the response
decoded in utf-8"""


import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url = sys.argv[1]
    req_data = urllib.parse.urlencode({"email": sys.argv[2]}).encode("ascii")
    request = urllib.request.Request(url, req_data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode('utf-8'))
