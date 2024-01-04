#!/usr/bin/python3

"""
A Python script that, for a given employee ID,
returns information about his/her TODO list progress.
"""

if __name__ == '__main__':
    import requests
    import sys


    if len(sys.argv) != 2:
        print(f'Usage: {sys.argv[0]} <user_id>', file=sys.stderr)
        exit(1)

    employee_id = sys.argv[1]
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    employee_name = requests.get(user_url).json().get('name')

    todos_url = f'https: // jsonplaceholder.typicode.com / users / {
        employee_id} / todos'
    todos = requests.get(todos_url).json()
    completed_count = 0
    completed_tasks = []

    """
    Loop through the tasks and count the completed tasks
    """
    for task in todos:
        if task.get('completed'):
            completed_tasks.append(task)
            completed_count += 1

    """
    Print the progress of the employee's tasks
    """
    print(
        f'Employee {employee_name} is done with tasks({completed_count} / {
            len(todos)}): ')
    for task in completed_tasks:
        print(f'\t {task.get("title")}')
