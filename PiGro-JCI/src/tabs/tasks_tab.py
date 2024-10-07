from tkinter import *
from tkinter import ttk
import psutil
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *


class TasksTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.main_frame = ttk.Frame(
            self
        )

        self.main_frame.pack(fill="both", expand=True)

        self.proc_frame = ttk.Frame(
            self.main_frame,
            padding=20

        )

        self.proc_frame.pack(fill="both", expand=True)

        # create the treeview
        self.tree = ttk.Treeview(self.proc_frame, columns=("pid", "memory"))
        self.tree.heading("#0", text="Process Name")
        self.tree.heading("pid", text="PID")
        self.tree.heading("memory", text="Memory Usage (MB)")
        # create a scrollbar for the treeview
        scrollbar = ttk.Scrollbar(
            self.proc_frame, orient="vertical", command=self.tree.yview
        )
        self.tree.configure(yscrollcommand=scrollbar.set)

        # pack the treeview and scrollbar widgets
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        # create a dictionary to store the running processes and their IDs in the treeview
        self.processes = {}

        # create a button to terminate the selected process
        self.terminate_button = ttk.Button(
            self.main_frame,
            text="Terminate Process",
            command=self.terminate_process,
            style="Custom.TButton"
        )
        self.terminate_button.pack(fill="x", padx=20, pady=10)

        # schedule the update_processes method to run every second
        self.update_processes()

    def update_processes(self):
        # get a list of running processes
        running_processes = psutil.process_iter()

        # loop through each process and add it to the treeview
        for proc in running_processes:
            pid = proc.pid
            try:
                name = proc.name()
                memory = proc.memory_info().rss
                # convert memory usage to MB
                memory_mb = round(memory / (1024 * 1024), 2)
                if name not in self.processes:
                    # add the process to the treeview
                    item = self.tree.insert(
                        "", "end", text=name, values=(pid, memory_mb)
                    )
                    # store the process ID and treeview item for later use
                    self.processes[name] = (pid, item)
                else:
                    # update the existing process's memory usage in the treeview
                    self.tree.set(self.processes[name][1], "memory", memory_mb)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                # ignore any processes we can't access
                pass

        # schedule the function to run again in 1 second
        self.after(1000, self.update_processes)

    def terminate_process(self):
        # get the selected process from the treeview
        selected_item = self.tree.selection()
        if not selected_item:
            return
        name = self.tree.item(selected_item)["text"]
        pid = self.processes[name][0]
        # terminate the process
        try:
            proc = psutil.Process(pid)
            proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
