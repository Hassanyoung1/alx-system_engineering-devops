#!/usr/bin/python3

"""
A Python script that, using REST API, for a given employee ID, returns
information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys

    """
    Usage: python3 gather_data_from_an_API.py <user_id>
    """
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <user_id>", sys.stderr)
        exit(1)

    user_id = sys.argv[1]
    baseUrl = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    employee_name = requests.get(baseUrl).json().get('name')

    todosUrl = f"https://jsonplaceholder.typicode.com/users/{user_id}/todos"
    todos = requests.get(todosUrl).json()
    done = 0
    tasks = []

    """
    Loop through the todos and count the completed tasks
    """
    for todo in todos:
        if todo.get('completed'):
            tasks.append(todo.get('title'))
            done += 1

    """
    Print the progress of the employee's tasks
    """
    print(f"Employee {employee_name} is done with tasks({done}/{len(tasks)}):")
    for task in tasks:
        print("\t{}".format(task))
