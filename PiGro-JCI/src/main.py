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


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__(className="PiGro")
        self.title("PiGro - Just Click It! (Odio i vermi!)")
        self["background"] = maincolor
        app_width = 1200
        app_height = 900
        # Define Screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        # self.icon is still needed for some DEs
        self.icon = tk.PhotoImage(
            file=f"/usr/share/icons/hicolor/256x256/apps/pigro-logo.png"
        )
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        # Notebook Icons

        if "dark" in theme or "noir" in theme:
            self.status_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/dash_dark_24x24.png"
            )

            self.system_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sys_dark_24x24.png"
            )
            self.update_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/update_dark_24x24.png"
            )
            self.install_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/software_dark_24x24.png"
            )
            self.look_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/look_dark_24x24.png"
            )
            self.tuning_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tuning_dark_24x24.png"
            )
            self.links_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/links_dark_24x24.png"
            )
            self.support_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/about_dark_24x24.png"
            )
            self.cam_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/gtkam-camera.png"
            )
            self.ubuntu_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-ubuntu.png"
            )
            self.auto_start = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/auto_dark_24x24.png"
            )
            self.kill_proc = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tasks_dark_24x24.png"
            )
            self.git_more = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_dark_24x24.png"
            )

            self.deb_pack = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/backup_dark_24x24.png"
            )
            self.source_lists = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sources_dark_16x16.png"
            )

        else:
            self.status_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/dash_light_24x24.png"
            )
            self.system_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sys_light_24x24.png"
            )
            self.update_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/update_light_24x24.png"
            )
            self.install_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/software_light_24x24.png"
            )
            self.look_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/look_light_24x24.png"
            )
            self.tuning_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tuning_light_24x24.png"
            )
            self.links_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/links_light_24x24.png"
            )
            self.support_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/about_light_24x24.png"
            )
            self.cam_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/gtkam-camera.png"
            )
            self.ubuntu_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-ubuntu.png"
            )
            self.auto_start = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/auto_light_24x24.png"
            )
            self.kill_proc = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tasks_light_24x24.png"
            )
            self.git_more = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_light_24x24.png"
            )

            self.deb_pack = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/backup_light_24x24.png"
            )
            self.source_lists = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sources_light_16x16.png"
            )

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
            self.dash_tab, compound=LEFT, text="Dashboard", image=self.status_icon
        )
        self.notebook.add(
            self.update_tab, compound=LEFT, text="Update", image=self.update_icon
        )
        self.notebook.add(
            self.sources_tab, compound=LEFT, text="Source List", image=self.source_lists
        )
        self.notebook.add(
            self.system_tab, compound=LEFT, text="System", image=self.system_icon
        )
        self.notebook.add(
            self.look_tab, compound=LEFT, text="Look & Feel", image=self.look_icon
        )
        self.notebook.add(
            self.autostart_tab, compound=LEFT, text="Autostart", image=self.auto_start
        )
        self.notebook.add(
            self.tasks_tab, compound=LEFT, text="Tasks", image=self.kill_proc
        )
        self.notebook.add(
            self.software_tab, compound=LEFT, text="Software", image=self.install_icon
        )
        self.notebook.add(
            self.tuning_tab, compound=LEFT, text="Tuning", image=self.tuning_icon
        )
        self.notebook.add(
            self.deb_recovery_tab, compound=LEFT, text="Backup", image=self.deb_pack
        )
        self.notebook.add(
            self.links_tab, compound=LEFT, text="Links", image=self.links_icon
        )
        self.notebook.add(
            self.about_tab, compound=LEFT, text="About", image=self.support_icon
        )

        # Notebook Theming
        global noteStyler
        noteStyler = ttk.Style(self)
        # noteStyler.theme_use('clam')
        noteStyler.configure(
            "TNotebook",
            borderwidth=0,
            background=nav_color,
            tabposition="w",
            highlightthickness=0,
        )
        noteStyler.configure(
            "TNotebook.Tab",
            borderwidth=0,
            background=nav_color,
            foreground=main_font,
            font=font_10,
            width=15,
            highlightthickness=0,
        )
        noteStyler.configure("TFrame", background=maincolor)
        noteStyler.map(
            "TNotebook.Tab",
            background=[("selected", nav_color)],
            foreground=[("selected", "#cf274e")],
        )

        noteStyler.configure(
            "Vertical.TScrollbar",
            background=ext_btn,
            troughcolor="white",
            arrowcolor=ext_btn_font,
        )

        TROUGH_COLOR = nav_color
        BAR_COLOR = "#007acc"

        noteStyler.configure(
            "TSpinbox",
            troughcolor=TROUGH_COLOR,
            bordercolor=TROUGH_COLOR,
            background=BAR_COLOR,
            lightcolor=BAR_COLOR,
            darkcolor=BAR_COLOR,
            font=("Helvetica", 12),
        )

        noteStyler.configure(
            "Treeview.Heading",
            font=("TkDefaultFont", 12),
            foreground=main_font,
            background=frame_color,
            relief=FLAT,
        )

        # Seperator Theme
        noteStyler.configure("Line.TSeparator", background="grey", rekief="sunken")

        # Compbox Theme
        noteStyler.configure(
            "TCombobox",
            background=ext_btn,
            fieldbackground="white",
            arrowcolor=ext_btn_font,
            arrowsize=15,
            bordercolor="white",
            borderwidth=0,
            relief=FLAT,
        )
        noteStyler.map(
            "TCombobox",
            foreground=[("hover", "black")],
            background=[("hover", "white")],
        )


if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
