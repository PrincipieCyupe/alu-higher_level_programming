#!/usr/bin/python3
<<<<<<< HEAD
"""__summary__
- Write a Python script that
- fetches https://intranet.hbtn.io/status.
=======
"""Fetches url
using the request module
>>>>>>> a28372db1aa3ae9ad47f2bbc456c76858f03f7c5
"""
import requests


if __name__ == "__main__":
<<<<<<< HEAD
    r = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
=======
    url = 'https://intranet.hbtn.io/status'
    if url.startswith('https://'):
        url = "https://alu-intranet.hbtn.io/status"
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))
>>>>>>> a28372db1aa3ae9ad47f2bbc456c76858f03f7c5
