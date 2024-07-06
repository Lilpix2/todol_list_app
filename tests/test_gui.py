import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from tkcalendar import DateEntry
from datetime import datetime, date
from todo_list.task import Task
from todo_list.todo_list import ToDoList
from gui import ToDoListGUI

class TestToDoListGUI(unittest.TestCase):
    def setUp(self):
        self.root = tk.Tk()
        self.app = ToDoListGUI(self.root)

    def tearDown(self):
        self.root.update_idletasks()
        self.root.destroy()

    def test_add_task_with_time(self):
        self.app.task_entry.insert(0, "Test Task with Time")
        self.app.priority_combobox.set("5")
        self.app.category_combobox.set("Work")
        self.app.date_entry.set_date(datetime.strptime("2023-12-31", "%Y-%m-%d"))
        self.app.no_time_var.set(0)  # Ensure "No specific time" is not selected
        self.app.time_entry.insert(0, "14:00")

        self.app.add_task()

        self.assertEqual(len(self.app.to_do_list.tasks), 1)
        self.assertEqual(self.app.to_do_list.tasks[0].description, "Test Task with Time")
        self.assertEqual(self.app.to_do_list.tasks[0].priority, 5)
        self.assertEqual(self.app.to_do_list.tasks[0].category, "Work")
        self.assertEqual(self.app.to_do_list.tasks[0].due_date, datetime(2023, 12, 31, 14, 0))

    def test_add_task_without_time(self):
        self.app.task_entry.insert(0, "Test Task without Time")
        self.app.priority_combobox.set("5")
        self.app.category_combobox.set("Work")
        self.app.date_entry.set_date(datetime.strptime("2023-12-31", "%Y-%m-%d"))
        self.app.no_time_var.set(1)  # Select "No specific time"

        self.app.add_task()

        self.assertEqual(len(self.app.to_do_list.tasks), 1)
        self.assertEqual(self.app.to_do_list.tasks[0].description, "Test Task without Time")
        self.assertEqual(self.app.to_do_list.tasks[0].priority, 5)
        self.assertEqual(self.app.to_do_list.tasks[0].category, "Work")
        self.assertEqual(self.app.to_do_list.tasks[0].due_date, date(2023, 12, 31))

    @patch('tkinter.messagebox.showwarning')
    def test_mark_complete_no_selection(self, mock_showwarning):
        self.app.mark_complete()
        mock_showwarning.assert_called_once_with("No task selected", "Please select a task to mark as complete")

    @patch('tkinter.messagebox.showwarning')
    def test_delete_task_no_selection(self, mock_showwarning):
        self.app.delete_task()
        mock_showwarning.assert_called_once_with("No task selected", "Please select a task to delete")

    @patch('gui.save_to_file')
    @patch('tkinter.messagebox.showinfo')
    def test_save_tasks(self, mock_showinfo, mock_save_to_file):
        self.app.task_entry.insert(0, "Test Task")
        self.app.priority_combobox.set("5")
        self.app.category_combobox.set("Work")
        self.app.date_entry.set_date(datetime.strptime("2023-12-31", "%Y-%m-%d"))
        self.app.no_time_var.set(1)  # Select "No specific time"
        self.app.add_task()

        self.app.save_tasks()
        mock_save_to_file.assert_called_once_with("tasks.json", self.app.to_do_list.tasks)
        mock_showinfo.assert_called_once_with("Tasks Saved", "Tasks have been saved to tasks.json")

    @patch('gui.load_from_file', return_value=[Task("Loaded Task", date(2023, 12, 31), "Work", 5)])
    @patch('tkinter.messagebox.showinfo')
    def test_load_tasks(self, mock_showinfo, mock_load_from_file):
        self.app.load_tasks()
        mock_load_from_file.assert_called_once()
        mock_showinfo.assert_called_once_with("Tasks Loaded", "Tasks have been loaded from tasks.json")
        self.assertEqual(len(self.app.to_do_list.tasks), 1)
        self.assertEqual(self.app.to_do_list.tasks[0].description, "Loaded Task")
        self.assertEqual(self.app.to_do_list.tasks[0].due_date, date(2023, 12, 31))

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
