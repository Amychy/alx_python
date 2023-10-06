#!/usr/bin/python3
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    user_info = r.json()
    
    if r.status_code == 200:
        print(user_info.get("id"))
    else:
        print(None)
