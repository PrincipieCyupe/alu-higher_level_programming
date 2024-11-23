#!/usr/bin/python3
"""__summary__
- Write a Python script that fetches http://0.0.0.0:5050/status
- using the urllib package.
"""
import urllib.request

if __name__ == '__main__':
    url = 'http://0.0.0.0:5050/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
