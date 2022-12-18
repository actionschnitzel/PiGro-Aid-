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
from scripts.get_info import *


class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        """defines the basic look of the app"""
        # Window Basics
        self.title("PiGro - Just Click It! (A più di novemila, accipicchia!)")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self["background"] = maincolor
        self.resizable(0, 0)
        app_width = 1200
        app_height = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.wait_visibility(self)
        # self.wm_attributes("-alpha", translate_p)

        # Notebook Definition
        self.notebook = ttk.Notebook(self)
        self.Dash_Tab = Dash_Tab(self.notebook)
        self.Update_Tab = Update_Tab(self.notebook)
        self.System_Tab = System_Tab(self.notebook)
        self.Software_Tab = Software_Tab(self.notebook)
        self.Deb_Recover_Tab = Deb_Recover(self.notebook)
        self.Look_Tab = Look_Tab(self.notebook)
        self.Tuning_Tab = Tuning_Tab(self.notebook)
        self.Links_Tab = Links_Tab(self.notebook)
        self.About_Tab = About_Tab(self.notebook)
        self.System_Ubuntu_Tab = System_Ubuntu_Tab(self.notebook)
        self.Autostarts_Tab = Autostarts_Tab(self.notebook)
        self.Tasks_Tab = Tasks_Tab(self.notebook)
        self.Git_More_Tab = Git_More_Tab(self.notebook)

        # Notebook Icons
        self.status_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/com.github.hannesschulze.optimizer.png"
        )
        self.system_icon = PhotoImage(file=r"images/icons/papirus/48x48/kcontrol.png")
        self.update_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/aptdaemon-upgrade.png"
        )
        self.install_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/softwarecenter.png"
        )
        self.look_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/com.github.cassidyjames.palette.png"
        )
        self.tuning_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/blackmagicraw-speedtest.png"
        )
        self.links_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-webapps.png"
        )
        self.support_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/4137_winhlp32.0.png"
        )
        self.cam_icon = PhotoImage(file=r"images/icons/papirus/48x48/gtkam-camera.png")
        self.ubuntu_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-ubuntu.png"
        )
        self.auto_start = PhotoImage(
            file=r"images/icons/papirus/48x48/cs-startup-programs.png"
        )
        self.kill_proc = PhotoImage(
            file=r"images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.git_more = PhotoImage(file=r"images/icons/papirus/48x48/git-dag.png")

        self.deb_pack = PhotoImage(file=r"images/icons/papirus/48x48/debian-logo.png")

        # Puts tabs in nav bar
        self.notebook.add(
            self.Dash_Tab, compound=LEFT, text="Dashboard", image=self.status_icon
        )

        self.notebook.add(
            self.System_Tab, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.System_Ubuntu_Tab, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.Update_Tab, compound=LEFT, text="Update", image=self.update_icon
        )

        self.notebook.add(
            self.Look_Tab, compound=LEFT, text="Look & Feel", image=self.look_icon
        )

        self.notebook.add(
            self.Autostarts_Tab, compound=LEFT, text="Autostart", image=self.auto_start
        )

        self.notebook.add(
            self.Tasks_Tab, compound=LEFT, text="Tasks", image=self.kill_proc
        )

        self.notebook.add(
            self.Software_Tab, compound=LEFT, text="Software", image=self.install_icon
        )

        self.notebook.add(
            self.Deb_Recover_Tab, compound=LEFT, text="Backup", image=self.deb_pack
        )
        self.notebook.add(
            self.Git_More_Tab, compound=LEFT, text="Git & More", image=self.git_more
        )

        self.notebook.add(
            self.Tuning_Tab, compound=LEFT, text="Tuning", image=self.tuning_icon
        )
        self.notebook.add(
            self.Links_Tab, compound=LEFT, text="Links", image=self.links_icon
        )

        self.notebook.add(
            self.About_Tab, compound=LEFT, text="About", image=self.support_icon
        )

        self.notebook.pack(fill="both", expand=True, anchor=W)

        # Hides Ubuntu settings when distro is debian
        if distro_get == "debian" or distro_get == "raspbian":
            self.notebook.hide(self.System_Ubuntu_Tab)

        # Hides RPi OS settings when distro is Ubuntu
        if distro_get == "ubuntu":
            self.notebook.hide(self.System_Tab)
            self.notebook.hide(self.Update_Tab)
            self.notebook.hide(self.Tasks_Tab)

        # Notebook Theming
        global noteStyler
        noteStyler = ttk.Style(self)
        # noteStyler.theme_use('alt')
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
            font=font_14,
            width=10,
            highlightthickness=0,
        )
        noteStyler.configure("TFrame", background=maincolor)
        noteStyler.map(
            "TNotebook.Tab",
            background=[("selected", nav_color)],
            foreground=[("selected", label_frame_color)],
        )

        TROUGH_COLOR = nav_color
        BAR_COLOR = "#007acc"

        noteStyler.configure(
            "bar.Horizontal.TProgressbar",
            troughcolor=TROUGH_COLOR,
            bordercolor=TROUGH_COLOR,
            background=BAR_COLOR,
            lightcolor=BAR_COLOR,
            darkcolor=BAR_COLOR,
        )

        # Seperator Theme
        noteStyler.configure("Line.TSeparator", background="grey", rekief="sunken")
        # Compbox Theme

        noteStyler.configure(
            "TCombobox",
            background=ext_btn,
            fieldbackground="white",
            arrowcolor="black",
            arrowsize=15,
            bordercolor=nav_color,
        )
        noteStyler.map(
            "TCombobox",
            foreground=[("hover", "black")],
            background=[("hover", "white")],
        )


