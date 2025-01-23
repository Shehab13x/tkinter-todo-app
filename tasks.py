import json
from datetime import datetime

TASKS_FILE = 'todo_data.json'

def load_tasks():
    """
    Loads the tasks from the JSON file.
    Returns a list of tasks (dictionaries).
    If no file exists, returns an empty list.
    """
    try:
        with open(TASKS_FILE, 'r') as file:
            tasks = json.load(file)
        return tasks
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_tasks(tasks):
    """
    Saves the current list of tasks to a JSON file.
    
    Args:
    tasks (list): A list of tasks to save.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file)

def add_task(tasks, task):
    """
    Adds a new task to the tasks list.
    
    Args:
    tasks (list): The current list of tasks.
    task (dict): The task to add (contains title, date, priority, etc).
    """
    tasks.append(task)
    save_tasks(tasks)

def remove_task(tasks, task_index):
    """
    Removes a task from the list by its index.
    
    Args:
    tasks (list): The current list of tasks.
    task_index (int): The index of the task to remove.
    """
    del tasks[task_index]
    save_tasks(tasks)

def toggle_task_status(tasks, task_index):
    """
    Toggles the status of a task between completed and undone.
    
    Args:
    tasks (list): The current list of tasks.
    task_index (int): The index of the task to toggle.
    """
    task = tasks[task_index]
    task['completed'] = not task['completed']
    save_tasks(tasks)
