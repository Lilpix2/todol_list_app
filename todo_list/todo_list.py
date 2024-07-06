from typing import List, Optional, Union
from datetime import datetime, date
from .task import Task

class ToDoList:
    """
    Represents a collection of tasks in a to-do list.

    Attributes:
        tasks (List[Task]): A list of Task objects.
    """

    def __init__(self):
        self.tasks: List[Task] = []

    def add_task(self, task: Task) -> None:
        """
        Add a new task to the to-do list.

        Args:
            task (Task): The task to be added.
        """
        self.tasks.append(task)

    def remove_task(self, index: int) -> None:
        """
        Remove a task from the to-do list by its index.

        Args:
            index (int): The index of the task to be removed.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            del self.tasks[index]
        except IndexError as e:
            print(f"Error removing task: {e}")

    def mark_completed(self, index: int) -> None:
        """
        Mark a task as completed by its index.

        Args:
            index (int): The index of the task to be marked as completed.

        Raises:
            IndexError: If the index is out of range.
        """
        try:
            self.tasks[index].completed = True
        except IndexError as e:
            print(f"Error marking task as completed: {e}")

    def filter_tasks(self, category: Optional[str] = None, priority: Optional[int] = None, completed: Optional[bool] = None) -> List[Task]:
        """
        Filter the tasks based on the provided criteria.

        Args:
            category (str, optional): The category to filter by.
            priority (int, optional): The priority level to filter by.
            completed (bool, optional): Whether to filter completed or incomplete tasks.

        Returns:
            List[Task]: A list of tasks that match the specified criteria.
        """
        filtered_tasks = []
        for task in self.tasks:
            if (category is None or task.category == category) and \
               (priority is None or task.priority == priority) and \
               (completed is None or task.completed == completed):
                filtered_tasks.append(task)
        return filtered_tasks

    def list_tasks(self) -> None:
        """
        List all tasks in the to-do list.
        """
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")