class Dash_Tab(ttk.Frame):
    """shows system stats"""

    def __init__(
        self,
        container,
    ):
        super().__init__()

        # Checks if Update Window pops up

        def update_checker():
            up_chk = Update_Pop(self)
            up_chk.grab_set()

        try:
            if github_release > current_version:
                print("[Info]: An Update is avalible !!!")
                update_checker()
            elif github_release < current_version:
                print("WTF HAPPEND HERE?!! You must be Actionschnitzel !!!")
            elif github_release == current_version:
                print("[Info]: PiGro is Up To Date !!!")
        except:
            print("[Info]: Version Check not Possible")
        # Ram Size
        def get_size(bytes, suffix="B"):
            """
            Scale bytes to its proper format
            e.g:
                1253656 => '1.20MB'
                1253656678 => '1.17GB'
            """
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        # IP Address
        def extract_ip():
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:
                st.connect(("10.255.255.255", 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = "127.0.0.1"
            finally:
                st.close()
            return IP

        # Sensetiv Data Button Images
        global on_btn_icon
        on_btn_icon = PhotoImage(file=r"images/icons/pigro_icons/on_s_b.png")

        global off_btn_icon
        off_btn_icon = PhotoImage(file=r"images/icons/pigro_icons/off_s_b.png")

        # Hide/Show sensetiv data definition
        def Simpletoggle():
            if self.toggle_button.config("text")[-1] == "ON":
                self.toggle_button.config(text="OFF")
                self.toggle_button.config(image=off_btn_icon)
                self.ip_label.config(text=f"IP Address: {IPAddr}")
                self.mac_add_label.config(text=f"MAC Address: {get_mac}")
                sys_label_d.config(text=f"Device Name: {my_system.node}")
                sys_label_u.config(text=f"User Name: {user}")
            else:
                self.toggle_button.config(text="ON")
                self.toggle_button.config(image=on_btn_icon)
                self.ip_label.config(text=f"IP Address: XXXXXXXXXXXXX")
                self.mac_add_label.config(text=f"MAC Address: XXXXXXXXXXXXX")
                sys_label_d.config(text=f"Device Name: XXXXXXXXXXXXX")
                sys_label_u.config(text="User Name: XXXXXXXXXXXXX")

        # MAC Address
        get_mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))

        # HDD usage
        obj_Disk = psutil.disk_usage("/")

        # Parameters for System
        global distro
        distro = distro.id()
        my_system = platform.uname()
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        IPAddr = extract_ip()
        Pi_Model = open("/proc/device-tree/model", "r")
        total, used, free = shutil.disk_usage("/")
        current_month = strftime("%B")

        # Main frame for system stats

        self.sys_logo = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.sys_logo.place(x=65, y=20, width=885)  #
        self.sys_logo["background"] = maincolor

        self.pigro_img = ImageTk.PhotoImage(
            Image.open("images/icons/pigro_icons/pigrologo.png")
        )

        self.pigroh_img = ImageTk.PhotoImage(
            Image.open("images/icons/pigro_icons/pigrologoh.png")
        )

        self.pigrox_img = ImageTk.PhotoImage(
            Image.open("images/icons/pigro_icons/pigrologox.png")
        )

        def pigro_sound():
            popen(f"mpg123 {home}/PiGro-Aid-/scripts/PiGro-just_click_it.mp3")

        # Sys Info Labels
        self.sysinf_btn = Button(
            self.sys_logo,
            borderwidth=0,
            bg=frame_color,
            highlightthickness=0,
            command=pigro_sound,
        )
        self.sysinf_btn.pack(pady=20)

        # Changes Header
        if current_month == "October":
            self.sysinf_btn.config(image=self.pigroh_img)
        elif current_month == "December":
            self.sysinf_btn.config(image=self.pigrox_img)
        else:
            self.sysinf_btn.config(image=self.pigro_img)

        self.info_main_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=20,
            padx=10,
        )

        self.info_main_frame.place(x=65, y=240)  # pack(pady=20)
        self.info_main_frame["background"] = frame_color

        # Main Frame
        self.sys_info_main_frame = Frame(
            self.info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )
        # Column 0
        self.sys_info_main_frame.pack(side=LEFT)
        self.sys_info_main_frame["background"] = frame_color

        self.sys_info_main_Update_Tab = Frame(
            self.info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=0,
            padx=0,
        )
        # Column 1
        self.sys_info_main_Update_Tab.pack(side=LEFT, anchor="n")
        self.sys_info_main_Update_Tab["background"] = frame_color

        # Column 2
        self.sys_info_main_System_Tab = Frame(
            self.info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=0,
            padx=0,
        )

        self.sys_info_main_System_Tab.pack(side=LEFT, anchor="n")
        self.sys_info_main_System_Tab["background"] = frame_color

        # System Frame
        self.sys_frame_1 = LabelFrame(
            self.sys_info_main_frame,
            text="System Info",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_1.pack(anchor="n", pady=5)
        self.sys_frame_1["background"] = frame_color

        sys_label_list = [
            "Platform:",
            "Distro:",
            "Desktop:",
            "Shell:",
            "Session:",
            "Language:",
            "Kernel:",
            "Architecture:",
            "Board:",
        ]

        sys_label_list1 = []

        for sys_label in sys_label_list:

            sys_label_x = Label(
                self.sys_frame_1,
                text=" ",
                font=font_12,
                justify="left",
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                width=35,
                anchor=W,
            )

            sys_label_x.pack()
            sys_label_list1.append(sys_label_x)

            if sys_label == "Platform:":
                sys_label_x.config(text=f"Platform: {my_system.system}")
            if sys_label == "Distro:":
                sys_label_x.config(text=f"Distro: {nice_name[13:-2]}")
            if sys_label == "Desktop:":
                sys_label_x.config(text=f"Desktop: {get_de}")
            if sys_label == "Shell:":
                sys_label_x.config(text=f"Shell: {os.environ['SHELL'][5:]}")
            if sys_label == "Session:":
                sys_label_x.config(text=f"Session: {os.environ['XDG_SESSION_TYPE']}")
            if sys_label == "Language:":
                sys_label_x.config(text=f"Language: {os.environ['LANG']}")
            if sys_label == "Kernel:":
                sys_label_x.config(text=f"Kernel: {my_system.release}")
            if sys_label == "Architecture:":
                sys_label_x.config(text=f"Architecture: {os_arch_output}")
            if sys_label == "Board:":
                sys_label_x.config(text=f"Board: {Pi_Model.read()}")

        sys_label_u = Label(
            self.sys_frame_1,
            text=f"User Name: {user}",
            font=font_12,
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
            width=35,
            anchor=W,
        )

        sys_label_u.pack()

        sys_label_d = Label(
            self.sys_frame_1,
            text=f"Device Name: {my_system.node}",
            font=font_12,
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
            width=35,
            anchor=W,
        )

        sys_label_d.pack()

        # CPU Frame
        self.sys_frame_2 = LabelFrame(
            self.sys_info_main_frame,
            text="CPU",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_2.pack(pady=5)
        self.sys_frame_2["background"] = frame_color

        self.curr_cpu_perc_label = Label(
            self.sys_frame_2,
            text="",
            background=frame_color,
            foreground=main_font,
            width=35,
            font=font_12,
            anchor=W,
        )
        self.curr_cpu_perc_label.pack()

        self.max_cpu_frq_label = Label(
            self.sys_frame_2,
            text=f"Max Freq: {cpufreq.max:.0f} Mhz",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=35,
            font=font_12,
            anchor=W,
        ).pack()

        self.curr_cpu_frq_label = Label(
            self.sys_frame_2,
            text="",
            background=frame_color,
            foreground=main_font,
            width=35,
            font=font_12,
            anchor=W,
        )
        self.curr_cpu_frq_label.pack()

        self.min_cpu_frq_label = Label(
            self.sys_frame_2,
            text=f"Min Freq: {cpufreq.min:.0f} Mhz",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=35,
            font=font_12,
            anchor=W,
        ).pack()

        self.cpu_temp_label = Label(
            self.sys_frame_2,
            text="",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=35,
            font=font_12,
            anchor=W,
        )
        self.cpu_temp_label.pack()

        # Mamory Frame
        self.sys_frame_3 = LabelFrame(
            self.sys_info_main_Update_Tab,
            text="Memory",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_3.pack(side=TOP, pady=5)
        self.sys_frame_3["background"] = frame_color

        self.ut_ram_label = Label(
            self.sys_frame_3,
            text="",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        )
        self.ut_ram_label.pack()

        self.total_ram_label = Label(
            self.sys_frame_3,
            text=f"RAM Total: {get_size(svmem.total)}",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        self.total_swap_label = Label(
            self.sys_frame_3,
            text=f"SWAP Total: {get_size(swap.total)}",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        # Network Frame
        self.sys_frame_4 = LabelFrame(
            self.sys_info_main_Update_Tab,
            text="Network",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_4.pack(pady=5)
        self.sys_frame_4["background"] = frame_color

        self.ip_label = Label(
            self.sys_frame_4,
            text=f"IP Address: {IPAddr}",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        )
        self.ip_label.pack()

        self.mac_add_label = Label(
            self.sys_frame_4,
            text=f"MAC Address: {get_mac}",
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        )
        self.mac_add_label.pack()

        # Disk
        self.sys_frame_5 = LabelFrame(
            self.sys_info_main_Update_Tab,
            text="Disk",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_5.pack(pady=5)
        self.sys_frame_5["background"] = frame_color

        self.sysinf_hdd_t = Label(
            self.sys_frame_5,
            text=("Total Disk Space: %d GiB" % (total // (2**30))),
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        self.hdd_used_label = Label(
            self.sys_frame_5,
            text=("Used Disk Space: %d GiB" % (used // (2**30))),
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        self.hdd_free_label = Label(
            self.sys_frame_5,
            text=("Free Disk Space: %d GiB" % (free // (2**30))),
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        self.hdd_used_per_label = Label(
            self.sys_frame_5,
            text=(f"Used Disk Space: {obj_Disk.percent} %"),
            justify="left",
            background=frame_color,
            foreground=main_font,
            width=30,
            font=font_12,
            anchor=W,
        ).pack()

        def disc_step():
            self.pb1["value"] = obj_Disk.percent

        self.pb1 = ttk.Progressbar(
            self.sys_frame_5,
            style="bar.Horizontal.TProgressbar",
            orient=HORIZONTAL,
            length=200,
            mode="determinate",
        )
        self.pb1.pack(expand=True, anchor="w")
        disc_step()

        # Custom Settings
        self.ov_display_frame = LabelFrame(
            self.sys_info_main_System_Tab,
            text="Custom Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.ov_display_frame.pack(pady=5)
        self.ov_display_frame["background"] = frame_color

        global dash_arm_f_display
        dash_arm_f_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="Arm Freq: N/A",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=20,
        )
        dash_arm_f_display.grid(column=1, row=2)

        global dash_gpu_f_display
        dash_gpu_f_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="Gpu Freq: N/A",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=20,
        )
        dash_gpu_f_display.grid(column=1, row=3)

        global dash_gpu_m_display
        dash_gpu_m_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="Gpu Mem: N/A",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=20,
        )
        dash_gpu_m_display.grid(column=1, row=4)

        global dash_over_v_display
        dash_over_v_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="Over Voltage: N/A",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=20,
        )
        dash_over_v_display.grid(column=1, row=5)

        global dash_force_t_display
        dash_force_t_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="Force Turbo: N/A",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=20,
        )
        dash_force_t_display.grid(column=1, row=6)

        self.sys_frame_6 = LabelFrame(
            self.sys_info_main_Update_Tab,
            text="Installed Packages",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.sys_frame_6.pack(pady=5)
        self.sys_frame_6["background"] = frame_color

        self.sys_soft = Label(
            self.sys_frame_6,
            text=f"Debian: {deb_counted[:-1]}",
            font=font_12,
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
            width=30,
            anchor=W,
        ).pack()

        self.sys_flat = Label(
            self.sys_frame_6,
            text=f"Flatpak: 0",
            font=font_12,
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
            width=30,
            anchor=W,
        )
        self.sys_flat.pack()

        # Flatpak counter
        if os.path.isfile("/bin/flatpak"):
            self.sys_flat.config(text=f"Flatpaks: {flat_counted[:-1]}")

        # Needs to be removed
        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def refresh_OV_stats():
            """Refreshes thuning settings every secon"""
            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "arm_freq" in line:
                    dash_arm_f_display.config(
                        text=f"Arm Freq: {line[9:-1]} MHz",
                        foreground=main_font,
                        font=font_12,
                    )

                if "#arm_freq=800" in line:
                    dash_arm_f_display.config(
                        text="Arm Freq: N/A",
                        foreground=main_font,
                        font=font_12,
                    )

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "gpu_freq" in line:
                    dash_gpu_f_display.config(
                        text=f"Gpu Freq: {line[9:-1]} MHz",
                        foreground=main_font,
                        font=font_12,
                    )

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "force_turbo" in line:
                    dash_force_t_display.config(
                        text=f"Force Turbo: {line[12:-1]}",
                        foreground=main_font,
                        font=font_12,
                    )

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "over_voltage" in line:
                    dash_over_v_display.config(
                        text=f"Over Voltage: {line[13:-1]}",
                        foreground=main_font,
                        font=font_12,
                    )

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "gpu_mem" in line:
                    dash_gpu_m_display.config(
                        text=f"Gpu Mem: {line[8:-1]} MB",
                        foreground=main_font,
                        font=font_12,
                    )

            self.after(1000, refresh_OV_stats)

        refresh_OV_stats()

        def refresh_sys_stats():
            """Refresches the system stats every second"""
            # Parameters for System
            cpufreq = psutil.cpu_freq()
            cpu_temp = psutil.sensors_temperatures()
            cpu_temp = round(cpu_temp["cpu_thermal"][0][1])
            cpu_perc = psutil.cpu_percent()
            total_ram_load = psutil.virtual_memory().percent

            self.curr_cpu_perc_label.configure(text=f"Utilization: {cpu_perc} %")
            self.curr_cpu_frq_label.configure(
                text=f"Current Freq: {cpufreq.current:.0f} Mhz"
            )
            self.cpu_temp_label.configure(text=f"Temp: {str(cpu_temp)}°C")
            self.ut_ram_label.configure(text=f"Utilization: {total_ram_load} %")

            self.after(1000, refresh_sys_stats)

        # Custom Settings
        self.usage_frame = LabelFrame(
            self.sys_info_main_System_Tab,
            text="Usage",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.usage_frame.pack(pady=5)
        self.usage_frame["background"] = frame_color

        self.info_main_Update_Tab = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=20,
            padx=10,
        )

        self.info_main_Update_Tab.place(x=65, y=750, width=885)
        self.info_main_Update_Tab["background"] = frame_color

        # Hide/Show Butten & Label
        self.sensitiv = Label(
            self.info_main_Update_Tab,
            text=f"Hide Sensitiv Data:",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            anchor=W,
        ).pack(side=LEFT)

        self.toggle_button = Button(
            self.info_main_Update_Tab,
            text="OFF",
            image=off_btn_icon,
            font=(font_10),
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            command=Simpletoggle,
        )
        self.toggle_button.pack(anchor="w")

        refresh_sys_stats()


class Update_Tab(ttk.Frame):
    """Frame for Update & Upgrade functions + xterm frame"""

    def __init__(self, container):
        super().__init__()

        self.folder_icon = PhotoImage(file=r"images/icons/pigro_icons/folder_s.png")
        self.up_icon = PhotoImage(file=r"images/icons/pigro_icons/pack_up_s.png")
        self.gup_icon = PhotoImage(file=r"images/icons/pigro_icons/pack_upg_s.png")
        self.recover_icon = PhotoImage(file=r"images/icons/pigro_icons/recover_s.png")
        self.fup_icon = PhotoImage(file=r"images/icons/pigro_icons/pack_fupg_s.png")
        self.allow_icon = PhotoImage(file=r"images/icons/pigro_icons/allow_s.png")
        self.arm_icon = PhotoImage(file=r"images/icons/pigro_icons/del_s.png")
        self.confa_icon = PhotoImage(file=r"images/icons/pigro_icons/confa_s.png")
        self.re_icon = PhotoImage(file=r"images/icons/pigro_icons/re_s.png")
        self.inst_icon = PhotoImage(file=r"images/icons/pigro_icons/debinst_s.png")
        self.term_icon = PhotoImage(file=r"images/icons/pigro_icons/terminal_s.png")

        self.background = maincolor

        self.rep_main_frame = Frame(
            self, borderwidth=0, highlightthickness=0, relief=GROOVE
        )
        self.rep_main_frame.pack(pady=20, padx=5)
        self.rep_main_frame["background"] = frame_color

        self.off_rep_frame = LabelFrame(
            self.rep_main_frame,
            text="Official Repository",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=20,
        )

        self.off_rep_frame.grid(row=0, column=0)
        self.off_rep_frame["background"] = frame_color

        self.man_rep_frame = LabelFrame(
            self.rep_main_frame,
            text="Integrated Source",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=10,
            padx=10,
        )

        self.man_rep_frame.grid(row=0, column=1, rowspan=10)
        self.man_rep_frame["background"] = frame_color

        self.man_left = Frame(
            self.man_rep_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=10,
            padx=10,
        )
        self.man_left.pack(side=LEFT)
        self.man_left["background"] = frame_color

        self.man_right = Frame(
            self.man_rep_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=10,
            padx=10,
        )
        self.man_right.pack(side=LEFT)
        self.man_right["background"] = frame_color

        def open_ppa(text):
            os.popen("sudo mousepad /etc/apt/sources.list.d/" + text)

        sources_d = os.listdir("/etc/apt/sources.list.d")
        sources_d1 = []

        for file in sources_d:
            self.sources_d_label = Button(
                self.man_right,
                text=file,
                justify=LEFT,
                anchor=W,
                bg=ext_btn,
                fg=main_font,
                borderwidth=0,
                highlightthickness=0,
                command=lambda text=file: open_ppa(text),
                width=25,
            )
            self.sources_d_label.pack(anchor=W, pady=5)
            sources_d1.append(self.sources_d_label)

        self.tu_info = Label(
            self.off_rep_frame,
            text="Info: Never edit the source lists unless you know exactly what you are doing.\n",
            font=font_8_b,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=info_color,
        ).pack()

        a_file1 = open("/etc/apt/sources.list")

        lines = a_file1.readlines()
        for line in lines:
            self.repo = Label(
                self.off_rep_frame,
                width=70,
                justify=LEFT,
                anchor="w",
                text=line[0:-1],
                fg=main_font,
                bg=frame_color,
            )

            self.repo.pack(anchor=W)

        def up_action(text):
            """Passes commands du auto generated buttons"""
            if text == "Update":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/update.sh && exit ; exec bash"'
                    % wid
                )
            if text == "Update & Upgrade":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/upgrade.sh && exit; exec bash"'
                    % wid
                )
            if text == "Full Upgrade":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/full_upgrade.sh && exit; exec bash"'
                    % wid
                )
            if text == "Allow Sources":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/addunsignedrepo.sh && exit; exec bash"'
                    % wid
                )
            if text == "Autoremove":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/auto_remove.sh && exit ; exec bash"'
                    % wid
                )
            if text == "dpkg -i (File Picker)":
                self.filename = filedialog.askopenfilename(
                    initialdir="~",
                    title="Select A File",
                    filetypes=((".deb files", "*.deb"),),
                )
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "sudo dpkg -i {self.filename} && exit ; exec bash"'
                    % wid
                )

            if text == "Open Sources.list.d":
                if get_de == "XFCE":
                    popen("sudo thunar /etc/apt/sources.list.d/")
                else:
                    popen("sudo pcmanfm /etc/apt/sources.list.d/")

            if text == "dpkg --configure -a":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/config_a.sh && exit; exec bash"'
                    % wid
                )
            if text == "Reboot":
                popen(f"{legit} reboot")
            if text == "Gimme a Terminal":
                popen("x-terminal-emulator")

        self.update_btn_frame = LabelFrame(
            self,
            text="Update Options",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            relief=GROOVE,
            highlightthickness=0,
            padx=20,
            pady=20,
        )
        self.update_btn_frame.pack(padx=28, pady=10, anchor="n", expand=True, fill="x")
        self.update_btn_frame["background"] = frame_color

        self.btn_frame = Frame(
            self.update_btn_frame,
            borderwidth=0,
            relief=GROOVE,
            highlightthickness=0,
            background=frame_color,
        )
        self.btn_frame.pack(anchor="w")

        self.termf = Frame(
            self.update_btn_frame,
            height=300,
            width=960,
            padx=20,
            highlightthickness=0,
            borderwidth=0,
        )
        global wid
        wid = self.termf.winfo_id()
        self.termf["background"] = frame_color

        # Button list
        up_button_list = [
            "Update",
            "Update & Upgrade",
            "Full Upgrade",
            "Allow Sources",
            "Autoremove",
            "Open Sources.list.d",
            "dpkg --configure -a",
            "dpkg -i (File Picker)",
            "Gimme a Terminal",
            "Reboot",
        ]

        up_button_list1 = []
        conf_row = 0
        conf_column = 0
        for up_button in up_button_list:
            # Generates buttons from list with grid
            self.up_button_x = Button(
                self.btn_frame,
                justify="left",
                compound="left",
                width=200,
                anchor="w",
                text=up_button,
                command=lambda text=up_button: up_action(text),
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=main_font,
            )
            self.up_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            up_button_list1.append(self.up_button_x)
            conf_column = conf_column + 1
            if conf_column == 4:
                conf_row = conf_row + 1
                conf_column = 0
            if up_button == "Update":
                self.up_button_x.config(image=self.up_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x, "sudo apt-get update -y |lolcat"
                )
            if up_button == "Update & Upgrade":
                self.up_button_x.config(image=self.gup_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x,
                    "sudo apt-get update -y |lolcat && sudo apt-get upgrade -y|lolcat",
                )

            if up_button == "Full Upgrade":
                self.up_button_x.config(image=self.fup_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x,
                    "sudo apt update -y && sudo apt full-upgrade -y && sudo apt dist-upgrade -y |lolcat",
                )

            if up_button == "Allow Sources":
                self.up_button_x.config(image=self.allow_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x,
                    """sudo apt update 2>&1 1>/dev/null | sed -ne 's/.*NO_PUBKEY //p' | while read key; do if ! [[ ${keys[*]} =~ "$key" ]]; then sudo apt-key adv --keyserver hkp://pool.sks-keyservers.net:80 --recv-keys "$key"; keys+=("$key"); fi; done""",
                )
            if up_button == "Autoremove":
                self.up_button_x.config(image=self.arm_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x, "sudo apt autoremove|lolcat"
                )
            if up_button == "dpkg -i (File Picker)":
                self.up_button_x.config(image=self.inst_icon)
                up_button_x_ttp = CreateToolTip(self.up_button_x, "Install a .DEB file")
            if up_button == "dpkg --configure -a":
                self.up_button_x.config(image=self.confa_icon)
                up_button_x_ttp = CreateToolTip(
                    self.up_button_x,
                    "--configure package...|-a|--pending\nReconfigure an unpacked package. If -a  or  --pending  is  given\ninstead  of  package, all unpacked but unconfigured packages are\nconfigured.",
                )
            if up_button == "Open Sources.list.d":
                self.up_button_x.config(image=self.folder_icon)
            if up_button == "Reboot":
                self.up_button_x.config(image=self.re_icon)
            if up_button == "Gimme a Terminal":
                self.up_button_x.config(image=self.term_icon)

        self.termf.pack(anchor="w")


class System_Tab(ttk.Frame):
    """standard system tab for all rpi os distros"""

    def __init__(self, container):
        super().__init__()

        """System Tab Icons"""
        self.raspi_config_cli_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.raspi_config_gui_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.rename_user_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.edit_config_txt_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/mousepad.png"
        )
        self.gparted_icon = PhotoImage(file=r"images/icons/papirus/48x48/gparted.png")
        self.mouse_keyboard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gnome-settings-keybinding.png"
        )
        self.deskpipro_icon = PhotoImage(file=r"images/icons/pigro_icons/deskpi.png")
        self.network_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/blueman-server.png"
        )
        self.sd_card_copier_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/media-flash-sd-mmc.png"
        )
        self.printer_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/boomaga.png"
        )
        self.desktop_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/com.github.bluesabre.darkbar.png"
        )
        self.screen_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/grandr.png"
        )
        self.neofetch_icon = PhotoImage(file=r"images/icons/pigro_icons/neofetch.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )
        self.kernel_2_latest_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-madlinux.png"
        )
        self.boot_log_icon = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.xfce_autostarts_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.xfce_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.taskmanager_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.bash_history_icon = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.cron_job_icon = PhotoImage(file=r"images/icons/papirus/48x48/mousepad.png")
        self.alacard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/classicmenu-indicator-light.png"
        )
        self.source_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )

        # Raspberry Pi Settings

        def pi_settings(text):
            """commands for auto generated buttons"""
            if text == "Raspi-Config GUI":
                popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")
            if text == "Raspi-Config CLI":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"sudo raspi-config; exec bash\"'"
                )
            if text == "Rename User":
                global pop_u_name
                pop_u_name = Toplevel(self)
                pop_u_name.config(bg=maincolor)
                app_width = 500
                app_height = 150
                screen_width = pop_u_name.winfo_screenwidth()
                screen_height = pop_u_name.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2) - (app_height / 2)
                pop_u_name.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
                pop_u_name.resizable(0, 0)

                def pop_u_name_dest():
                    pop_u_name.destroy()

                def do_it():
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"{legit} rename-user; exec bash\"'"
                    )
                    print("[Info]: Name will be changed")
                    pop_u_name.destroy()

                frame_pop_u_name = Frame(pop_u_name, borderwidth=0, relief=GROOVE)
                frame_pop_u_name.pack()
                frame_pop_u_name["background"] = maincolor

                frame_pop_u_name_1 = Frame(pop_u_name, borderwidth=0, relief=GROOVE)
                frame_pop_u_name_1.pack()
                frame_pop_u_name_1["background"] = maincolor

                pop_lbl_2000 = Label(
                    frame_pop_u_name,
                    anchor="w",
                    text="Do you really want to change the user name?\nrename-user will run on reboot.",
                    font=font_12,
                    highlightthickness=0,
                    borderwidth=2,
                    background=maincolor,
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_lbl_2000.pack(pady=20)

                pop_btn_2000 = Button(
                    frame_pop_u_name_1,
                    text="No",
                    anchor="w",
                    command=pop_u_name_dest,
                    highlightthickness=0,
                    borderwidth=0,
                    background=ext_btn,
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_btn_2000.pack(padx=5, pady=20, side=LEFT)
                pop_btn_shut = Button(
                    frame_pop_u_name_1,
                    text="Do It!",
                    anchor="w",
                    command=do_it,
                    highlightthickness=0,
                    borderwidth=0,
                    background="#f03838",
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_btn_shut.pack(padx=5, pady=20)

            if text == "Edit Config.txt":
                popen(f"{legit} mousepad {config_path}")

        self.pi_set = LabelFrame(
            self,
            text="Raspberry Pi Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
        )
        self.pi_set.pack(pady=20, padx=40, fill="both")  #
        self.pi_set["background"] = frame_color

        pi_settings_btn_list = [
            "Raspi-Config CLI",
            "Raspi-Config GUI",
            "Rename User",
            "Edit Config.txt",
        ]

        pi_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for pi_settings_btn in pi_settings_btn_list:
            self.pi_button_x = Button(
                self.pi_set,
                width=140,
                height=100,
                text=pi_settings_btn,
                command=lambda text=pi_settings_btn: pi_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.pi_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            pi_settings_btn_list1.append(self.pi_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if pi_settings_btn == "Raspi-Config CLI":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
            if pi_settings_btn == "Raspi-Config GUI":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
            if pi_settings_btn == "Rename User":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
            if pi_settings_btn == "Edit Config.txt":
                self.pi_button_x.config(image=self.edit_config_txt_icon)

        # Raspberry Pi Settings
        def device_settings(text):
            if text == "Gparted":
                popen(f"{legit} gparted")
            if text == "Mouse & Keyboard":
                popen("lxinput")
            if text == "DeskpiPro Control":
                popen("x-terminal-emulator -e 'bash -c \"deskpi-config; exec bash\"'")
            if text == "SD Card Copier":
                popen(
                    "env SUDO_ASKPASS=/usr/lib/piclone/pwdpic.sh sudo -AE dbus-launch piclone"
                )
            if text == "Printer Settings":
                popen("system-config-printer")
            if text == "Desktop Settings":
                popen("pcmanfm --desktop-pref")
            if text == "Screen Settings":
                popen("lxrandr")
            if text == "NeoFetch":
                popen("x-terminal-emulator -e 'bash -c \"neofetch; exec bash\"'")

        self.device_set = LabelFrame(
            self,
            text="Device Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=0,
            padx=10,
            width=300,
        )
        self.device_set.pack(pady=20, padx=40, fill="both")  #
        self.device_set["background"] = frame_color

        device_settings_btn_list = [
            "Gparted",
            "Mouse & Keyboard",
            "DeskpiPro Control",
            "SD Card Copier",
            "Printer Settings",
            "Desktop Settings",
            "Screen Settings",
            "NeoFetch",
        ]

        device_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for device_settings_btn in device_settings_btn_list:
            self.device_button_x = Button(
                self.device_set,
                width=140,
                height=100,
                text=device_settings_btn,
                command=lambda text=device_settings_btn: device_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.device_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            device_settings_btn_list1.append(self.device_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if device_settings_btn == "Gparted":
                self.device_button_x.config(image=self.gparted_icon)
                if os.path.isfile("/usr/sbin/gparted"):
                    print("[Info]: Gparted is installed")
                    self.device_button_x.configure(state=NORMAL)
                else:
                    print("[Info]: Gparted is not installed")
                    self.device_button_x.configure(state=DISABLED)

            if device_settings_btn == "Mouse & Keyboard":
                self.device_button_x.config(image=self.mouse_keyboard_icon)
            if device_settings_btn == "DeskpiPro Control":
                self.device_button_x.config(image=self.deskpipro_icon)
            if device_settings_btn == "SD Card Copier":
                self.device_button_x.config(image=self.sd_card_copier_icon)
            if device_settings_btn == "Printer Settings":
                self.device_button_x.config(image=self.printer_settings_icon)
            if device_settings_btn == "Desktop Settings":
                self.device_button_x.config(image=self.desktop_settings_icon)
            if device_settings_btn == "Screen Settings":
                self.device_button_x.config(image=self.screen_settings_icon)
            if device_settings_btn == "NeoFetch":
                self.device_button_x.config(image=self.neofetch_icon)
                if os.path.isfile("/bin/neofetch"):
                    print("[Info]: Neofetch is installed")
                    self.device_button_x.configure(state=NORMAL)
                else:
                    print("[Info]: Neofetch is not installed")
                    self.device_button_x.configure(state=DISABLED)

        def ops_settings(text):
            if text == "FM God Mode":
                if get_de == "XFCE":
                    popen("sudo thunar /")
                else:
                    popen("sudo pcmanfm /")

                print("[Info]: With great power comes great responsibility")
                Notification(
                    title="Sudo File Manager\n",
                    description="With great power comes great responsibility\n\n                          - Oncle Ben",
                    icon_path=f"{Application_path}/images/icons/Logotab.png",
                    duration=5,
                    urgency="normal",
                ).send()

            if text == "Upgrade Linux Kernel":
                global pop_kernel
                pop_kernel = Toplevel(self)
                pop_kernel.config(bg=maincolor)
                app_width = 500
                app_height = 150
                screen_width = pop_kernel.winfo_screenwidth()
                screen_height = pop_kernel.winfo_screenheight()
                x = (screen_width / 2) - (app_width / 2)
                y = (screen_height / 2) - (app_height / 2)
                pop_kernel.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
                pop_kernel.resizable(0, 0)

                def pop_kernel_dest():
                    pop_kernel.destroy()

                def do_it():
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"{legit} BRANCH=next rpi-update; exec bash\"'"
                    )
                    print("[Info]: Kernel Upgrade GO!")
                    pop_kernel.destroy()

                frame_pop_kernel = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
                frame_pop_kernel.pack()
                frame_pop_kernel["background"] = maincolor

                frame_pop_kernel_1 = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
                frame_pop_kernel_1.pack()
                frame_pop_kernel_1["background"] = maincolor

                pop_lbl_2000 = Label(
                    frame_pop_kernel,
                    anchor="w",
                    text="Do you really want to Upgrade the Kernel?",
                    font=font_12,
                    highlightthickness=0,
                    borderwidth=2,
                    background=maincolor,
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_lbl_2000.pack(pady=20)

                pop_btn_2000 = Button(
                    frame_pop_kernel_1,
                    text="No",
                    anchor="w",
                    command=pop_kernel_dest,
                    highlightthickness=0,
                    borderwidth=0,
                    background="#2246c4",
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_btn_2000.pack(padx=5, pady=20, side=LEFT)
                pop_btn_shut = Button(
                    frame_pop_kernel_1,
                    text="Do It!",
                    anchor="w",
                    command=do_it,
                    highlightthickness=0,
                    borderwidth=0,
                    background="#f03838",
                    foreground=main_font,
                    compound=LEFT,
                )
                pop_btn_shut.pack(padx=5, pady=20)

            if text == "Boot Log":
                popen("x-terminal-emulator -e 'bash -c \"dmesg; exec bash\"'")

            if text == "Xfce Autostarts":
                popen("xfce4-session-settings")

            if text == "Xfce Settings":
                popen("xfce4-settings-manager")

            if text == "Taskmanager":
                popen("lxtask")

            if text == "Bash History":
                popen(f"xdg-open {home}/.bash_history")

            if text == "Cron Job":
                popen(f"{legit} mousepad /etc/crontab")

            if text == "Menu Settings\nAlacart":
                popen("alacarte")

            if text == "Update-Alternatives":
                add_auto = Update_Alternatives(self)
                add_auto.grab_set()

        self.ops_set = LabelFrame(
            self,
            text="Operating System",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=0,
            width=300,
        )
        self.ops_set.pack(pady=20, padx=40, fill="both")
        self.ops_set["background"] = frame_color

        ops_settings_btn_list = [
            "FM God Mode",
            "Upgrade Linux Kernel",
            "Boot Log",
            "Xfce Autostarts",
            "Xfce Settings",
            "Taskmanager",
            "Bash History",
            "Cron Job",
            "Menu Settings\nAlacart",
            "Update-Alternatives",
        ]

        ops_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for ops_settings_btn in ops_settings_btn_list:
            self.ops_button_x = Button(
                self.ops_set,
                width=140,
                height=100,
                text=ops_settings_btn,
                command=lambda text=ops_settings_btn: ops_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.ops_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            ops_settings_btn_list1.append(self.ops_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if ops_settings_btn == "Gparted":
                self.ops_button_x.config(image=self.gparted_icon)
                if os.path.isfile("/usr/sbin/gparted"):
                    print("[Info]: Gparted is installed")
                    self.ops_button_x.configure(state=NORMAL)
                else:
                    print("[Info]: Gparted is not installed")
                    self.ops_button_x.configure(state=DISABLED)

            if ops_settings_btn == "FM God Mode":
                self.ops_button_x.config(image=self.fm_godmode_icon)
            if ops_settings_btn == "Upgrade Linux Kernel":
                self.ops_button_x.config(image=self.kernel_2_latest_icon)
            if ops_settings_btn == "Boot Log":
                self.ops_button_x.config(image=self.boot_log_icon)
            if ops_settings_btn == "Xfce Autostarts":
                self.ops_button_x.config(image=self.xfce_autostarts_icon)
                self.ops_button_x.configure(state=DISABLED)
                if get_de == "XFCE":
                    self.ops_button_x.configure(state=NORMAL)
            if ops_settings_btn == "Xfce Settings":
                self.ops_button_x.config(image=self.xfce_settings_icon)
                self.ops_button_x.configure(state=DISABLED)
                if get_de == "XFCE":
                    self.ops_button_x.configure(state=NORMAL)
            if ops_settings_btn == "Taskmanager":
                self.ops_button_x.config(image=self.taskmanager_icon)
            if ops_settings_btn == "Bash History":
                self.ops_button_x.config(image=self.bash_history_icon)
            if ops_settings_btn == "Cron Job":
                self.ops_button_x.config(image=self.cron_job_icon)
            if ops_settings_btn == "Menu Settings\nAlacart":
                self.ops_button_x.config(image=self.alacard_icon)
            if ops_settings_btn == "Update-Alternatives":
                self.ops_button_x.config(image=self.bash_history_icon)


class System_Ubuntu_Tab(ttk.Frame):
    """system tab for ubuntu"""

    def __init__(self, container):
        super().__init__()

        # Icon Set
        self.bp01 = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.bp02 = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )

        """System Tab Icons"""
        self.raspi_config_cli_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.raspi_config_gui_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.rename_user_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.edit_config_txt_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/mousepad.png"
        )
        self.gparted_icon = PhotoImage(file=r"images/icons/papirus/48x48/gparted.png")
        self.mouse_keyboard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gnome-settings-keybinding.png"
        )
        self.deskpipro_icon = PhotoImage(file=r"images/icons/pigro_icons/deskpi.png")
        self.network_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/blueman-server.png"
        )
        self.sd_card_copier_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/media-flash-sd-mmc.png"
        )
        self.printer_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/boomaga.png"
        )
        self.desktop_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/com.github.bluesabre.darkbar.png"
        )
        self.screen_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/grandr.png"
        )
        self.neofetch_icon = PhotoImage(file=r"images/icons/pigro_icons/neofetch.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )
        self.kernel_2_latest_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-madlinux.png"
        )
        self.boot_log_icon = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.xfce_autostarts_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.xfce_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.taskmanager_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.bash_history_icon = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.cron_job_icon = PhotoImage(file=r"images/icons/papirus/48x48/mousepad.png")
        self.alacard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/classicmenu-indicator-light.png"
        )
        self.source_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )

        self.update_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/aptdaemon-upgrade.png"
        )

        def pi_ubu_settings(text):
            if text == "Raspi-Config CLI":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} raspi-config; exec bash\"'"
                )

            if text == "Edit Config.txt":
                popen(
                    f"gnome-terminal -e 'bash -c \"{Application_path}/scripts/ubu_config_txt.sh; exec bash\"'"
                )

            if text == "NeoFetch":
                popen("x-terminal-emulator -e 'bash -c \"neofetch; exec bash\"'")

            if text == "DeskpiPro Control":
                popen("x-terminal-emulator -e 'bash -c \"deskpi-config; exec bash\"'")

            if text == "Bash History":
                popen(f"xdg-open {home}/.bash_history")

            if text == "Gnome Tweaks":
                popen("gnome-tweaks")

            if text == "Menu Settings\nAlacart":
                popen("alacarte")

            if text == "Gparted":
                popen(f"{legit} gparted")

            if text == "FM God Mode":
                popen(
                    f"gnome-terminal -e 'bash -c \"{Application_path}/scripts/ubu_FMGM.sh; exec bash\"'"
                )
                print("[Info]: With great power comes great responsibility")
                Notification(
                    title="Sudo File Manager\n",
                    description="With great power comes great responsibility\n\n                          - Oncle Ben",
                    icon_path=f"{Application_path}/images/icons/Logotab.png",
                    duration=5,
                    urgency="normal",
                ).send()
            if text == "Gnome Extensions":
                popen("xdg-open https://extensions.gnome.org/")
            if text == "Software\nUpdates":
                popen("update-manager")
            if text == "Update\nSettings":
                popen("software-properties-gtk")

        self.pi_ubu_set = LabelFrame(
            self,
            text="Raspberry Pi Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
        )
        self.pi_ubu_set.pack(pady=20, padx=40, fill="both")
        self.pi_ubu_set["background"] = maincolor

        pi_ubu_settings_btn_list = [
            "Raspi-Config CLI",
            "Edit Config.txt",
            "NeoFetch",
            "DeskpiPro Control",
            "Bash History",
            "Gnome Tweaks",
            "Menu Settings\nAlacart",
            "Gparted",
            "FM God Mode",
            "Gnome Extensions",
            "Software\nUpdates",
            "Update\nSettings",
        ]

        pi_ubu_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for pi_ubu_settings_btn in pi_ubu_settings_btn_list:
            self.pi_ubu_button_x = Button(
                self.pi_ubu_set,
                width=140,
                height=100,
                text=pi_ubu_settings_btn,
                command=lambda text=pi_ubu_settings_btn: pi_ubu_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=maincolor,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.pi_ubu_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            pi_ubu_settings_btn_list1.append(self.pi_ubu_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if pi_ubu_settings_btn == "Raspi-Config CLI":
                self.pi_ubu_button_x.config(image=self.raspi_config_cli_icon)
                if os.path.isfile("/bin/raspi-config"):
                    print("[Info]: Raspi-Config is installed")
                    self.pi_ubu_button_x.configure(state=NORMAL)
                else:
                    print("[Info]: Raspi-Config is not installed")
                    self.pi_ubu_button_x.configure(state=DISABLED)
            if pi_ubu_settings_btn == "Edit Config.txt":
                self.pi_ubu_button_x.config(image=self.edit_config_txt_icon)
            if pi_ubu_settings_btn == "NeoFetch":
                self.pi_ubu_button_x.config(image=self.neofetch_icon)
                if os.path.isfile("/bin/neofetch"):
                    print("[Info]: Neofetch is installed")
                    self.pi_ubu_button_x.configure(state=NORMAL)
                else:
                    print("[Info]: Neofetch is not installed")
                    self.pi_ubu_button_x.configure(state=DISABLED)
            if pi_ubu_settings_btn == "DeskpiPro Control":
                self.pi_ubu_button_x.config(image=self.deskpipro_icon)
            if pi_ubu_settings_btn == "Bash History":
                self.pi_ubu_button_x.config(image=self.bash_history_icon)
            if pi_ubu_settings_btn == "Gnome Tweaks":
                self.pi_ubu_button_x.config(image=self.source_settings_icon)
            if pi_ubu_settings_btn == "Menu Settings\nAlacart":
                self.pi_ubu_button_x.config(image=self.alacard_icon)
            if pi_ubu_settings_btn == "Gparted":
                self.pi_ubu_button_x.config(image=self.gparted_icon)
            if pi_ubu_settings_btn == "FM God Mode":
                self.pi_ubu_button_x.config(image=self.fm_godmode_icon)
            if pi_ubu_settings_btn == "Gnome Extensions":
                self.pi_ubu_button_x.config(image=self.source_settings_icon)
            if pi_ubu_settings_btn == "Software\nUpdates":
                self.pi_ubu_button_x.config(image=self.update_icon)
            if pi_ubu_settings_btn == "Update\nSettings":
                self.pi_ubu_button_x.config(image=self.update_icon)
            if pi_ubu_settings_btn == "Settings":
                self.pi_ubu_button_x.config(image=self.source_settings_icon)


class Autostarts_Tab(ttk.Frame):
    """displays all files in the autostart folder in a listbox"""

    def __init__(self, container):
        super().__init__()

        self.plus_icon = PhotoImage(file=r"images/icons/pigro_icons/plus_s.png")
        self.minus_icon = PhotoImage(file=r"images/icons/pigro_icons/minus_s.png")
        self.add_app_icon = PhotoImage(file=r"images/icons/pigro_icons/add_app1_s.png")
        self.help_icon = PhotoImage(file=r"images/icons/pigro_icons/help_s.png")
        self.edit_icon = PhotoImage(file=r"images/icons/pigro_icons/edit_app_s.png")

        def add_auto():
            add_child = Add_Autostart(self)
            add_child.grab_set()

        def add_app_auto():
            add_app_child = Add_App_Autostart(self)
            add_app_child.grab_set()

        def edit_auto():
            edit_child = Edit_Autostart(self)
            edit_child.grab_set()

        # Checks is autostart folder exists
        dir = os.path.join(f"{home}/.config/autostart")
        if not os.path.exists(dir):
            print(f"[Info]: {dir} does not exist.")
            print(f"[Info]: Created {dir} does not exist.")
            os.mkdir(dir)
        else:
            print(f"[Info]: {dir} exists.")

        auto_files = [
            f
            for f in listdir(f"{home}/.config/autostart")
            if isfile(join(f"{home}/.config/autostart", f))
        ]

        with open(f"/home/{user}/.pigro/autostart.list", "w") as f:
            for item in auto_files:
                f.write("%s\n" % item)

        def del_enrty():
            global pop_del_entry
            pop_del_entry = Toplevel()
            pop_del_entry.title = " "
            pop_del_entry.config(bg=maincolor)
            app_width = 330
            app_height = 179
            screen_width = pop_del_entry.winfo_screenwidth()
            screen_height = pop_del_entry.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_del_entry.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_del_entry.resizable(0, 0)

            def yes_btn_command():
                os.remove(f"/home/{user}/.config/autostart/{auto_selected.get()}")
                auto_list.delete(tk.ACTIVE)
                auto_selected.delete(0, END)
                pop_del_entry.destroy()

            def no_btn_command():
                pop_del_entry.destroy()

            yes_btn = tk.Button(pop_del_entry)
            yes_btn["bg"] = ext_btn
            yes_btn["borderwidth"] = 0
            yes_btn["highlightthickness"] = 0
            yes_btn["font"] = font_10
            yes_btn["fg"] = main_font
            yes_btn["justify"] = "center"
            yes_btn["text"] = "Yes"
            yes_btn.place(x=70, y=120, width=70, height=25)
            yes_btn["command"] = yes_btn_command

            no_btn = tk.Button(pop_del_entry)
            no_btn["bg"] = ext_btn
            no_btn["borderwidth"] = 0
            no_btn["highlightthickness"] = 0
            no_btn["font"] = font_10
            no_btn["fg"] = main_font
            no_btn["justify"] = "center"
            no_btn["text"] = "No"
            no_btn.place(x=180, y=120, width=70, height=25)
            no_btn["command"] = no_btn_command

            del_label = tk.Label(pop_del_entry)
            del_label["font"] = font_10
            del_label["bg"] = maincolor
            del_label["fg"] = main_font
            del_label["justify"] = "center"
            del_label["text"] = f"Do you really want delete:\n{auto_selected.get()}?"
            del_label.place(x=40, y=40, width=249, height=30)

        # Update the listbox
        def update3(data3):
            # Clear the listbox
            auto_list.delete(0, END)

            # Add toppings to listbox
            for item3 in data3:
                auto_list.insert(END, item3)

        # Update entry box with listbox clicked

        def fillout3(event):
            # Delete wot is in  Box
            auto_selected.delete(0, END)
            # Add clicked list item to enty box
            auto_selected.insert(0, auto_list.get(ACTIVE))

        # Checkfunktion Entry vs. List

        def check3(event):
            # grad inserted
            typed3 = auto_selected.get()

            if typed3 == "":
                data3 = content3
            else:
                data3 = []
                for item3 in content3:
                    if typed3.lower() in item3.lower():
                        data3.append(item3)

            # updates listbox with selected item
            update3(data3)

        auto_main_frame = LabelFrame(
            self,
            text="Autostart Config",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            background=frame_color,
            pady=20,
            padx=20,
        )
        auto_main_frame.pack(pady=20)

        auto_button_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background=frame_color,
            highlightthickness=0,
            pady=10,
        )
        auto_button_frame.pack(side="left", anchor="n", fill=BOTH, expand=True)

        auto_select_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background=frame_color,
            highlightthickness=0,
            pady=10,
        )
        auto_select_frame.pack()

        auto_header_frame = Frame(
            auto_select_frame,
            borderwidth=0,
            background=frame_color,
            highlightthickness=0,
            pady=10,
        )
        auto_header_frame.pack()
        inst_btn3 = Label(
            auto_header_frame,
            text="Selected: \n",
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
            font=font_10,
        )
        inst_btn3.pack(side=LEFT)

        # Create an entry box
        global auto_selected
        auto_selected = Entry(
            auto_header_frame,
            font=font_12,
            highlightthickness=0,
            borderwidth=0,
            bg=frame_color,
            fg=main_font,
        )
        auto_selected.pack()

        global auto_list
        auto_list = Listbox(
            auto_select_frame,
            width=60,
            height=30,
            highlightthickness=2,
            highlightcolor="grey",
            borderwidth=0,
            # background=frame_color,
            # foreground=main_font,
        )
        auto_list.pack()

        fo3 = open(f"/home/{user}/.pigro/autostart.list", "r")
        content3 = fo3.readlines()
        for i3, s3 in enumerate(content3):
            content3[i3] = s3.strip()

        # Add toppings
        update3(content3)

        # Create binding
        auto_list.bind("<<ListboxSelect>>", fillout3)
        auto_selected.bind("<KeyRelease>", check3)

        note_lbl = Label(
            auto_select_frame,
            text="double click to select",
            background=frame_color,
            foreground=info_color,
            font=font_14,
        )
        # note_lbl.pack(pady=5)

        auto_bottom_frame = Frame(
            auto_select_frame,
            borderwidth=0,
            background=frame_color,
            highlightthickness=0,
            pady=10,
        )
        auto_bottom_frame.pack()

        fo3 = open(f"/home/{user}/.pigro/autostart.list", "r")
        content3 = fo3.readlines()

        inst_btn3 = Button(
            auto_bottom_frame,
            image=self.minus_icon,
            text=" - ",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=del_enrty,
        )
        inst_btn3.pack(side=LEFT)

        uninst_btn3 = Button(
            auto_bottom_frame,
            text=" + ",
            image=self.plus_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=add_auto,
        )
        uninst_btn3.pack(side=LEFT, padx=10)

        uninst_btn3 = Button(
            auto_bottom_frame,
            image=self.add_app_icon,
            text="+++",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=add_app_auto,
        )
        uninst_btn3.pack(side=LEFT)

        uninst_btn3 = Button(
            auto_bottom_frame,
            image=self.help_icon,
            text=" E ",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=edit_auto,
        )
        uninst_btn3.pack(side=LEFT, padx=10)


