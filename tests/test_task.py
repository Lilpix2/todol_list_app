import unittest
from datetime import datetime, date
from todo_list.task import Task

class TestTask(unittest.TestCase):
    def test_task_creation_with_datetime(self):
        task = Task(description="Test Task with Time", due_date=datetime(2023, 12, 31, 14, 0), category="Work", priority=5)
        self.assertEqual(task.description, "Test Task with Time")
        self.assertEqual(task.due_date, datetime(2023, 12, 31, 14, 0))
        self.assertEqual(task.category, "Work")
        self.assertEqual(task.priority, 5)
        self.assertFalse(task.completed)

    def test_task_creation_with_date(self):
        task = Task(description="Test Task without Time", due_date=date(2023, 12, 31), category="Work", priority=5)
        self.assertEqual(task.description, "Test Task without Time")
        self.assertEqual(task.due_date, date(2023, 12, 31))
        self.assertEqual(task.category, "Work")
        self.assertEqual(task.priority, 5)
        self.assertFalse(task.completed)

    def test_task_to_dict_with_datetime(self):
        task = Task(description="Test Task with Time", due_date=datetime(2023, 12, 31, 14, 0), category="Work", priority=5)
        task_dict = task.to_dict()
        expected_dict = {
            "description": "Test Task with Time",
            "due_date": "2023-12-31T14:00:00",
            "category": "Work",
            "priority": 5,
            "completed": False
        }
        self.assertEqual(task_dict, expected_dict)

    def test_task_to_dict_with_date(self):
        task = Task(description="Test Task without Time", due_date=date(2023, 12, 31), category="Work", priority=5)
        task_dict = task.to_dict()
        expected_dict = {
            "description": "Test Task without Time",
            "due_date": "2023-12-31",
            "category": "Work",
            "priority": 5,
            "completed": False
        }
        self.assertEqual(task_dict, expected_dict)

    def test_task_from_dict_with_datetime(self):
        task_dict = {
            "description": "Test Task with Time",
            "due_date": "2023-12-31T14:00:00",
            "category": "Work",
            "priority": 5,
            "completed": False
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.description, "Test Task with Time")
        self.assertEqual(task.due_date, datetime(2023, 12, 31, 14, 0))
        self.assertEqual(task.category, "Work")
        self.assertEqual(task.priority, 5)
        self.assertFalse(task.completed)

    def test_task_from_dict_with_date(self):
        task_dict = {
            "description": "Test Task without Time",
            "due_date": "2023-12-31",
            "category": "Work",
            "priority": 5,
            "completed": False
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.description, "Test Task without Time")
        self.assertEqual(task.due_date, date(2023, 12, 31))
        self.assertEqual(task.category, "Work")
        self.assertEqual(task.priority, 5)
        self.assertFalse(task.completed)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
