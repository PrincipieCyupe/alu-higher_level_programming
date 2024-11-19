#!/usr/bin/python3
"""
This script fetches a URL's status using the urllib package.
"""
import urllib.request

if __name__ == '__main__':
    # URL to fetch - update it based on the required test case
    url = 'https://intranet.hbtn.io/status'

    # Create a request with a User-Agent header to avoid HTTP 403 errors
    request = urllib.request.Request(
        url, headers={'User-Agent': 'Mozilla/5.0'}
    )

    # Using 'with' to handle the URL response
    with urllib.request.urlopen(request) as response:
        content = response.read()

        # Print the output in the required format
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))

