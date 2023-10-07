import csv
import requests
import sys
import os

def user_info(employee_id):
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    employee_data = employee_response.json()
    todo_data = todos_response.json()
    employee_name = employee_data.get("name", "Unknown Employee")

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            task_completed_status = "Completed" if task["completed"] else "Not Completed"
            csv_writer.writerow([employee_id, employee_name, task_completed_status, task["title"]])

    # Check if the CSV file exists before opening it
    if os.path.exists(csv_filename):
        with open(csv_filename, 'r') as f:
            # Perform any required operations with the file
            pass
    else:
        print(f"Error: CSV file '{csv_filename}' does not exist.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        user_info(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
