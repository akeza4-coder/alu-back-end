#!/usr/bin/python3
"""
A script that uses a REST API (JSONPlaceholder) to return information
about a given employee's TODO list progress.
"""
import requests
import sys


def get_todo_progress(employee_id):
    """Fetches and displays the employee's TODO list progress."""
    base_url = "https://jsonplaceholder.typicode.com"
    
    # Fetch user details
    user_url = "{}/users/{}".format(base_url, employee_id)
    user_response = requests.get(user_url)
    
    # If user doesn't exist, exit quietly
    if user_response.status_code != 200:
        return
        
    employee_name = user_response.json().get("name")
    
    # Fetch TODO tasks for the user
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()
    
    # Calculate tasks tracking
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    number_of_done_tasks = len(done_tasks)
    
    # Print the formatted output
    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks
    ))
    
    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            emp_id = int(sys.argv[1])
            get_todo_progress(emp_id)
        except ValueError:
            pass
