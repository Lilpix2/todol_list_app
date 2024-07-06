from datetime import datetime, date
from typing import Union, Optional

class Task:
    """
    Represents a single task in a to-do list.

    Attributes:
        description (str): A brief description of the task.
        due_date (Union[datetime, date]): The due date for the task.
        category (str): The category or context of the task.
        priority (int): The priority level of the task (1-10, with 10 being the highest).
        completed (bool): Whether the task has been completed or not.
    """

    def __init__(self, description: str, due_date: Optional[Union[datetime, date]] = None, category: str = "General",
                 priority: int = 3, completed: bool = False):
        self.description = description
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.completed = completed

    def to_dict(self) -> dict:
        """
        Convert the Task object to a dictionary representation.

        Returns:
            dict: A dictionary containing the task's attributes.
        """
        return {
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "category": self.category,
            "priority": self.priority,
            "completed": self.completed
        }

    @classmethod
    def from_dict(cls, task_dict: dict) -> "Task":
        """
        Create a Task object from a dictionary representation.

        Args:
            task_dict (dict): A dictionary containing the task's attributes.

        Returns:
            Task: A Task object created from the dictionary.
        """
        due_date_str = task_dict.get("due_date")
        if due_date_str:
            try:
                due_date = datetime.fromisoformat(due_date_str)
                if due_date.time() == datetime.min.time():
                    due_date = due_date.date()
            except ValueError:
                due_date = date.fromisoformat(due_date_str)
        else:
            due_date = None

        return cls(
            description=task_dict["description"],
            due_date=due_date,
            category=task_dict["category"],
            priority=task_dict["priority"],
            completed=task_dict["completed"]
        )

    def __str__(self) -> str:
        """
        Return a string representation of the Task object.

        Returns:
            str: A string representation of the Task object.
        """
        if isinstance(self.due_date, datetime):
            due_date_str = self.due_date.strftime("%Y-%m-%d %H:%M")
        elif isinstance(self.due_date, date):
            due_date_str = self.due_date.strftime("%Y-%m-%d")
        else:
            due_date_str = "No due date"

        completed_str = "Completed" if self.completed else "Not completed"
        return f"{self.description} ({due_date_str}) - {self.category} - Priority: {self.priority} - {completed_str}"
