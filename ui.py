
import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from tasks import add_task, remove_task, toggle_task_status

def create_ui(root, tasks):
    """
    Creates the user interface for the to-do list app.
    
    Args:
    root (tk.Tk): The main Tkinter window.
    tasks (list): The list of tasks to display.
    """
    def on_add_task():
        """
        Adds a new task with the title, deadline, and priority to the task list.
        """
        task_title = task_entry.get().strip()
        deadline = cal.get_date()
        priority = priority_var.get()

        if not task_title:
            messagebox.showwarning("Input Error", "Please enter a task title")
            return

        task = {
            'title': task_title,
            'deadline': deadline,
            'priority': priority,
            'completed': False
        }
        
        add_task(tasks, task)
        update_task_list()

    def on_remove_task(task_index):
        """
        Removes the selected task from the task list.
        
        Args:
        task_index (int): The index of the task to remove.
        """
        remove_task(tasks, task_index)
        update_task_list()

    def on_toggle_task_status(task_index):
        """
        Toggles the completion status of the selected task.
        
        Args:
        task_index (int): The index of the task to toggle.
        """
        toggle_task_status(tasks, task_index)
        update_task_list()

    def update_task_list():
        """
        Updates the displayed list of tasks.
        """
        for widget in task_list_frame.winfo_children():
            widget.destroy()

        for i, task in enumerate(tasks):
            task_text = f"{task['title']} | {task['deadline']} | {task['priority']}"
            task_button = tk.Button(task_list_frame, text=task_text, command=lambda i=i: on_toggle_task_status(i))
            task_button.grid(row=i, column=0, sticky="w")

            remove_button = tk.Button(task_list_frame, text="Remove", command=lambda i=i: on_remove_task(i))
            remove_button.grid(row=i, column=1)

    # UI Elements
    task_entry = tk.Entry(root, width=30)
    task_entry.grid(row=0, column=0, padx=10, pady=10)

    cal = Calendar(root, selectmode='day', date_pattern='yyyy-mm-dd')
    cal.grid(row=0, column=1, padx=10, pady=10)

    priority_var = tk.StringVar(value="Medium")
    priority_menu = tk.OptionMenu(root, priority_var, "Low", "Medium", "High")
    priority_menu.grid(row=0, column=2, padx=10, pady=10)

    add_button = tk.Button(root, text="Add Task", command=on_add_task)
    add_button.grid(row=0, column=3, padx=10, pady=10)

    task_list_frame = tk.Frame(root)
    task_list_frame.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

    update_task_list()
