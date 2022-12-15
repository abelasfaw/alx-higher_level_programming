#!/bin/bash
#sends a request to passed URL and displays only the status code of the response
curl -sI "$1" | grep -iF 'http' | cut -d ' ' -f2 | tr -d '\n'
