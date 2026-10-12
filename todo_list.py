
import tkinter as tk
from tkinter import messagebox


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("CodeByEman - To-Do List")
        self.root.geometry("520x600")
        self.root.configure(bg="#101827")
        self.root.resizable(False, False)

        self.tasks = []

        # Heading
        tk.Label(
            root,
            text="MY TO-DO LIST",
            font=("Arial", 24, "bold"),
            bg="#101827",
            fg="#38bdf8"
        ).pack(pady=(25, 5))

        tk.Label(
            root,
            text="Organize your day, one task at a time!",
            font=("Arial", 10),
            bg="#101827",
            fg="#cbd5e1"
        ).pack(pady=(0, 20))

        # Input area
        input_frame = tk.Frame(root, bg="#101827")
        input_frame.pack(padx=25, fill="x")

        self.task_entry = tk.Entry(
            input_frame,
            font=("Arial", 12),
            bg="#1e293b",
            fg="white",
            insertbackground="white",
            relief="flat"
        )
        self.task_entry.pack(
            side="left", fill="x", expand=True, ipady=12, padx=(0, 8)
        )
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        tk.Button(
            input_frame,
            text="Add +",
            command=self.add_task,
            bg="#0284c7",
            fg="white",
            activebackground="#0369a1",
            relief="flat",
            font=("Arial", 10, "bold"),
            padx=12,
            pady=10,
            cursor="hand2"
        ).pack(side="right")

        # Task list
        self.task_frame = tk.Frame(root, bg="#101827")
        self.task_frame.pack(
            fill="both", expand=True, padx=25, pady=20
        )

        self.task_list = tk.Listbox(
            self.task_frame,
            font=("Arial", 12),
            bg="#1e293b",
            fg="white",
            selectbackground="#0284c7",
            selectforeground="white",
            relief="flat",
            borderwidth=0,
            activestyle="none"
        )
        self.task_list.pack(fill="both", expand=True)

        # Action buttons
        button_frame = tk.Frame(root, bg="#101827")
        button_frame.pack(pady=5)

        tk.Button(
            button_frame,
            text="Complete ✓",
            command=self.complete_task,
            bg="#16a34a",
            fg="white",
            relief="flat",
            padx=12,
            pady=9,
            cursor="hand2"
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Delete 🗑",
            command=self.delete_task,
            bg="#dc2626",
            fg="white",
            relief="flat",
            padx=12,
            pady=9,
            cursor="hand2"
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Clear All",
            command=self.clear_tasks,
            bg="#475569",
            fg="white",
            relief="flat",
            padx=12,
            pady=9,
            cursor="hand2"
        ).grid(row=0, column=2, padx=5)

        # Task counter
        self.counter = tk.Label(
            root,
            text="Total: 0 | Completed: 0",
            font=("Arial", 10),
            bg="#101827",
            fg="#94a3b8"
        )
        self.counter.pack(pady=15)

    def add_task(self):
        task = self.task_entry.get().strip()

        if not task:
            messagebox.showwarning("Empty Task", "Please enter a task!")
            return

        self.tasks.append({"text": task, "completed": False})
        self.task_entry.delete(0, tk.END)
        self.refresh_tasks()

    def complete_task(self):
        selection = self.task_list.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection", "Please select a task first!"
            )
            return

        index = selection[0]
        self.tasks[index]["completed"] = not self.tasks[index]["completed"]
        self.refresh_tasks()

    def delete_task(self):
        selection = self.task_list.curselection()

        if not selection:
            messagebox.showwarning(
                "No Selection", "Please select a task to delete!"
            )
            return

        del self.tasks[selection[0]]
        self.refresh_tasks()

    def clear_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Empty List", "There are no tasks to clear.")
            return

        confirm = messagebox.askyesno(
            "Confirm", "Do you want to delete all tasks?"
        )

        if confirm:
            self.tasks.clear()
            self.refresh_tasks()

    def refresh_tasks(self):
        self.task_list.delete(0, tk.END)

        completed_count = 0

        for task in self.tasks:
            if task["completed"]:
                display_text = "✓  " + task["text"] + " (Completed)"
                completed_count += 1
            else:
                display_text = "○  " + task["text"]

            self.task_list.insert(tk.END, display_text)

        self.counter.config(
            text=f"Total: {len(self.tasks)} | Completed: {completed_count}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
