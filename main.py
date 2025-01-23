import tkinter as tk
from ui import create_ui
from tasks import load_tasks, save_tasks

def main():
    """
    Main function to start the to-do list application.
    It loads existing tasks from the data file and creates the UI.
    """
    root = tk.Tk()
    root.title("To-Do List App")

    # Load tasks from the file
    tasks = load_tasks()

    # Create the UI components and pass in the tasks
    create_ui(root, tasks)

    # Run the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
