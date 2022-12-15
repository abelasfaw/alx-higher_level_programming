#!/bin/bash
#sends a request to passed URL and displays only the status code of the response
curl -s "$1" -o /dev/null -w "%{http_code}"
