#!/usr/bin/python3

import os
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from resorcess import *
from apt_manage import *
from snap_manage import *
from flatpak_alias_list import *
from flatpak_manage import *
from tabs.pop_ups import *
from resorcess import pi_identify
import gettext
import threading
import subprocess
from icon_lib import UpdateTabIcons


class UpdateTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.update_tab_icons = UpdateTabIcons()

        def execute_command(command, event=None):
            self.term_logo_label.grid_forget()
            self.terminal.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

            self.terminal_scroll.grid(row=0, column=1, sticky="ns")
            self.terminal.config(yscrollcommand=self.terminal_scroll.set)
            if command.strip() == "":
                return

            # Starte den Befehl in einem separaten Thread, um das GUI nicht zu blockieren
            thread = threading.Thread(target=run_command, args=(command,))
            thread.start()

        def run_command(command):
            # Starte den Prozess mit Popen
            process = subprocess.Popen(
                command,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
            )

            # Lese Zeile für Zeile und aktualisiere das Text-Widget
            for line in iter(process.stdout.readline, ""):
                self.terminal.insert(tk.END, line)
                self.terminal.see(tk.END)  # Auto-Scroll

            process.stdout.close()
            process.wait()
            self.term_quit_button.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        def kill_term():
            self.terminal.delete(1.0, tk.END)
            self.terminal.grid_forget()
            self.terminal_scroll.grid_forget()
            self.term_quit_button.grid_forget()
            self.term_logo_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        def all_up_action():
            allup = f"{permit} {application_path}/scripts/all_up"
            execute_command(allup)

        def update_action():
            update_command = f"{permit} {application_path}/scripts/nala_update_wrap"
            execute_command(update_command)

        def upgrade_action():
            upgrade_command = f"{permit} {application_path}/scripts/nala_upgrade_wrap"
            execute_command(upgrade_command)

        def apt_showupgrade_action():
            show_command = f"{application_path}/scripts/apt_list_upgradeble_wrap"
            execute_command(show_command)

        def apt_autremove_action():
            autorm_command = f"pkexec {application_path}/scripts/nala_autopurge_wrap"
            execute_command(autorm_command)

        def apt_broken_action():
            fix_broken_action = f"pkexec {application_path}/scripts/apt_fix_broken_wrap"
            execute_command(fix_broken_action)

        def apt_missing_action():
            fix_missing_action = (
                f"pkexec {application_path}/scripts/apt_fix_missing_wrap"
            )
            execute_command(fix_missing_action)

        def apt_reconf_action():
            fix_missing_action = f"pkexec {application_path}/scripts/conf-a_wrap"
            execute_command(fix_missing_action)

        def flatpak_update_action():
            flat_up_command = (
                f"{application_path}/scripts/flatpak_update_wrap && exit ; exec bash"
            )
            execute_command(flat_up_command)

        def flatpak_clean_action():
            flat_clean_command = f"{application_path}/scripts/flatpak_clean_wrap"
            execute_command(flat_clean_command)


        self.update_button_frame = ttk.Frame(self, padding=20)
        self.update_button_frame.grid(row=0, column=0, sticky="ns")


        self.apt_option_frame = ttk.LabelFrame(
            self.update_button_frame,
            text="APT-Optionen",
        )
        self.apt_option_frame.pack(pady=10)

        self.apt_update_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Update",
            image=self.update_tab_icons.up_icon,
            command=update_action,
            width=20,
        )

        self.apt_update_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.apt_upgrade_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Upgrade",
            image=self.update_tab_icons.gup_icon,
            command=upgrade_action,
            width=20,
        )

        self.apt_upgrade_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.apt_showupgrade_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Show Upgradeble",
            image=self.update_tab_icons.up_icon,
            command=apt_showupgrade_action,
            width=20,
        )

        self.apt_showupgrade_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")

        self.apt_autoremove_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Autoremove",
            image=self.update_tab_icons.arm_icon,
            command=apt_autremove_action,
            width=20,
        )

        self.apt_autoremove_button.grid(row=3, column=0, padx=5, pady=5, sticky="ew")

        self.apt_broken_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Fix Broken",
            image=self.update_tab_icons.up_icon,
            command=apt_broken_action,
            width=20,
        )

        self.apt_broken_button.grid(row=4, column=0, padx=5, pady=5, sticky="ew")

        self.apt_missing_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="Fix Missing",
            image=self.update_tab_icons.up_icon,
            command=apt_missing_action,
            width=20,
        )

        self.apt_missing_button.grid(row=5, column=0, padx=5, pady=5, sticky="ew")

        self.apt_cinfigure_a_button = ttk.Button(
            self.apt_option_frame,
            compound="left",
            text="dpkg --configure -a",
            image=self.update_tab_icons.confa_icon,
            command=apt_reconf_action,
            width=20,
        )

        self.apt_cinfigure_a_button.grid(row=6, column=0, padx=5, pady=5, sticky="ew")

        self.flatpak_option_frame = ttk.LabelFrame(
            self.update_button_frame,
            text="Flatpak-Optionen",
        )
        self.flatpak_option_frame.pack(pady=10)

        self.flatpak_update_button = ttk.Button(
            self.flatpak_option_frame,
            compound="left",
            text="Update",
            image=self.update_tab_icons.up_icon,
            command=flatpak_update_action,
            width=20,
        )

        self.flatpak_update_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.flatpak_clean_button = ttk.Button(
            self.flatpak_option_frame,
            compound="left",
            text="Tidy Up Unused",
            image=self.update_tab_icons.arm_icon,
            command=flatpak_clean_action,
            width=20,
        )

        self.flatpak_clean_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        self.update_term_frame = ttk.LabelFrame(self, text="Prozess")
        self.update_term_frame.grid(row=0, column=1, sticky="nesw", padx=20, pady=20)
        self.update_term_frame.grid_rowconfigure(0, weight=1)
        self.update_term_frame.grid_columnconfigure(0, weight=1)

        self.term_logo_label = Label(
            self.update_term_frame,
            image=self.update_tab_icons.term_logo,
        )
        self.term_logo_label.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)

        self.terminal = tk.Text(
            self.update_term_frame, height=20, borderwidth=0, highlightthickness=0
        )

        self.terminal_scroll = ttk.Scrollbar(
            self.update_term_frame, orient="vertical", command=self.terminal.yview
        )

        self.term_quit_button = ttk.Button(
            self.update_term_frame,
            text="Beenden",
            style="Accent.TButton",
            command=kill_term,
        )

        # Erstelle ein Frame-Widget mit fester Größe
        self.update_info_frame = ttk.LabelFrame(self, text="Info")
        self.update_info_frame.grid(
            row=1, column=0, columnspan=2, sticky="nesw", padx=20, pady=20
        )

        # Setze die feste Größe des Frames und deaktiviere die automatische Größenanpassung
        self.update_info_frame.config(width=900, height=100)
        self.update_info_frame.pack_propagate(False)

        # Erstelle ein Label-Widget innerhalb des Frames
        self.update_info_label = ttk.Label(
            self.update_info_frame, text="", justify="left", wraplength=880
        )
        self.update_info_label.pack(anchor="sw", fill="x", padx=10, pady=5)

        # Binde die Ereignisse an die Buttons
        self.apt_update_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'apt update' command is executed to refresh the package index. This ensures that the package manager is aware of the latest versions of packages available from the repositories."
            ),
        )
        self.apt_update_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_upgrade_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'apt update && apt upgrade' command sequence is executed to first refresh the package index and then upgrade all installed packages to their latest available versions. This ensures that your system is up-to-date with the latest software improvements and security patches."
            ),
        )
        self.apt_upgrade_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_showupgrade_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="This command lists all packages that have available upgrades. It provides a summary of the packages that can be updated, allowing you to review them before proceeding with an upgrade."
            ),
        )
        self.apt_showupgrade_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_autoremove_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'apt autoremove' command removes packages that were automatically installed to satisfy dependencies for other packages and are now no longer needed. This helps to free up disk space and keep your system clean."
            ),
        )
        self.apt_autoremove_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_broken_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'apt --fix-broken install' command attempts to repair broken package dependencies. It installs any missing dependencies and fixes any issues with packages that are in a broken state, ensuring the integrity of your package management system."
            ),
        )
        self.apt_broken_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_missing_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'apt install --fix-missing' command downloads and installs any missing package files that were not successfully downloaded during a previous attempt. This command helps to complete the installation process by fetching the necessary files."
            ),
        )
        self.apt_missing_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.apt_cinfigure_a_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'dpkg --configure -a' command configures all packages that have been unpacked but not yet fully configured. This command is useful for fixing installation issues and ensuring that all packages are properly set up."
            ),
        )
        self.apt_cinfigure_a_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.flatpak_update_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="This command updates all installed Flatpak applications to their latest versions. It ensures that your Flatpak applications are up-to-date with the latest features and security patches."
            ),
        )
        self.flatpak_update_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )

        self.flatpak_clean_button.bind(
            "<Enter>",
            lambda event: self.update_info_label.configure(
                text="The 'flatpak clean' command removes any leftover dependencies and temporary files that are no longer needed. This helps to free up disk space and keep your Flatpak environment clean."
            ),
        )
        self.flatpak_clean_button.bind(
            "<Leave>", lambda event: self.update_info_label.configure(text="")
        )
