#!/usr/bin/python3
"""
Python script to fetch an employee's TODO list progress from a REST API.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Validate that the argument is an integer
    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_id = int(employee_id)

    # Base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee information
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        print("User not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Fetch TODOs for the employee
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    print(f"Employee {employee_name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")

