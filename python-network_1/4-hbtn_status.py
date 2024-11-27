#!/usr/bin/python3
"""
Fetches a URL using the requests module.
Supports fetching both https://intranet.hbtn.io/status and
https://alu-intranet.hbtn.io/status based on conditions.
"""
import requests

if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    # Adjust URL if necessary
    if url.startswith("https://"):
        url = "https://alu-intranet.hbtn.io/status"
    
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))

