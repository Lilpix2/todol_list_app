import unittest
from datetime import datetime
from todo_list.task import Task

class TestTask(unittest.TestCase):
    def test_to_dict(self):
        task = Task("Test task", datetime(2024, 7, 5, 14, 0), "Work", 8)
        task_dict = task.to_dict()
        expected_dict = {
            "description": "Test task",
            "completed": False,
            "due_date": "2024-07-05T14:00:00",
            "category": "Work",
            "priority_score": 8
        }
        self.assertEqual(task_dict, expected_dict)

    def test_from_dict(self):
        task_dict = {
            "description": "Test task",
            "completed": False,
            "due_date": "2024-07-05T14:00:00",
            "category": "Work",
            "priority_score": 8
        }
        task = Task.from_dict(task_dict)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)
        self.assertEqual(task.due_date, datetime(2024, 7, 5, 14, 0))
        self.assertEqual(task.category, "Work")
        self.assertEqual(task.priority_score, 8)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
