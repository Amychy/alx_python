import requests
import sys

def get_employee_todo_list_progress(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Send a GET request to fetch employee details
    employee_response = requests.get(f"{base_url}/users/{employee_id}")

    # Send a GET request to fetch the TODO list for the employee
    todo_response = requests.get(f"{base_url}/users/{employee_id}/todos")

    if employee_response.status_code != 200 or todo_response.status_code != 200:
        print("Error: Unable to fetch data from the API.")
        return

    employee_data = employee_response.json()
    todo_data = todo_response.json()

    # Print the employee's TODO list progress
    print(f"Employee {employee_data['name']} is done with tasks:")

    # Print the titles and status of all tasks
    for task in todo_data:
        task_status = "OK" if task["completed"] else "Incomplete"
        print(f"Task {task['id']} in output: {task_status}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_list_progress(employee_id)
    except ValueError:
        print("Error: Employee ID must be an integer.")
