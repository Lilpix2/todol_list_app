import json
from typing import List
from .task import Task

def save_to_file(file_path: str, tasks: List[Task]) -> None:
    """
    Save a list of tasks to a JSON file.

    Args:
        file_path (str): The path to the file where the tasks will be saved.
        tasks (List[Task]): The list of tasks to be saved.

    Raises:
        IOError: If there is an error writing to the file.
        TypeError: If the tasks list contains objects that are not instances of the Task class.
    """
    try:
        with open(file_path, 'w') as file:
            json.dump([task.to_dict() for task in tasks], file, indent=4)
        print(f"Saved to-do list to {file_path}")
    except IOError as e:
        print(f"Error saving to-do list: {e}")
    except TypeError as e:
        print(f"Error saving to-do list: {e}")

def load_from_file(file_path: str) -> List[Task]:
    """
    Load a list of tasks from a JSON file.

    Args:
        file_path (str): The path to the file where the tasks are stored.

    Returns:
        List[Task]: A list of Task objects loaded from the file.

    Raises:
        IOError: If there is an error reading from the file.
        JSONDecodeError: If the file contains invalid JSON data.
    """
    try:
        with open(file_path, 'r') as file:
            tasks_data = json.load(file)
            tasks = [Task.from_dict(data) for data in tasks_data]
        print(f"Loaded to-do list from {file_path}")
        return tasks
    except IOError as e:
        print(f"Error loading to-do list: {e}")
        return []
    except json.JSONDecodeError as e:
        print(f"Error loading to-do list: {e}")
        return []