from __future__ import annotations

from tkinter import Tk
from functools import partial
from pathlib import Path
from tkinter import ttk
import os
import subprocess
import sys

TCL_THEME_FILE_PATH = Path(__file__).with_name("azure.tcl").absolute()
# print(TCL_THEME_FILE_PATH)


def run_command(command):
    """Helper function to run shell commands and capture output."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        return None


def get_desktop_environment():
    xdg_current_desktop = os.environ.get("XDG_CURRENT_DESKTOP").lower()
    # print(xdg_current_desktop)
    # Check for specific desktop environments
    if xdg_current_desktop == "x-cinnamon" or xdg_current_desktop == "cinnamon":
        return "CINNAMON"
    elif xdg_current_desktop == "unity":
        return "UNITY"
    elif xdg_current_desktop == "ubuntu:gnome":
        return "GNOME"
    elif "gnome" in xdg_current_desktop:
        return "GNOME"
    elif "plasma" == xdg_current_desktop or "kde" == xdg_current_desktop:
        return "KDE"
    elif "xfce" == xdg_current_desktop:
        return "XFCE"
    elif "lxde" == xdg_current_desktop:
        return "LXDE"
    elif "lxde-pi-wayfire" == xdg_current_desktop:
        return "PI-WAYFIRE"
    elif "mate" == xdg_current_desktop:
        return "MATE"
    else:
        return "Unknown"


def get_lxde_theme_name():
    """Retrieve the current theme for LXDE from the desktop.conf file."""
    directory_path = os.path.expanduser("~/.config/lxsession/LXDE-pi/")
    config_file_path = os.path.join(directory_path, "desktop.conf")

    # Ensure ~/.config/lxsession/LXDE-pi/desktop.conf exists
    if not os.path.exists(directory_path):
        print("Directory does not exist. Creating", directory_path)
        os.makedirs(directory_path)
        with open(config_file_path, "w") as f:
            f.write(
                """[GTK]
sNet/ThemeName=PiXflat
sGtk/ColorScheme=selected_bg_color:#87919B\nselected_fg_color:#F0F0F0\nbar_bg_color:#EDECEB\nbar_fg_color:#000000\n
sGtk/FontName=PibotoLt 12
iGtk/ToolbarIconSize=3
sGtk/IconSizes=gtk-large-toolbar=24,24
iGtk/CursorThemeSize=24"""
            )
        return "PiXflat"
    else:
        with open(config_file_path, "r") as file:
            for line in file:
                if "sNet/ThemeName=" in line:
                    theme_name = line.split("=")[1].strip()
                    return theme_name
        return "Theme not found."


def get_theme():
    """Get the current GTK or KDE theme based on the desktop environment."""
    de = get_desktop_environment()

    if not de:
        return "Desktop Environment not detected."

    # KDE/Plasma
    if "KDE" in de or "PLASMA" in de:
        kde_config_file = os.path.expanduser("~/.config/kdeglobals")
        if os.path.exists(kde_config_file):
            kde_theme = run_command(f"grep 'Name=' {kde_config_file}")
            if kde_theme:
                return kde_theme.split("=")[-1].strip().strip("'")
        return "KDE theme not found."

    elif "CINNAMON" in de:
        theme = run_command("gsettings get org.cinnamon.desktop.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."
    elif "UNITY" in de:
        theme = run_command("gsettings get org.gnome.desktop.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."

    elif "GNOME" in de:
        theme = run_command("gsettings get org.gnome.desktop.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."

    elif "BUDGIE" in de:
        theme = run_command("gsettings get org.gnome.desktop.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."

    elif "PI-WAYFIRE" in de:
        theme = run_command("gsettings get org.gnome.desktop.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."
    elif "MATE" in de:
        theme = run_command("gsettings get org.mate.interface gtk-theme")
        return theme.strip("'") if theme else "Theme not found."
    elif "XFCE" in de:
        theme = run_command("xfconf-query -c xsettings -p /Net/ThemeName")
        return theme.strip("'") if theme else "Theme not found."
    elif "LXDE" in de or "LXDE-PI" in de:
        return get_lxde_theme_name()

    return "Unsupported Desktop Environment."


theme_name = get_theme()


# print(theme_name)
class SetTheme:
    def __init__(self, tk_instance):
        self.tk = tk_instance
        self.tk.call("source", TCL_THEME_FILE_PATH)
        if "dark" in get_theme() or "noir" in get_theme():
            self.tk.call("set_theme", "dark")
        else:
            self.tk.call("set_theme", "light")
