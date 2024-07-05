from datetime import datetime
from .task import Task

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, due_date=None, category="Self", priority_score=1):
        task = Task(description, due_date, category, priority_score)
        self.tasks.append(task)
        print(f"Added task: {description}")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed_task = self.tasks.pop(index)
            print(f"Deleted task: {removed_task.description}")
        else:
            print("Invalid task index.")

    def mark_task_complete(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_complete()
            print(f"Marked task as complete: {self.tasks[index].description}")
        else:
            print("Invalid task index.")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

    def list_next_three_tasks(self):
        important_tasks = sorted(self.tasks, key=lambda x: (x.due_date or datetime.max, x.get_category_rank(), -x.priority_score))
        next_three_tasks = [task for task in important_tasks if not task.completed][:3]
        for task in next_three_tasks:
            print(task)

    def list_high_priority_tasks(self, start_date, end_date):
        high_priority_tasks = [task for task in self.tasks if task.due_date and start_date <= task.due_date <= end_date and task.priority_score >= 8]
        high_priority_tasks.sort(key=lambda x: (x.due_date, x.get_category_rank(), -x.priority_score))
        for task in high_priority_tasks:
            print(task)

    def list_completed_tasks(self, start_date, end_date):
        completed_tasks = [task for task in self.tasks if task.completed and task.due_date and start_date <= task.due_date <= end_date]
        completed_tasks.sort(key=lambda x: (x.due_date, x.get_category_rank(), -x.priority_score))
        for task in completed_tasks:
            print(task)
