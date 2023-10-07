import csv
import requests
import sys

def export_tasks_to_csv(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")

    # Send a GET request to fetch the TODO list for the employee
    todos_response = requests.get(f"{base_url}/todos?userId={employee_id}")

    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    employee_data = employee_response.json()
    todo_data = todos_response.json()

    employee_username = employee_data.get("username", "unknown employee")
    csv_filename = f"{employee_id}.csv"

    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            task_completed_status = "True" if task["completed"] else "False"
            csv_writer.writerow([employee_id, employee_username, task_completed_status, task["title"]])

    print(f"Data exported to {csv_filename}")

    # Now you can open and read the CSV file using the correct filename
    with open(csv_filename, 'r') as f:
        pass

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_CSV.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        export_tasks_to_csv(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
