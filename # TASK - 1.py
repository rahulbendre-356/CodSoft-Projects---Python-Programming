from tkinter import *
import tkinter.messagebox as msg
import os
from termcolor import colored

class ZenTaskManager(Tk):
    def __init__(self):
        super().__init__()
        # Setup window
        self.setup_window()
        # Create interface 
        self.build_interface()
        # Initialize data
        self.load_tasks()

    def setup_window(self):
        """Configure main window properties"""
        w, h = 900, 650
        x = (self.winfo_screenwidth() // 2) - (w // 2)
        y = (self.winfo_screenheight() // 2) - (h // 2)
        self.geometry(f'{w}x{h}+{x}+{y}')
        self.title("🧘 Zen Task Manager")
        self.resizable(False, False)
        self.configure(bg="#f8f9fa")

    def build_interface(self):
        """Create all UI components"""
        # Header
        header = Frame(self, bg="#6c5ce7", height=80)
        header.pack(fill=X)
        Label(header, text="🧘 ZEN TASK MANAGER", font=("Georgia", 24, "bold"), 
              fg="white", bg="#6c5ce7").pack(pady=20)

        # Input section
        input_frame = Frame(self, bg="#ddd6fe", height=80)
        input_frame.pack(fill=X, padx=20, pady=10)
        
        self.task_entry = Entry(input_frame, font=("Segoe UI", 16), bd=0, relief="flat",
                               bg="white", fg="#2d3748", insertbackground="#6c5ce7")
        self.task_entry.pack(side=LEFT, fill=X, expand=True, padx=(20, 10), pady=20, ipady=8)
        
        Button(input_frame, text="➕ ADD", font=("Segoe UI", 12, "bold"), 
               bg="#00b894", fg="white", bd=0, cursor="hand2", padx=20,
               command=self.add_task).pack(side=RIGHT, padx=(0, 20), pady=20)

        # Main content area
        content = Frame(self, bg="#f8f9fa")
        content.pack(fill=BOTH, expand=True, padx=20, pady=10)

        # Task list with scrollbar
        list_frame = Frame(content, bg="white", relief="solid", bd=1)
        list_frame.pack(fill=BOTH, expand=True, pady=(0, 10))
        
        self.task_list = Listbox(list_frame, font=("Segoe UI", 14), bd=0, relief="flat",
                                bg="white", fg="#2d3748", selectbackground="#a29bfe",
                                activestyle="none", cursor="hand2")
        self.task_list.pack(side=LEFT, fill=BOTH, expand=True, padx=10, pady=10)
        
        scrollbar = Scrollbar(list_frame, command=self.task_list.yview)
        scrollbar.pack(side=RIGHT, fill=Y, pady=10, padx=(0, 10))
        self.task_list.config(yscrollcommand=scrollbar.set)

        # Action buttons
        actions = Frame(content, bg="#f8f9fa")
        actions.pack(fill=X)
        
        buttons = [
            ("✏️ Edit", "#fdcb6e", self.edit_task),
            ("✓ Complete", "#00b894", self.complete_task),
            ("↩️ Restore", "#74b9ff", self.restore_task),
            ("🗑️ Delete", "#e17055", self.delete_task),
            ("🧹 Clear All", "#6c5ce7", self.clear_all)
        ]
        
        for text, color, cmd in buttons:
            Button(actions, text=text, font=("Segoe UI", 10, "bold"), bg=color,
                  fg="white", bd=0, cursor="hand2", pady=8, width=12,
                  command=cmd).pack(side=LEFT, padx=5)

    def ensure_file_exists(self):
        """Create todo file if it doesn't exist"""
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as f:
                pass

    def load_tasks(self):
        """Load tasks from file and display in listbox"""
        self.ensure_file_exists()
        self.task_list.delete(0, END)
        
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    if line.strip():
                        self.task_list.insert(END, line.strip())
        except Exception as e:
            print(colored(f"Error loading tasks: {e}", "red"))

    def save_tasks(self):
        """Save all tasks from listbox to file"""
        try:
            with open("tasks.txt", "w") as f:
                for i in range(self.task_list.size()):
                    f.write(self.task_list.get(i) + "\n")
        except Exception as e:
            print(colored(f"Error saving tasks: {e}", "red"))

    def add_task(self):
        """Add new task to the list"""
        task = self.task_entry.get().strip()
        if task:
            self.task_list.insert(END, task)
            self.task_entry.delete(0, END)
            self.save_tasks()
            print(colored(f"Added task: {task}", "green"))
        else:
            msg.showwarning("Warning", "Please enter a task!")

    def get_selected(self):
        """Get selected task index or show warning"""
        selection = self.task_list.curselection()
        if not selection:
            msg.showwarning("Warning", "Please select a task!")
            return None
        return selection[0]

    def complete_task(self):
        """Mark selected task as completed (gray out)"""
        idx = self.get_selected()
        if idx is not None:
            self.task_list.itemconfig(idx, fg="#95a5a6")
            self.task_list.selection_clear(0, END)
            msg.showinfo("Success", "Task marked as completed!")

    def restore_task(self):
        """Restore completed task to active state"""
        idx = self.get_selected()
        if idx is not None:
            self.task_list.itemconfig(idx, fg="#2d3748")
            self.task_list.selection_clear(0, END)
            msg.showinfo("Success", "Task restored!")

    def edit_task(self):
        """Edit selected task in popup window"""
        idx = self.get_selected()
        if idx is None:
            return
            
        current_task = self.task_list.get(idx)
        
        # Create edit popup
        popup = Toplevel(self)
        popup.geometry("500x200")
        popup.title("Edit Task")
        popup.configure(bg="#f8f9fa")
        popup.resizable(False, False)
        
        Label(popup, text="Edit your task:", font=("Segoe UI", 14, "bold"),
              bg="#f8f9fa", fg="#2d3748").pack(pady=20)
        
        entry = Entry(popup, font=("Segoe UI", 14), width=40, bd=2, relief="solid")
        entry.pack(pady=10, ipady=5)
        entry.insert(0, current_task)
        entry.focus()
        
        def save_edit():
            new_task = entry.get().strip()
            if new_task:
                self.task_list.delete(idx)
                self.task_list.insert(idx, new_task)
                self.save_tasks()
                popup.destroy()
                msg.showinfo("Success", "Task updated!")
            else:
                msg.showwarning("Warning", "Task cannot be empty!")
        
        btn_frame = Frame(popup, bg="#f8f9fa")
        btn_frame.pack(pady=20)
        
        Button(btn_frame, text="Save", font=("Segoe UI", 12, "bold"),
               bg="#00b894", fg="white", bd=0, padx=20, pady=5,
               command=save_edit).pack(side=LEFT, padx=10)
        
        Button(btn_frame, text="Cancel", font=("Segoe UI", 12, "bold"),
               bg="#e17055", fg="white", bd=0, padx=20, pady=5,
               command=popup.destroy).pack(side=LEFT, padx=10)

    def delete_task(self):
        """Delete completed (grayed out) tasks"""
        deleted_count = 0
        
        # Collect completed tasks
        completed_tasks = []
        for i in range(self.task_list.size()):
            if self.task_list.itemcget(i, 'fg') == "#95a5a6":
                completed_tasks.append((i, self.task_list.get(i)))
        
        if not completed_tasks:
            msg.showinfo("Info", "No completed tasks to delete. Complete tasks first!")
            return
        
        # Confirm and delete
        if msg.askyesno("Confirm", f"Delete {len(completed_tasks)} completed task(s)?"):
            for idx, task in reversed(completed_tasks):
                self.task_list.delete(idx)
                deleted_count += 1
                print(colored(f"Deleted: {task}", "red"))
            
            self.save_tasks()
            msg.showinfo("Success", f"Deleted {deleted_count} task(s)!")

    def clear_all(self):
        """Clear all tasks after confirmation"""
        if self.task_list.size() == 0:
            msg.showinfo("Info", "No tasks to clear!")
            return
            
        if msg.askyesno("Confirm", "Clear all tasks?"):
            self.task_list.delete(0, END)
            self.save_tasks()
            msg.showinfo("Success", "All tasks cleared!")
            print(colored("All tasks cleared", "yellow"))

    def run(self):
        """Start the application"""
        self.mainloop()

if __name__ == '__main__':
    app = ZenTaskManager()
    app.run()