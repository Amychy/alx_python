#!/usr/bin/python3
"""For a given employee ID, returns information about
their TODO list progress and exports data in CSV format."""

import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    userId = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(userId))

    if user.status_code != 200:
        print("Error: Unable to fetch user data.")
        sys.exit(1)

    user_data = user.json()
    name = user_data.get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTasks = 0
    completed = 0
    user_tasks = []

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTasks += 1
            if task.get('completed'):
                completed += 1
            user_tasks.append(task)

    print('Employee {} is done with tasks({}/{}):'
          .format(name, completed, totalTasks))

    csv_filename = f"{userId}.csv"

    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in user_tasks:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow([userId, name, task_completed_status, task["title"]])

    print(f"Data exported to {csv_filename} successfully.")
