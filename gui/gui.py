import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
from todo_list.todo_list import ToDoList
from todo_list.file_manager import save_to_file, load_from_file

class ToDoListGUI:
    def __init__(self, root):
        self.to_do_list = ToDoList()
        
        self.root = root
        self.root.title("To-Do List Application")

        # Frame for the listbox and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.frame, width=80, height=20)
        self.task_listbox.pack(side=tk.LEFT, padx=10)

        # Scrollbar for the listbox
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)

        self.task_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        # Frame for task entry
        self.entry_frame = tk.Frame(self.root)
        self.entry_frame.pack(padx=10, pady=10)

        # Labels and entry fields for task details
        tk.Label(self.entry_frame, text="Task Description:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.task_entry = tk.Entry(self.entry_frame, width=40)
        self.task_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.entry_frame, text="Priority (1-10):").grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.priority_combobox = ttk.Combobox(self.entry_frame, values=list(range(1, 11)), width=3)
        self.priority_combobox.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(self.entry_frame, text="Category:").grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.category_combobox = ttk.Combobox(self.entry_frame, values=["Self", "Family", "School", "Work", "Friends", "Hobbies"], width=15)
        self.category_combobox.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)

        tk.Label(self.entry_frame, text="Due Date (YYYY-MM-DD HH:MM):").grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.date_entry = tk.Entry(self.entry_frame, width=20)
        self.date_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        # Buttons for adding, marking complete, deleting, saving, and loading tasks
        self.add_button = tk.Button(self.entry_frame, text="Add Task", command=self.add_task)
        self.add_button.grid(row=4, column=0, padx=5, pady=5, columnspan=2)

        self.complete_button = tk.Button(self.root, text="Mark Complete", command=self.mark_complete)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

        self.save_button = tk.Button(self.root, text="Save Tasks", command=self.save_tasks)
        self.save_button.pack(pady=5)

        self.load_button = tk.Button(self.root, text="Load Tasks", command=self.load_tasks)
        self.load_button.pack(pady=5)

        self.list_tasks()

    def add_task(self):
        description = self.task_entry.get().strip()
        priority = self.priority_combobox.get().strip()
        category = self.category_combobox.get().strip()
        date_str = self.date_entry.get().strip()

        if not description or not priority or not category or not date_str:
            messagebox.showerror("Error", "All fields must be filled out")
            return

        try:
            priority = int(priority)
            if not (1 <= priority <= 10):
                raise ValueError
        except ValueError:
            messagebox.showerror("Error", "Priority must be an integer between 1 and 10")
            return

        try:
            due_date = datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        except ValueError:
            messagebox.showerror("Error", "Date must be in YYYY-MM-DD HH:MM format")
            return

        self.to_do_list.add_task(description, due_date, category, priority)
        self.list_tasks()

        self.task_entry.delete(0, tk.END)
        self.priority_combobox.set('')
        self.category_combobox.set('')
        self.date_entry.delete(0, tk.END)

    def list_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.to_do_list.tasks:
            self.task_listbox.insert(tk.END, str(task))

    def mark_complete(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No task selected", "Please select a task to mark as complete")
            return

        self.to_do_list.mark_task_complete(selected_index[0])
        self.list_tasks()

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("No task selected", "Please select a task to delete")
            return

        self.to_do_list.delete_task(selected_index[0])
        self.list_tasks()

    def save_tasks(self):
        save_to_file("tasks.json", self.to_do_list.tasks)
        messagebox.showinfo("Tasks Saved", "Tasks have been saved to tasks.json")

    def load_tasks(self):
        self.to_do_list.tasks = load_from_file("tasks.json")
        self.list_tasks()
        messagebox.showinfo("Tasks Loaded", "Tasks have been loaded from tasks.json")

def main():
    root = tk.Tk()
    app = ToDoListGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
