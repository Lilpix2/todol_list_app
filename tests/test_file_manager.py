import unittest
import tempfile
import os
import json
from datetime import datetime
from todo_list.file_manager import save_to_file, load_from_file
from todo_list.todo_list import ToDoList

class TestFileManager(unittest.TestCase):
    def setUp(self):
        self.to_do_list = ToDoList()
        self.to_do_list.add_task("Buy groceries", datetime(2024, 7, 5, 14, 0), "Family", 8)
        self.to_do_list.add_task("Read a book", datetime(2024, 7, 10, 18, 0), "Self", 5)
        self.to_do_list.add_task("Pay bills", datetime(2024, 7, 4, 9, 0), "Work", 9)

    def test_save_to_file(self):
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            save_to_file(tmp_file.name, self.to_do_list.tasks)
            tmp_file_path = tmp_file.name

        with open(tmp_file_path, 'r') as file:
            data = json.load(file)
            self.assertEqual(len(data), 3)
            self.assertEqual(data[0]["description"], "Buy groceries")
            self.assertEqual(data[1]["description"], "Read a book")
            self.assertEqual(data[2]["description"], "Pay bills")

        os.remove(tmp_file_path)

    def test_load_from_file(self):
        tasks_data = [
            {"description": "Task 1", "completed": False, "due_date": "2024-07-01T09:00:00", "category": "Work", "priority_score": 9},
            {"description": "Task 2", "completed": True, "due_date": "2024-07-02T14:00:00", "category": "Family", "priority_score": 8}
        ]
        
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            json.dump(tasks_data, tmp_file)
            tmp_file_path = tmp_file.name

        loaded_tasks = load_from_file(tmp_file_path)
        
        self.assertEqual(len(loaded_tasks), 2)
        self.assertEqual(loaded_tasks[0].description, "Task 1")
        self.assertFalse(loaded_tasks[0].completed)
        self.assertEqual(loaded_tasks[0].due_date, datetime(2024, 7, 1, 9, 0))
        self.assertEqual(loaded_tasks[0].category, "Work")
        self.assertEqual(loaded_tasks[0].priority_score, 9)

        self.assertEqual(loaded_tasks[1].description, "Task 2")
        self.assertTrue(loaded_tasks[1].completed)
        self.assertEqual(loaded_tasks[1].due_date, datetime(2024, 7, 2, 14, 0))
        self.assertEqual(loaded_tasks[1].category, "Family")
        self.assertEqual(loaded_tasks[1].priority_score, 8)

        os.remove(tmp_file_path)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
