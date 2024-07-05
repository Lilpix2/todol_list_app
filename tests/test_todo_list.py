import unittest
from datetime import datetime
from todo_list.todo_list import ToDoList

class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.to_do_list = ToDoList()
        self.to_do_list.add_task("Buy groceries", datetime(2024, 7, 5, 14, 0), "Family", 8)
        self.to_do_list.add_task("Read a book", datetime(2024, 7, 10, 18, 0), "Self", 5)
        self.to_do_list.add_task("Pay bills", datetime(2024, 7, 4, 9, 0), "Work", 9)
        self.to_do_list.add_task("Exercise", datetime(2024, 7, 6, 7, 0), "Self", 6)
        self.to_do_list.add_task("Meet with friends", datetime(2024, 7, 4, 19, 0), "Friends", 7)

    def test_list_next_three_tasks(self):
        expected_tasks = [
            "✘ Pay bills [Due: 2024-07-04 09:00, Category: Work, Priority: 9]",
            "✘ Meet with friends [Due: 2024-07-04 19:00, Category: Friends, Priority: 7]",
            "✘ Buy groceries [Due: 2024-07-05 14:00, Category: Family, Priority: 8]"
        ]

        captured_output = []
        important_tasks = sorted(self.to_do_list.tasks, key=lambda x: (x.due_date or datetime.max, x.get_category_rank(), -x.priority_score))
        next_three_tasks = [task for task in important_tasks if not task.completed][:3]
        for task in next_three_tasks:
            captured_output.append(str(task))

        self.assertEqual(captured_output, expected_tasks)

    def test_list_high_priority_tasks(self):
        start_date = datetime(2024, 7, 1)
        end_date = datetime(2024, 7, 10)
        expected_tasks = [
            "✘ Pay bills [Due: 2024-07-04 09:00, Category: Work, Priority: 9]",
            "✘ Buy groceries [Due: 2024-07-05 14:00, Category: Family, Priority: 8]"
        ]

        captured_output = []
        high_priority_tasks = [task for task in self.to_do_list.tasks if task.due_date and start_date <= task.due_date <= end_date and task.priority_score >= 8]
        high_priority_tasks.sort(key=lambda x: (x.due_date, x.get_category_rank(), -x.priority_score))
        for task in high_priority_tasks:
            captured_output.append(str(task))

        self.assertEqual(captured_output, expected_tasks)

    def test_list_completed_tasks(self):
        start_date = datetime(2024, 7, 1)
        end_date = datetime(2024, 7, 10)
        self.to_do_list.mark_task_complete(0)  # Mark "Buy groceries" as complete
        expected_tasks = [
            "✔ Buy groceries [Due: 2024-07-05 14:00, Category: Family, Priority: 8]"
        ]

        captured_output = []
        completed_tasks = [task for task in self.to_do_list.tasks if task.completed and task.due_date and start_date <= task.due_date <= end_date]
        completed_tasks.sort(key=lambda x: (x.due_date, x.get_category_rank(), -x.priority_score))
        for task in completed_tasks:
            captured_output.append(str(task))

        self.assertEqual(captured_output, expected_tasks)

if __name__ == '__main__':
    unittest.main(argv=[''], exit=False)
