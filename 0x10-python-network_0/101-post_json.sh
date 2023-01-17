#!/bin/bash
# sends JSON POST request to URL $1, and displays the response body
curl -sL -X POST -H "Content-Type: application/json" "$1" -d @"$2"
