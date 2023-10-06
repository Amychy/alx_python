#!/usr/bin/python3
"""Sends a POST request to a given URL with a given email.
Usage: ./2-post_email.py <URL> <email>
  - Displays the body of the response.
"""
import sys
import requests

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./2-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an exception for HTTP errors (4xx, 5xx)
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        sys.exit(1)
