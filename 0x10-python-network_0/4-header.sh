#!/bin/bash
# sends a GET request to the URL in the argument, and displays response body
curl -s "$1" -H "X-School-User-Id: 98"
