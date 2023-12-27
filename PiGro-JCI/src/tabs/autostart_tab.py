import os
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *


class AutostartsTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.create_autostart_frame = LabelFrame(
            self,
            text="Create An Autostart File",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
            padx=40,
            background=frame_color,
        )

        self.create_autostart_frame.pack(pady=20, padx=40, fill="x")
        self.create_autostart_frame.columnconfigure(1, weight=1)
        self.create_autostart_frame.rowconfigure(1, weight=1)

        self.filename_label = tk.Label(
            self.create_autostart_frame,
            text="Filename:",
            anchor="w",
            justify=LEFT,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
        )
        self.filename_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.filename_entry = tk.Entry(
            self.create_autostart_frame,
            highlightthickness=0,
            borderwidth=0,
        )
        self.filename_entry.grid(
            row=0, column=1, columnspan=2, padx=10, pady=5, sticky="ewns"
        )

        self.command_label = tk.Label(
            self.create_autostart_frame,
            text="Command:",
            anchor="w",
            justify=LEFT,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
        )
        self.command_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")

        self.command_entry = tk.Entry(
            self.create_autostart_frame,
            highlightthickness=1,
            borderwidth=0,
        )
        self.command_entry.grid(
            row=1, column=1, columnspan=2, padx=10, pady=5, sticky="ewns"
        )

        self.create_button = Button(
            self.create_autostart_frame,
            text="Create Autostart",
            command=self.create_autostart_file,
            foreground=ext_btn_font,
            background=ext_btn,
            borderwidth=0,
            highlightthickness=0,
        )
        self.create_button.grid(
            row=2, column=1, columnspan=2, padx=10, pady=5, sticky="ew"
        )

        self.list_autostart_frame = LabelFrame(
            self,
            text="Existing Autostarts",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
            padx=40,
            background=frame_color,
        )

        self.list_autostart_frame.pack(pady=20, padx=40, fill="both", expand=True)

        self.treeview = ttk.Treeview(
            self.list_autostart_frame,
            columns=("Filename", "Command"),
            show="headings",
        )
        self.treeview.heading("Filename", text="Filename")
        self.treeview.heading("Command", text="Command")
        self.treeview.pack(fill="both", expand=True)

        self.populate_treeview()

        self.remove_button = tk.Button(
            self.list_autostart_frame,
            text="Remove Selected",
            command=self.remove_autostart,
            foreground=ext_btn_font,
            background=ext_btn,
            borderwidth=0,
            highlightthickness=0,
        )
        self.remove_button.pack(pady=10, fill="x")

    def error_mass(self):
        e_mass = Error_Mass(self)
        e_mass.grab_set()

    def create_autostart_file(self):
        if self.filename_entry.get() == "" or self.command_entry.get() == "":
            self.error_mass()
        else:
            filename = self.filename_entry.get()
            command = self.command_entry.get()
            if not filename or not command:
                return

            autostart_path = os.path.expanduser("~/.config/autostart/")
            os.makedirs(autostart_path, exist_ok=True)
            filepath = os.path.join(autostart_path, f"{filename}.desktop")
            with open(filepath, "w") as f:
                f.write("[Desktop Entry]\n")
                f.write("Type=Application\n")
                f.write(f"Name={filename}\n")
                f.write(f"Exec={command}\n")
                f.write("X-GNOME-Autostart-enabled=true\n")
            self.populate_treeview()

    def remove_autostart(self):
        selected_item = self.treeview.selection()
        if not selected_item:
            return

        autostart_path = os.path.expanduser("~/.config/autostart/")
        selected_filename = self.treeview.item(selected_item)["values"][0]

        try:
            filepath = os.path.join(autostart_path, selected_filename)
            os.remove(filepath)
            self.treeview.delete(selected_item)
        except Exception as e:
            print(
                f"\033[48;5;236m\033[38;5;231m[Info] \033[38;5;208mError removing autostart: {e}\033[0;0m"
            )

    def populate_treeview(self):
        autostart_path = os.path.expanduser("~/.config/autostart/")
        self.treeview.delete(*self.treeview.get_children())
        for filename in os.listdir(autostart_path):
            if filename.endswith(".desktop"):
                filepath = os.path.join(autostart_path, filename)
                with open(filepath, "r") as f:
                    lines = f.readlines()
                    entry = [
                        line.strip().split("=")[1]
                        for line in lines
                        if line.startswith("Name=") or line.startswith("Exec=")
                    ]
                    if len(entry) == 2:
                        self.treeview.insert("", "end", values=(filename, entry[1]))
