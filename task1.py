from tkinter import *
from tkinter import messagebox
import os

root = Tk()
root.title("To-Do List")
root.geometry("500x600")
root.config(bg="#1f1f1f")

tasks = []

def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            saved_tasks = file.readlines()

        for task in saved_tasks:
            task = task.strip()
            tasks.append(task)
            task_listbox.insert(END, task)

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()

    if task == "":
        messagebox.showwarning("Warning", "Please enter a task")
        return

    tasks.append(task)
    task_listbox.insert(END, task)

    save_tasks()
    task_entry.delete(0, END)

def delete_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task first")
        return

    index = selected[0]

    task_listbox.delete(index)
    tasks.pop(index)

    save_tasks()

def update_task():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task to update")
        return

    new_task = task_entry.get().strip()

    if new_task == "":
        messagebox.showwarning("Warning", "Enter updated task")
        return

    index = selected[0]

    tasks[index] = new_task

    task_listbox.delete(index)
    task_listbox.insert(index, new_task)

    save_tasks()

    task_entry.delete(0, END)

def mark_complete():
    selected = task_listbox.curselection()

    if not selected:
        messagebox.showwarning("Warning", "Select a task")
        return

    index = selected[0]
    task = tasks[index]

    if "✓" not in task:
        updated_task = task + "  ✓"

        tasks[index] = updated_task

        task_listbox.delete(index)
        task_listbox.insert(index, updated_task)

        save_tasks()

def clear_all():
    confirm = messagebox.askyesno(
        "Clear Tasks",
        "Do you want to remove all tasks?"
    )

    if confirm:
        tasks.clear()
        task_listbox.delete(0, END)
        save_tasks()

title = Label(
    root,
    text="My To-Do List",
    font=("Arial", 22, "bold"),
    bg="#1f1f1f",
    fg="white"
)

title.pack(pady=20)

task_entry = Entry(
    root,
    width=32,
    font=("Arial", 14),
    bd=4
)

task_entry.pack(pady=10)

add_btn = Button(
    root,
    text="Add Task",
    width=18,
    font=("Arial", 11, "bold"),
    bg="#4CAF50",
    fg="white",
    command=add_task
)

add_btn.pack(pady=10)

task_listbox = Listbox(
    root,
    width=42,
    height=15,
    font=("Arial", 12),
    selectbackground="#6c63ff"
)

task_listbox.pack(pady=20)

button_frame = Frame(root, bg="#1f1f1f")
button_frame.pack()

update_btn = Button(
    button_frame,
    text="Update",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#2196F3",
    fg="white",
    command=update_task
)

update_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = Button(
    button_frame,
    text="Delete",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#f44336",
    fg="white",
    command=delete_task
)

delete_btn.grid(row=0, column=1, padx=5, pady=5)

complete_btn = Button(
    button_frame,
    text="Complete",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#9c27b0",
    fg="white",
    command=mark_complete
)

complete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = Button(
    button_frame,
    text="Clear All",
    width=14,
    font=("Arial", 10, "bold"),
    bg="#ff9800",
    fg="white",
    command=clear_all
)

clear_btn.grid(row=1, column=1, padx=5, pady=5)

load_tasks()

root.mainloop()