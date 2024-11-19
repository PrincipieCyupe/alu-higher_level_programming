#!/usr/bin/python3
"""
Fetch a URL's status using the urllib package.
"""
import urllib.request
import sys

if __name__ == '__main__':
    # Default URL (for the first task)
    url = 'https://alu-intranet.hbtn.io/status'
    
    # Check if a custom URL was passed as an argument
    if len(sys.argv) > 1:
        url = sys.argv[1]
    
    # Adding a User-Agent header to prevent HTTP 403 errors
    request = urllib.request.Request(
        url, headers={'User-Agent': 'Mozilla/5.0'}
    )
    
    # Using 'with' to fetch and read the response
    with urllib.request.urlopen(request) as response:
        content = response.read()
        
        # Printing the response in the expected format
        print("Body response:")
        print("\t- type: {}".format(type(content)))  # Type of the response
        print("\t- content: {}".format(content))  # Raw content (bytes)
        print("\t- utf8 content: {}".format(content.decode("utf-8")))  # Decoded content

