#!/bin/bash
# Script to display the size of the response body

# Check if URL is provided as argument
if [ -z "$1" ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# Send a GET request to the URL and display only the size of the response body in bytes
curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}' 

