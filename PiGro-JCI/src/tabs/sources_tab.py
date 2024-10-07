#!/usr/bin/python3

import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *


class SourcesTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")


        self.rep_main_frame = ttk.Frame(
            self
        )
        self.rep_main_frame.pack(fill=BOTH, expand=True, pady=20, padx=20)

        self.off_rep_frame = ttk.LabelFrame(
            self.rep_main_frame,
            text="Official Repository",
            padding=20
        )

        self.off_rep_frame.pack(fill=BOTH, expand=True)

        self.tu_info = ttk.Label(
            self.off_rep_frame,
            text="Info: Never edit the source lists unless you know exactly what you are doing.\n",

        ).pack()

        self.tree = ttk.Treeview(self.off_rep_frame)
        self.tree.pack(expand=True, fill=BOTH)

        # add columns to the treeview
        self.tree["columns"] = ("one", "two", "three")
        self.tree.column("#0", width=30, minwidth=30)
        self.tree.column("one", width=10, minwidth=100)
        self.tree.column("two", width=350, minwidth=100)
        self.tree.column("three", width=350, minwidth=100)

        # add column headings
        self.tree.heading("#0", text="Nr.",)
        self.tree.heading("one", text="Type")
        self.tree.heading("two", text="Source URL")
        self.tree.heading("three", text="Source Parameters")

        try:
            with open("/etc/apt/sources.list", "r") as f:
                sources = f.readlines()

            for i, source in enumerate(sources):
                source_cols = source.strip().split(" ", 2)
                self.tree.insert(
                    parent="",
                    index=i,
                    iid=i,
                    text=str(i + 1),
                    values=(source_cols[0], source_cols[1], source_cols[2]),
                )
        except:
            pass

        self.added_repositories = ttk.LabelFrame(
            self.rep_main_frame,
            text="Added Repository",
            padding=20
        )
        self.added_repositories.pack(fill="both", expand=True)

        self.added_tree_frame = tk.Frame(self.added_repositories)
        self.added_tree_frame.pack(fill="both", expand=True)

        self.added_treeview = ttk.Treeview(
            self.added_tree_frame, columns=("name"), show="headings"
        )
        self.added_treeview.heading("name", text="Name")
        self.added_treeview.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(
            self.added_tree_frame, orient="vertical", command=self.added_treeview.yview
        )
        self.scrollbar.pack(side="right", fill="y")

        self.added_treeview.configure(yscrollcommand=self.scrollbar.set)

        self.add_sources_to_treeview()

        def open_source_f_d():
            if pi_identify() == "pi_os":
                popen(f"sudo pcmanfm /etc/apt/sources.list.d")
                print("[Info] With great power comes great responsibility")
            else:
                popen(
                    f"pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xdg-open /etc/apt/sources.list.d"
                )

        self.open_source_folder = ttk.Button(
            self.rep_main_frame,
            text="Open sources.list.d",
            command=open_source_f_d,
            style="Custom.TButton"

        )
        self.open_source_folder.pack(padx=20, expand=True, fill="x")

    def add_sources_to_treeview(self):
        sources_d1 = os.listdir("/etc/apt/sources.list.d")

        for file in sources_d1:
            self.added_treeview.insert("", "end", values=(file))
