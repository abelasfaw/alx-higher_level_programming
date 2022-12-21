#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body
of the response decoded in utf-8. prints Error code followed by the
HTTP status code in case of http errors"""


import sys
import urllib.request
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    request = urllib.request.Request(url)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
