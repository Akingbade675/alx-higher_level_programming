#!/bin/bash
# sends a GET request to the URL, and displays the response body
curl -sfL "$1" -X GET
