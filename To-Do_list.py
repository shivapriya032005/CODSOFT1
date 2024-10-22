import tkinter as tk
from tkinter import messagebox


# Function to add a task with a checkbox
def add_task():
    task = task_entry.get()
    if task.strip() != "":
        task_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(frame_tasks, text=task, variable=task_var, font=("Helvetica", 12), bg="#f0f0f0")
        checkbox.var = task_var
        checkbox.pack(anchor='w', padx=10, pady=2)
        tasks.append((checkbox, task_var))
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task cannot be empty.")

# Function to remove selected tasks
def remove_task():
    global tasks
    for checkbox, task_var in tasks:
        if task_var.get():
            checkbox.pack_forget()
    tasks = [(cb, var) for cb, var in tasks if not var.get()]

# Function to mark selected tasks as completed
def mark_task_completed():
    for checkbox, task_var in tasks:
        if task_var.get():
            checkbox.config(fg='gray', font=("Helvetica", 10, "italic"))

# Function to select all tasks
def select_all_tasks():
    for checkbox, task_var in tasks:
        task_var.set(True)

# Function to update the selected (checked) tasks
def update_task():
    global tasks
    task_text = task_entry.get()
    if task_text.strip() == "":
        messagebox.showwarning("Input Error", "Task cannot be empty.")
        return

    updated_any = False
    for checkbox, task_var in tasks:
        if task_var.get():  # Only update checked tasks
            checkbox.config(text=task_text)  # Update the checkbox text
            updated_any = True

    if updated_any:
        task_entry.delete(0, tk.END)  # Clear entry after updating
    else:
        messagebox.showwarning("Update Error", "No task selected for update.")

# Creating the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("400x550")
root.config(bg="#f0f0f0")

# Title Label
title_label = tk.Label(root, text="To-Do List", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Frame to hold the tasks (checkboxes)
frame_tasks = tk.Frame(root, bg="#f0f0f0")
frame_tasks.pack(pady=10, padx=10, fill="both", expand=True)

# List to store tasks (checkbox widgets and their states)
tasks = []

# Entry widget to input tasks with increased height and curved edges
task_entry = tk.Entry(root, width=30, font=("Helvetica", 12), bd=3, relief="solid")
task_entry.pack(pady=10, padx=10, ipady=8)

# Control Buttons with the new layout
controls_frame = tk.Frame(root, bg="#f0f0f0")
controls_frame.pack(pady=10)

# Add Task button (now placed above the Remove, Update, and Finished buttons)
add_task_button = tk.Button(controls_frame, text="Add", font=("Arial", 15), width=10, height=1, bg="#4CAF50", fg="white", bd=0, command=add_task)
add_task_button.grid(row=0, column=0, padx=10, pady=5)

# Update Task button (for modifying a selected task)
update_task_button = tk.Button(controls_frame, text="Update", font=("Arial", 15), width=10, height=1, bg="#FFC107", fg="black", bd=0, command=update_task)
update_task_button.grid(row=0, column=1, padx=10, pady=5)

# Remove and Finished buttons (below the Add Task button)
remove_task_button = tk.Button(controls_frame, text="Remove", font=("Arial", 15), width=10, height=1, bg="#F44336", fg="white", bd=0, command=remove_task)
remove_task_button.grid(row=1, column=0, padx=10, pady=5)

mark_completed_button = tk.Button(controls_frame, text="Finished", font=("Arial", 15), width=10, height=1, bg="#2196F3", fg="white", bd=0, command=mark_task_completed)
mark_completed_button.grid(row=1, column=1, padx=10, pady=5)

# Select All button (new feature)
select_all_button = tk.Button(controls_frame, text="Select All", font=("Arial", 15), width=22, height=1, bg="#FFC107", fg="black", bd=0, command=select_all_tasks)
select_all_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

# Footer to indicate usage of buttons
footer_label = tk.Label(root, text="Use 'Add' to add, select task and use 'Update' to modify,\n'Remove' to delete, 'Finished' to mark completed,\n 'Select All' to select all tasks", font=("Helvetica", 10), bg="#f0f0f0")
footer_label.pack(pady=10)

# Start the main event loop
root.mainloop()