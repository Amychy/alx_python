import csv
import os
import requests
import sys

def user_info(user_id):
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    filename = "{}.csv".format(user_id)

    # Check if the file already exists, delete it
    if os.path.exists(filename):
        os.remove(filename)

    with open(filename, "w", newline="\n") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id, username, t.get("completed"), t.get("title")]) for t in todos]

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    user_info(int(user_id))
