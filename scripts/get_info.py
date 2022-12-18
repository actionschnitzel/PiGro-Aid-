#!/usr/bin/python3

import os
import os.path
from os import chmod
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter.dialog import DIALOG_ICON
from turtle import left, width
import tkinter.font as tkFont
from tkinter import filedialog
import webbrowser
from os import popen
from os import system as cmd
from os import listdir
from os.path import isfile, join
import platform
import shutil
import psutil
from collections import namedtuple
from datetime import datetime
from time import strftime
import distro
import socket
from pathlib import Path
from cgitb import enable
from pynotifier import Notification
import threading
from threading import Thread
from concurrent.futures import thread
from faulthandler import disable
from turtle import width
import re
import uuid
from http.client import SWITCHING_PROTOCOLS
from PIL import ImageTk, Image
from curses.textpad import Textbox
from distutils.filelist import translate_pattern
import requests


# Check line 338-441: [1:-2] MUST BE REMOVED BEFORE 32.01 RELEASE!!!!!!!!!!!!!!!!!!!!!
class Get_Sys_Info:
    """Gathers system stats that are needed to run PiGro"""

    def get_user_name():
        # Say Hallo!
        global user
        user = os.environ["USER"]  # os.getlogin()
        print(f"[Info]: Hi,{user} waz uuuuup?!")

    get_user_name()

    def get_home_path():
        # Define Home
        global home
        home = os.environ["HOME"]  # str(Path.home())
        print(f"[Info]: {home} is your home directory!")

    get_home_path()

    def get_pigro_path():
        # Gets path to PiGro
        global Application_path
        Application_path = str(os.getcwd())
        print(f"[Info]: PiGro directory is {Application_path}")

    get_pigro_path()

    def chmod_x_scripts():
        # Makes all .sh files in /scripts executable if PiGro in $HOME
        if Application_path == f"{home}/PiGro-Aid-":
            popen(
                'find ~/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;'
            )
            print(f"[Info]: All files executable")

    chmod_x_scripts()

    def check_if_pigro_settings_exsists():
        # Checks if settings folder exists
        pigro_conf_folder = os.path.isdir(f"{home}/.pigro")
        if pigro_conf_folder == False:
            print("[Info]: Folder:.pigro not found will created")
            os.mkdir(f"{home}/.pigro")
            open(f"{home}/.pigro/autostart.list", "a").close()
            open(f"{home}/.pigro/pi-apps_list.list", "a").close()
            open(f"{home}/.pigro/pi-apps_installed.list", "a").close()
        if pigro_conf_folder == True:
            print("[Info]: Folder: .pigro exsists")

        # Checks if pigro.conf exists
        pigro_conf_file = os.path.exists(f"{home}/.pigro/pigro.conf")
        if pigro_conf_file == False:
            open(f"{home}/.pigro/pi-apps_list.list", "a")
            with open(f"{home}/.pigro/pigro.conf", "a") as p_file:
                p_file.write(
                    "[PiGro - Just Click It! Configs]\n\nfirst_run = true\ntheme = dark\ntransparency = 1.00\nperm = true"
                )
                p_file.close()
            print("[Info]: pigro.conf created")
        if pigro_conf_file == True:
            print("[Info]: pigro.conf exsists")

        # Autostarteble Apps
        popen(f"rm {home}/.pigro/auto_plus.list")
        desktop_files = [
            df
            for df in listdir("/usr/share/applications/")
            if isfile(join("/usr/share/applications/", df))
        ]
        desktop_files.sort()

        # print(desktop_files.sort())

        for fn in desktop_files:
            add_app = open(f"{home}/.pigro/auto_plus.list", "a")
            add_app.write(str(fn[:-8] + "\n"))
            add_app.close()

        sudo_perm = open(f"{home}/.pigro/pigro.conf", "r")
        read_sudo = sudo_perm.readlines()
        sudo_perm.close()
        found = False
        for line in read_sudo:
            if str("perm = ") in line:
                found = True

        if not found:
            sudo_perm = open(f"{home}/.pigro/pigro.conf", "a")
            sudo_perm.write(str("perm = true"))
            sudo_perm.close()

        legit_check = open(f"{home}/.pigro/pigro.conf", "r")
        read_check = legit_check.readlines()
        legit_check.close()
        for line in read_check:
            if str("perm = true") in line:
                global legit
                legit = "pkexec"
            else:
                legit = "sudo"

    check_if_pigro_settings_exsists()

    def check_if_pigro_is_in_bin():
        # Checks if pigro bin exists
        popen(f"{Application_path}/scripts/check_bin.sh ")

    check_if_pigro_is_in_bin()

    def get_distro_name():
        # Get Distro
        global distro_get
        distro_get = distro.id()
        print("[Info]: Your Distro is: " + str(distro_get))
        # Gets nice Distro name
        global nice_name
        nice_name = popen("egrep '^(PRETTY_NAME)=' /etc/os-release")
        nice_name = nice_name.read()

    get_distro_name()

    def get_position_of_config_txt():
        # Location of config.txt
        global config_path
        if os.path.exists("/boot/config.txt"):
            config_path = "/boot/config.txt"
        elif os.path.exists("/boot/firmware/usercfg.txt"):
            config_path = "/boot/firmware/usercfg.txt"
        elif os.path.exists("/boot/firmware/config.txt"):
            config_path = "/boot/firmware/config.txt"
        else:
            print("[Info]: Can't find config.txt")

    get_position_of_config_txt()

    def get_desktop_env():
        # Get Desktop Environment
        global get_de
        get_de = os.environ.get("XDG_CURRENT_DESKTOP")
        print("[Info]: Your DE is: " + str(get_de))

    get_desktop_env()

    def check_if_piapps_is_installed():
        # Checks if pi-apps is installed an imports the app list
        open(f"{home}/.pigro/pi-apps_installed.list", "w").close()
        open(f"{home}/.pigro/pi-apps_list.list", "w").close()
        global piapps_path
        piapps_path = os.path.isdir(f"{home}/pi-apps")  # Need full path
        if piapps_path == False:
            print("[Info]: Pi-Apps not found")
        if piapps_path == True:
            print("[Info]: Pi-Apps is installed list will be added")
            # popen(f"ls ~/pi-apps/apps/ > /home/{user}/.pigro/pi-apps_list.list")

            for installed_pi_apps in os.listdir(f"{home}/pi-apps/data/status"):
                pi_apps_status = open(
                    f"/home/{user}/pi-apps/data/status/{installed_pi_apps}", "r"
                )
                status = pi_apps_status.read()
                pi_apps_status.close()
                if status.strip() == "installed":
                    with open(f"{home}/.pigro/pi-apps_installed.list", "a") as pa_file:
                        pa_file.write(f"{installed_pi_apps}\n")
                        pa_file.close()

    check_if_piapps_is_installed()

    def get_arch():
        arch_bash = """#determine if host system is 64 bit arm64 or 32 bit armhf
    if [ "$(od -An -t x1 -j 4 -N 1 "$(readlink -f /sbin/init)")" = ' 02' ];then
    arch=64
    printf "arm64"
    elif [ "$(od -An -t x1 -j 4 -N 1 "$(readlink -f /sbin/init)")" = ' 01' ];then
    arch=32
    printf "armhf"
    else
    error "Failed to detect OS CPU architecture! Something is very wrong."
    fi"""

        global os_arch_output
        os_arch = popen(arch_bash)
        os_arch_output = os_arch.read()

    get_arch()

    def check_if_snapd_is_installed():
        # Checks if snapd exists
        global snap_deamon_check
        snap_deamon_check = os.path.isfile("/bin/snap")

        if snap_deamon_check == True:
            print("[Info]: Snap is installed")
        else:
            print("[Info]: Snap is not installed")

    check_if_snapd_is_installed()

    def check_if_flatpak_is_installed():
        # Checks if flatpak exists
        if os.path.isfile("/bin/flatpak"):
            print("[Info]: Flatpak is installed")
            global flat_counted
            flat_count = popen("flatpak list | wc --lines")
            flat_counted = flat_count.read()
            flat_count.close()
            global flatpak_path
            flatpak_path = True
            print(f"[Info]: {flat_counted[:-1]} Flatpaks are installed")
        else:
            print("[Info]: Flatpak is not installed")
            flatpak_path = False

    check_if_flatpak_is_installed()

    def check_if_conf_file_exsists():
        # Checks if pigro.conf exists
        if os.path.isfile(f"{home}/.pigro/pigro.conf"):
            print("[Info]: pigro.conf exists")
        else:
            print("[Info]: pigro.conf not found")
            with open(f"{home}/.pigro/pigro.conf", "a") as pigro_config_f:
                pigro_config_f.write(
                    "[PiGro - Just Click It! Configs]\n\nfirst_run = true\ntheme = dark"
                )
                print("[Info]: pigro.conf was created")

    check_if_conf_file_exsists()

    def get_installed_deb_num():
        # Counts installed .DEBs
        deb_count = popen("dpkg --list | wc --lines")
        global deb_counted
        deb_counted = deb_count.read()
        deb_count.close()
        print(f"[Info]: {deb_counted[:-1]} .deb Packages Installed")

    get_installed_deb_num()

    def set_theme():
        # Color Theme Identifier
        conf_file = open(f"{home}/.pigro/pigro.conf", "r")
        read_conf = conf_file.readlines()
        conf_file.close()

        for line in read_conf:
            # Dark Theme Settings
            if str("theme = dark") in line:
                print("[Info]: Dark Theme")
                global maincolor
                maincolor = "#404040"
                global nav_color
                nav_color = "#2b2b2b"
                global frame_color
                frame_color = "#383838"
                global main_font
                main_font = "white"
                global info_color
                info_color = "yellow"
                global ext_btn
                ext_btn = "#007acc"
                global label_frame_color
                label_frame_color = "#d4244d"
                if distro_get == "ubuntu":
                    maincolor = "#333333"
                    nav_color = "#272727"
                    frame_color = "#333333"
                    main_font = "white"
                    info_color = "yellow"
                    ext_btn = "#333333"

            # Light Theme Settings
            if str("theme = light") in line:
                print("[Info]: Light Theme")
                maincolor = "#f5f5f5"
                nav_color = "#e8e8e8"
                frame_color = "#f5f5f5"
                main_font = "black"
                info_color = "#0075b7"
                ext_btn = "#c5c5c5"
                label_frame_color = "#0075b7"
                if distro_get == "ubuntu":
                    maincolor = "#fafafa"
                    nav_color = "#ffffff"
                    frame_color = "#fafafa"
                    main_font = "black"
                    info_color = "#0075b7"
                    ext_btn = "#fafafa"

        # Font Definition Vars
        global font_20
        font_20 = ("Sans", 20)
        global font_16
        font_16 = ("Sans", 16)
        global font_14
        font_14 = ("Sans", 14)
        global font_12_b
        font_12_b = ("Sans", 12, "bold")
        global font_12
        font_12 = ("Sans", 12)
        global font_10
        font_10 = ("Sans", 10)
        global font_10_b
        font_10_b = ("Sans", 10, "bold")
        global font_9_b
        font_9_b = ("Sans", 9, "bold")
        global font_9
        font_9 = ("Sans", 9)
        global font_8_b
        font_8_b = ("Sans", 8, "bold")
        global font_8
        font_8 = ("Sans", 8)

    set_theme()

    def get_info_version():
        # MUST BE UPDATED WITH EVER NEW RELEASE!
        global current_version
        current_version = float(23.01)
        # Gets latest github release
        url = "https://github.com/actionschnitzel/PiGro-Aid-/releases/latest"
        r = requests.get(url)

        global github_release
        github_release = r.url.split("/")[-1][
            1:-2
        ]  # Check line 338-441: [1:-2] MUST BE REMOVED BEFORE 32.01 RELEASE!!!!!!!!!!!!!!!!!!!!!
        github_release = float(github_release)

    get_info_version()