class Update_Alternatives(tk.Toplevel):
    """child window for editing update-alternatives"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 400
        app_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Update-Alternatives")
        self["background"] = maincolor

        def choose_up():
            popen(
                f"x-terminal-emulator -e 'bash -c \"sudo update-alternatives --config {self.choosen.get()}; exec bash\"'"
            )

        self.up_al_frame = Frame(self, background=maincolor)
        self.up_al_frame.pack(padx=20, pady=20)

        n1 = tk.StringVar()
        self.choosen = ttk.Combobox(self.up_al_frame, width=30, textvariable=n1)
        # Adding combobox drop down list
        self.choosen["values"] = (
            "editor",
            "start-here.svg",
            "x-cursor-theme",
            "x-session-manager",
            "x-terminal-emulator",
            "x-window-manager",
            "x-www-browser",
        )

        self.choosen.grid(column=0, row=0, pady=50)

        self.choosen_btn3 = Button(
            self.up_al_frame,
            text="Config",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=choose_up,
        )
        self.choosen_btn3.grid(column=1, row=0)


class Edit_Autostart(tk.Toplevel):
    """child window for editing a .desktopfile in autostart folder"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 630
        app_height = 300
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Details & Edit")
        self["background"] = maincolor

        def done_edit():
            done_child = Done_(self)
            done_child.grab_set()

        def edit_entries():
            popen(f"xdg-open /home/{user}/.config/autostart/{auto_selected.get()}")

        # App Name
        name_label = Label(
            self,
            text="Name:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        name_label.grid(column=0, row=0, padx=5, pady=5, sticky="w")

        name_entry = Entry(self, width=50)

        name_entry.grid(column=1, row=0, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Name=" in line:
                name_entry.insert(0, line[5:-1])

        # App Exec
        exec_label = Label(
            self,
            text="Exec:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        exec_label.grid(column=0, row=1, padx=5, pady=5, sticky="w")

        exec_entry = Entry(self, width=50)
        exec_entry.grid(column=1, row=1, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Exec=" in line:
                exec_entry.insert(0, line[5:-1])

        # App Terminal
        terminal_label = Label(
            self,
            text="Terminal:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        terminal_label.grid(column=0, row=3, padx=5, pady=5, sticky="w")

        terminal_entry = Entry(self, width=50)

        terminal_entry.grid(column=1, row=3, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Terminal=" in line:
                terminal_entry.insert(0, line[9:-1])

        # App Type
        type_label = Label(
            self,
            text="Type:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        type_label.grid(column=0, row=4, padx=5, pady=5, sticky="w")

        type_entry = Entry(self, width=50)

        type_entry.grid(column=1, row=4, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Type=" in line:
                type_entry.insert(0, line[5:-1])

        # App X-GNOME-Autostart-enabled
        x_g_label = Label(
            self,
            text="GNOME Autostart:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        x_g_label.grid(column=0, row=5, padx=5, pady=5, sticky="w")

        x_g_entry = Entry(self, width=50)

        x_g_entry.grid(column=1, row=5, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "X-GNOME-Autostart-enabled=" in line:
                x_g_entry.insert(0, line[26:-1])

        # App X-GNOME-Autostart-Delay
        x_gd_label = Label(
            self,
            text="GNOME Delay:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        x_gd_label.grid(column=0, row=6, padx=5, pady=5, sticky="w")

        x_gd_entry = Entry(self, width=50)

        x_gd_entry.grid(column=1, row=6, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "X-GNOME-Autostart-Delay=" in line:
                x_gd_entry.insert(0, line[24:-1])

        # App Hidden
        hidden_label = Label(
            self,
            text="Hidden:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        hidden_label.grid(column=0, row=7, padx=5, pady=5, sticky="w")

        hidden_entry = Entry(self, width=50)

        hidden_entry.grid(column=1, row=7, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Hidden=" in line:
                hidden_entry.insert(0, line[7:-1])

        # App NoDisplay
        no_display_label = Label(
            self,
            text="NoDisplay:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        no_display_label.grid(column=0, row=8, padx=5, pady=5, sticky="w")

        no_display_entry = Entry(self, width=50)

        no_display_entry.grid(column=1, row=8, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "NoDisplay=" in line:
                no_display_entry.insert(0, line[10:])

        set_btn = Button(
            self,
            text="Open",
            width=10,
            background=ext_btn,
            foreground=main_font,
            command=edit_entries,
        )

        close_butn = Button(
            self,
            text="Close",
            width=10,
            background=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            command=self.destroy,
        )
        close_butn.grid(column=0, row=10, padx=5, pady=5, sticky="w")


class Add_Autostart(tk.Toplevel):
    """child window for creating a .desktopfile in autostart folder"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 180
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Add Entry")
        self["background"] = maincolor

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def add_enrty():

            if add_name.get() == "" or add_path.get() == "":
                error_mass()
            else:
                file_name = f"/home/{user}/.config/autostart/{add_name.get()}.desktop"
                f = open(file_name, "a+")
                f.write(
                    f"[Desktop Entry]\nName={add_name.get()}\nExec={add_path.get()}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true\nX-GNOME-Autostart-Delay=10\nHidden=false\nNoDisplay=false"
                )
                f.close()
                auto_list.insert("end", f"{add_name.get()}.desktop")

                with open(f"/home/{user}/.pigro/autostart.list", "a") as file:
                    file.write(f"{add_name.get()}.desktop")

        add_frame = Frame(self, background=maincolor)
        add_frame.pack(padx=10, pady=10)

        add_name_lbl = Label(
            add_frame,
            text="Name:",
            justify="left",
            anchor="w",
            width=10,
            background=maincolor,
            foreground=main_font,
        )
        add_name_lbl.grid(row=0, column=0)

        add_path_lbl = Label(
            add_frame,
            text="Path to File:",
            justify="left",
            anchor="w",
            width=10,
            background=maincolor,
            foreground=main_font,
        )
        add_path_lbl.grid(row=1, column=0)

        add_name = Entry(
            add_frame,
            width=45,
            highlightthickness=0,
            borderwidth=0,
        )
        add_name.grid(row=0, column=1)

        add_path = Entry(
            add_frame,
            width=45,
            highlightthickness=0,
            borderwidth=0,
        )
        add_path.grid(row=1, column=1)

        example_path_lbl = Label(
            add_frame,
            text="Example: /bin/conky (*options)",
            justify="left",
            anchor="w",
            width=45,
            background=maincolor,
            foreground=main_font,
        )
        example_path_lbl.grid(row=2, column=1)

        set_auto = Button(
            add_frame,
            text="Add",
            width=10,
            command=add_enrty,
            background=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            highlightcolor="white",
        )
        set_auto.grid(row=3, column=0, pady=5)

        cancel_add = Button(
            add_frame,
            text="Close",
            width=10,
            command=self.destroy,
            background=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            highlightcolor="white",
        )
        cancel_add.grid(row=4, column=0, pady=5)


class Add_App_Autostart(tk.Toplevel):
    """child window for creating a .desktopfile in autostart folder"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 100
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Search & Add Entry")
        self["background"] = frame_color

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def add_enrty():
            pass

        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        # apt-get_entry
        self.apt_frame = Frame(
            self,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.apt_frame.pack()
        self.apt_frame["background"] = frame_color

        fo = open(f"/home/{user}/.pigro/auto_plus.list", "r")
        content = fo.readlines()
        for i, s in enumerate(content):
            content[i] = s.strip()
        # print(content)

        def check_input_apt_in(event):
            value = event.widget.get()

            if value == "":
                apt_inst_combo_box["values"] = content
            else:
                data = []
                for item in content:
                    if value.lower() in item.lower():
                        data.append(item)
                apt_inst_combo_box["values"] = data

        def error_mass_0():

            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_mass_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()
            error_y2.config(text="Not in the list! Check for misspell.")

        def inst_btn1():
            if apt_inst_combo_box.get() == "":

                error_mass_0()
            elif apt_inst_combo_box.get() not in content:
                error_mass_1()
            else:
                with open(
                    f"/usr/share/applications/{apt_inst_combo_box.get()}.desktop", "r"
                ) as fp:
                    for line in lines_that_contain("Exec=", fp):
                        # print(line)
                        if line:
                            file_name = f"/home/{user}/.config/autostart/{apt_inst_combo_box.get()}.desktop"
                            f = open(file_name, "w")
                            f.write(
                                f"[Desktop Entry]\nName={apt_inst_combo_box.get()}\n{line[:-1]}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true\nHidden=false\n"
                            )
                            f.close()
                    auto_list.insert("end", f"{apt_inst_combo_box.get()}.desktop")

        # global apt_inst_combo_box
        apt_inst_combo_box = ttk.Combobox(self.apt_frame)
        apt_inst_combo_box["values"] = content
        apt_inst_combo_box.bind("<KeyRelease>", check_input_apt_in)
        apt_inst_combo_box.config(width=30)

        def apt_inst_combo_box_pop_in_kontext_menu(event):
            in_kontext_menu.tk_popup(event.x_root, event.y_root)

        def apt_inst_combo_box_paste():
            apt_inst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        in_kontext_menu = Menu(apt_inst_combo_box, tearoff=0, bg="white", fg="black")
        # options
        in_kontext_menu.add_command(label="Paste", command=apt_inst_combo_box_paste)

        # Make the in_kontext_menu pop up
        apt_inst_combo_box.bind("<Button - 3>", apt_inst_combo_box_pop_in_kontext_menu)

        self.apt_ico = Label(
            self.apt_frame,
            text="Select:",
            foreground=label_frame_color,
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.apt_ico["background"] = frame_color
        self.apt_ico.grid(
            column=0,
            row=0,
        )
        apt_inst_combo_box.grid(column=2, row=0)

        set_auto = Button(
            self.apt_frame,
            text="Add",
            width=10,
            background=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            highlightcolor="white",
            command=inst_btn1,
        )
        set_auto.grid(row=3, column=0, pady=5)

        cancel_add = Button(
            self.apt_frame,
            text="Close",
            width=10,
            command=self.destroy,
            background=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
            highlightcolor="white",
        )
        cancel_add.grid(row=4, column=0, pady=5)


class Tuning_Legende(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Overclocking Legend")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.tu_1 = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV_rm.png")
        self.tu_2 = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV1.png")
        self.tu_3 = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV2.png")
        self.tu_4 = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV3.png")
        self.tu_5 = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV4.png")

        # Main Frame
        self.tu_main_frame = Frame(self, bg=maincolor)
        self.tu_main_frame.pack(pady=20)

        # Reset
        self.rm_lbl = Label(
            self.tu_main_frame,
            text="Reset Settings",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            justify=LEFT,
        )
        self.rm_lbl.grid(row=0, column=0)

        self.rm_ov = Label(self.tu_main_frame, image=self.tu_1, bg=maincolor)
        self.rm_ov.grid(row=1, column=0)

        self.rm_text = Label(
            self.tu_main_frame,
            text="Removes all\noverclocking parameters\n\n",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.rm_text.grid(row=1, column=1)

        # OV_1
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Crank It Up!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=2, column=0)

        self.ov_1 = Label(
            self.tu_main_frame, image=self.tu_2, bg=maincolor, foreground=main_font
        )
        self.ov_1.grid(row=3, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2000\ngpu_freq = 750\nover_voltage = 6\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_1_text.grid(row=3, column=1)

        # OV_2
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="You Sir, Need A Fan!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=1)

        self.ov_1 = Label(
            self.tu_main_frame, image=self.tu_3, bg=maincolor, foreground=main_font
        )
        self.ov_1.grid(row=5, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2147\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_1_text.grid(row=5, column=1)

        # OV_3
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Take It To The Max!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=1)

        self.ov_1 = Label(
            self.tu_main_frame, image=self.tu_4, bg=maincolor, foreground=main_font
        )
        self.ov_1.grid(row=7, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2200\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_1_text.grid(row=7, column=1)

        # OV_4
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Honey,the fuse blew again!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=1)

        self.ov_1 = Label(
            self.tu_main_frame, image=self.tu_5, bg=maincolor, foreground=main_font
        )
        self.ov_1.grid(row=9, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2300\ngpu_freq = 750\nover_voltage = 14\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_1_text.grid(row=9, column=1)

        self.tu_main_Update_Tab = Frame(self, bg=maincolor)
        self.tu_main_Update_Tab.pack(pady=20)


class Done_Restart_P(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        done_label = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=12)
        done_label["font"] = ft
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Restart of PiGro is require\nfor changes to take effect"
        done_label.pack(pady=20)

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"
        cont_btn["font"] = font_10
        cont_btn["fg"] = main_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Got It!"
        cont_btn.pack()
        cont_btn["command"] = self.destroy


class Done_(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 180
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"

        cont_btn["font"] = font_10
        cont_btn["fg"] = main_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        global done_label
        done_label = tk.Label(self)
        done_label["font"] = font_14
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)


class Done_Reboot(tk.Toplevel):
    """a custom massagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done! Reboot?")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 180
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"
        ft = tkFont.Font(family="Sans", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = main_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        rebt_btn = tk.Button(self)
        rebt_btn["bg"] = "#efefef"
        rebt_btn["font"] = font_10
        rebt_btn["fg"] = main_font
        rebt_btn["bg"] = ext_btn
        rebt_btn["justify"] = "center"
        rebt_btn["highlightthickness"] = 0
        rebt_btn["borderwidth"] = 0
        rebt_btn["text"] = "Reboot"
        rebt_btn.place(x=160, y=130, width=70, height=25)
        rebt_btn["command"] = self.rebt_btn_command

        done_label = tk.Label(self)
        done_label["font"] = font_14
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)

    def rebt_btn_command(self):
        popen(f"{legit} reboot")


class Overclocking_Expert(tk.Toplevel):
    """entry fields to custom configure config.txt"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Expert Mode")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        # arm_freq
        def set_arm_freq():
            if (
                arm_freq_entry.get() == "Default is 1500/1800"
                or arm_freq_entry.get() == ""
            ):
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "arm_freq={arm_freq_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                arm_freq_set.config(state=DISABLED)
                arm_freq_reset.config(state=NORMAL)

        def reset_arm_freq():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/arm_freq/d' config.txt"
                )
                arm_freq_set.config(state=NORMAL)
                arm_freq_reset.config(state=DISABLED)
                arm_f_display.config(text="not configured")
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/arm_freq/d' config.txt")
                arm_freq_set.config(state=NORMAL)
                arm_freq_reset.config(state=DISABLED)
                arm_f_display.config(text="not configured")

        # gpu_freq
        def set_gpu_freq():
            if gpu_freq_entry.get() == "Default is 500" or gpu_freq_entry.get() == "":
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "gpu_freq={gpu_freq_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                gpu_freq_set.config(state=DISABLED)
                gpu_freq_reset.config(state=NORMAL)

        def reset_gpu_freq():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/gpu_freq/d' config.txt"
                )
                gpu_freq_set.config(state=NORMAL)
                gpu_freq_reset.config(state=DISABLED)
                gpu_f_display.config(text="not configured")
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/gpu_freq/d' config.txt")
                gpu_freq_set.config(state=NORMAL)
                gpu_freq_reset.config(state=DISABLED)
                gpu_f_display.config(text="not configured")

        # set_gpu_mem
        def set_gpu_mem():
            if gpu_mem_entry.get() == "Minimum 16" or gpu_mem_entry.get() == "":
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "gpu_mem={gpu_mem_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                gpu_mem_set.config(state=DISABLED)
                gpu_mem_reset.config(state=NORMAL)

        def reset_gpu_mem():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/gpu_mem/d' config.txt"
                )
                gpu_mem_set.config(state=NORMAL)
                gpu_mem_reset.config(state=DISABLED)
                gpu_m_display.config(text="not configured")
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/gpu_mem/d' config.txt")
                gpu_mem_set.config(state=NORMAL)
                gpu_mem_reset.config(state=DISABLED)
                gpu_m_display.config(text="not configured")

        # set_over_voltage
        def set_over_voltage():
            if (
                over_voltage_entry.get() == "Default 0"
                or over_voltage_entry.get() == ""
            ):
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "over_voltage={over_voltage_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                over_voltage_set.config(state=DISABLED)
                over_voltage_reset.config(state=NORMAL)

        def reset_over_voltage():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/over_voltage/d' config.txt"
                )
                over_voltage_set.config(state=NORMAL)
                over_voltage_reset.config(state=DISABLED)
                over_v_display.config(text="not configured")
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/over_voltage/d' config.txt")
                over_voltage_set.config(state=NORMAL)
                over_voltage_reset.config(state=DISABLED)
                over_v_display.config(text="not configured")

        # set_disable_splash
        def set_disable_splash():
            if (
                disable_splash_entry.get() == "Default 0"
                or disable_splash_entry.get() == ""
            ):
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "disable_splash={disable_splash_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                disable_splash_set.config(state=DISABLED)
                disable_splash_reset.config(state=NORMAL)

        def reset_disable_splash():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/disable_splash/d' config.txt"
                )
                disable_splash_set.config(state=NORMAL)
                disable_splash_reset.config(state=DISABLED)
                force_t_display.config(text="not configured")
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/disable_splash/d' config.txt")
                disable_splash_set.config(state=NORMAL)
                disable_splash_reset.config(state=DISABLED)
                force_t_display.config(text="not configured")

        # set_force_turbo
        def set_force_turbo():
            if force_turbo_entry.get() == "Default 0" or force_turbo_entry.get() == "":
                error_mass()
            else:
                os.system(
                    f"""{legit} sh -c 'echo "force_turbo={force_turbo_entry.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
                force_turbo_set.config(state=DISABLED)
                force_turbo_reset.config(state=NORMAL)

        def reset_force_turbo():
            if distro_get == "ubuntu":
                os.popen(
                    f" cd /boot/firmware/ && {legit} sed -i '/force_turbo/d' config.txt"
                )
                force_turbo_set.config(state=NORMAL)
                force_turbo_reset.config(state=DISABLED)
            else:
                os.popen(f" cd /boot/ && {legit} sed -i '/force_turbo/d' config.txt")
                force_turbo_set.config(state=NORMAL)
                force_turbo_reset.config(state=DISABLED)

        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def reboot_n():
            popen(f"{legit} reboot")

        # Expert Frame
        x_mode_frame = Frame(self, bg=maincolor)
        x_mode_frame.pack(pady=20)

        # arm_freq
        arm_freq_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="arm_freq = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        arm_freq_label.grid(row=0, column=0)

        global arm_freq_entry
        arm_freq_entry = Entry(x_mode_frame, borderwidth=0, highlightthickness=2)
        arm_freq_entry.grid(row=0, column=1)
        arm_freq_entry.insert(0, "Default is 1500/1800")

        global arm_freq_set
        arm_freq_set = Button(
            x_mode_frame,
            text="Set",
            command=set_arm_freq,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        arm_freq_set.grid(row=0, column=2, padx=10, pady=10)

        global arm_freq_reset
        arm_freq_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_arm_freq,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        arm_freq_reset.grid(row=0, column=3, padx=10, pady=10)

        with open(f"{config_path}", "r") as fp:
            for line_a_f in lines_that_contain("arm_freq", fp):
                # print(line3)
                if line_a_f:
                    arm_freq_set.config(state=DISABLED)
                    arm_freq_reset.config(state=NORMAL)
        # gpu_freq
        gpu_freq_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="gpu_freq = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        gpu_freq_label.grid(row=1, column=0)

        global gpu_freq_entry
        gpu_freq_entry = Entry(
            x_mode_frame,
        )
        gpu_freq_entry.grid(row=1, column=1)
        gpu_freq_entry.insert(0, "Default is 500")

        global gpu_freq_set
        gpu_freq_set = Button(
            x_mode_frame,
            text="Set",
            command=set_gpu_freq,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        gpu_freq_set.grid(row=1, column=2)

        global gpu_freq_reset
        gpu_freq_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_gpu_freq,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        gpu_freq_reset.grid(row=1, column=3)

        with open(f"{config_path}", "r") as fp:
            for line_g_f in lines_that_contain("gpu_freq", fp):
                # print(line3)
                if line_g_f:
                    gpu_freq_set.config(state=DISABLED)
                    gpu_freq_reset.config(state=NORMAL)
        # gpu_mem
        gpu_mem_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="gpu_mem = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        gpu_mem_label.grid(row=2, column=0)

        global gpu_mem_entry
        gpu_mem_entry = Entry(
            x_mode_frame,
        )
        gpu_mem_entry.grid(row=2, column=1)
        gpu_mem_entry.insert(0, "Minimum 16/Not Set")

        global gpu_mem_set
        gpu_mem_set = Button(
            x_mode_frame,
            text="Set",
            command=set_gpu_mem,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        gpu_mem_set.grid(row=2, column=2, padx=10, pady=10)

        global gpu_mem_reset
        gpu_mem_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_gpu_mem,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        gpu_mem_reset.grid(row=2, column=3, padx=10, pady=10)

        with open(f"{config_path}", "r") as fp:
            for line_g_m in lines_that_contain("gpu_mem", fp):
                # print(line3)
                if line_g_m:
                    gpu_mem_set.config(state=DISABLED)
                    gpu_mem_reset.config(state=NORMAL)

        # over_voltage
        over_voltage_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="over_voltage = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        over_voltage_label.grid(row=3, column=0)

        global over_voltage_entry
        over_voltage_entry = Entry(
            x_mode_frame,
        )
        over_voltage_entry.grid(row=3, column=1)
        over_voltage_entry.insert(0, "Default is 0/Not Set")

        global over_voltage_set
        over_voltage_set = Button(
            x_mode_frame,
            text="Set",
            command=set_over_voltage,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        over_voltage_set.grid(row=3, column=2)

        global over_voltage_reset
        over_voltage_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_over_voltage,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        over_voltage_reset.grid(row=3, column=3)

        with open(f"{config_path}", "r") as fp:
            for line_o_v in lines_that_contain("over_voltage", fp):
                # print(line3)
                if line_o_v:
                    over_voltage_set.config(state=DISABLED)
                    over_voltage_reset.config(state=NORMAL)

        # disable_splash
        disable_splash_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="disable_splash = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        disable_splash_label.grid(row=4, column=0)

        global disable_splash_entry
        disable_splash_entry = Entry(
            x_mode_frame,
        )
        disable_splash_entry.grid(row=4, column=1)
        disable_splash_entry.insert(0, "Default is 0/Not Set")

        global disable_splash_set
        disable_splash_set = Button(
            x_mode_frame,
            text="Set",
            command=set_disable_splash,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        disable_splash_set.grid(row=4, column=2, padx=10, pady=10)

        global disable_splash_reset
        disable_splash_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_disable_splash,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        disable_splash_reset.grid(row=4, column=3, padx=10, pady=10)

        with open(f"{config_path}", "r") as fp:
            for line_d_s in lines_that_contain("disable_splash", fp):
                # print(line3)
                if line_d_s:
                    disable_splash_set.config(state=DISABLED)
                    disable_splash_reset.config(state=NORMAL)

        # force_turbo
        force_turbo_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="force_turbo = ",
            bg=maincolor,
            foreground=main_font,
            anchor="w",
            width=15,
        )
        force_turbo_label.grid(row=5, column=0)

        global force_turbo_entry
        force_turbo_entry = Entry(
            x_mode_frame,
        )
        force_turbo_entry.grid(row=5, column=1)
        force_turbo_entry.insert(0, "Default is 0/Not Set")

        global force_turbo_set
        force_turbo_set = Button(
            x_mode_frame,
            text="Set",
            command=set_force_turbo,
            bg=ext_btn,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        force_turbo_set.grid(row=5, column=2)

        global force_turbo_reset
        force_turbo_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_force_turbo,
            bg="red",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
        )
        force_turbo_reset.grid(row=5, column=3)

        with open(f"{config_path}", "r") as fp:
            for line_f_t in lines_that_contain("force_turbo", fp):
                # print(line3)
                if line_f_t:
                    force_turbo_set.config(state=DISABLED)
                    force_turbo_reset.config(state=NORMAL)

        reboot_e = Button(
            self,
            justify=LEFT,
            font=(font_12_b),
            text="Reboot",
            bg=maincolor,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=2,
            command=reboot_n,
        )
        reboot_e.pack()


class Custom_Installer(tk.Toplevel):
    """child window that makes the the install process graphicle"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"{pigro_skript_name}")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 500
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # progressbar
        global inst_show
        inst_show = Label(
            self,
            text="",
            bg="#333333",
            foreground=main_font,
        )
        inst_show.pack(pady=20)

        anim = Loading_Throbber(self, "images/icons/loading.gif")
        anim["borderwidth"] = "0"
        anim.pack()

        def stop_it():
            anim.after_cancel(anim.cancel)

        self.cust_inst_termf = Frame(
            self, height=300, width=600, highlightthickness=0, borderwidth=0
        )

        self.cust_inst_wid = self.cust_inst_termf.winfo_id()

        self.cust_inst_termf["background"] = "#333333"
        self.cust_inst_termf.pack(padx=45, pady=20)

        def install_parameter():
            os.system(
                f'xterm -into %d -bg Grey11 -geometry 120x25 -e "{pigro_skript}; exec bash"'
                % self.cust_inst_wid
            )

            stop_it()
            anim.forget()
            close_btn.configure(state=NORMAL)
            self.title(f"Done!")
            inst_show.configure(text=" ")
            cancel_btn.place_forget()

        # place the progressbar

        def close_btn_command():
            Custom_Installer.destroy(self)

        close_btn = tk.Button(self)
        ft = tkFont.Font(family="Sans", size=12)
        close_btn["font"] = ft
        close_btn["justify"] = "center"
        close_btn["highlightthickness"] = 0
        close_btn["borderwidth"] = 0
        close_btn["background"] = ext_btn
        close_btn["foreground"] = main_font
        close_btn["text"] = "Close"
        close_btn.place(x=580, y=450, width=70, height=25)
        close_btn["command"] = close_btn_command
        close_btn.configure(state=DISABLED)

        cancel_btn = tk.Button(self)
        cancel_btn["font"] = font_12
        cancel_btn["justify"] = "center"
        cancel_btn["highlightthickness"] = 0
        cancel_btn["borderwidth"] = 0
        cancel_btn["background"] = ext_btn
        cancel_btn["foreground"] = main_font
        cancel_btn["text"] = "Cancel"
        cancel_btn.place(x=500, y=450, width=70, height=25)
        cancel_btn["command"] = close_btn_command

        Thread(target=install_parameter).start()


class Pkg_info_frame(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title(pkg_skript_name)
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)

        global done_label
        done_label = tk.Label(self)
        done_label["font"] = font_10
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "left"
        done_label["text"] = read_pkg_infos
        done_label.pack()


class Software_Tab(ttk.Frame):
    def __init__(self, container):
        """lets you install apps via APT, snap, pi-apps and flatpak in one single window"""
        super().__init__()

        notebook = ttk.Notebook(self)
        notebook.pack(fill=BOTH, expand=True)

        # create frames
        apt_frame = ttk.Frame(notebook)
        piapp_frame = ttk.Frame(notebook)
        flat_frame = ttk.Frame(notebook)
        snap_frame = ttk.Frame(notebook)
        repo_frame = ttk.Frame(notebook)

        apt_frame.pack(fill="both", expand=True)
        piapp_frame.pack(fill="both", expand=True)
        flat_frame.pack(fill="both", expand=True)
        snap_frame.pack(fill="both", expand=True)
        repo_frame.pack(fill="both", expand=True)

        # add frames to notebook

        notebook.add(apt_frame, text="APT")
        notebook.add(piapp_frame, text="Pi Apps")
        notebook.add(flat_frame, text="Flatpak")
        notebook.add(snap_frame, text="Snap")
        notebook.add(repo_frame, text="\nInstant\nInstall")

        # apt-get_entry
        self.apt_inst_frame = LabelFrame(
            apt_frame,
            text="Advanced Packaging Tool",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            padx=20,
            pady=20,
        )
        self.apt_inst_frame.pack(pady=20)
        self.apt_inst_frame["background"] = frame_color

        fo = os.popen("apt-cache pkgnames")
        content = fo.readlines()
        for i, s in enumerate(content):
            content[i] = s.strip()
        # print(content)

        def check_input_apt_in(event):
            value = event.widget.get()

            if value == "":
                apt_inst_combo_box["values"] = content
            else:
                data = []
                for item in content:
                    if value.lower() in item.lower():
                        data.append(item)
                apt_inst_combo_box["values"] = data

        def error_mass_0():

            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_mass_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()
            error_y2.config(text="Not in the list! Check for misspell.")

        def apt_install():
            if apt_inst_combo_box.get() == "":

                error_mass_0()
            elif apt_inst_combo_box.get() not in content:
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Installing... {apt_inst_combo_box.get()}"
                global pigro_skript
                pigro_skript = (
                    f"{legit} apt install {apt_inst_combo_box.get()} -y && exit"
                )
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        global apt_inst_combo_box
        apt_inst_combo_box = ttk.Combobox(self.apt_inst_frame)
        apt_inst_combo_box["values"] = content
        apt_inst_combo_box.bind("<KeyRelease>", check_input_apt_in)
        apt_inst_combo_box.config(width=25)

        def apt_inst_combo_box_pop_in_kontext_menu(event):
            in_kontext_menu.tk_popup(event.x_root, event.y_root)

        def apt_inst_combo_box_paste():
            apt_inst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        in_kontext_menu = Menu(apt_inst_combo_box, tearoff=0, bg="white", fg="black")
        # options
        in_kontext_menu.add_command(label="Paste", command=apt_inst_combo_box_paste)

        # Make the in_kontext_menu pop up
        apt_inst_combo_box.bind("<Button - 3>", apt_inst_combo_box_pop_in_kontext_menu)

        def apt_info():
            if apt_inst_combo_box.get() == "":

                error_mass_0()
            elif apt_inst_combo_box.get() not in content:
                error_mass_1()
            else:
                global pkg_skript_name
                pkg_skript_name = f"Info: {apt_inst_combo_box.get()}"
                global read_pkg_infos
                pkg_infos = popen(
                    f"apt show -a {apt_inst_combo_box.get()}"  # |grep 'Package:\|Homepage:\|Version:\|Maintainer:\|Section:\|Download-Size:\|Installed-Size:\|Description:'"
                )
                read_pkg_infos = pkg_infos.read()

                # pkg_i = Pkg_info_frame(self)
                # pkg_i.grab_set()

                quote = read_pkg_infos
                T.delete("1.0", "end")
                T.insert(END, quote)

        self.apt_inst_btn = Button(
            self.apt_inst_frame,
            text="install",
            command=apt_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )
        self.apt_inst_info_btn = Button(
            self.apt_inst_frame,
            text="Info",
            command=apt_info,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        apt_inst_combo_box.grid(column=1, row=0, padx=5)
        self.apt_inst_btn.grid(column=0, row=0)
        self.apt_inst_info_btn.grid(column=0, row=1, pady=10)

        ua_fo = os.popen("dpkg --get-selections |sed -e s/install//g")
        un_content = ua_fo.readlines()
        for i, s in enumerate(un_content):
            un_content[i] = s.strip()

        def check_input_apt_un(event):
            value = event.widget.get()

            if value == "":
                apt_un_combo_box["values"] = un_content
            else:
                data = []
                for item in un_content:
                    if value.lower() in item.lower():
                        data.append(item)
                apt_un_combo_box["values"] = data

        def apt_uninstall():
            if apt_un_combo_box.get() == "":
                error_mass_0()
            elif apt_un_combo_box.get() not in un_content:
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Uninstalling... {apt_un_combo_box.get()}"
                global pigro_skript
                pigro_skript = (
                    f"{legit} apt install {apt_un_combo_box.get()} -y && exit"
                )
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        global apt_un_combo_box
        apt_un_combo_box = ttk.Combobox(self.apt_inst_frame)
        apt_un_combo_box["values"] = un_content
        apt_un_combo_box.bind("<KeyRelease>", check_input_apt_un)
        apt_un_combo_box.config(width=25)

        self.un_apt_inst_btn = Button(
            self.apt_inst_frame,
            text="remove",
            command=apt_uninstall,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        apt_un_combo_box.grid(column=3, row=0)
        self.un_apt_inst_btn.grid(column=2, row=0, padx=5)

        apt_inst_combo_box.set("Select/Search a package -->")
        apt_un_combo_box.set("Select/Search a package -->")

        def apt_un_combo_box_pop_kontext_menu(event):
            un_kontext_menu.tk_popup(event.x_root, event.y_root)

        def apt_un_combo_box_paste():
            apt_un_combo_box.event_generate("<<Paste>>")

        # Right Click kontext_menu
        un_kontext_menu = Menu(apt_un_combo_box, tearoff=0, bg="white", fg="black")
        # options
        un_kontext_menu.add_command(label="Paste", command=apt_un_combo_box_paste)

        # Make the kontext_menu pop up
        apt_un_combo_box.bind("<Button - 3>", apt_un_combo_box_pop_kontext_menu)

        info_frame = LabelFrame(
            apt_frame,
            text="Package Information",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=20,
        )
        info_frame["background"] = frame_color
        info_frame.pack(fill=BOTH, expand=True, padx=55, pady=20)

        T = Text(
            info_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
        )
        T.pack(fill=BOTH, expand=True)

        # pi apps_entry
        self.piapps_inst_frame = LabelFrame(
            piapp_frame,
            text="Pi Apps",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            padx=20,
            pady=20,
        )
        self.piapps_inst_frame.pack(pady=20)
        self.piapps_inst_frame["background"] = frame_color

        fo_pa = popen(
            f"ls ~/pi-apps/apps/ "
        )  # open(f"/home/{user}/.pigro/pi-apps_list.list", "r")
        content_pa = fo_pa.readlines()
        for i, s in enumerate(content_pa):
            content_pa[i] = s.strip()
        # print(content)

        def check_input_pa_in(event):
            value = event.widget.get()

            if value == "":
                piapps_inst_combo_box["values"] = content_pa
            else:
                data_pa = []
                for item in content_pa:
                    if value.lower() in item.lower():
                        data_pa.append(item)
                piapps_inst_combo_box["values"] = data_pa

        def piapps_install():
            if piapps_inst_combo_box.get() == "":
                error_mass_0()
            else:
                fullstring = piapps_inst_combo_box.get()
                substring = " "
                if substring in fullstring:
                    replace_space = fullstring.replace(" ", "\ ")
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage install {replace_space}; exec bash\"'"
                    )
                else:
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage install {piapps_inst_combo_box.get()}; exec bash\"'"
                    )

        global piapps_inst_combo_box
        piapps_inst_combo_box = ttk.Combobox(self.piapps_inst_frame)
        piapps_inst_combo_box["values"] = content_pa
        piapps_inst_combo_box.bind("<KeyRelease>", check_input_pa_in)
        piapps_inst_combo_box.config(width=25)

        def piapps_inst_combo_box_pop_in_kontext_menu(event):
            pa_in_kontext_menu.tk_popup(event.x_root, event.y_root)

        def piapps_inst_combo_box_paste():
            piapps_inst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        pa_in_kontext_menu = Menu(
            piapps_inst_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        pa_in_kontext_menu.add_command(
            label="Paste", command=piapps_inst_combo_box_paste
        )

        # Make the in_kontext_menu pop up
        piapps_inst_combo_box.bind(
            "<Button - 3>", piapps_inst_combo_box_pop_in_kontext_menu
        )

        def pi_apps_info():
            if piapps_inst_combo_box.get() == "":
                error_mass_0()
            else:
                global pkg_skript_name
                pkg_skript_name = f"Info: {piapps_inst_combo_box.get()}"

                pkg_infos = open(
                    f"{home}/pi-apps/apps/{piapps_inst_combo_box.get()}/description",
                    "r",
                )
                global read_pkg_infos
                read_pkg_infos = pkg_infos.read()
                pkg_infos.close()
                # pkg_i = Pkg_info_frame(self)
                # pkg_i.grab_set()

                quote_pi_aps = read_pkg_infos
                T_piapps.delete("1.0", "end")
                T_piapps.insert(END, quote_pi_aps)

        global piapps_inst_btn
        piapps_inst_btn = Button(
            self.piapps_inst_frame,
            text="install",
            command=piapps_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        piapps_inst_info_btn = Button(
            self.piapps_inst_frame,
            text="Info",
            command=pi_apps_info,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        piapps_inst_combo_box.grid(column=1, row=0, padx=5)
        piapps_inst_btn.grid(column=0, row=0)
        piapps_inst_info_btn.grid(column=0, row=1, pady=10)

        ua_fo_pa = open(f"/home/{user}/.pigro/pi-apps_installed.list", "r")
        un_content_pa = ua_fo_pa.readlines()
        for i, s in enumerate(un_content_pa):
            un_content_pa[i] = s.strip()

        def check_input_pa_un(event):
            value = event.widget.get()

            if value == "":
                piapps_un_combo_box["values"] = un_content_pa
            else:
                data_un_pa = []
                for item in un_content_pa:
                    if value.lower() in item.lower():
                        data_un_pa.append(item)
                piapps_un_combo_box["values"] = data_un_pa

        def piapps_uninstall():
            if piapps_un_combo_box.get() == "":
                error_mass_0()
            else:
                fullstring = piapps_un_combo_box.get()
                substring = " "
                if substring in fullstring:
                    replace_space = fullstring.replace(" ", "\ ")
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage uninstall {replace_space}; exec bash\"'"
                    )
                else:
                    popen(
                        f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage uninstall {piapps_un_combo_box.get()}; exec bash\"'"
                    )

        global piapps_un_combo_box
        piapps_un_combo_box = ttk.Combobox(self.piapps_inst_frame)
        piapps_un_combo_box["values"] = un_content_pa
        piapps_un_combo_box.bind("<KeyRelease>", check_input_pa_un)
        piapps_un_combo_box.config(width=25)

        un_piapps_inst_btn = Button(
            self.piapps_inst_frame,
            text="remove",
            command=piapps_uninstall,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        piapps_un_combo_box.grid(column=3, row=0)
        un_piapps_inst_btn.grid(column=2, row=0, padx=5)
        if piapps_path == True:
            piapps_inst_combo_box.set("Select/Search a package -->")
            piapps_un_combo_box.set("Select/Search a package -->")

        if piapps_path == False:
            piapps_inst_btn.config(state=DISABLED)
            piapps_inst_combo_box.set("Pi-Apps is not installed")
            un_piapps_inst_btn.config(state=DISABLED)
            piapps_un_combo_box.set("Pi-Apps is not installed")
            notebook.tab(2,state=DISABLED)

        def piapps_un_combo_box_pop_kontext_menu(event):
            pa_un_kontext_menu.tk_popup(event.x_root, event.y_root)

        def piapps_un_combo_box_paste():
            piapps_un_combo_box.event_generate("<<Paste>>")

        # Right Click kontext_menu
        pa_un_kontext_menu = Menu(
            piapps_un_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        pa_un_kontext_menu.add_command(label="Paste", command=piapps_un_combo_box_paste)

        # Make the kontext_menu pop up
        piapps_un_combo_box.bind("<Button - 3>", piapps_un_combo_box_pop_kontext_menu)

        info_frame = LabelFrame(
            piapp_frame,
            text="Package Information",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=20,
        )
        info_frame["background"] = frame_color
        info_frame.pack(fill=BOTH, expand=True, padx=55, pady=20)

        T_piapps = Text(
            info_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
        )
        T_piapps.pack(fill=BOTH, expand=True)

        # flatpak apps_entry
        self.flatpak_inst_frame = LabelFrame(
            flat_frame,
            text="Flatpak",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            padx=20,
            pady=20,
        )
        self.flatpak_inst_frame.pack(pady=20)
        self.flatpak_inst_frame["background"] = frame_color

        # VARs for Flatpak remote list
        f1 = "flatpak remote-ls --columns=name"
        f2 = "flatpak remote-ls --columns=application"

        # Get Name Key
        flat_name_content = os.popen(f1)
        flat_name_list = flat_name_content.readlines()
        for i1, s1 in enumerate(flat_name_list):
            flat_name_list[i1] = s1.strip()

        # Get App Key
        flat_app_content = os.popen(f2)
        flat_app_list = flat_app_content.readlines()
        for i2, s2 in enumerate(flat_app_list):
            flat_app_list[i2] = s2.strip()

        # Zips NAME & APP
        zip_name_app = zip(flat_name_list, flat_app_list)

        # Puts zip_name_app in dict
        Flat_remote_dict = dict(zip_name_app)

        # print(Flat_remote_dict)

        var_material = tk.StringVar()

        def check_input_flatpak_in(event):
            value = event.widget.get()

            if value == "":
                flatpak_inst_combo_box["values"] = Flat_remote_dict.keys()
            else:
                data_flatpak = []
                for item in Flat_remote_dict.keys():
                    if value.lower() in item.lower():
                        data_flatpak.append(item)
                flatpak_inst_combo_box["values"] = data_flatpak

        def flat_install():
            if flatpak_inst_combo_box.get() == "":

                error_mass_0()
            elif flatpak_inst_combo_box.get() not in Flat_remote_dict.keys():
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Installing... {flatpak_inst_combo_box.get()}"
                global pigro_skript
                pigro_skript = f"flatpak install flathub {Flat_remote_dict[var_material.get()]} -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()
                print(Flat_remote_dict[var_material.get()])

        global flatpak_inst_combo_box
        flatpak_inst_combo_box = ttk.Combobox(
            self.flatpak_inst_frame,
            values=list(Flat_remote_dict.keys()),
            justify="left",
            textvariable=var_material,
        )
        flatpak_inst_combo_box.bind("<KeyRelease>", check_input_flatpak_in)
        flatpak_inst_combo_box.config(width=25)

        def flatpak_inst_combo_box_pop_in_kontext_menu(event):
            flatpak_install_kontext_menu.tk_popup(event.x_root, event.y_root)

        def flatpak_inst_combo_box_paste():
            flatpak_inst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        flatpak_install_kontext_menu = Menu(
            flatpak_inst_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        flatpak_install_kontext_menu.add_command(
            label="Paste", command=flatpak_inst_combo_box_paste
        )

        # Make the in_kontext_menu pop up
        flatpak_inst_combo_box.bind(
            "<Button - 3>", flatpak_inst_combo_box_pop_in_kontext_menu
        )
        global flatpak_inst_btn
        flatpak_inst_btn = Button(
            self.flatpak_inst_frame,
            text="install",
            command=flat_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        flatpak_info_btn = Button(
            self.flatpak_inst_frame,
            text="Info",
            command=flat_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
            state=DISABLED,
        )

        flatpak_inst_combo_box.grid(column=1, row=0, padx=5)
        flatpak_inst_btn.grid(column=0, row=0)
        flatpak_info_btn.grid(column=0, row=1, pady=10)

        if flatpak_path == True:
            flatpak_inst_combo_box.set("Select/Search a package -->")

        if flatpak_path == False:
            flatpak_inst_btn.config(state=DISABLED)
            flatpak_inst_combo_box.set("Flatpak is not installed")

        # VARs for Flatpak installed list
        fu1 = "flatpak list --columns=name"
        fu2 = "flatpak list --columns=application"

        # Get Name Key
        flat_un_name_content = os.popen(fu1)
        flat_un_name_list = flat_un_name_content.readlines()
        for i3, s3 in enumerate(flat_un_name_list):
            flat_un_name_list[i3] = s3.strip()

        # Get App Key
        flat_un_app_content = os.popen(fu2)
        flat_un_app_list = flat_un_app_content.readlines()
        for i4, s4 in enumerate(flat_un_app_list):
            flat_un_app_list[i4] = s4.strip()

        # Zips NAME & APP
        zip_un_name_app = zip(flat_un_name_list, flat_un_app_list)

        # Puts zip_un_name_app in dict
        flat_uninstalled_dict = dict(zip_un_name_app)

        # print(flat_uninstalled_dict)

        un_var_material = tk.StringVar()

        def check_input_flatpak_un(event):
            value = event.widget.get()

            if value == "":
                flatpak_uninst_combo_box["values"] = flat_uninstalled_dict.keys()
            else:
                un_data_flatpak = []
                for item in flat_uninstalled_dict.keys():
                    if value.lower() in item.lower():
                        un_data_flatpak.append(item)
                flatpak_uninst_combo_box["un_values"] = un_data_flatpak

        def flat_uninstall():
            if flatpak_uninst_combo_box.get() == "":

                error_mass_0()
            elif flatpak_uninst_combo_box.get() not in flat_uninstalled_dict.keys():
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Uinstalling... {flatpak_uninst_combo_box.get()}"
                global pigro_skript
                pigro_skript = f"flatpak uninstall flathub {flat_uninstalled_dict[un_var_material.get()]} -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        flatpak_uninst_combo_box = ttk.Combobox(
            self.flatpak_inst_frame,
            values=list(flat_uninstalled_dict.keys()),
            justify="left",
            textvariable=un_var_material,
        )
        flatpak_uninst_combo_box.bind("<KeyRelease>", check_input_flatpak_un)
        flatpak_uninst_combo_box.config(width=25)

        def flatpak_uninst_combo_box_pop_in_kontext_menu(event):
            flatpak_un_kontext_menu.tk_popup(event.x_root, event.y_root)

        def flatpak_uninst_combo_box_paste():
            flatpak_uninst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        flatpak_un_kontext_menu = Menu(
            flatpak_uninst_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        flatpak_un_kontext_menu.add_command(
            label="Paste", command=flatpak_uninst_combo_box_paste
        )

        # Make the in_kontext_menu pop up
        flatpak_uninst_combo_box.bind(
            "<Button - 3>", flatpak_uninst_combo_box_pop_in_kontext_menu
        )

        flatpak_inst_btn = Button(
            self.flatpak_inst_frame,
            text="remove",
            command=flat_uninstall,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        flatpak_uninst_combo_box.grid(column=3, row=0)
        flatpak_inst_btn.grid(column=2, row=0, padx=5)

        if flatpak_path == True:
            flatpak_uninst_combo_box.set("Select/Search a package -->")

        if flatpak_path == False:
            flatpak_inst_btn.config(state=DISABLED)
            flatpak_uninst_combo_box.set("Flatpak is not installed")
            notebook.tab(2,state=DISABLED)
        info_frame_flat = LabelFrame(
            flat_frame,
            text="Package Information",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=20,
        )
        info_frame_flat["background"] = frame_color
        info_frame_flat.pack(fill=BOTH, expand=True, padx=55, pady=20)

        T_flatpak = Text(
            info_frame_flat,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
        )
        T_flatpak.pack(fill=BOTH, expand=True)

        quote_flat = "Infos currently disabled"
        T_flatpak.delete("1.0", "end")
        T_flatpak.insert(END, quote_flat)
        

        # snap_entry
        self.snap_inst_frame = LabelFrame(
            snap_frame,
            text="Snap",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            padx=25,
            pady=20,
        )
        self.snap_inst_frame.pack(pady=20)
        self.snap_inst_frame["background"] = frame_color

        def error_mass_0():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_mass_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()
            error_y2.config(text="Not in the list! Check for misspell.")

        def snap_install():
            if snap_inst_combo_box.get() == "":

                error_mass_0()
            elif snap_inst_combo_box.get() not in content:
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Installing... {snap_inst_combo_box.get()}"
                global pigro_skript
                pigro_skript = f"snap install {snap_inst_combo_box.get()} -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        global snap_inst_combo_box
        snap_inst_combo_box = Entry(self.snap_inst_frame)
        snap_inst_combo_box.config(width=26)

        def snap_inst_combo_box_pop_in_kontext_menu(event):
            snap_in_kontext_menu.tk_popup(event.x_root, event.y_root)

        def snap_inst_combo_box_paste():
            snap_inst_combo_box.event_generate("<<Paste>>")

        # Right Click in_kontext_menu
        snap_in_kontext_menu = Menu(
            snap_inst_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        snap_in_kontext_menu.add_command(
            label="Paste", command=snap_inst_combo_box_paste
        )

        # Make the in_kontext_menu pop up
        snap_inst_combo_box.bind(
            "<Button - 3>", snap_inst_combo_box_pop_in_kontext_menu
        )

        self.snap_inst_btn = Button(
            self.snap_inst_frame,
            text="install",
            command=snap_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        self.snap_info_btn = Button(
            self.snap_inst_frame,
            text="Info",
            command=snap_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
            state=DISABLED,
        )

        snap_inst_combo_box.grid(column=1, row=0)
        self.snap_inst_btn.grid(column=0, row=0, pady=10, padx=5)
        self.snap_info_btn.grid(column=0, row=1, padx=5)

        def un_snap_install():
            if snap_un_combo_box.get() == "":
                error_mass_0()
            elif snap_un_combo_box.get() not in un_content:
                error_mass_1()
            else:
                global pigro_skript_name
                pigro_skript_name = f"Uninstalling... {snap_un_combo_box.get()}"
                global pigro_skript
                pigro_skript = f"snap install {snap_un_combo_box.get()} -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        global snap_un_combo_box
        snap_un_combo_box = Entry(self.snap_inst_frame)
        snap_un_combo_box.config(width=26)

        self.un_snap_inst_btn = Button(
            self.snap_inst_frame,
            text="remove",
            command=un_snap_install,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "10"),
            width=10,
        )

        snap_un_combo_box.grid(column=3, row=0)
        self.un_snap_inst_btn.grid(column=2, row=0, padx=5)

        if snap_deamon_check is True:
            snap_inst_combo_box.insert(0, "Enter a package -->")
            snap_un_combo_box.insert(0, "Enter a package -->")
            self.un_snap_inst_btn.config(state=NORMAL)
            self.snap_inst_btn.config(state=NORMAL)
        else:
            snap_inst_combo_box.insert(0, "Snap is not installed")
            snap_un_combo_box.insert(0, "Snap is not installed")
            self.un_snap_inst_btn.config(state=DISABLED)
            self.snap_inst_btn.config(state=DISABLED)
            notebook.tab(3,state=DISABLED)

        def snap_un_combo_box_pop_kontext_menu(event):
            snap_un_kontext_menu.tk_popup(event.x_root, event.y_root)

        def snap_un_combo_box_paste():
            snap_un_combo_box.event_generate("<<Paste>>")

        # Right Click kontext_menu
        snap_un_kontext_menu = Menu(
            snap_un_combo_box, tearoff=0, bg="white", fg="black"
        )
        # options
        snap_un_kontext_menu.add_command(label="Paste", command=snap_un_combo_box_paste)

        # Make the kontext_menu pop up
        snap_un_combo_box.bind("<Button - 3>", snap_un_combo_box_pop_kontext_menu)

        info_frame_snap = LabelFrame(
            snap_frame,
            text="Package Information",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=20,
        )
        info_frame_snap["background"] = frame_color
        info_frame_snap.pack(fill=BOTH, expand=True, padx=55, pady=20)

        T_snap = Text(
            info_frame_snap,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
        )
        T_snap.pack(fill=BOTH, expand=True)

        quote_snap = "Infos currently disabled"
        T_snap.delete("1.0", "end")
        T_snap.insert(END, quote_snap)

        
        self.repo_sec_frame = LabelFrame(
            repo_frame,
            text="From The Repository",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            padx=40,
            pady=10,
        )
        self.repo_sec_frame["background"] = frame_color
        self.repo_sec_frame.pack(
            pady=20,
        )

        def instant_install(text):
            if text == "Neofetch":
                global pigro_skript_name
                pigro_skript_name = "Installing... Neofetch"
                global pigro_skript
                pigro_skript = f"{legit} apt install neofetch -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Gimp":
                pigro_skript_name = "Installing... Gimp"
                pigro_skript = f"{legit} apt install gimp -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Audacity":
                pigro_skript_name = "Installing... Audacity"
                pigro_skript = f"{legit} apt install audacity -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Kodi":
                pigro_skript_name = "Installing... Kodi"
                pigro_skript = f"{legit} apt install kodi -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Rhythmbox":
                pigro_skript_name = "Installing... Rhythmbox"
                pigro_skript = f"{legit} apt install rhythmbox -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Tilix":
                pigro_skript_name = "Installing... Tilix"
                pigro_skript = f"{legit} apt install tilix -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Guake":
                pigro_skript_name = "Installing... Guake"
                pigro_skript = f"{legit} apt install guake -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Supertux":
                pigro_skript_name = "Installing... Supertux"
                pigro_skript = f"{legit} apt install supertux -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "SupertuxKart":
                pigro_skript_name = "Installing... SupertuxKart"
                pigro_skript = f"{legit} apt install supertuxkart -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Kapman":
                pigro_skript_name = "Installing... Kapman"
                pigro_skript = f"{legit} apt install kapman -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Transmission":
                pigro_skript_name = "Installing... Transmission"
                pigro_skript = f"{legit} apt install transmission -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Thunderbird":
                pigro_skript_name = "Installing... Thunderbird"
                pigro_skript = f"{legit} apt install thunderbird -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Visual Studio Code":
                pigro_skript_name = "Installing... Visual Studio Code"
                pigro_skript = f"{legit} apt install code -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Libre Office":
                pigro_skript_name = "Installing... Libre Office"
                pigro_skript = f"{legit} apt install libreoffice -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Synaptic":
                pigro_skript_name = "Installing... Synaptic"
                pigro_skript = f"{legit} apt install synaptic -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Gnome Software":
                pigro_skript_name = "Installing... Gnome Software"
                pigro_skript = f"{legit} apt install gnome-software -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()



            if text == "Bleach Bit":
                # global pigro_skript_name
                pigro_skript_name = "Installing... bleachbit"
                # global pigro_skript
                pigro_skript = f"{legit} apt install bleachbit -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "BPYTop":
                # global pigro_skript_name
                pigro_skript_name = "Installing... bpytop"
                # global pigro_skript
                pigro_skript = f"{legit} apt install bpytop -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Compiz":
                # global pigro_skript_name
                pigro_skript_name = "Installing... compiz"
                # global pigro_skript
                pigro_skript = f"{legit} apt install compiz -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Gnome-Pie":
                # global pigro_skript_name
                pigro_skript_name = "Installing... gnome-pie"
                # global pigro_skript
                pigro_skript = f"{legit} apt install gnome-pie -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "GParted":
                # global pigro_skript_name
                pigro_skript_name = "Installing... gparted"
                # global pigro_skript
                pigro_skript = f"{legit} apt install gparted -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Pi Imager":
                # global pigro_skript_name
                pigro_skript_name = "Installing... rpi-imager"
                # global pigro_skript
                pigro_skript = f"{legit} apt install rpi-imager -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Plank":
                # global pigro_skript_name
                pigro_skript_name = "Installing... plank"
                # global pigro_skript
                pigro_skript = f"{legit} apt install plank -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if text == "Xfce4 Screenshooter":
                # global pigro_skript_name
                pigro_skript_name = "Installing... xfce4-screenshooter"
                # global pigro_skript
                pigro_skript = f"{legit} apt install xfce4-screenshooter -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        self.deb_icon = PhotoImage(file=r"images/icons/pigro_icons/deb_s.png")

        instant_install_btn_list = [
            "Audacity",
            "Bleach Bit",
            "BPYTop",
            "Compiz",
            "Gimp",
            "Gnome-Pie",
            "GParted",
            "Guake",
            "Kapman",
            "Kodi",
            "Libre Office",
            "Neofetch",
            "Pi Imager",
            "Plank",
            "Rhythmbox",
            "Supertux",
            "Supertuxkart",
            "Synaptic",
            "Thunderbird",
            "Tilix",
            "Transmission",
            "Visual Studio Code",
            "Xfce4 Screenshooter",
            "Gnome Software",
            
        ]

        instant_install_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for instant_install_btn in instant_install_btn_list:
            self.instant_install_button_x = Button(
                self.repo_sec_frame,
                width=180,
                justify="left",
                anchor="w",
                compound="left",
                image=self.deb_icon,
                text=instant_install_btn,
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=main_font,
                command=lambda text=instant_install_btn: instant_install(text),
            )

            self.instant_install_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5
            )
            instant_install_btn_list1.append(self.instant_install_button_x)
            conf_column = conf_column + 1
            if conf_column == 3:
                conf_row = conf_row + 1
                conf_column = 0




class Git_More_Tab(ttk.Frame):
    def __init__(self, container):
        """lets you install apps via APT, snap, pi-apps and flatpak in one single window"""
        super().__init__()

        self.app_albert = PhotoImage(file=r"images/apps/app_albert.png")
        self.app_argon = PhotoImage(file=r"images/apps/app_argon.png")
        self.app_deskpi = PhotoImage(file=r"images/apps/app_deskpi.png")
        self.app_doom = PhotoImage(file=r"images/apps/app_doom.png")
        self.app_duke = PhotoImage(file=r"images/apps/app_duke.png")
        self.app_fan_s = PhotoImage(file=r"images/apps/app_fan_s.png")
        self.app_ferdium = PhotoImage(file=r"images/apps/app_ferdium.png")
        self.app_gnome_s = PhotoImage(file=r"images/apps/app_gnome_s.png")
        self.app_papirus = PhotoImage(file=r"images/apps/app_papirus.png")
        self.app_pi_apps = PhotoImage(file=r"images/apps/app_pi_apps.png")
        self.app_pi_kiss = PhotoImage(file=r"images/apps/app_pi_kiss.png")
        self.app_space_c = PhotoImage(file=r"images/apps/app_space_c.png")
        self.app_sub_m = PhotoImage(file=r"images/apps/app_sub_m.png")
        self.app_sub_t = PhotoImage(file=r"images/apps/app_sub_t.png")
        self.app_warpinator = PhotoImage(file=r"images/apps/app_warpinator.png")
        self.app_xpad = PhotoImage(file=r"images/apps/app_xpad.png")
        self.app_wine64 = PhotoImage(file=r"images/apps/app_wine64.png")
        self.place_holder = PhotoImage(file=r"images/apps/git_more_placeholder.png")
        self.app_icon = PhotoImage(file=r"images/icons/pigro_icons/terminal_s.png")

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def git_tab(text):

            if text == "Albert":
                self.appname_header.config(text="Albert")
                self.app_disc.config(
                    text="Desktop agnostic launcher\nAccess everything with virtually zero effort.\nRun applications, open files or their paths,\nopen bookmarks in your browser,\nsearch the web, calculate things and a lot more.\nDowload-Link:"
                )
                self.web_link.config(
                    text=r"https://software.opensuse.org/download.html?project=home:manuelschneid3r&package=albert"
                )
                self.app_pic.config(image=self.app_albert)
                self.app_inst.forget()
            if text == "Argon One Driver":
                self.appname_header.config(text="Argon One/M.2 Case Driver")
                self.app_disc.config(text="Driver for the Argon One Case\n\n\n\n\n")
                self.web_link.config(
                    text=r"https://www.waveshare.com/wiki/PI4-CASE-ARGON-ONE"
                )
                self.app_pic.config(image=self.app_argon)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end", "curl https://download.argon40.com/argon1.sh | bash"
                )
                self.app_pic.config(text="Argon")
            if text == "DeskPi Pro Driver":
                self.appname_header.config(text="DeskPi Pro Driver")
                self.app_disc.config(
                    text="Driver & Fan Control for the DeskPi Pro Case\n\n\n\n\n"
                )
                self.web_link.config(text=r"https://github.com/DeskPi-Team/deskpi")
                self.app_pic.config(image=self.app_deskpi)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "cd ~\ngit clone https://github.com/DeskPi-Team/deskpi.git\ncd ~/deskpi/\nchmod +x install.sh\nsudo ./install.sh\n\n#Pi OS 64 Bit\nchmod +x install-raspios-64bit.sh\nsudo ./install-raspios-64bit.sh",
                )
            if text == "FanShim Driver":
                self.appname_header.config(text="Fan Shim Driver")
                self.app_disc.config(text="Driver for the Pimoroni FanShim\n\n\n\n\n")
                self.web_link.config(
                    text=r"https://learn.pimoroni.com/article/getting-started-with-fan-shim"
                )
                self.app_pic.config(image=self.app_fan_s)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "git clone https://github.com/pimoroni/fanshim-python\ncd fanshim-python\nsudo ./install.sh",
                )
            if text == "Papirus Icon Theme":
                self.appname_header.config(text="Papirus Icon Theme/Folders")
                self.app_disc.config(
                    text="The popular icon theme plus the ability to change the order color\n\n\n\n\n"
                )
                self.web_link.config(
                    text=r"https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
                )
                self.app_pic.config(image=self.app_papirus)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "Icon Theme:\nwget -qO- https://git.io/papirus-icon-theme-install | sh\n\nFolder Theme:\nwget -qO- https://git.io/papirus-folders-install | sh\n\nHow To:\nSelect the papirus icon theme then:\npapirus-folders -C brown --theme Papirus-Dark\n\nColors:\nadwaita,black,bluegrey,breeze,brown,carminecyan,darkcyan,\ndeeporange,green,grey,indigo,magenta,nordic,orange,palebrown,\npaleorange,pink,red,teal,violet,white,yaru,yellow",
                )
                self.app_pic.config(image=self.app_papirus)
            if text == "Pi-Apps":
                self.appname_header.config(text="Pi-Apps")
                self.app_disc.config(
                    text="The go to apps store when it comes to\nprograms that are not in repository.\n\n\n\n"
                )
                self.web_link.config(text=r"https://pi-apps.io/")
                self.app_pic.config(image=self.app_pi_apps)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash",
                )
            if text == "PiKiss":
                self.appname_header.config(text="piKiss")
                self.app_disc.config(
                    text="System Tweak Tool & Game Installer for ARM/Raspberry Pi\n\n\n\n\n"
                )
                self.web_link.config(text=r"https://github.com/jmcerrejon/PiKISS")
                self.app_pic.config(image=self.app_pi_kiss)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "curl -sSL https://git.io/JfAPE | bash",
                )
            if text == "Sublime Merge aarch64":
                self.appname_header.config(text="Sublime Merge aarch64")
                self.app_disc.config(text="Great Git GUI\n\n\n\n\n")
                self.web_link.config(text=r"https://www.sublimemerge.com/")
                self.app_pic.config(image=self.app_sub_m)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -\n\nsudo apt-get install apt-transport-https\n\necho "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list\n\nsudo apt-get update\nsudo apt-get install sublime-merge -y\n""",
                )
            if text == "Sublime Text aarch64":
                self.appname_header.config(text="Sublime Text aarch64")
                self.app_disc.config(text="Very good Text Editor\n\n\n\n\n")
                self.web_link.config(text=r"https://www.sublimetext.com/")
                self.app_inst.pack(anchor="w", pady=10)
                self.app_pic.config(image=self.app_sub_t)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -\n\nsudo apt-get install apt-transport-https\n\necho "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list\n\nsudo apt-get update\nsudo apt-get install sublime-text -y\n""",
                )
            if text == "Xpad-Neo":
                self.appname_header.config(text="Xpad Neo")
                self.app_disc.config(
                    text="Advanced Linux Driver for\nXbox Wireless Gamepad\nAdds FULL support for all Xbox controlers\n\n\n"
                )
                self.web_link.config(text=r"https://github.com/atar-axis/xpadneo")
                self.app_pic.config(image=self.app_xpad)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    "sudo apt-get install dkms raspberrypi-kernel-headers\n\ngit clone https://github.com/atar-axis/xpadneo.git\n\ncd xpadneo\n\nsudo ./install.sh",
                )
            if text == "Ferdium":
                self.appname_header.config(text="Ferdium arm64/armv7l")
                self.app_disc.config(
                    text="All your services in one place\nbuilt by the community\n\n\n\n"
                )
                self.web_link.config(text=r"https://ferdium.org/")
                self.app_pic.config(image=self.app_ferdium)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """Download: https://ferdium.org/download\n\nsudo dpkg -i Ferdium-linux-X.X.X-amdX.deb""",
                )
            if text == "eDuke32":
                self.appname_header.config(text="eDuke32 Flathub")
                self.app_disc.config(text="A Duke Nukem 3D Source Port\n\n\n\n\n")
                self.web_link.config(
                    text=r"https://flathub.org/apps/details/com.eduke32.EDuke32"
                )
                self.app_pic.config(image=self.app_duke)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """# Flatpak support needed!\nflatpak install flathub com.eduke32.EDuke32\n\n# [DUKE3D.GRP IS NOT INCLUDED]\n\ncp /path/to/duke3d.grp  ~/.var/app/com.eduke32.EDuke32/.config/eduke32\n# [PLAY!]""",
                )

            if text == "GZDoom":
                self.appname_header.config(text="GZDoom 3.4.1_armhf")
                self.app_disc.config(text="A Doom Source Port\n\n\n\n\n")
                self.web_link.config(text=r"https://zdoom.org/index")
                self.app_pic.config(image=self.app_doom)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """wget https://zdoom.org/files/gzdoom/bin/gzdoom_3.4.1_armhf.deb\n\nsudo dpkg -i gzdoom_3.4.1_armhf.deb\n# Put .WAD Files in ~/.config/gzdoom/""",
                )

            if text == "Space Cadet Pinball":
                self.appname_header.config(text="Space Cadet Pinball (WinXP)")
                self.app_disc.config(
                    text="Reverse engineering of 3D Pinball\nfor Windows - Space Cadet,\na game bundled with Windows.\n\n\n"
                )
                self.app_pic.config(image=self.app_space_c)
                self.web_link.config(
                    text=r"https://github.com/k4zmu2a/SpaceCadetPinball"
                )
                self.app_pic.config(image=self.app_space_c)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """# Flatpak support needed!\n\nflatpak install flathub com.github.k4zmu2a.spacecadetpinball""",
                )

            if text == "Gnome-Software + Flatpak":
                self.appname_header.config(text="Gnome-Software + Flatpak Support")
                self.app_disc.config(
                    text="The popular package manager GUI + Flatpak Plugin\n\n\n\n\n"
                )
                self.web_link.config(
                    text=r"https://gitlab.gnome.org/GNOME/gnome-software"
                )
                self.app_pic.config(image=self.app_gnome_s)
                self.app_inst.pack(anchor="w", pady=10)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """sudo apt install gnome-software\n\nsudo apt install flatpak\n\nflatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo\n\nsudo apt install gnome-software-plugin-flatpak\nreboot""",
                )

            if text == "Warpinator":
                self.appname_header.config(text="Warpinator (Flathub)")
                self.app_disc.config(
                    text="Linux Mints awesome data transfer tool\n\n\n\n\n"
                )
                self.web_link.config(
                    text=r"https://flathub.org/apps/details/org.x.Warpinator"
                )
                self.app_inst.pack(anchor="w", pady=10)
                self.app_pic.config(image=self.app_warpinator)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """flatpak install flathub org.x.Warpinator""",
                )
            if text == "Wine64":
                self.appname_header.config(text="Box64 + Box86 + Wine64")
                self.app_disc.config(
                    text="A tutorial how to use Wine on arm64\nRequires Pi Apps!\n\n\n"
                )
                self.web_link.config(
                    text=r"https://www.playonlinux.com/wine/binaries/phoenicis/upstream-linux-amd64/"
                )
                self.app_inst.pack(anchor="w", pady=10)
                self.app_pic.config(image=self.app_wine64)
                self.app_inst.delete("1.0", END)
                self.app_inst.insert(
                    "end",
                    """~/pi-apps/manage install Box64\n\n~/pi-apps/manage install Box86\n\ncd ~\n\nmkdir wine64\n\ncd wine64\n\nwget https://www.playonlinux.com/wine/binaries/phoenicis/upstream-linux-amd64/PlayOnLinux-wine-3.0.3-upstream-linux-amd64.tar.gz\n\ntar -xf PlayOnLinux-wine-3.0.3-upstream-linux-amd64.tar.gz\nrm PlayOnLinux-wine-3.0.3-upstream-linux-amd64.tar.gz\n\nsudo ln -s /home/USER/wine64/bin/wine64 /usr/local/bin/wine64\n\nTest: wine64 winecfg""",
                )

        self.link_main = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
        )
        self.link_main.pack(expand=True, fill=BOTH)
        self.link_main["background"] = maincolor

        self.link_left = Frame(
            self.link_main,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            padx=20,
            pady=20,
        )
        self.link_left.pack(side=LEFT, expand=True, fill=BOTH)
        self.link_left["background"] = maincolor

        sources_l = [
            "Albert",
            "Argon One Driver",
            "DeskPi Pro Driver",
            "eDuke32",
            "Ferdium",
            "FanShim Driver",
            "Gnome-Software + Flatpak",
            "GZDoom",
            "Papirus Icon Theme",
            "Pi-Apps",
            "PiKiss",
            "Space Cadet Pinball",
            "Sublime Merge aarch64",
            "Sublime Text aarch64",
            "Warpinator",
            "Wine64",
            "Xpad-Neo",
        ]

        sources_l1 = []

        for file in sources_l:
            self.choice_link2 = Button(
                self.link_left,
                image=self.app_icon,
                justify=LEFT,
                anchor=W,
                width=220,
                text=file,
                compound=LEFT,
                command=lambda text=file: git_tab(text),
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=main_font,
            ).pack(pady=5)
            sources_l1.append(self.choice_link2)

        # Right Frame
        self.link_right = Frame(
            self.link_main,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
            padx=10,
        )
        self.link_right.pack(side=LEFT, expand=True, fill=BOTH, padx=20)
        self.link_right["background"] = frame_color

        self.appname_header = Label(
            self.link_right,
            text=" ",
            width=50,
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_16,
            justify="left",
            anchor="w",
        )
        self.appname_header.pack(anchor="w", pady=10)

        self.app_disc = Label(
            self.link_right,
            justify="left",
            text=" ",
            width=50,
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            anchor="w",
        )
        self.app_disc.pack(anchor="w")

        self.web_link = tk.Label(
            self.link_right,
            text=r" ",
            width=50,
            background=frame_color,
            foreground="blue",
            cursor="hand2",
            anchor="w",
        )
        self.web_link.pack(anchor="w", pady=10)
        self.web_link.bind("<Button-1>", callback)

        self.app_pic = Label(
            self.link_right,
            justify="left",
            text=" ",
            image=self.place_holder,
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            anchor="w",
        )
        self.app_pic.pack(anchor="w")

        self.app_inst = Text(self.link_right, width=90, height=20, borderwidth=0)

        def app_inst_pop_in_kontext_menu(event):
            in_kontext_menu.tk_popup(event.x_root, event.y_root)

        def app_inst_copy():
            self.app_inst.event_generate("<<Copy>>")

        # Right Click in_kontext_menu
        in_kontext_menu = Menu(self.app_inst, tearoff=0, bg="white", fg="black")
        # options
        in_kontext_menu.add_command(label="Copy", command=app_inst_copy)

        # Make the in_kontext_menu pop up
        self.app_inst.bind("<Button - 3>", app_inst_pop_in_kontext_menu)


class Look_Tab(ttk.Frame):
    """a tool collection to customize the debian desktop"""

    def __init__(self, container):
        super().__init__()

        def done_1():
            d_msg1 = Done_Restart_P(self)
            d_msg1.grab_set()

        def perm_selected():
            if perm_select_clicked.get() == "passwordless (RPiOS ONLY!)":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("perm = true", "perm = false")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                done_1()

            if perm_select_clicked.get() == "pkexec (default)":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("perm = false", "perm = true")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                done_1()

        def color_selected():
            if select_clicked.get() == "Light Theme":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("theme = dark", "theme = light")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                done_1()

            if select_clicked.get() == "Dark Theme":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("theme = light", "theme = dark")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                done_1()

        # Images/Icons

        self.bash_history_icon = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )
        self.ico_m = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )
        self.bp03 = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.ico_m2 = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-webapps.png"
        )
        self.ip01 = PhotoImage(file=r"images/icons/pigro_icons/download_ico.png")

        self.bluetooth = PhotoImage(file=r"images/icons/papirus/48x48/blueman.png")
        self.wifi = PhotoImage(
            file=r"images/icons/papirus/48x48/kali-wireless-attacks-trans.png"
        )

        def gui_settings(text):
            if text == "Tasksel":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} tasksel; exec bash\"'"
                )
            if text == "Change Desktop":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} update-alternatives --config x-session-manager; exec bash\"'"
                )
            if text == "Change Win-Manager":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} update-alternatives --config x-window-manager; exec bash\"'"
                )
            if text == "Theme Folder":
                theme_f_ext = os.path.isdir(f"{home}/.themes")
                if theme_f_ext == True:
                    print("[Info]: /.themes found")
                if theme_f_ext == False:
                    print("[Info]: /.themes not found will created")
                    os.mkdir(f"{home}/.themes")
                if get_de == "XFCE":
                    popen("sudo thunar /usr/share/themes/")
                else:
                    popen("sudo pcmanfm /usr/share/themes/")
            if text == "Icon Folder":
                icon_f_ext = os.path.isdir(f"{home}/.icons")
                if icon_f_ext == True:
                    print("[Info]: /.icons found")
                if icon_f_ext == False:
                    print("[Info]: /.icons not found will created")
                    os.mkdir(f"{home}/.icons")
                if get_de == "XFCE":
                    popen(f"sudo thunar {home}/.icons")
                else:
                    popen(f"sudo pcmanfm {home}/.icons")

        self.gui_set = LabelFrame(
            self,
            text="GUI Tweaks",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.gui_set.pack(pady=20, padx=40, fill="both")  #
        self.gui_set["background"] = frame_color

        gui_settings_btn_list = [
            "Tasksel",
            "Change Desktop",
            "Change Win-Manager",
            "Theme Folder",
            "Icon Folder",
        ]

        gui_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for gui_settings_btn in gui_settings_btn_list:
            self.gui_button_x = Button(
                self.gui_set,
                width=140,
                height=100,
                text=gui_settings_btn,
                command=lambda text=gui_settings_btn: gui_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.gui_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)

            gui_settings_btn_list1.append(self.gui_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if gui_settings_btn == "Tasksel":
                self.gui_button_x.config(image=self.bash_history_icon)
            if gui_settings_btn == "Change Desktop":
                self.gui_button_x.config(image=self.bash_history_icon)
            if gui_settings_btn == "Change Win-Manager":
                self.gui_button_x.config(image=self.bash_history_icon)
            if gui_settings_btn == "Theme Folder":
                self.gui_button_x.config(image=self.fm_godmode_icon)
            if gui_settings_btn == "Icon Folder":
                self.gui_button_x.config(image=self.fm_godmode_icon)

        # xfce_tweaks

        x_lan_fix = """"#!/bin/bash
sudo apt install network-manager-gnome -y
sudo systemctl disable dhcpcd
sudo /etc/init.d/dhcpcd stop
exit
"""

        x_blue_fix = """apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware -y && exit"""

        def xfce4_settings(text):
            if text == "Xfwm4 Settings":
                popen("xfwm4-settings")
            if text == "Xfce4 Appearance":
                popen("xfce4-appearance-settings")
            if text == "Bluetooth Fix":
                global pigro_skript_name
                pigro_skript_name = "Bluetooth Fix"
                global pigro_skript
                pigro_skript = x_blue_fix
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()
            if text == "WiFi Fix":
                pigro_skript_name = "Lan/WiFi Fix"
                pigro_skript = x_lan_fix
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        self.xfce4_set = LabelFrame(
            self,
            text="Xfce Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.xfce4_set.pack(pady=20, padx=40, fill="both")  #
        self.xfce4_set["background"] = frame_color

        xfce4_settings_btn_list = [
            "Xfwm4 Settings",
            "Xfce4 Appearance",
            "WiFi Fix",
            "Bluetooth Fix",
        ]

        xfce4_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for xfce4_settings_btn in xfce4_settings_btn_list:
            self.xfce4_button_x = Button(
                self.xfce4_set,
                width=140,
                height=100,
                text=xfce4_settings_btn,
                command=lambda text=xfce4_settings_btn: xfce4_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.xfce4_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            self.xfce4_button_x.configure(state=DISABLED)
            xfce4_settings_btn_list1.append(self.xfce4_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if get_de == "XFCE":
                self.xfce4_button_x.configure(state=NORMAL)
            if xfce4_settings_btn == "Xfwm4 Settings":
                self.xfce4_button_x.config(image=self.ico_m)
            if xfce4_settings_btn == "Xfce4 Appearance":
                self.xfce4_button_x.config(image=self.ico_m)
            if xfce4_settings_btn == "WiFi Fix":
                self.xfce4_button_x.config(image=self.wifi)
            if xfce4_settings_btn == "Bluetooth Fix":
                self.xfce4_button_x.config(image=self.bluetooth)

        def pixel_settings(text):
            if text == "LXAppearance":
                popen("lxappearance")
            if text == "OpenBox Conf":
                popen("obconf")

            if text == "Pi Appeariance":
                popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")
            if text == "Set Wallpaper":
                global my_image
                self.filename = filedialog.askopenfilename(
                    initialdir="~",
                    title="Select A File",
                    filetypes=(
                        ("jpeg files", "*.jpeg"),
                        ("jpg files", "*.jpg"),
                        ("png files", "*.png"),
                        ("all files", "*.*"),
                    ),
                )
                os.popen(f"pcmanfm --set-wallpaper {self.filename}")

            if text == "Backup Panel\nSettings":
                popen("mv ~/.config/lxpanel lxpanel.bak")

            if text == "Restore\nDefault Panel":
                popen(
                    f"cp /etc/xdg/lxpanel/LXDE-pi/panels/panel {home}/.config/lxpanel/LXDE-pi/panels/panel && lxpanelctl restart"
                )
            if text == "Restart\nPanel":
                popen("lxpanelctl restart")

        self.pixel_set = LabelFrame(
            self,
            text="Pixel Tweaks",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.pixel_set.pack(pady=20, padx=40, fill="both")  #
        self.pixel_set["background"] = frame_color

        pixel_settings_btn_list = [
            "LXAppearance",
            "OpenBox Conf",
            "Pi Appeariance",
            "Set Wallpaper",
            "Backup Panel\nSettings",
            "Restore\nDefault Panel",
            "Restart\nPanel",
        ]

        pixel_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for pixel_settings_btn in pixel_settings_btn_list:
            self.pixel_button_x = Button(
                self.pixel_set,
                width=140,
                height=100,
                text=pixel_settings_btn,
                command=lambda text=pixel_settings_btn: pixel_settings(text),
                highlightthickness=0,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.pixel_button_x.grid(row=conf_row, column=conf_column, padx=5, pady=5)
            pixel_settings_btn_list1.append(self.pixel_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0
            if pixel_settings_btn == "LXAppearance":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "OpenBox Conf":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "Pi Appeariance":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "Set Wallpaper":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "Backup Panel\nSettings":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "Restore\nDefault Panel":
                self.pixel_button_x.config(image=self.ico_m)
            if pixel_settings_btn == "Restart\nPanel":
                self.pixel_button_x.config(image=self.ico_m)

        if distro_get == "ubuntu":

            self.pixel_set.forget()
            self.xfce4_set.forget()

        # pigrotweaks
        self.rahmen43 = LabelFrame(
            self,
            text="Pigro Tweaks",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=FLAT,
            pady=10,
            padx=15,
        )
        self.rahmen43.pack(padx=40, pady=20, fill="both")
        self.rahmen43["background"] = frame_color

        # Theme Selction Dropdown Menu
        theme_select_frame = Frame(
            self.rahmen43, highlightthickness=0, borderwidth=0, background=maincolor
        )
        theme_select_frame.grid(row=0, column=0)
        options = [
            "Dark Theme",
            "Light Theme",
        ]
        global select_clicked
        select_clicked = StringVar()
        select_clicked.set("Select Theme")
        drop_th = OptionMenu(
            theme_select_frame,
            select_clicked,
            *options,
        )
        drop_th.grid(column=0, row=0)
        drop_th.config(
            bg=frame_color,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
            width=15,
        )
        drop_th["menu"].config(
            bg=maincolor,
            fg=main_font,
            activebackground=frame_color,
            activeforeground=main_font,
        )

        drop_th["highlightbackground"] = maincolor
        drop_th["relief"] = "flat"

        select_theme_btn = Button(
            theme_select_frame,
            text="Select",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_12,
            command=color_selected,
        )
        select_theme_btn.grid(column=1, row=0)

        # Permission Selction Dropdown Menu
        permission_select_frame = Frame(
            self.rahmen43, highlightthickness=0, borderwidth=0, background=maincolor
        )
        permission_select_frame.grid(row=0, column=2)
        options = [
            "passwordless (RPiOS ONLY!)",
            "pkexec (default)",
        ]
        global perm_select_clicked
        perm_select_clicked = StringVar()
        perm_select_clicked.set("Select permission")
        drop_p = OptionMenu(
            permission_select_frame,
            perm_select_clicked,
            *options,
        )
        drop_p.grid(column=0, row=0)
        drop_p.config(
            bg=frame_color,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
            width=20,
        )
        drop_p["menu"].config(
            bg=maincolor,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
        )

        drop_p["highlightbackground"] = maincolor
        drop_p["relief"] = "flat"

        perm_select_permission_btn = Button(
            permission_select_frame,
            text="Select",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_12,
            command=perm_selected,
        )
        perm_select_permission_btn.grid(column=1, row=0)


class Update_Pop(tk.Toplevel):
    """NOT IMPLEMENTED YET!"""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("PiGro Updater")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.config(bg=maincolor)

        def pigro_github_update():
            popen(
                f"x-terminal-emulator -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash; exec bash\"'"
            )
            app.quit()

        def pigro_piapps_update():
            popen(
                f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage update PiGro; exec bash\"'"
            )
            app.quit()

        self.auto_start = PhotoImage(file=r"images/icons/logo1.png")

        self.actn_shn = Label(
            self,
            image=self.auto_start,
            background=maincolor,
        ).pack(pady=20)

        GLabel_0 = tk.Label(self)
        GLabel_0["font"] = font_14
        GLabel_0["bg"] = maincolor
        GLabel_0["fg"] = main_font
        GLabel_0["text"] = "An Update For PiGro - Just Click It!\nIs Available."
        GLabel_0.pack(pady=20)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = ext_btn
        GButton_883["width"] = 20
        GButton_883["highlightthickness"] = 0
        GButton_883["borderwidth"] = 0
        GButton_883["font"] = font_10
        GButton_883["fg"] = main_font
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Github Update"
        GButton_883.pack(pady=10)
        GButton_883["command"] = pigro_github_update

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = ext_btn
        GButton_585["width"] = 20
        GButton_585["highlightthickness"] = 0
        GButton_585["borderwidth"] = 0
        GButton_585["font"] = font_10
        GButton_585["fg"] = main_font
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Pi-Apps Update"
        GButton_585.pack()
        GButton_585["command"] = pigro_piapps_update

        PATH = f"/home/{user}/pi-apps/data/status/PiGro"

        if os.path.isfile(PATH) is True:
            pigro_via_pi_apps = open(f"/home/{user}/pi-apps/data/status/PiGro", "r")
            install_status = pigro_via_pi_apps.read()
            pigro_via_pi_apps.close()
            if install_status.strip() == "installed":
                GButton_883.forget()

        else:
            GButton_585.forget()


class Z_Ram_Pop(tk.Toplevel):
    """child window that lets one install zram"""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 280
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.ip03 = PhotoImage(file=r"images/icons/pigro_icons/download_ico.png")

        def z_ram_install():

            if distro_get == "ubuntu":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} apt install zram-config ; exec bash\"'"
                )
            else:
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} apt install zram-tools; exec bash\"'"
                )

            Notification(
                title="ZRAMr\n",
                description="ZRAM has been installed",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        def z_ram_uninstall():

            if distro_get == "ubuntu":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} apt remove zram-config ; exec bash\"'"
                )
            else:
                popen(
                    f"x-terminal-emulator -e 'bash -c \"{legit} apt remove zram-tools; exec bash\"'"
                )

            Notification(
                title="ZRAMr\n",
                description="ZRAM has been uninstalled",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        GLabel_804 = tk.Label(self)
        GLabel_804["font"] = font_10
        GLabel_804["fg"] = maincolor
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.ip03
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(self)
        GLabel_0["font"] = font_14
        GLabel_0["fg"] = maincolor
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "ZRAM"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(self)
        GLabel_29["font"] = font_10
        GLabel_29["fg"] = maincolor
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Zram is a Linux kernel module that allows\nyou to set up compressed filesystems in RAM.\nzram-tools uses this module to set up compressed \nswap space.\nThis is useful on systems with low memory or servers\nrunning a large amount of services with data that's\neasily swappable but that you may wish to swap back\nfast without sacrificing disk bandwidth.\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = "#efefef"
        GButton_883["font"] = font_10
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = z_ram_install

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#efefef"
        GButton_585["font"] = font_10
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = z_ram_uninstall


class Tuning_Tab(ttk.Frame):
    """tool to edit profomance relevant options in config.txt/displays these settings"""

    def __init__(self, container):
        super().__init__()

        # Current OV settings
        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def tuning_legende():
            tu_le = Tuning_Legende(self)
            tu_le.grab_set()

        def z_ram():
            z_ram = Z_Ram_Pop(self)
            z_ram.grab_set()

        def expert_mode():
            x_mode = Overclocking_Expert(self)
            x_mode.grab_set()

        # BG + Icons
        self.rm_ov_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV_rm.png")
        self.ov1_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV1.png")
        self.ov2_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV2.png")
        self.ov3_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV3.png")
        self.ov4_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV4.png")
        self.ov5_icon = PhotoImage(file=r"images/icons/pigro_icons/PiGroOV5.png")
        self.ip03 = PhotoImage(file=r"images/icons/pigro_icons/download_ico.png")
        self.tu_legend_ico = PhotoImage(
            file=r"images/icons/papirus/48x48/io.otsaloma.nfoview.png"
        )
        self.zram_icon = PhotoImage(file=r"images/icons/papirus/48x48/device_mem.png")

        # OV Notifications

        def done_msg():
            d_msg = Done_Reboot(self)
            d_msg.grab_set()

        # overclocking_default/reset

        def set_default():
            os.system(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{legit} {Application_path}/scripts/rm_ov.sh && exit ; exec bash"'
                % wid
            )
            done_msg()
            tu_btn1.config(state=NORMAL)
            tu_btn2.config(state=NORMAL)
            tu_btn3.config(state=NORMAL)
            tu_btn4.config(state=NORMAL)

            pigro_t_display.config(text="not nonfigured", foreground="green")
            arm_f_display.config(text="not configured")
            gpu_f_display.config(text="not configured")
            gpu_m_display.config(text="not configured")
            over_v_display.config(text="not configured")
            force_t_display.config(text="not configured")
            dash_arm_f_display.config(text="Arm Freq: not configured")
            dash_gpu_f_display.config(text="Gpu Freq: not configured")
            dash_gpu_m_display.config(text="Gpu Mem: not configured")
            dash_over_v_display.config(text="Over Voltage: not configured")
            dash_force_t_display.config(text="Force Turbo: not configured")

            Notification(
                title="PiGro Overclocking\n",
                description="All Settings Restored\n\n",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # overclocking_2000

        def ov_2000():
            os.system(
                f"""xterm -into %d -bg Grey11 -geometry 1000x25 -e {legit} sh -c 'echo "#Pigro_Overclocking1\narm_freq=2000\ngpu_freq=750\nover_voltage=6\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
                % wid
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2000\ngpu_fequ = 750\nover_voltage = 6\nforce_turbo = 1",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # overclocking_2147
        def ov_2147():
            os.system(
                f"""xterm -into %d -bg Grey11 -geometry 1000x25 -e {legit} sh -c 'echo "#Pigro_Overclocking2\narm_freq=2147\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
                % wid
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2147\ngpu_fequ = 750\nover_voltage = 8\nforce_turbo = 1",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # overclocking_2200

        def ov_2200():
            os.system(
                f"""xterm -into %d -bg Grey11 -geometry 1000x25 -e {legit} sh -c 'echo "#Pigro_Overclocking3\narm_freq=2200\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
                % wid
            )

            done_msg()
            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2200\ngpu_fequ = 750\nover_voltage = 8\force_turbo = 1",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        # overclocking_2300
        def ov_2300():
            os.system(
                f"""xterm -into %d -bg Grey11 -geometry 1000x25 -e {legit} sh -c 'echo "#Pigro_Overclocking4\narm_freq=2300\ngpu_freq=750\nover_voltage=14\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
                % wid
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2300\ngpu_fequ = 750\nover_voltage = 14\nforce_turbo = 1",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # OV_Button_Frame
        self.ov_buttons = LabelFrame(
            self,
            text="Tuning Options",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
            padx=40,
        )
        self.ov_buttons.pack(side=LEFT, pady=20, padx=20, fill=BOTH)
        self.ov_buttons["background"] = maincolor

        # Overclocking State Main Frame
        self.ov_state_display_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.ov_state_display_frame.pack(
            anchor="n", padx=10, pady=20, fill=BOTH, expand=True
        )
        self.ov_state_display_frame["background"] = maincolor

        # Overclocking Values Frame
        self.ov_display_frame = LabelFrame(
            self.ov_state_display_frame,
            text="Current Settings",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=10,
            pady=10,
        )
        self.ov_display_frame.pack(anchor="n")
        self.ov_display_frame["background"] = frame_color

        # Additional Infos
        # +üpp

        self.ov_helps_frame = Frame(
            self.ov_state_display_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.ov_helps_frame.pack(padx=20)
        self.ov_helps_frame["background"] = maincolor

        # Overclocking Stats

        # Tuning_Button_Frame
        pigro_t_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="PiGro Berry: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        pigro_t_label.grid(column=0, row=0)

        global pigro_t_display
        pigro_t_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground="green",
            font=font_12,
            width=25,
        )
        pigro_t_display.grid(column=1, row=0)

        arm_f_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="Arm Freq: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        arm_f_label.grid(column=0, row=2)

        global arm_f_display
        arm_f_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=25,
        )
        arm_f_display.grid(column=1, row=2)

        gpu_f_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="Gpu Freq: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        gpu_f_label.grid(column=0, row=3)

        global gpu_f_display
        gpu_f_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=25,
        )
        gpu_f_display.grid(column=1, row=3)

        gpu_m_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="Gpu Mem: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        gpu_m_label.grid(column=0, row=4)

        global gpu_m_display
        gpu_m_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=25,
        )
        gpu_m_display.grid(column=1, row=4)

        over_v_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="Over Voltage: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        over_v_label.grid(column=0, row=5)

        global over_v_display
        over_v_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=25,
        )
        over_v_display.grid(column=1, row=5)

        force_t_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="Force Turbo: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        force_t_label.grid(column=0, row=6)

        global force_t_display
        force_t_display = Label(
            self.ov_display_frame,
            anchor="w",
            justify=LEFT,
            text="not configured",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=25,
        )
        force_t_display.grid(column=1, row=6)

        # Tuning_Button_Frame

        self.tu_reset = Button(
            self.ov_buttons,
            justify="left",
            image=self.rm_ov_icon,
            text="Reset Overclocking",
            anchor="w",
            command=set_default,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        ).grid(column=0, row=2, pady=10)

        global tu_btn1
        tu_btn1 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov1_icon,
            text="Crank It Up",
            anchor="w",
            command=ov_2000,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        )
        tu_btn1.grid(column=0, row=4, pady=10)

        global tu_btn2
        tu_btn2 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov2_icon,
            text="You Sir... Need A Fan!",
            anchor="w",
            command=ov_2147,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        )
        tu_btn2.grid(column=0, row=6, pady=10)

        global tu_btn3
        tu_btn3 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov3_icon,
            text="Take It To The Max!",
            anchor="w",
            command=ov_2200,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        )
        tu_btn3.grid(column=0, row=8, pady=10)

        global tu_btn4
        tu_btn4 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov4_icon,
            text="Honey,\nthe fuse blew again!",
            anchor="w",
            command=ov_2300,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        )
        tu_btn4.grid(column=0, row=9, pady=10)

        global tu_btn5
        tu_btn5 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov5_icon,
            text="I really like typing\nin random numbers\nand see what happens!",
            command=expert_mode,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=font_10,
            width=200,
        )
        tu_btn5.grid(column=0, row=10, pady=10)

        # ZRAM Button
        self.tu_zbtn = Button(
            self.ov_buttons,
            image=self.zram_icon,
            justify="left",
            text="Install ZRAM",
            font=font_12,
            anchor="w",
            command=z_ram,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            compound=LEFT,
            foreground=main_font,
            width=200,
        ).grid(column=0, row=12, pady=20)

        self.tu_legende = Button(
            self.ov_buttons,
            text="Legende",
            font=font_8,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=info_color,
            command=tuning_legende,
            image=self.tu_legend_ico,
        ).grid(column=0, row=13, pady=10)

        self.pigro_t_info = Label(
            self.ov_buttons,
            anchor="w",
            # justify=LEFT,
            text="To unlock the overclocking options\non 'first use' click on:\nReset Overclocking",
            highlightthickness=0,
            borderwidth=2,
            background=maincolor,
            foreground=info_color,
            font=font_8_b,
        )
        self.pigro_t_info.grid(column=0, row=14)

        def chromium_drm_cmd():
            if select_clicked1.get() == "Chromium 32":
                print("Chromium 32")
                global pigro_skript_name
                pigro_skript_name = "Chromium 32"
                global pigro_skript
                pigro_skript = f"{legit} apt install chromium-browser:armhf libwidevinecdm0 -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

            if select_clicked1.get() == "Chromium 64":
                print("Chromium 64")
                pigro_skript_name = "Chromium 64"
                pigro_skript = f"{legit} apt install chromium-browser:arm64 libwidevinecdm0- -y && exit"
                custom_pop = Custom_Installer(self)
                custom_pop.grab_set()

        self.chromium_drm = LabelFrame(
            self.ov_state_display_frame,
            text="Widevine on 64 Bit",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=FLAT,
            pady=10,
            padx=82,
        )
        self.chromium_drm.pack(padx=40, pady=20)
        self.chromium_drm["background"] = frame_color
        #
        options = [
            "Chromium 32",
            "Chromium 64",
        ]

        add_path_lbl = Label(
            self.chromium_drm,
            text="Chromium 64Bit has not but 32Bit has",
            justify="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        add_path_lbl.grid(column=0, columnspan=3, row=0, pady=10)

        global select_clicked1
        select_clicked1 = StringVar()
        select_clicked1.set("Switch to:")
        drop = OptionMenu(
            self.chromium_drm,
            select_clicked1,
            *options,
        )
        drop.grid(column=0, row=1)
        drop.config(
            bg=frame_color,
            fg=main_font,
            activebackground=frame_color,
            activeforeground=main_font,
            width=15,
        )
        drop["menu"].config(
            bg=maincolor,
            fg=main_font,
            activebackground=frame_color,
            activeforeground=main_font,
        )

        drop["highlightbackground"] = maincolor
        drop["relief"] = "flat"

        select_trasp_btn = Button(
            self.chromium_drm,
            text="Select",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_12,
            command=chromium_drm_cmd,
        )
        select_trasp_btn.grid(column=1, row=1)

        self.tu_info = Label(
            self.ov_state_display_frame,
            text="\n\n\n\n\n\n\n\nSettings tested with:\nRaspberry Pi 4B 8 GB Rev.1.4\nRaspberry Pi 4B 4 GB Rev.1.1\n+ Ice Tower Cooler & Pi400.\nI take no responsibility if\nyour Pi is damaged.\nPlease click on the Info Button\nto learn more",
            font=font_8_b,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=info_color,
        ).pack()

        def ov_display():
            # Overclock Display Functions
            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking1", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="Crank It Up",
                            foreground="yellow",
                            bg=frame_color,
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)

            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking2", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="You Sir... Need A Fan!",
                            foreground="red",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)

            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking3", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="Take It To The Max!",
                            foreground="pink",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)

            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking4", fp):
                    if line:
                        pigro_t_display.config(
                            text="Honey,the fuse blew again!",
                            foreground="purple",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "arm_freq" in line:
                    arm_f_display.config(
                        text=line[9:-1] + " MHz",
                        foreground=main_font,
                        font=font_12,
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)
                if "#arm_freq=800" in line:
                    arm_f_display.config(
                        text="not configured",
                        foreground=main_font,
                        font=font_12,
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "gpu_freq" in line:
                    gpu_f_display.config(
                        text=line[9:-1] + " MHz",
                        foreground=main_font,
                        font=font_12,
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "force_turbo" in line:
                    force_t_display.config(
                        text=line[12:-1],
                        foreground=main_font,
                        font=font_12,
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "over_voltage" in line:
                    over_v_display.config(
                        text=line[13:-1],
                        foreground=main_font,
                        font=font_12,
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)

            with open(f"{config_path}") as pi_conf:
                datafile = pi_conf.readlines()
            for line in datafile:
                if "gpu_mem" in line:
                    gpu_m_display.config(
                        text=line[8:-1] + " MB",
                        foreground=main_font,
                        font=font_12,
                    )

        def refresh_OV_stats():
            ov_display()
            self.after(3000, refresh_OV_stats)

        refresh_OV_stats()


class Links_Tab(ttk.Frame):
    """a tab that display lot of links to cool websites"""

    def __init__(self, container):
        super().__init__()

        self.link = PhotoImage(file=r"images/icons/pigro_icons/web.png")

        def link_tab(text):
            if text == "Mankier.com (Commandline Database)":
                popen("xdg-open https://mankier.com")
            if text == "Guake (Drop Down Terminal)":
                popen("xdg-open https://github.com/Guake/guake")
            if text == "OnBoard (Onscreen Keyboard)":
                popen("xdg-open https://wiki.ubuntuusers.de/Barrierefreiheit/onBoard/")
            if text == "Draculatheme.com":
                popen("xdg-open https://draculatheme.com/")
            if text == "Starship (Cross-Shell-Promt)":
                popen("xdg-open https://starship.rs/")
            if text == "Linuxcommandlibrary.com":
                popen("xdg-open https://linuxcommandlibrary.com/")
            if text == "LCD Wiki":
                open("xdg-open http://www.lcdwiki.com/Main_Page")
            if text == "Offical Raspberry Pi Documentation":
                popen("xdg-open https://www.raspberrypi.com/documentation/")
            if text == "Raspberry Pi Tutorials":
                popen("xdg-open https://tutorials-raspberrypi.com/")
            if text == "Papirus Nord Icon Theme":
                popen("xdg-open https://github.com/Adapta-Projects/Papirus-Nord")
            if text == "WaveShare Wiki":
                popen("xdg-open  https://www.waveshare.com/wiki/Main_Page")
            if text == "My ZSH Prompt":
                popen("xdg-open  https://github.com/actionschnitzel/my_zsh_prompt")
            if text == "xfce-look.org":
                popen("xdg-open  https://www.xfce-look.org/s/XFCE/browse/")
            if text == "Brave Browser Nighly arm64":
                popen("xdg-open  https://github.com/brave/brave-browser/releases")

        self.link_left = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            padx=20,
            pady=20,
        )
        self.link_left.pack(padx=40)
        self.link_left["background"] = maincolor

        sources_d = [
            "Brave Browser Nighly arm64",
            "Draculatheme.com",
            "Guake (Drop Down Terminal)",
            "LCD Wiki",
            "Linuxcommandlibrary.com",
            "Mankier.com (Commandline Database)",
            "My ZSH Prompt",
            "Offical Raspberry Pi Documentation",
            "OnBoard (Onscreen Keyboard)",
            "Papirus Nord Icon Theme",
            "Raspberry Pi Tutorials",
            "Starship (Cross-Shell-Promt)",
            "WaveShare Wiki",
            "xfce-look.org",
        ]

        sources_d1 = []

        for file in sources_d:
            self.choice_link1 = Button(
                self.link_left,
                anchor="w",
                justify="left",
                width=400,
                compound="left",
                text=file,
                image=self.link,
                command=lambda text=file: link_tab(text),
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=main_font,
                font=font_10,
            ).pack(pady=5)
            sources_d1.append(self.choice_link1)


class ProcessTree(ttk.Frame):
    """sets up a treeview of all runnning processes"""

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tree = ttk.Treeview(self, columns=("PID", "Name", "Memory"), height=30)
        self.tree.heading("#0", text="Process")
        self.tree.heading("#1", text="PID")
        self.tree.heading("#2", text="Memory")
        self.tree.column("#0", stretch=tk.YES)
        self.tree.column("#1", stretch=tk.YES)
        self.tree.column("#2", stretch=tk.YES)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.vsb.grid(row=0, column=1, sticky="nsew")
        self.populate_tree()

    def populate_tree(self):
        for proc in psutil.process_iter():
            try:
                pinfo = proc.as_dict(attrs=["pid", "name", "memory_percent"])
                self.tree.insert(
                    "",
                    "end",
                    text=pinfo["name"],
                    values=(pinfo["pid"], pinfo["memory_percent"]),
                )
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def OnDoubleClick(self, event):
        item = self.tree.identify_row(event.y)
        item_text = self.tree.item(item, "text")
        pid = self.tree.item(item, "values")[0]
        print(f"[Info]: Killed {item_text} with PID {pid}")
        os.system(f"kill {pid}")
        self.tree.delete(item)


class Tasks_Tab(ttk.Frame):
    """shows all running pocesses in a treeview"""

    def __init__(self, container, *args, **kwargs):
        super().__init__()

        self.proc_frame = LabelFrame(
            self,
            text="Process Killer",
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

        self.proc_frame.pack(pady=40)
        self.tree = ProcessTree(self.proc_frame)
        self.tree.pack(fill="both", expand=True)

        self.kill_button = Label(
            self.proc_frame,
            text="Double Click On The Process To End It",
            background=frame_color,
            foreground=info_color,
            borderwidth=0,
            highlightthickness=0,
        )
        self.kill_button.pack(pady=10)

        def kill_pid_num():
            popen(f"kill {self.kill_pid_entry.get()}")

        self.kill_pid = Frame(
            self.proc_frame,
            highlightthickness=0,
            highlightcolor="white",
            pady=10,
            background=frame_color,
        )
        self.kill_pid.pack(side=LEFT)

        self.kill_pid_label = Label(
            self.kill_pid,
            anchor="w",
            justify=LEFT,
            text="Kill by PID number: ",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_12,
            width=15,
        )
        self.kill_pid_label.grid(column=0, row=0)

        self.kill_pid_entry = Entry(self.kill_pid, width=15, borderwidth=0)
        self.kill_pid_entry.grid(column=1, row=0, padx=5)

        self.kill_pid_btn = Button(
            self.kill_pid,
            anchor="w",
            text="Kill Process",
            command=kill_pid_num,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
        )
        self.kill_pid_btn.grid(column=2, row=0, padx=5)


class About_Tab(ttk.Frame):
    """this tab contains infos and links to the devs website"""

    def __init__(self, container):
        super().__init__()

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def ch_log():
            popen(
                "xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki/Change-Log"
            )

        def paypal_link():
            popen("xdg-open https://www.paypal.com/paypalme/actionschnitzel")

        self.auto_start = PhotoImage(file=r"images/icons/logo1.png")

        self.paypal_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PayPal_donation.png"
        )

        self.rahmen102 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=0, pady=10, padx=10
        )
        self.rahmen102.pack(fill=BOTH, padx=50, pady=20)
        self.rahmen102["background"] = maincolor

        self.actn_shn = Label(
            self.rahmen102,
            image=self.auto_start,
            background=maincolor,
        ).pack(pady=20)

        self.poke_pig_21 = Label(
            self.rahmen102,
            text="PiGro - Just Click It!\n(A più di novemila, accipicchia!)\nVersion: 23.01",
            font=font_16,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.change_log = Button(
            self.rahmen102,
            text="Changelog",
            font=(font_10),
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=ch_log,
        )
        self.change_log.pack()

        self.gihub_link = tk.Label(
            self.rahmen102,
            text=r"https://github.com/actionschnitzel/PiGro-Aid-",
            fg="blue",
            background=maincolor,
            cursor="hand2",
        )
        self.gihub_link.pack(pady=5)
        self.gihub_link.bind("<Button-1>", callback)

        self.poke_pig_21 = Label(
            self.rahmen102,
            text="\n\n\nDeveloped and maintained by:\n\nTimo Westphal\n(Actionschnitzel)\n\n\n\n\nContact:",
            font=font_12,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.mail = Entry(self.rahmen102, bd=6, width=20, borderwidth=0)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.paypal = Button(
            self.rahmen102,
            text="Paypal",
            font=(font_10),
            image=self.paypal_icon,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            command=paypal_link,
            activebackground=maincolor,
        )
        self.paypal.pack()

        self.poke_pig_21 = Label(
            self.rahmen102,
            text="\n\n\nThis program comes with ABSOLUTELY NO WARRANTY!\nIt is licensed under the GNU General Public License v3.0\nIcons have been partially adopted and modified from the\nPapirus Icon Theme licensed under the\nGNU General Public License v3.0",
            font=font_9_b,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.papirus_link = tk.Label(
            self.rahmen102,
            text=r"https://github.com/PapirusDevelopmentTeam/papirus-icon-theme",
            fg="blue",
            background=maincolor,
            cursor="hand2",
        )
        self.papirus_link.pack()
        self.papirus_link.bind("<Button-1>", callback)


class Deb_Recover(ttk.Frame):
    """this tab contains infos and links to the devs website"""

    def __init__(self, container):
        super().__init__()

        self.folder_icon = PhotoImage(file=r"images/icons/pigro_icons/folder_s.png")
        self.backup_icon = PhotoImage(file=r"images/icons/pigro_icons/backup_s.png")
        self.deb_icon = PhotoImage(file=r"images/icons/pigro_icons/deb_s.png")
        self.recover_icon = PhotoImage(file=r"images/icons/pigro_icons/recover_s.png")

        def get_dir():
            self.filename = filedialog.askdirectory(
                initialdir="~", title="Select A Directory"
            )
            print(self.filename)

        def do_backup():
            popen(f"dpkg --get-selections > {self.filename}/packages.list")
            popen(f"xdg-open {self.filename}")

        def install_dselect():
            global pigro_skript_name
            pigro_skript_name = "dselect"
            global pigro_skript
            pigro_skript = f"{legit} apt install dselect -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def get_list():
            self.p_list = filedialog.askopenfilename(
                initialdir="~",
                title="Select packages.list",
                filetypes=(("list files", "*.list"),),
            )
            print(self.p_list)

        def do_recover():
            dselect_r = f"""sudo dselect update
sudo dpkg --set-selections < {self.p_list}
sudo apt-get dselect-upgrade
printf 'Done!'"""

            popen(f"x-terminal-emulator -e 'bash -c \"{dselect_r}; exec bash\"'")

        # Main Frame
        self.backup_main_frame = LabelFrame(
            self,
            text="Debian Package Backup",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=20,
        )

        self.backup_main_frame.pack(pady=20, padx=20, fill=BOTH)
        self.backup_main_frame["background"] = frame_color

        self.backup_discription = Label(
            self.backup_main_frame,
            text="This option creates a file named packages.list. It containes a list of all debian packages installed on this system.\n\n",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_12),
            anchor=W,
            pady=5,
        ).pack()

        # Backup Frame
        self.backup_frame1 = Frame(
            self.backup_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.backup_frame1.pack(pady=5, padx=20, fill="x")
        self.backup_frame1["background"] = frame_color

        self.step_1 = Label(
            self.backup_frame1,
            text="Step 1: Click on 'Select Directory' to select a place where the file should be deployed.\nFor example a usb dongle.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10_b),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path = Button(
            self.backup_frame1,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Select Directory",
            image=self.folder_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=get_dir,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.backup_frame2 = Frame(
            self.backup_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.backup_frame2.pack(pady=5, padx=20, fill="x")
        self.backup_frame2["background"] = frame_color

        self.step2 = Label(
            self.backup_frame2,
            text="Step 2: Click on 'Backup' to start the prosses.After 1 sec it should be done.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10_b),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path2 = Button(
            self.backup_frame2,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Backup",
            image=self.backup_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=do_backup,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        # Recovery Frame
        self.recover_main_frame = LabelFrame(
            self,
            text="Debian Package Recovery",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=20,
        )

        self.recover_main_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)
        self.recover_main_frame["background"] = frame_color

        self.recover_discription = Label(
            self.recover_main_frame,
            text="The recovery requires the tool 'dselect'. Please note that you should never use recovery cross distro or architecture.\nPackages from PPAs will be not installed if the PPA is not integrated.\n\n",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_12),
            anchor=W,
            pady=5,
        ).pack()

        self.recover_frame1 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame1.pack(pady=5, padx=20, fill="x")
        self.recover_frame1["background"] = frame_color

        self.step3 = Label(
            self.recover_frame1,
            text="Step 3: Click on 'Install dselect' ( or sudo apt install dselect ).",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10_b),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path1 = Button(
            self.recover_frame1,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Install dselect",
            image=self.deb_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=install_dselect,
        )
        self.select_path1.pack(padx=5, pady=15, side=tk.LEFT)

        dselect_check = os.path.exists("/bin/dselect")
        if dselect_check == True:
            self.select_path1.config(state=DISABLED, text="dselect is\ninstalled")

        self.recover_frame2 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame2.pack(pady=5, padx=20, fill="x")
        self.recover_frame2["background"] = frame_color

        self.step_4 = Label(
            self.recover_frame2,
            text="Step 4: Click on 'Select Backup' and choose the packages.list file",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10_b),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_file = Button(
            self.recover_frame2,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Select Backup",
            image=self.folder_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=get_list,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.recover_frame3 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame3.pack(pady=5, padx=20, fill="x")
        self.recover_frame3["background"] = frame_color

        self.step5 = Label(
            self.recover_frame3,
            text="Step 5: Click on 'Recovery' to start the prosses.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10_b),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.do_ds = Button(
            self.recover_frame3,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Recovery",
            image=self.recover_icon,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=font_10,
            command=do_recover,
        ).pack(padx=5, pady=15, side=tk.LEFT)


class Error_Mass(tk.Toplevel):
    """opens a popup when entry field is empty"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Info")
        self.icon = tk.PhotoImage(file="images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 400
        app_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def cu_error():
            Error_Mass.destroy(self)

        self.e_m = PhotoImage(file=f"{Application_path}/images/backgrounds/yuno.png")

        error_frame = Frame(self, bg=maincolor)
        error_frame.pack(pady=10)

        error_img = Label(error_frame, image=self.e_m, bg=maincolor)
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(
            error_frame, text="Y U MAKE ERROR?", foreground=main_font, bg=maincolor
        )
        error_y.grid(row=0, column=1)
        global error_y2
        error_y2 = Label(
            error_frame,
            text="You did not enter a value",
            foreground=main_font,
            bg=maincolor,
        )
        error_y2.grid(row=1, column=1)

        error_btn = Button(
            error_frame,
            text="...got It!",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
            bg="red",
            command=cu_error,
        )
        error_btn.grid(row=3, column=1)


class CreateToolTip(object):
    """create a tooltip for a given widget"""

    def __init__(self, widget, text="widget info"):
        self.waittime = 500
        self.wraplength = 180
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            self.tw,
            text=self.text,
            justify="left",
            background="#ffffff",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


class Loading_Throbber(Label):
    """This class animates the the .GIF in the install window"""

    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))
        except EOFError:
            pass

        try:
            self.delay = im.info["duration"]
        except KeyError:
            self.delay = 100

        first = seq[0].convert("RGBA")
        self.frames = [ImageTk.PhotoImage(first)]

        Label.__init__(self, master, image=self.frames[0])

        temp = seq[0]
        for image in seq[1:]:
            temp.paste(image)
            frame = temp.convert("RGBA")
            self.frames.append(ImageTk.PhotoImage(frame))

        self.idx = 0

        self.cancel = self.after(self.delay, self.play)

    def play(self):
        self.config(image=self.frames[self.idx])
        self.idx += 1
        if self.idx == len(self.frames):
            self.idx = 0
        self.cancel = self.after(self.delay, self.play)


# [End Of The Line]
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
