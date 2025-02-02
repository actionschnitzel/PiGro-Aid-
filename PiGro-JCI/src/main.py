#!/usr/bin/python3

from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.dash_tab import DashTab
from tabs.update_tab import UpdateTab
from tabs.sources_tab import SourcesTab
from tabs.system_tab import SystemTab
from tabs.look_tab import LookTab
from tabs.tasks_tab import TasksTab
from tabs.autostart_tab import AutostartsTab
from tabs.software_tab import *
from tabs.tuning_tab import TuningTab
from tabs.deb_recovery_tab import DebRecoverTab
from tabs.links_tab import LinksTab
from tabs.about_tab import AboutTab
from int_theme import SetTheme
from icon_lib import NavIcons, PigroIcons


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__(className="PiGro")
        self.title("PiGro - Just Click It! (A più di ottomila Accipicchia!)")

        app_width = 1200
        app_height = 900
        # Define Screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        # self.icon is still needed for some DEs
        self.pigro_icons = PigroIcons()
        self.tk.call("wm", "iconphoto", self._w, self.pigro_icons.pigro_256)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.nav_icons = NavIcons()
        self.set_theme = SetTheme(self)

        self.notebook = ttk.Notebook(self, width=app_width, height=app_height)
        self.notebook.grid(row=0, column=0, sticky="nsew")

        self.dash_tab = DashTab(self.notebook)
        self.update_tab = UpdateTab(self.notebook)
        self.sources_tab = SourcesTab(self.notebook)
        self.system_tab = SystemTab(self.notebook)
        self.look_tab = LookTab(self.notebook)
        self.autostart_tab = AutostartsTab(self.notebook)
        self.tasks_tab = TasksTab(self.notebook)
        self.software_tab = SoftwareTab(self.notebook)
        self.tuning_tab = TuningTab(self.notebook)
        self.deb_recovery_tab = DebRecoverTab(self.notebook)
        self.links_tab = LinksTab(self.notebook)
        self.about_tab = AboutTab(self.notebook)

        self.notebook.add(
            self.dash_tab,
            compound=LEFT,
            text="Dashboard",
            image=self.nav_icons.status_icon,
        )
        self.notebook.add(
            self.update_tab,
            compound=LEFT,
            text="Update",
            image=self.nav_icons.update_icon,
        )
        self.notebook.add(
            self.sources_tab,
            compound=LEFT,
            text="Source List",
            image=self.nav_icons.source_lists,
        )
        self.notebook.add(
            self.system_tab,
            compound=LEFT,
            text="System",
            image=self.nav_icons.system_icon,
        )
        self.notebook.add(
            self.look_tab,
            compound=LEFT,
            text="Look & Feel",
            image=self.nav_icons.look_icon,
        )
        self.notebook.add(
            self.autostart_tab,
            compound=LEFT,
            text="Autostart",
            image=self.nav_icons.auto_start,
        )
        self.notebook.add(
            self.tasks_tab, compound=LEFT, text="Tasks", image=self.nav_icons.kill_proc
        )
        self.notebook.add(
            self.software_tab,
            compound=LEFT,
            text="Software",
            image=self.nav_icons.install_icon,
        )
        self.notebook.add(
            self.tuning_tab,
            compound=LEFT,
            text="Tuning",
            image=self.nav_icons.tuning_icon,
        )
        self.notebook.add(
            self.deb_recovery_tab,
            compound=LEFT,
            text="Backup",
            image=self.nav_icons.deb_pack,
        )
        self.notebook.add(
            self.links_tab, compound=LEFT, text="Links", image=self.nav_icons.links_icon
        )
        self.notebook.add(
            self.about_tab,
            compound=LEFT,
            text="About",
            image=self.nav_icons.support_icon,
        )

        # Notebook Theming
        global noteStyler
        noteStyler = ttk.Style(self)
        noteStyler.configure(
            "TNotebook",
            borderwidth=0,
            tabposition="w",
            highlightthickness=0,
        )
        noteStyler.configure(
            "TNotebook.Tab",
            borderwidth=0,
            font=font_10,
            width=15,
            highlightthickness=0,
        )

        noteStyler.configure("TButton", justify="left", anchor="w")

        noteStyler.configure("Custom.TButton", justify="center", anchor="center")


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
