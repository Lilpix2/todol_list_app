import unittest
from datetime import datetime, date
from todo_list.todo_list import ToDoList
from todo_list.task import Task

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.todo_list = ToDoList()

    def test_add_task(self):
        task = Task(description="Test Task")
        self.todo_list.add_task(task)
        self.assertEqual(len(self.todo_list.tasks), 1)
        self.assertEqual(self.todo_list.tasks[0].description, "Test Task")

    def test_remove_task(self):
        task = Task(description="Test Task")
        self.todo_list.add_task(task)
        self.todo_list.remove_task(0)
        self.assertEqual(len(self.todo_list.tasks), 0)

    def test_mark_completed(self):
        task = Task(description="Test Task")
        self.todo_list.add_task(task)
        self.todo_list.mark_completed(0)
        self.assertTrue(self.todo_list.tasks[0].completed)

    def test_filter_tasks_by_category(self):
        task1 = Task(description="Task 1", category="Work")
        task2 = Task(description="Task 2", category="Home")
        self.todo_list.add_task(task1)
        self.todo_list.add_task(task2)
        filtered_tasks = self.todo_list.filter_tasks(category="Work")
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0].description, "Task 1")

    def test_filter_tasks_by_priority(self):
        task1 = Task(description="Task 1", priority=1)
        task2 = Task(description="Task 2", priority=5)
        self.todo_list.add_task(task1)
        self.todo_list.add_task(task2)
        filtered_tasks = self.todo_list.filter_tasks(priority=5)
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0].description, "Task 2")

    def test_filter_tasks_by_completion(self):
        task1 = Task(description="Task 1", completed=True)
        task2 = Task(description="Task 2", completed=False)
        self.todo_list.add_task(task1)
        self.todo_list.add_task(task2)
        filtered_tasks = self.todo_list.filter_tasks(completed=True)
        self.assertEqual(len(filtered_tasks), 1)
        self.assertEqual(filtered_tasks[0].description, "Task 1")

    def test_filter_tasks_by_due_date_datetime(self):
        task1 = Task(description="Task 1", due_date=datetime(2024, 1, 1, 10, 0))
        task2 = Task(description="Task 2", due_date=datetime(2024, 1, 1, 14, 0))
        self.todo_list.add_task(task1)
        self.todo_list.add_task(task2)
        filtered_tasks = self.todo_list.filter_tasks()
        self.assertEqual(len(filtered_tasks), 2)

    def test_filter_tasks_by_due_date_date(self):
        task1 = Task(description="Task 1", due_date=date(2024, 1, 1))
        task2 = Task(description="Task 2", due_date=date(2024, 1, 2))
        self.todo_list.add_task(task1)
        self.todo_list.add_task(task2)
        filtered_tasks = self.todo_list.filter_tasks()
        self.assertEqual(len(filtered_tasks), 2)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
