import json
from .task import Task

def save_to_file(file_path, tasks):
    with open(file_path, 'w') as file:
        json.dump([task.to_dict() for task in tasks], file)
    print(f"Saved to-do list to {file_path}")

def load_from_file(file_path):
    with open(file_path, 'r') as file:
        tasks_data = json.load(file)
        return [Task.from_dict(data) for data in tasks_data]
    print(f"Loaded to-do list from {file_path}")
