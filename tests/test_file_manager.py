import unittest
import os
from datetime import datetime, date
from todo_list.task import Task
from todo_list.file_manager import save_to_file, load_from_file

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.test_file = "test_tasks.json"
        self.tasks = [
            Task(description="Task 1", due_date=datetime(2024, 7, 5, 14, 0), category="Work", priority=1),
            Task(description="Task 2", due_date=date(2024, 7, 10), category="Home", priority=2)
        ]

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_to_file(self):
        save_to_file(self.test_file, self.tasks)
        self.assertTrue(os.path.exists(self.test_file))

    def test_load_from_file(self):
        save_to_file(self.test_file, self.tasks)
        loaded_tasks = load_from_file(self.test_file)
        self.assertEqual(len(loaded_tasks), len(self.tasks))
        for original, loaded in zip(self.tasks, loaded_tasks):
            self.assertEqual(original.description, loaded.description)
            self.assertEqual(original.category, loaded.category)
            self.assertEqual(original.priority, loaded.priority)
            self.assertEqual(original.completed, loaded.completed)
            if isinstance(original.due_date, datetime):
                self.assertIsInstance(loaded.due_date, datetime)
            elif isinstance(original.due_date, date):
                self.assertIsInstance(loaded.due_date, date)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
