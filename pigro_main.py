#!/usr/bin/env python3
import os
import os.path
import tkinter as tk
from tkinter.dialog import DIALOG_ICON
from turtle import left, width
import tkinter.font as tkFont
import webbrowser
from os import popen
from os import system as cmd
from os import listdir
from os.path import isfile, join
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import platform
import shutil
import psutil
from collections import namedtuple
from datetime import datetime
import distro
import socket
from gpiozero import CPUTemperature
from pathlib import Path
from cgitb import enable
from pynotifier import Notification
from subprocess import check_call, CalledProcessError
import threading
from threading import Thread
from concurrent.futures import thread
from faulthandler import disable
from tkinter import filedialog


# To Do:
# Always clear apt_cache,packages,PiGro.config
# before PUSH!


# Say Hallo!
global user
user = os.environ.get("LOGNAME")
print(f"INFO: Hi,{user} waz uuuuup?!")

# Define Home
global home
home = str(Path.home())
print(f"INFO: {home} is your home directory!")

# Gets path to PiGro
global Application_path
Application_path = str(Path().absolute())
print(f"INFO: PiGro directory is {Application_path}")

# Makes all .sh files in /sripts executable if PiGro in $HOME
if Application_path == f"{home}/PiGro-Aid-":
    popen('find ~/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;')
    print("INFO: All files executable")

# Get Distro
distro_get = distro.id()
print("INFO: Your Distro is: " + distro_get)

# Legitimation Vars // Test for Ubuntu compatiblety
global config_path
config_path = "/boot/config.txt"
global legit
legit = "sudo"

# Config.txt Path
if distro_get == "ubuntu":
    config_path = "/boot/firmware/config.txt"
else:
    config_path = "/boot/config.txt"

# Legitimation
if distro_get == "ubuntu":
    legit = "pkexec"
else:
    legit = "sudo"


# Get Desktop Environment
global get_de
get_de = os.environ.get("XDG_CURRENT_DESKTOP")
print("INFO: Your DE is: " + get_de)

# Checks if pi-apps exists
global piapps_path
piapps_path = os.path.isdir(f"{home}/pi-apps")  # Need full path
if piapps_path == False:
    print("INFO: Pi-Apps not found")
if piapps_path == True:
    print("INFO: Pi-Apps is installed")

# Checks if snapd exists
if os.path.isfile("/bin/snap"):
    print("INFO: Snap is installed")
else:
    print("INFO: Snap is not installed")

# Checks if flatpak exists
if os.path.isfile("/bin/flatpak"):
    print("INFO: Flatpak is installed")
else:
    print("INFO: Flatpak is not installed")




# [Main Winddow / Notebook Config / SysTray]
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        """Base Class That Sets Notbook And Theme"""

        # Window Basics
        self.title("PiGro - Just Click It! (Stupida Medusa)")
        self.icon = tk.PhotoImage(file="images/icons/pigro_icons/256x256.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self["background"] = "#333333"
        self.resizable(0, 0)
        app_width = 1200
        app_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.wait_visibility(self)
        self.wm_attributes("-alpha", 0.95)

        # Notebook Definition
        self.notebook = ttk.Notebook(self)
        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        self.Frame9 = Frame9(self.notebook)
        self.Frame8 = Frame8(self.notebook)
        self.Frame12 = Frame12(self.notebook)
        self.Frame13 = Frame13(self.notebook)

        # Notebook Icons
        self.welcome_icon = PhotoImage(file=r"images/icons/pigro_icons/Tab_Welcome.png")
        self.system_icon = PhotoImage(file=r"images/icons/system.png")
        self.update_icon = PhotoImage(file=r"images/icons/updatetab.png")
        self.install_icon = PhotoImage(file=r"images/icons/installer_ico.png")
        self.look_icon = PhotoImage(file=r"images/icons/look.png")
        self.tuning_icon = PhotoImage(file=r"images/icons/tuning.png")
        self.dm_icon = PhotoImage(file=r"images/icons/link_tab.png")
        self.pig_icon = PhotoImage(file=r"images/icons/pigpi.png")
        self.cam_icon = PhotoImage(file=r"images/icons/PyPiCam_Go.png")
        self.config_icon = PhotoImage(file=r"images/icons/config_txt.png")
        self.ubuntu_icon = PhotoImage(file=r"images/icons/ubuntu_logo.png")
        self.auto_start = PhotoImage(file=r"images/icons/autostart_icon.png")

        # Tabs
        self.notebook.add(
            self.Frame1, compound=LEFT, text="Welcome", image=self.welcome_icon
        )

        self.notebook.add(
            self.Frame3, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.Frame13, compound=LEFT, text="Autostart", image=self.auto_start
        )

        self.notebook.add(
            self.Frame12, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.Frame2, compound=LEFT, text="Update", image=self.update_icon
        )
        self.notebook.add(
            self.Frame4, compound=LEFT, text="Software", image=self.install_icon
        )
        self.notebook.add(self.Frame5, compound=LEFT, text="Look", image=self.look_icon)

        self.notebook.add(
            self.Frame6, compound=LEFT, text="Tuning", image=self.tuning_icon
        )
        self.notebook.add(self.Frame7, compound=LEFT, text="Links", image=self.dm_icon)

        self.notebook.add(
            self.Frame9, compound=LEFT, text="Pi Camera", image=self.cam_icon
        )

        self.notebook.add(self.Frame8, compound=LEFT, text="Pig-Grow", image=self.pig_icon)

        self.notebook.pack(fill="both", expand=True, anchor=W)

        if distro_get == "debian" or distro_get == "raspbian":
            self.notebook.hide(self.Frame12)

        if distro_get == "ubuntu":
            self.notebook.hide(self.Frame3)
            self.notebook.hide(self.Frame5)
            self.notebook.hide(self.Frame9)

        # Notebook Themeing
        self.noteStyler = ttk.Style(self)
        self.noteStyler.configure(
            "TNotebook",
            borderwidth=0,
            background="#222222",
            tabposition="w",
            highlightthickness=0,
        )
        self.noteStyler.configure(
            "TNotebook.Tab",
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 16),
            width=13,
            highlightthickness=0,
        )
        self.noteStyler.configure("TFrame", background="#222222")
        self.noteStyler.map(
            "TNotebook.Tab",
            background=[("selected", "#222222")],
            foreground=[("selected", "#d4244d")],
        )
        self.noteStyler.configure(
            "red.Horizontal.TProgressbar", foreground="red", background="green"
        )
        self.noteStyler.configure("Line.TSeparator", background="grey")


# [Changelog] Child
class Change_Log(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Overclocking Legend")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Changelog")
        self.update_info_btn = PhotoImage(file=r"images/icons/pigro_icons/128x128.png")
        logo_lbl = Label(
            self,
            image=self.update_info_btn,
            text="Changelog",
            highlightthickness=0,
            borderwidth=0,
            compound=TOP,
            font=("Helvetica", 20, "bold"),
        )
        logo_lbl.pack(pady=20)
        changelog_label = Label(
            self,
            justify="left",
            anchor=W,
            text="#Added:\n-Stressberry Support\n\n#Changed:\n-Icons improved.. Yes! Again!\n\n-Changelog pops up und fist start\nor after update \n\n#Improved:\n-Fixed some problems with the new overclocking options\n",
        )
        changelog_label.pack()

        # read input file
        fin = open(f"{Application_path}/scripts/PiGro.conf", "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        data = data.replace("First_Run = True", "First_Run = False")
        # close the input file
        fin.close()
        # open the input file in write mode
        fin = open(f"{Application_path}/scripts/PiGro.conf", "wt")
        # overrite the input file with the resulting data
        fin.write(data)
        # close the file
        fin.close()


# [Welcome] Tab
class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def ch_log():
            c_log = Change_Log(self)
            c_log.grab_set()

        # Check if Update or First run
        with open(f"{Application_path}/scripts/PiGro.conf") as f:
            if "First_Run = True" in f.read():
                print("First Run")

                ch_log()

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

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def stress_b():
            popen(
                f"xterm -e 'bash -c \"{Application_path}/scripts/stressberry.sh & echo DONE!; exec bash\"'"
            )

        self.bg = PhotoImage(file=f"{Application_path}/images/backgrounds/pigronew.png")
        self.welcome_canvas = Canvas(self, width=900, height=800, highlightthickness=0)
        self.welcome_canvas.pack(fill="both", expand=True)
        self.welcome_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.welcome_canvas.create_text(
            350,
            90,
            text=f"Hi, {user}\nwaz up?!",
            font=("Helvetica", 12, "bold"),
            fill="black",
        )

        self.web_link = tk.Label(
            self,
            text=r"https://www.actionschnitzel.de/PiGro/",
            fg="blue",
            cursor="hand2",
        )
        self.web_link.place(x=670, y=740)
        self.web_link.bind("<Button-1>", callback)

        self.web_link["background"] = "#333333"

        self.gihub_link = tk.Label(
            self,
            text=r"https://github.com/actionschnitzel/PiGro-Aid-",
            fg="blue",
            cursor="hand2",
        )
        self.gihub_link.place(x=670, y=770)
        self.gihub_link.bind("<Button-1>", callback)

        self.gihub_link["background"] = "#333333"

        self.stress = Button(
            self,
            text="Run/Install Stressberry",
            font=(
                ("Helvetica,bold"),
                "10",
            ),
            highlightthickness=2,
            borderwidth=0,
            background="#222222",
            foreground="white",
            command=stress_b,
        )
        self.stress.place(x=160, y=700)

        self.changelog_btn = Button(
            self,
            text="Changelog",
            font=(("Helvetica,bold"), "12", "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#fbc463",
            foreground="grey",
            command=ch_log,
        ).place(x=95, y=125)

        # Parameters for System
        global distro
        distro = distro.id()

        pid = os.getpid()
        ps = psutil.Process(pid)
        my_system = platform.uname()
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        hostname = socket.gethostname()
        IPAddr = extract_ip()
        cpu = CPUTemperature()
        Pi_Model = open("/proc/device-tree/model", "r")
        total, used, free = shutil.disk_usage("/")

        self.sys_info_main_frame = Frame(
            self, borderwidth=0, highlightthickness=5, relief=GROOVE, pady=10, padx=20
        )
        self.sys_info_main_frame.place(x=160, y=360)
        self.sys_info_main_frame["background"] = "#222222"

        self.sys_frame_left = Frame(
            self.sys_info_main_frame, borderwidth=0, highlightthickness=0, relief=GROOVE
        )
        self.sys_frame_left.pack(side=LEFT)
        self.sys_frame_left["background"] = "#222222"

        self.sys_frame_right = Frame(
            self.sys_info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=0,
            padx=20,
        )
        self.sys_frame_right.pack(pady=20)
        self.sys_frame_right["background"] = "#222222"

        self.raspi_img = ImageTk.PhotoImage(Image.open("images/icons/deb_logo.png"))
        self.raspi_label = Label(image=self.raspi_img)

        self.sysinf0 = Label(
            self.sys_frame_right,
            image=self.raspi_img,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="#d4244d",
            pady=10,
            padx=20,
            anchor=E,
        )
        self.sysinf0.pack()

        self.sysinf0 = Label(
            self.sys_frame_left,
            text=f"System: {my_system.system}",
            font=("Helvetica", 10, "bold"),
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            width=40,
            anchor=W,
        ).pack()

        self.sysinfd = Label(
            self.sys_frame_left,
            text=f"Distro: {distro}",
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf1 = Label(
            self.sys_frame_left,
            text=f"Device Name: {my_system.node}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=f"Board: {Pi_Model.read()}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf2 = Label(
            self.sys_frame_left,
            text=f"Kernel: {my_system.release}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"Architecture: {my_system.machine}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf8 = Label(
            self.sys_frame_left,
            text="",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        )
        self.sysinf8.pack()

        self.sysinf6 = Label(
            self.sys_frame_left,
            text=f"CPU Max Freq: {cpufreq.max:.0f} Mhz",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf7 = Label(
            self.sys_frame_left,
            text=f"CPU Min Freq: {cpufreq.min:.0f} Mhz",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf10 = Label(
            self.sys_frame_left,
            text="",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        )
        self.sysinf10.pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"RAM Total: {get_size(svmem.total)}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"SWAP Total: {get_size(swap.total)}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=f"IP Address: {IPAddr}",
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=("Total Disk Space: %d GiB" % (total // (2**30))),
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=("Used Disk Space: %d GiB" % (used // (2**30))),
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=("Free Disk Space: %d GiB" % (free // (2**30))),
            justify="left",
            background="#222222",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        def refresh_sys_stats():

            # Parameters for System
            pid = os.getpid()
            ps = psutil.Process(pid)
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            cpu = CPUTemperature()
            # print(cpu)

            self.sysinf8.configure(text=f"Current CPU Freq: {cpufreq.current:.0f} Mhz")
            self.sysinf10.configure(text=f"CPU Temp: {cpu.temperature:.1f} °C")
            self.after(1000, refresh_sys_stats)

        refresh_sys_stats()


# [Update] Tab
class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def info_update_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Update Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/update_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def update_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 1000x25 -e "{Application_path}/scripts/update.sh && exit ; exec bash"'
                % self.wid
            )

        def upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 1000x25 -e "{Application_path}/scripts/upgrade.sh && exit; exec bash"'
                % self.wid
            )

        def full_upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 1000x25 -e "{Application_path}/scripts/full_upgrade.sh && exit; exec bash"'
                % self.wid
            )

        def autoremove_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 1000x25 -e "{Application_path}/scripts/auto_remove.sh && exit ; exec bash"'
                % self.wid
            )

        def add_unsi_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 1000x25 -e "{Application_path}/scripts/addunsignedrepo.sh && exit; exec bash"'
                % self.wid
            )

        def button_gpk():
            popen(f"{legit} pi-gpk-update-viewer")

        def button_list():
            popen("xdg-open /etc/apt/sources.list.d/")

        def save_list():
            os.system(f"{legit} chmod 777 -R /etc/apt/sources.list")
            text_file = open("/etc/apt/sources.list", "w")
            text_file.write(s_list.get(1.0, END))
            m_text = "\
        \n\
        \n\
        Sources List has been saved\n\
        \n\
        \n\
        "
            messagebox.showinfo(message=m_text, title="Infos")

        def reboot_n():
            popen(f"{legit} reboot")

        self.update_info_btn = PhotoImage(file=r"images/icons/info_m.png")

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.source_list_frame = Frame(self, relief=GROOVE, borderwidth=0)
        self.source_list_frame.pack(padx=45, pady=40, anchor="w", fill=BOTH)
        self.source_list_frame["background"] = "#333333"

        self.termf = Frame(
            self, height=270, width=700, padx=10, highlightthickness=2, borderwidth=0
        )
        self.wid = self.termf.winfo_id()
        self.termf["background"] = "#333333"

        s_list = Text(
            self.source_list_frame, width=1550, height=10, highlightthickness=1
        )
        text_file = open("/etc/apt/sources.list", "r")
        stuff = text_file.read()
        s_list.insert(END, stuff)
        text_file.close()
        s_list.pack(anchor="w")

        self.update_btn_frame = Frame(
            self,
            borderwidth=0,
            relief=GROOVE,
            highlightthickness=3,
            highlightcolor="white",
            padx=5,
            pady=5,
        )
        self.update_btn_frame.pack(padx=45, anchor="w")
        self.update_btn_frame["background"] = "#222222"

        self.update_button = Button(
            self.update_btn_frame,
            text="Update",
            width=15,
            anchor="w",
            command=update_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.update_button.grid(column=0, row=0)

        self.update_button = Button(
            self.update_btn_frame,
            text="Upgrade",
            width=15,
            anchor="w",
            command=upgrade_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.update_button.grid(column=0, row=1)

        self.fupgrade_button = Button(
            self.update_btn_frame,
            text="Full Upgrade",
            width=15,
            anchor="w",
            command=full_upgrade_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.fupgrade_button.grid(column=0, row=2)

        self.gpk_button = Button(
            self.update_btn_frame,
            text="GPK UpdateViewer",
            width=15,
            anchor="w",
            command=button_gpk,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.gpk_button.grid(column=0, row=3)

        self.auth_button = Button(
            self.update_btn_frame,
            text="Allow Sources",
            width=20,
            anchor="w",
            command=add_unsi_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.auth_button.grid(column=1, row=0)

        self.rm_button = Button(
            self.update_btn_frame,
            text="Remove Config Files",
            width=20,
            anchor="w",
            command=autoremove_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.rm_button.grid(column=1, row=1)

        self.sv_button = Button(
            self.update_btn_frame,
            text="Save Source List",
            width=20,
            anchor="w",
            command=save_list,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="#d4244d",
            font=("Helvetica", 12, "bold"),
        )
        self.sv_button.grid(column=1, row=2)

        self.sv_button = Button(
            self.update_btn_frame,
            text="Open Sources.list.d",
            width=20,
            anchor="w",
            command=button_list,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="#d4244d",
            font=("Helvetica", 12, "bold"),
        )
        self.sv_button.grid(column=1, row=3)

        self.reboot_button = Button(
            self.update_btn_frame,
            text="Reboot",
            width=20,
            anchor="w",
            command=reboot_n,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="#d4244d",
            font=("Helvetica", 12, "bold"),
        )
        self.reboot_button.grid(column=1, row=4)

        self.termf.pack(padx=45, pady=20, anchor=W, fill=BOTH)

        self.info_up_btn = Button(
            self,
            image=self.update_info_btn,
            highlightthickness=0,
            borderwidth=0,
            command=info_update_tab,
        )
        self.info_up_btn.place(x=900, y=720)


# [System] tab
class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def source_sett():
            popen("pi-gpk-prefs")

        def screen_sett():
            popen("lxrandr")

        def desk_sett():
            popen("pcmanfm --desktop-pref")

        def desk_sess_sett():
            popen("lxsession-edit")

        def printer_sett():
            popen("system-config-printer")

        def menu_sett():
            popen("alacarte")

        def mouse_key_sett():
            popen("lxinput")

        def button_boot():
            popen("xterm -e 'bash -c \"dmesg; exec bash\"'")

        def rm_vscode():
            popen(
                f"xterm -e 'bash -c \"{legit} rm /etc/apt/sources.list.d/vscode.list & echo DONE!; exec bash\"'"
            )

        def net_set():
            popen("nm-connection-editor")

        def pi_configbutton():
            popen(f"xterm -e 'bash -c \"{legit} raspi-config; exec bash\"'")

        def pi_configbutton2():
            popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")

        def lx_task():
            popen("lxtask")

        def contxt_button():
            popen(f"{legit} mousepad /boot/config.txt")

        def neofetch_button():
            popen("xterm -e 'bash -c \"neofetch; exec bash\"'")

        def gparted_exec():
            popen(f"{legit} gparted")

        def cron_job():
            popen(f"{legit} mousepad /etc/crontab")

        def onc_ben():
            if get_de == "XFCE":
                popen("sudo thunar /")
            else:
                popen("sudo pcmanfm /")

            print("INFO: With great power comes great responsibility")
            Notification(
                title="Sudo File Manager\n",
                description="With great power comes great responsibility\n\n                          - Oncle Ben",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        def sd_copy():
            popen(
                "env SUDO_ASKPASS=/usr/lib/piclone/pwdpic.sh sudo -AE dbus-launch piclone"
            )

        def button_lk():
            global pop_kernel
            pop_kernel = Toplevel(self)
            pop_kernel.config(bg="#333333")
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
                    f"xterm -e 'bash -c \"{legit} BRANCH=next rpi-update; exec bash\"'"
                )
                print("INFO: Kernel Upgrade GO!")
                pop_kernel.destroy()

            frame_pop_kernel = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel.pack()
            frame_pop_kernel["background"] = "#333333"

            frame_pop_kernel_1 = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel_1.pack()
            frame_pop_kernel_1["background"] = "#333333"

            pop_lbl_2000 = Label(
                frame_pop_kernel,
                anchor="w",
                text="Do you really want to Upgrade the Kernel?",
                font=("Helvetica", 12),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
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
                foreground="white",
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
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def button_auto():
            popen("xfce4-session-settings")

        def button_xsett():
            popen("xfce4-settings-manager")

        def info_system_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("System Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/system_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def bash_log():
            popen(f"xdg-open {home}/.bash_history")

        def rename_user():
            global pop_u_name
            pop_u_name = Toplevel(self)
            pop_u_name.config(bg="#333333")
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
                popen(f"{legit} rename-user")
                print("INFO: Name will be changed")
                pop_u_name.destroy()

            frame_pop_u_name = Frame(pop_u_name, borderwidth=0, relief=GROOVE)
            frame_pop_u_name.pack()
            frame_pop_u_name["background"] = "#333333"

            frame_pop_u_name_1 = Frame(pop_u_name, borderwidth=0, relief=GROOVE)
            frame_pop_u_name_1.pack()
            frame_pop_u_name_1["background"] = "#333333"

            pop_lbl_2000 = Label(
                frame_pop_u_name,
                anchor="w",
                text="Do you really want to change the user name?\nrename-user will run on reboot.",
                font=("Helvetica", 12),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
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
                background="#2246c4",
                foreground="white",
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
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        # Icon Set
        self.bp01 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp02 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp03 = PhotoImage(file=r"images/icons/terminal.png")
        self.bp033 = PhotoImage(file=r"images/icons/terminal3.png")
        self.bp04 = PhotoImage(file=r"images/icons/gparted.png")
        self.bp05 = PhotoImage(file=r"images/icons/indicator-cpufreq.png")
        self.bp06 = PhotoImage(file=r"images/icons/folder.png")
        self.bp07 = PhotoImage(file=r"images/icons/links.png")
        self.ico_m = PhotoImage(file=r"images/icons/gui_icon.png")
        self.ico_m2 = PhotoImage(file=r"images/icons/weblink_icon.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.hist_doc = PhotoImage(file=r"images/icons/hist_doc.png")
        self.keyboard = PhotoImage(file=r"images/icons/keyboard.png")
        self.deskpi_ico = PhotoImage(file=r"images/icons/deskpi.png")
        self.net = PhotoImage(file=r"images/icons/net.png")
        self.sd = PhotoImage(file=r"images/icons/sd.png")
        self.neo = PhotoImage(file=r"images/icons/neofetch.png")
        self.display_settings_icon = PhotoImage(
            file=r"images/icons/display_settings_icon.png"
        )
        self.mouse_settings_icon = PhotoImage(
            file=r"images/icons/mouse_settings_icon.png"
        )
        self.printer_settings_icon = PhotoImage(
            file=r"images/icons/printer_settings_icon.png"
        )

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#222222")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        # Button Set/Frame1
        self.rahmen2 = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            padx=20,
            pady=20,
        )
        self.rahmen2.pack(pady=20)
        self.rahmen2["background"] = "#222222"

        sys_rc_cli_btn = Button(
            self.rahmen2,
            image=self.bp01,
            width=140,
            height=100,
            text="Raspi-Config CLI",
            command=pi_configbutton,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_rc_cli_btn.grid(row=0, column=0)

        sys_rc_gui_btn = Button(
            self.rahmen2,
            image=self.bp01,
            width=140,
            height=100,
            text="Raspi-Config GUI",
            command=pi_configbutton2,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_rc_gui_btn.grid(row=0, column=1)

        sys_conf_btn = Button(
            self.rahmen2,
            image=self.hist_doc,
            width=140,
            height=100,
            text="Config.txt",
            command=contxt_button,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_conf_btn.grid(row=0, column=2)

        sys_btnvs = Button(
            self.rahmen2,
            image=self.bp03,
            width=140,
            height=100,
            text="rm vscode.list ",
            command=rm_vscode,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btnvs.grid(row=0, column=3)

        sys_gparted_btn = Button(
            self.rahmen2,
            image=self.bp04,
            width=140,
            height=100,
            text="Gparted",
            command=gparted_exec,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_gparted_btn.grid(row=1, column=0)

        if os.path.isfile("/usr/sbin/gparted"):
            print("INFO: Gparted is installed")
            sys_gparted_btn.configure(state=NORMAL)
        else:
            print("INFO: Gparted is not installed")
            sys_gparted_btn.configure(state=DISABLED)

        sys_neo_btn = Button(
            self.rahmen2,
            image=self.neo,
            width=140,
            height=100,
            text="NeoFetch",
            command=neofetch_button,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_neo_btn.grid(row=1, column=1)

        if os.path.isfile("/bin/neofetch"):
            print("INFO: Neofetch is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("INFO: Neofetch is not installed")
            sys_neo_btn.configure(state=DISABLED)

        sys_FMGM_btn = Button(
            self.rahmen2,
            image=self.bp06,
            width=140,
            height=100,
            text="FM God Mode",
            command=onc_ben,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_FMGM_btn.grid(row=1, column=2)
        sys_FMGM_btn = CreateToolTip(
            sys_FMGM_btn,
            "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)",
        )

        sys_kernel_btn = Button(
            self.rahmen2,
            image=self.bp07,
            width=140,
            height=100,
            text="Upgrade Linux Kernel",
            command=button_lk,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_kernel_btn.grid(row=1, column=3)

        sys_dpp_btn = Button(
            self.rahmen2,
            image=self.deskpi_ico,
            width=140,
            height=100,
            text="DeskpiPro Control",
            command=button_dpfc,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_dpp_btn.grid(row=2, column=0)

        sys_b_log_btn = Button(
            self.rahmen2,
            image=self.bp03,
            width=140,
            height=100,
            text="Boot Log",
            command=button_boot,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_b_log_btn.grid(row=2, column=1)

        sys_xf_auto_btn = Button(
            self.rahmen2,
            image=self.bp033,
            width=140,
            height=100,
            text="Xfce Autostarts",
            command=button_auto,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_xf_auto_btn.grid(row=2, column=2)
        sys_xf_auto_btn.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_xf_auto_btn.configure(state=NORMAL)

        sys_xf_sett_btn = Button(
            self.rahmen2,
            image=self.bp033,
            width=140,
            height=100,
            text="Xfce Settings",
            command=button_xsett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_xf_sett_btn.grid(row=2, column=3)
        sys_xf_sett_btn.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_xf_sett_btn.configure(state=NORMAL)

        sys_netset_btn = Button(
            self.rahmen2,
            image=self.net,
            width=140,
            height=100,
            text="Network Settings",
            command=net_set,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_netset_btn.grid(row=3, column=0)

        sys_task_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            width=140,
            height=100,
            text="Taskmanager",
            command=lx_task,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_task_btn.grid(row=3, column=1)

        sys_bash_btn = Button(
            self.rahmen2,
            image=self.hist_doc,
            width=140,
            height=100,
            text="Bash History",
            command=bash_log,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_bash_btn.grid(row=3, column=2)

        sys_cron_btn = Button(
            self.rahmen2,
            image=self.hist_doc,
            width=140,
            height=100,
            text="Cron Job",
            command=cron_job,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_cron_btn.grid(row=3, column=3)

        sys_sd_btn = Button(
            self.rahmen2,
            image=self.sd,
            width=140,
            height=100,
            text="SD Card Copier",
            command=sd_copy,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_sd_btn.grid(row=4, column=0)

        screen_sett_btn = Button(
            self.rahmen2,
            image=self.display_settings_icon,
            width=140,
            height=100,
            text="Screen Settings",
            command=screen_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        screen_sett_btn.grid(row=4, column=1)

        desk_sett_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            width=140,
            height=100,
            text="Desktop Settings",
            command=desk_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        desk_sett_btn.grid(row=4, column=2)

        printer_sett_btn = Button(
            self.rahmen2,
            image=self.printer_settings_icon,
            width=140,
            height=100,
            text="Printer Settings",
            command=printer_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        printer_sett_btn.grid(row=4, column=3)

        menu_sett_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            width=140,
            height=100,
            text="Menu Settings",
            command=menu_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        menu_sett_btn.grid(row=5, column=0)

        source_sett_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            width=140,
            height=100,
            text="Source Settings",
            command=source_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        source_sett_btn.grid(row=5, column=1)

        mouse_key_sett_btn = Button(
            self.rahmen2,
            image=self.keyboard,
            width=140,
            height=100,
            text="Mouse & Keyboard",
            command=mouse_key_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        mouse_key_sett_btn.grid(row=5, column=2)

        rename_user_btn = Button(
            self.rahmen2,
            image=self.bp01,
            width=140,
            height=100,
            text="Rename User",
            command=rename_user,
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        rename_user_btn.grid(row=5, column=3)

        self.info_sys_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_system_tab,
        )
        self.info_sys_btn.place(x=900, y=720)


# [System For Ubuntu] tab
class Frame12(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def ubu_prefs():
            popen("gnome-control-center")

        def g_tweaks():
            popen("gnome-tweaks")

        def menu_sett():
            popen("alacarte")

        def button_boot():
            popen("xterm -e 'bash -c \"{legit} dmesg; exec bash\"'")

        def pi_configbutton():
            popen(f"xterm -e 'bash -c \"{legit} raspi-config; exec bash\"'")

        def neofetch_button():
            popen("xterm -e 'bash -c \"neofetch; exec bash\"'")

        def gparted_exec():
            popen(f"{legit} gparted")

        def contxt_button():
            popen(
                f"gnome-terminal -e 'bash -c \"{Application_path}/scripts/ubu_config_txt.sh; exec bash\"'"
            )

        def onc_ben():
            popen(
                f"gnome-terminal -e 'bash -c \"{Application_path}/scripts/ubu_FMGM.sh; exec bash\"'"
            )
            print("INFO: With great power comes great responsibility")
            Notification(
                title="Sudo File Manager\n",
                description="With great power comes great responsibility\n\n                          - Oncle Ben",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def info_system_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("System Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/system_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def bash_log():
            popen(f"xdg-open {home}/.bash_history")

        def gX_web():
            popen("xdg-open https://extensions.gnome.org/")

        # Icon Set
        self.bp01 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp02 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp03 = PhotoImage(file=r"images/icons/terminal.png")
        self.bp033 = PhotoImage(file=r"images/icons/terminal3.png")
        self.bp04 = PhotoImage(file=r"images/icons/gparted.png")
        self.bp05 = PhotoImage(file=r"images/icons/indicator-cpufreq.png")
        self.bp06 = PhotoImage(file=r"images/icons/folder.png")
        self.bp07 = PhotoImage(file=r"images/icons/links.png")
        self.ico_m = PhotoImage(file=r"images/icons/gui_icon.png")
        self.ico_m2 = PhotoImage(file=r"images/icons/weblink_icon.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.hist_doc = PhotoImage(file=r"images/icons/hist_doc.png")
        self.display_settings_icon = PhotoImage(
            file=r"images/icons/display_settings_icon.png"
        )
        self.mouse_settings_icon = PhotoImage(
            file=r"images/icons/mouse_settings_icon.png"
        )
        self.printer_settings_icon = PhotoImage(
            file=r"images/icons/printer_settings_icon.png"
        )

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        # Button Set/Frame1
        self.rahmen2 = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, padx=60, pady=10
        )
        self.rahmen2.pack(padx=40, pady=20, fill="both")
        self.rahmen2["background"] = "#333333"

        sys_rc_cli_btn = Button(
            self.rahmen2,
            image=self.bp01,
            text="Raspi-Config CLI",
            command=pi_configbutton,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_rc_cli_btn.grid(row=0, column=0)

        if os.path.isfile("/bin/raspi-config"):
            print("INFO: Raspi-Config is installed")
            sys_rc_cli_btn.configure(state=NORMAL)
        else:
            print("INFO: Raspi-Config is not installed")
            sys_rc_cli_btn.configure(state=DISABLED)

        sys_ubu_pref_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Ubuntu Settings",
            command=ubu_prefs,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_ubu_pref_btn.grid(row=0, column=1)

        sys_conf_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Config.txt",
            command=contxt_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_conf_btn.grid(row=0, column=2)

        sys_neo_btn = Button(
            self.rahmen2,
            image=self.bp05,
            text="NeoFetch",
            command=neofetch_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_neo_btn.grid(row=0, column=3)

        if os.path.isfile("/bin/neofetch"):
            print("INFO: Neofetch is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("INFO: Neofetch is not installed")
            sys_neo_btn.configure(state=DISABLED)

        sys_dpp_btn = Button(
            self.rahmen2,
            image=self.bp03,
            text="DeskpiPro Control",
            command=button_dpfc,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_dpp_btn.grid(row=0, column=4)

        sys_bash_btn = Button(
            self.rahmen2,
            image=self.hist_doc,
            text="Bash History",
            command=bash_log,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_bash_btn.grid(row=1, column=1)

        g_tweaks_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Gnome Tweaks",
            command=g_tweaks,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        g_tweaks_btn.grid(row=1, column=2)

        if os.path.isfile("/bin/gnome-tweaks"):
            print("INFO: gnome-tweaks is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("INFO: gnome-tweaks is not installed")
            g_tweaks_btn.configure(state=DISABLED)

        menu_sett_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Menu Settings",
            command=menu_sett,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        menu_sett_btn.grid(row=1, column=3)

        if os.path.isfile("/bin/alacarte"):
            print("INFO: alacarte is installed")
            menu_sett_btn.configure(state=NORMAL)
        else:
            print("INFO: Gparted is not installed")
            menu_sett_btn.configure(state=DISABLED)

        sys_gparted_btn = Button(
            self.rahmen2,
            image=self.bp04,
            text="Gparted",
            command=gparted_exec,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_gparted_btn.grid(row=1, column=4)

        if os.path.isfile("/usr/sbin/gparted"):
            print("INFO: Gparted is installed")
            sys_gparted_btn.configure(state=NORMAL)
        else:
            print("INFO: Gparted is not installed")
            sys_gparted_btn.configure(state=DISABLED)

        sys_FMGM_btn = Button(
            self.rahmen2,
            image=self.bp06,
            text="FM God Mode",
            command=onc_ben,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_FMGM_btn.grid(row=1, column=0)
        sys_FMGM_btn = CreateToolTip(
            sys_FMGM_btn,
            "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)",
        )

        sys_gX_btn = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Gnome Extensions",
            command=gX_web,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_gX_btn.grid(row=2, column=0)

        self.info_sys_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_system_tab,
        )
        self.info_sys_btn.place(x=900, y=720)


# [Autostarts] tab
class Frame13(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        def add_auto():
            add_child = Add_Autostart(self)
            add_child.grab_set()

        # Checks is autostart folder exists
        dir = os.path.join(f"{home}/.config/autostart")  #
        if not os.path.exists(dir):
            print(f"INFO: {dir} does not exist.")
            print(f"INFO: Created {dir} does not exist.")
            os.mkdir(dir)
        else:
            print(f"INFO: {dir} exists.")

        onlyfiles = [
            f
            for f in listdir(f"{home}/.config/autostart")
            if isfile(join(f"{home}/.config/autostart", f))
        ]

        # print(onlyfiles)

        with open("scripts/autostart.list", "w") as f:
            for item in onlyfiles:
                f.write("%s\n" % item)

        auto_main_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            background="#222222",
            pady=20,
            padx=20,
        )
        auto_main_frame.pack(pady=20)

        auto_button_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background="#222222",
            highlightthickness=0,
            pady=10,
        )
        auto_button_frame.pack(side="left", anchor="n", fill=BOTH, expand=True)

        auto_select_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background="#222222",
            highlightthickness=0,
            pady=10,
        )
        auto_select_frame.pack()

        def del_enrty():
            os.remove(f"{home}/.config/autostart/{my_entry3.get()}")
            my_list3.delete(tk.ACTIVE)

        # Update the listbox
        def update3(data3):
            # Clear the listbox
            my_list3.delete(0, END)

            # Add toppings to listbox
            for item3 in data3:
                my_list3.insert(END, item3)

        # Update entry box with listbox clicked

        def fillout3(event):
            # Delete wot is in  Box
            my_entry3.delete(0, END)
            # Add clicked list item to enty box
            my_entry3.insert(0, my_list3.get(ACTIVE))

        # Checkfunktion Entry vs. List

        def check3(event):
            # grad inserted
            typed3 = my_entry3.get()

            if typed3 == "":
                data3 = content3
            else:
                data3 = []
                for item3 in content3:
                    if typed3.lower() in item3.lower():
                        data3.append(item3)

            # updates listbox with selected item
            update3(data3)

        fo3 = open("scripts/autostart.list", "r")
        content3 = fo3.readlines()
        # print(content3)

        inst_btn3 = Label(
            auto_button_frame,
            text="Selected: \n",
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="#d4244d",
            font=(("Helvetica,bold"), "14"),
        )
        inst_btn3.pack(anchor="n")

        inst_btn3 = Button(
            auto_button_frame,
            text="Delete",
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
            command=del_enrty,
        )
        inst_btn3.pack(anchor="s")

        uninst_btn3 = Button(
            auto_button_frame,
            text="Add",
            highlightthickness=0,
            borderwidth=0,
            background="#222222",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
            command=add_auto,
        )
        uninst_btn3.pack(anchor="s")

        # Create an entry box


        my_entry3 = Entry(auto_select_frame, font=("Helvetica", 12), width=60)
        my_entry3.pack()

        note_lbl = Label(
            auto_select_frame,
            text="double click to select",
            background="#222222",
            foreground="yellow",
            font=("Helvetica", 14)
        )
        note_lbl.pack(pady=5)

        global my_list3
        my_list3 = Listbox(auto_select_frame, width=60, height=30)
        my_list3.pack()

        fo3 = open("scripts/autostart.list", "r")
        content3 = fo3.readlines()
        for i3, s3 in enumerate(content3):
            content3[i3] = s3.strip()
        # print(content3)

        # Add toppings
        update3(content3)

        # Create binding
        my_list3.bind("<<ListboxSelect>>", fillout3)
        my_entry3.bind("<KeyRelease>", check3)


# [Autostart Add Entry Child]
class Add_Autostart(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
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
        self["background"] = "#333333"

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def add_enrty():

            if add_name.get() == "" or add_path.get() == "":
                error_mass()
            else:
                file_name = f"{home}/.config/autostart/{add_name.get()}.desktop"
                f = open(file_name, "a+")  # open file in append mode
                f.write(
                    f"[Desktop Entry]\nName={add_name.get()}\nExec={add_path.get()}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true\nHidden=false\n"
                )
                f.close()
                my_list3.insert("end", f"{add_name.get()}.desktop")

                with open("scripts/autostart.list", "a") as file:
                    file.write(f"{add_name.get()}.desktop")

        add_frame = Frame(self, background="#333333")
        add_frame.pack(padx=10, pady=10)

        add_name_lbl = Label(
            add_frame,
            text="Name:",
            justify="left",
            anchor="w",
            width=10,
            background="#333333",
            foreground="white",
        )
        add_name_lbl.grid(row=0, column=0)

        add_path_lbl = Label(
            add_frame,
            text="Path to File:",
            justify="left",
            anchor="w",
            width=10,
            background="#333333",
            foreground="white",
        )
        add_path_lbl.grid(row=1, column=0)

        add_name = Entry(add_frame, width=45)
        add_name.grid(row=0, column=1)

        add_path = Entry(add_frame, width=45)
        add_path.grid(row=1, column=1)

        example_path_lbl = Label(
            add_frame,
            text="Example: /bin/conky",
            justify="left",
            anchor="w",
            width=45,
            background="#333333",
            foreground="white",
        )
        example_path_lbl.grid(row=2, column=1)

        set_auto = Button(
            add_frame,
            text="Add",
            width=10,
            command=add_enrty,
            background="#333333",
            foreground="white",
            highlightthickness=1,
            borderwidth=0,
            highlightcolor="white",
        )
        set_auto.grid(row=3, column=0, pady=5)

        cancel_add = Button(
            add_frame,
            text="Close",
            width=10,
            command=self.destroy,
            background="#333333",
            foreground="white",
            highlightthickness=1,
            borderwidth=0,
            highlightcolor="white",
        )
        cancel_add.grid(row=4, column=0, pady=5)


# [Overclocking_Legend Popup] Child
class Tuning_Legende(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title("Overclocking Legend")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 650
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.tu_1 = PhotoImage(file=r"images/icons/PiGroOV_rm.png")
        self.tu_2 = PhotoImage(file=r"images/icons/PiGroOV1.png")
        self.tu_3 = PhotoImage(file=r"images/icons/PiGroOV2.png")
        self.tu_4 = PhotoImage(file=r"images/icons/PiGroOV3.png")
        self.tu_5 = PhotoImage(file=r"images/icons/PiGroOV4.png")

        # Main Frame
        self.tu_main_frame = Frame(self, bg="#333333")
        self.tu_main_frame.pack(pady=20)

        # Reset
        self.rm_lbl = Label(
            self.tu_main_frame,
            text="Reset Settings",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.rm_lbl.grid(row=0, column=0)

        self.rm_ov = Label(self.tu_main_frame, image=self.tu_1, bg="#333333")
        self.rm_ov.grid(row=1, column=0)

        self.rm_text = Label(
            self.tu_main_frame,
            text="Removes all\noverclocking parameters\n\n",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.rm_text.grid(row=1, column=1)

        # OV_1
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Crank It Up!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=2, column=0)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_2, bg="#333333", fg="white")
        self.ov_1.grid(row=3, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2000\ngpu_freq = 750\nover_voltage = 6\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=3, column=1)

        # OV_2
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="You Sir, Need A Fan!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg="#333333",
            fg="yellow",
            font=("Helvetica", 9),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=1)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_3, bg="#333333", fg="white")
        self.ov_1.grid(row=5, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2147\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=5, column=1)

        # OV_3
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Take It To The Max!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg="#333333",
            fg="yellow",
            font=("Helvetica", 9),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=1)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_4, bg="#333333", fg="white")
        self.ov_1.grid(row=7, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2200\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=7, column=1)

        # OV_4
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Honey,the fuse blew again!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg="#333333",
            fg="yellow",
            font=("Helvetica", 9),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=1)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_5, bg="#333333", fg="white")
        self.ov_1.grid(row=9, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2300\ngpu_freq = 700\nover_voltage = 14\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=9, column=1)

        self.tu_main_frame2 = Frame(self, bg="#333333")
        self.tu_main_frame2.pack(pady=20)


# [Done_Reboot Popup] Child
class Done_Reboot(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
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
        ft = tkFont.Font(family="Helvetica", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = "white"
        cont_btn["bg"] = "#333333"
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 2
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        rebt_btn = tk.Button(self)
        rebt_btn["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        rebt_btn["font"] = ft
        rebt_btn["fg"] = "white"
        rebt_btn["bg"] = "#333333"
        rebt_btn["justify"] = "center"
        rebt_btn["highlightthickness"] = 2
        rebt_btn["borderwidth"] = 0
        rebt_btn["text"] = "Reboot"
        rebt_btn.place(x=160, y=130, width=70, height=25)
        rebt_btn["command"] = self.rebt_btn_command

        done_label = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=14)
        done_label["font"] = ft
        done_label["fg"] = "white"
        done_label["bg"] = "#333333"
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)

    def rebt_btn_command(self):
        popen(f"{legit} reboot")


# [Overclocking_Expert Popup] Child
class Overclocking_Expert(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title("Expert Mode")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
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

        def fi_fy_fo_bar():
            self.title("This tool is great for Youtubers to make useless vidios")

        # Expert Frame
        x_mode_frame = Frame(self, bg="#333333")
        x_mode_frame.pack(pady=20)

        # arm_freq
        arm_freq_label = Label(
            x_mode_frame,
            justify=LEFT,
            text="arm_freq = ",
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        arm_freq_set.grid(row=0, column=2, padx=10, pady=10)

        global arm_freq_reset
        arm_freq_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_arm_freq,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        gpu_freq_set.grid(row=1, column=2)

        global gpu_freq_reset
        gpu_freq_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_gpu_freq,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        gpu_mem_set.grid(row=2, column=2, padx=10, pady=10)

        global gpu_mem_reset
        gpu_mem_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_gpu_mem,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        over_voltage_set.grid(row=3, column=2)

        global over_voltage_reset
        over_voltage_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_over_voltage,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        disable_splash_set.grid(row=4, column=2, padx=10, pady=10)

        global disable_splash_reset
        disable_splash_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_disable_splash,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            bg="#333333",
            foreground="white",
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
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
        )
        force_turbo_set.grid(row=5, column=2)

        global force_turbo_reset
        force_turbo_reset = Button(
            x_mode_frame,
            text="Reset",
            command=reset_force_turbo,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
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
            font=("Helvetica", 12, "bold"),
            text="Reboot",
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=2,
            command=reboot_n,
        )
        reboot_e.pack()

        note_e = Label(
            self,
            justify=LEFT,
            font=("Helvetica", 12, "bold"),
            text="Soon More!",
            bg="#333333",
            foreground="white",
        )
        note_e.pack(pady=20)

        buttton_button = Button(
            self,
            bg="#333333",
            foreground="white",
            borderwidth=0,
            highlightthickness=0,
            command=fi_fy_fo_bar,
        )
        buttton_button.place(x=495, y=595)


# [APT Installer Popup] Child
class APT_Installer_Popup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"Installing ... {apt_inst_combo_box.get()}")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.overrideredirect(True)

        # progressbar
        global inst_show
        inst_show = Label(
            self,
            text="",  # {apt_inst_combo_box.get()}
            bg="#333333",
            fg="white",
        )
        inst_show.pack(pady=20)

        anim = Loading_Throbber(self, "images/icons/loading.gif")
        anim["borderwidth"] = "0"
        anim.pack()

        def stop_it():
            anim.after_cancel(anim.cancel)

        self.apt_inst_termf = Frame(
            self, height=50, width=600, highlightthickness=0, borderwidth=0
        )

        self.apt_inst_wid = self.apt_inst_termf.winfo_id()

        self.apt_inst_termf["background"] = "#333333"
        self.apt_inst_termf.pack(padx=45, pady=20)
        # ää

        def install_parameter():

            if distro_get == "ubuntu":
                os.system(
                    f'xterm -into %d -bg Grey1 -geometry 120x25 -e "pkexec apt install -y {apt_inst_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")

            else:
                os.system(
                    f'xterm -into %d -bg Grey1 -geometry 120x25 -e "sudo apt install -y {apt_inst_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )

                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")

        # place the progressbar

        def GButton_916_command():
            # Inst_compl_Popup.destroy()
            # Installer_Popup.destroy()
            APT_Installer_Popup.destroy(self)

        GButton_916 = tk.Button(self)
        GButton_916["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Helvetica", size=12)
        GButton_916["font"] = ft
        GButton_916["fg"] = "white"
        GButton_916["justify"] = "center"
        GButton_916["bg"] = "#333333"
        GButton_916["text"] = "Close"
        GButton_916.place(x=580, y=200, width=70, height=25)
        GButton_916["command"] = GButton_916_command
        GButton_916.configure(state=DISABLED)

        Thread(target=install_parameter).start()


# [APT Uninstaller Popup] Child
class APT_Uninstaller_Popup(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"Removing ... {apt_un_combo_box.get()}")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 250
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.overrideredirect(True)

        # progressbar
        global inst_show
        inst_show = Label(
            self,
            text="",  # {apt_inst_combo_box.get()}
            bg="#333333",
            fg="white",
        )
        inst_show.pack(pady=20)

        anim = Loading_Throbber(self, "images/icons/loading.gif")
        anim["borderwidth"] = "0"
        anim.pack()

        def stop_it():
            anim.after_cancel(anim.cancel)

        self.apt_inst_termf = Frame(
            self, height=50, width=600, highlightthickness=0, borderwidth=0
        )

        self.apt_inst_wid = self.apt_inst_termf.winfo_id()

        self.apt_inst_termf["background"] = "#333333"
        self.apt_inst_termf.pack(padx=45, pady=20)

        def install_parameter():
            if distro_get == "ubuntu":
                os.system(
                    f'xterm -into %d -bg Grey1 -geometry 120x25 -e "pkexec apt remove -y {apt_un_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")

            else:
                os.system(
                    f'xterm -into %d -bg Grey1 -geometry 120x25 -e "sudo apt remove -y {apt_un_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")

        # place the progressbar

        def GButton_916_command():
            # Inst_compl_Popup.destroy()
            # Installer_Popup.destroy()
            APT_Installer_Popup.destroy(self)

        GButton_916 = tk.Button(self)
        GButton_916["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Helvetica", size=12)
        GButton_916["font"] = ft
        GButton_916["fg"] = "white"
        GButton_916["justify"] = "center"
        GButton_916["bg"] = "grey"
        GButton_916["text"] = "Close"
        GButton_916.place(x=580, y=200, width=70, height=25)
        GButton_916["command"] = GButton_916_command
        GButton_916.configure(state=DISABLED)

        Thread(target=install_parameter).start()


# [Software] Tab
class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def info_installer_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Installer Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/installer_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def pi_apps_list():
            global pop_pi_apps_list
            pop_pi_apps_list = Toplevel()
            pop_pi_apps_list.geometry("700x800")
            pop_pi_apps_list.title("pi_apps_list")
            scrollbar = Scrollbar(pop_pi_apps_list)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_pi_apps_list, yscrollcommand=scrollbar.set)
            text_file = open("scripts/pi-apps_list.list")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)
            # scrollbar.config(command=mylist.yview)

        def info_done():
            global done_pop
            done_pop = Toplevel()
            done_pop.title("")
            # setting window size
            width = 247
            height = 179
            screenwidth = done_pop.winfo_screenwidth()
            screenheight = done_pop.winfo_screenheight()
            alignstr = "%dx%d+%d+%d" % (
                width,
                height,
                (screenwidth - width) / 2,
                (screenheight - height) / 2,
            )
            done_pop.geometry(alignstr)
            done_pop.resizable(width=False, height=False)
            done_pop["bg"] = "#333333"

            def GButton_234_command():
                done_pop.destroy()

            GLabel_198 = tk.Label(done_pop)
            ft = tkFont.Font(family="Helvetica", size=10)
            GLabel_198["font"] = ft
            GLabel_198["fg"] = "white"
            GLabel_198["justify"] = "center"
            GLabel_198["text"] = "label"
            GLabel_198["image"] = self.ip03
            GLabel_198.place(x=10, y=20, width=75, height=76)
            GLabel_198["bg"] = "#333333"

            GLabel_159 = tk.Label(done_pop)
            ft = tkFont.Font(family="Helvetica", size=14)
            GLabel_159["font"] = ft
            GLabel_159["fg"] = "white"
            GLabel_159["justify"] = "center"
            GLabel_159["text"] = "Done!"
            GLabel_159.place(x=90, y=40, width=131, height=32)
            GLabel_159["bg"] = "#333333"

            GButton_234 = tk.Button(done_pop)
            GButton_234["bg"] = "#333333"
            ft = tkFont.Font(family="Helvetica", size=10)
            GButton_234["font"] = ft
            GButton_234["fg"] = "white"
            GButton_234["justify"] = "center"
            GButton_234["text"] = "OK"
            GButton_234.place(x=150, y=130, width=81, height=31)
            GButton_234["command"] = GButton_234_command
            GButton_234["highlightthickness"] = 2
            GButton_234["borderwidth"] = 0

        def open_must_haves():
            os.system(f"python3 {Application_path}/Shop/Shop.py")

        def snapcraft():
            popen("xdg-open https://snapcraft.io/store")

        def flatflat():
            popen("xdg-open https://flathub.org/")

        # images/icons/BG
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.ipshop = PhotoImage(file=r"images/icons/shop.png")
        self.ipfinst = PhotoImage(file=r"images/icons/fast_install.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")

        # Shop
        self.rahmen_shop = Frame(self, borderwidth=0, highlightthickness=1)
        self.rahmen_shop.pack(padx=40, pady=40)
        self.rahmen_shop["background"] = "#333333"

        self.shop_click = Button(
            self.rahmen_shop,
            image=self.ipshop,
            command=open_must_haves,
            highlightthickness=1,
            borderwidth=5,
            background="green",
            foreground="white",
            compound=LEFT,
            width=500,
        )
        self.shop_click.pack()
        self.shop_click_ttp = CreateToolTip(
            self.shop_click,
            "The shop is currently deactivated due to renovations. All installers can be found under Must Haves",
        )
        # Fast_Installer Main_Frame
        self.fast_main_frame = Frame(
            self,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            pady=10,
            padx=10,
        )
        self.fast_main_frame["background"] = "green"
        self.fast_main_frame.pack()

        # Definition Fast Installer Label
        self.sysinf0 = Label(
            self.fast_main_frame,
            image=self.ipfinst,
            compound=LEFT,
            anchor="n",
            font=("Helvetica", 16),
            highlightthickness=0,
            borderwidth=0,
            background="green",
            foreground="white",
        )
        self.sysinf0.pack(pady=5)

        # Sec Fast Frame
        self.fast_sec_frame = Frame(
            self.fast_main_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=1,
            padx=42,
            pady=20,
        )
        self.fast_sec_frame.pack()
        self.fast_sec_frame["background"] = "#333333"

        # apt-get_entry
        self.apt_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.apt_frame.pack()
        self.apt_frame["background"] = "#333333"

        fo = open("scripts/apt_cache.list", "r")
        content = fo.readlines()
        for i, s in enumerate(content):
            content[i] = s.strip()
        # print(content)

        def check_input(event):
            value = event.widget.get()

            if value == "":
                apt_inst_combo_box["values"] = content
            else:
                data = []
                for item in content:
                    if value.lower() in item.lower():
                        data.append(item)
                apt_inst_combo_box["values"] = data

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def inst_btn1():
            if apt_inst_combo_box.get() == "":
                error_mass()
            else:
                inst_pop = APT_Installer_Popup(self)
                inst_pop.grab_set()

        def uninst_btn1():
            popen(f"{legit} synaptic")

        self.p4 = PhotoImage(file=r"images/icons/apt-get.png")

        # self.eingabefeld1 = Entry(self.apt_frame, bd=5, width=31, borderwidth=1)
        global apt_inst_combo_box
        apt_inst_combo_box = ttk.Combobox(self.apt_frame)
        apt_inst_combo_box["values"] = content
        apt_inst_combo_box.bind("<KeyRelease>", check_input)
        apt_inst_combo_box.config(width=30)

        self.apt_inst_btn = Button(
            self.apt_frame,
            text="install",
            command=inst_btn1,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.apt_inst_btn_ttp = CreateToolTip(
            self.apt_inst_btn,
            'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.',
        )

        self.apt_ico = Label(self.apt_frame, image=self.p4, fg="white")
        self.apt_ico["background"] = "#333333"
        self.apt_ico.grid(
            column=0,
            row=0,
        )
        apt_inst_combo_box.grid(column=2, row=0)
        self.apt_inst_btn.grid(column=1, row=0)

        # APT- remove
        self.un_apt_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.un_apt_frame.pack()
        self.un_apt_frame["background"] = "#333333"

        ua_fo = open("scripts/packages.list", "r")
        un_content = ua_fo.readlines()
        for i, s in enumerate(un_content):
            un_content[i] = s.strip()

        def check_input(event):
            value = event.widget.get()

            if value == "":
                self.apt_un_combo_box["values"] = un_content
            else:
                data = []
                for item in un_content:
                    if value.lower() in item.lower():
                        data.append(item)

                self.apt_un_combo_box["values"] = data

        def un_inst_btn1():
            if apt_un_combo_box.get() == "":
                error_mass()
            else:
                uninst_pop = APT_Uninstaller_Popup(self)
                uninst_pop.grab_set()

        self.apt_un_ico = PhotoImage(file=r"images/icons/apt-get.png")

        global apt_un_combo_box
        apt_un_combo_box = ttk.Combobox(self.un_apt_frame)
        apt_un_combo_box["values"] = un_content
        apt_un_combo_box.bind("<KeyRelease>", check_input)
        apt_un_combo_box.config(width=30)

        self.un_apt_inst_btn = Button(
            self.un_apt_frame,
            text="remove",
            command=un_inst_btn1,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="red",
            font=(("Helvetica,bold"), "8"),
        )

        self.apt_ico = Label(self.un_apt_frame, fg="white", width=10)
        self.apt_ico["background"] = "#333333"
        self.apt_ico.grid(
            column=0,
            row=0,
        )
        apt_un_combo_box.grid(column=2, row=0)
        self.un_apt_inst_btn.grid(column=1, row=0)

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=10)

        # pi-apps_entry

        self.pi_apps = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.pi_apps.pack()
        self.pi_apps["background"] = "#333333"

        def inst_pi_apps():
            if self.pi_apps_entry.get() == "":
                error_mass()
            else:
                # entry_text = self.pi_apps_entry.get()
                popen(
                    f"xterm -e 'bash -c \"{Application_path}/pi-apps/manage install {self.pi_apps_entry.get()}; exec bash\"'"
                )

        self.pa6 = PhotoImage(file=r"images/icons/pi-app.png")

        self.pi_apps_ico = Label(
            self.pi_apps, image=self.pa6, text="piapps install", fg="white"
        )
        self.pi_apps_ico["background"] = "#333333"

        self.pi_apps_entry = Entry(self.pi_apps, bd=5, width=31, borderwidth=1)
        self.pi_apps_inst_btn = Button(
            self.pi_apps,
            text="install",
            command=inst_pi_apps,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )

        self.pi_apps_inst_btn3 = Button(
            self.pi_apps,
            text="Search Pi-Apps",
            command=pi_apps_list,
            highlightthickness=1,
            borderwidth=0,
            width=32,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        if piapps_path == False:
            print("INFO: Pi-Apps not found")
            self.pi_apps_entry.insert(0, "Pi-Apps is not installed")
            self.pi_apps_inst_btn.configure(state=DISABLED)

        self.pi_apps_ico.grid(column=0, row=0)
        self.pi_apps_entry.grid(column=2, row=0)
        self.pi_apps_inst_btn.grid(column=1, row=0)
        self.pi_apps_inst_btn3.grid(column=2, row=1)

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=10)

        # snap_entry
        self.snap_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.snap_frame.pack()
        self.snap_frame["background"] = "#333333"

        def inst_btn2():
            if self.snap_entry.get() == "":
                error_mass()
            else:
                popen(
                    f"xterm -e 'bash -c \"{legit} snap install {self.snap_entry.get()}; exec bash\"'"
                )

        self.p6 = PhotoImage(file=r"images/icons/snap.png")

        self.snap_ico = Label(
            self.snap_frame, image=self.p6, text="Snap install", fg="white"
        )
        self.snap_ico["background"] = "#333333"

        self.snap_entry = Entry(self.snap_frame, bd=5, width=31, borderwidth=1)
        self.snap_inst_btn = Button(
            self.snap_frame,
            text="install",
            command=inst_btn2,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.snap_inst_btn_ttp = CreateToolTip(
            self.snap_inst_btn,
            "*to use snap install, you must\napt-get install snapd xD lol",
        )

        self.snapstore_btn = Button(
            self.snap_frame,
            text="Search Snaps",
            command=snapcraft,
            highlightthickness=1,
            borderwidth=0,
            width=32,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        if os.path.isfile("/bin/snap"):
            self.snap_inst_btn.configure(state=NORMAL)
        else:
            self.snap_inst_btn.configure(state=DISABLED)
            self.snap_entry.insert(0, "Snap is not installed")

        self.snap_ico.grid(column=0, row=0)
        self.snap_entry.grid(column=2, row=0)
        self.snap_inst_btn.grid(column=1, row=0)
        self.snapstore_btn.grid(column=2, row=1)

        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=10)

        # flat_entry
        self.flat_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.flat_frame.pack()
        self.flat_frame["background"] = "#333333"

        def inst_btn4():
            if self.flat_entry.get() == "":
                error_mass()
            else:
                popen(
                    f" xterm -e 'bash -c \"{legit} flatpak install flathub {self.flat_entry.get()}; exec bash\"'"
                )

        self.p66 = PhotoImage(file=r"images/icons/flathub.png")

        self.flatp_ico = Label(
            self.flat_frame, image=self.p66, text="Flat install", fg="white"
        )
        self.flatp_ico["background"] = "#333333"

        self.flat_entry = Entry(self.flat_frame, bd=5, width=31, borderwidth=1)
        self.flatp_inst_btn = Button(
            self.flat_frame,
            text="install",
            command=inst_btn4,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.flatp_inst_btn_ttp = CreateToolTip(
            self.flatp_inst_btn,
            "*past without--->>>flatpak install flathub<<< org.mozilla.firefox",
        )

        self.flat_btn = Button(
            self.flat_frame,
            text="Search Flathub",
            command=flatflat,
            highlightthickness=1,
            width=32,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        if os.path.isfile("/bin/flatpak"):
            self.flatp_inst_btn.configure(state=NORMAL)
        else:
            self.flatp_inst_btn.configure(state=DISABLED)
            self.flat_entry.insert(0, "Flatpak is not installed")

        self.flatp_ico.grid(column=0, row=0)
        self.flat_entry.grid(column=2, row=0)
        self.flatp_inst_btn.grid(column=1, row=0)
        self.flat_btn.grid(column=2, row=1)

        self.info_inst_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_installer_tab,
        )
        self.info_inst_btn.place(x=900, y=720)


# [Look] Tab
class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def button_xf4s():
            popen("xfwm4-settings")

        def info_look_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Looks Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/looks_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)
            # scrollbar.config(command=mylist.yview)

        def pi_appear():
            popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")

        def opbox_button():
            popen(f"{legit} obconf")

        def lxap_button():
            popen("lxappearance")

        def xfceappear_button():
            popen("xfce4-appearance-settings")

        def tasksel_button():
            popen(f"xterm -e 'bash -c \"{legit} tasksel; exec bash\"'")

        def xfcelook_f():
            popen("xdg-open https://www.xfce-look.org/browse/cat/")

        def ch_desk():
            popen(
                f"xterm -e 'bash -c \"{legit} update-alternatives --config x-session-manager; exec bash\"'"
            )

        def button_xfwm():
            popen(
                f"xterm -e 'bash -c \"{legit} update-alternatives --config x-window-manager; exec bash\"'"
            )

        def theme_f():
            if get_de == "XFCE":
                popen("sudo thunar /usr/share/themes/")
            else:
                popen("sudo pcmanfm /usr/share/themes/")

        def icon_f():
            if get_de == "XFCE":
                popen("sudo thunar /usr/share/images/icons/")
            else:
                popen("sudo pcmanfm /usr/share/images/icons/")

        def xfcefix():
            popen(
                f"xterm -e 'bash -c \"{legit} apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'"
            )

        def xfcefix2():
            popen(
                f"xterm -e 'bash -c \"{Application_path}/scripts/xfce4fix.sh; exec bash\"'"
            )

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def web_OVC():
            popen("xdg-open https://www.xfce-look.org/browse/")

        # kl
        def set_wp():
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

        # Images/Icons
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.bp06 = PhotoImage(file=r"images/icons/folder.png")
        self.ico_m = PhotoImage(file=r"images/icons/gui_icon.png")
        self.bp03 = PhotoImage(file=r"images/icons/terminal.png")
        self.ico_m2 = PhotoImage(file=r"images/icons/weblink_icon.png")
        self.ip01 = PhotoImage(file=r"images/icons/download_ico.png")
        self.ttp01 = PhotoImage(file=r"images/icons/tuxterm.png")
        self.ip02 = PhotoImage(file=r"images/icons/fix1i.png")
        self.bluetooth = PhotoImage(file=r"images/icons/bluetooth.png")
        self.wifi = PhotoImage(file=r"images/icons/wifi.png")

        # Frame/Button Set
        self.rahmen4 = LabelFrame(
            self,
            text="GUI Tweaks",
            font=("Helvetica", 14, "bold"),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.rahmen4.pack(pady=40, padx=40, fill="both")  #
        self.rahmen4["background"] = "#333333"

        self.in_btn1 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Tasksel",
            font=("Helvetica", 10, "bold"),
            command=tasksel_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn1.grid(column=0, row=0, padx=5)

        self.in_btn2 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Change Desktop",
            command=ch_desk,
            font=("Helvetica", 10, "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn2.grid(column=1, row=0, padx=5)

        self.in_btn3 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Change Win-Manager",
            command=button_xfwm,
            font=("Helvetica", 10, "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn3.grid(column=2, row=0, padx=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.bp06,
            text="Theme Folder",
            font=("Helvetica", 10, "bold"),
            command=theme_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn7.grid(column=0, row=1, padx=5, pady=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.bp06,
            text="Icon Folder",
            font=("Helvetica", 10, "bold"),
            command=icon_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn7.grid(column=1, row=1, padx=5)

        self.xfcelook_ttp = CreateToolTip(
            self.in_btn7,
            "*download the themes extract em and throw it into Theme/Icon Folder",
        )

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.ico_m2,
            text="Get Themes",
            font=("Helvetica", 10, "bold"),
            command=web_OVC,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn7.grid(column=2, row=1, padx=5)

        # xfce_tweaks
        self.rahmen41 = LabelFrame(
            self,
            text="Xfce Tweaks",
            font=("Helvetica", 14, "bold"),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=15,
        )
        self.rahmen41.pack(padx=40, pady=20, fill="both")
        self.rahmen41["background"] = "#333333"

        self.in_btn3 = Button(
            self.rahmen41,
            image=self.ico_m,
            justify="left",
            text="Xfwm4 Settings",
            command=button_xf4s,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn3.grid(column=1, row=0, padx=5)
        self.in_btn3.configure(state=DISABLED)

        self.in_btn5 = Button(
            self.rahmen41,
            image=self.wifi,
            justify="left",
            text="WiFi Fix",
            compound=LEFT,
            command=xfcefix2,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn5.grid(column=3, row=0)
        self.in_btn5.configure(state=DISABLED)

        self.in_btn51 = Button(
            self.rahmen41,
            image=self.bluetooth,
            justify="left",
            text="Bluetooth Fix",
            compound=LEFT,
            command=xfcefix,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn51.grid(column=2, row=0)
        self.in_btn51.configure(state=DISABLED)

        self.in_btn52 = Button(
            self.rahmen41,
            image=self.ico_m,
            justify="left",
            text="Xfce4 Appearance",
            compound=LEFT,
            command=xfceappear_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn52.grid(column=1, row=1)
        self.in_btn52.configure(state=DISABLED)

        self.in_btn7 = Button(
            self.rahmen41,
            image=self.ico_m2,
            justify="left",
            text="Xfce_look",
            compound=LEFT,
            command=xfcelook_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn7.grid(column=2, row=1)
        self.in_btn7.configure(state=DISABLED)

        self.in_btn8 = Button(
            self.rahmen41,
            image=self.ico_m2,
            justify="left",
            text="Make-Me-Xfce",
            compound=LEFT,
            command=xfce_make,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn8.grid(column=3, row=1)

        if get_de == "XFCE":
            self.in_btn3.configure(state=NORMAL)
            self.in_btn5.configure(state=NORMAL)
            self.in_btn51.configure(state=NORMAL)
            self.in_btn52.configure(state=NORMAL)
            self.in_btn7.configure(state=NORMAL)

        # gui_tweaks
        self.rahmen42 = LabelFrame(
            self,
            text="PIXEL Tweaks",
            font=("Helvetica", 14, "bold"),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=FLAT,
            pady=10,
            padx=15,
        )
        self.rahmen42.pack(padx=40, pady=20, fill="both")
        self.rahmen42["background"] = "#333333"

        self.lx_btn0 = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="LXAppearace",
            compound=LEFT,
            command=lxap_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lx_btn0.grid(column=1, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="OpenBox Conf",
            compound=LEFT,
            command=opbox_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lxde.grid(column=2, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Pi Appeariance",
            compound=LEFT,
            command=pi_appear,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lxde.grid(column=3, row=0)

        self.set_wp_btn = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Set Wallpaper",
            compound=LEFT,
            command=set_wp,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.set_wp_btn.grid(column=4, row=0)
        # öü
        self.info_look_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_look_tab,
        )
        self.info_look_btn.place(x=900, y=720)


# [ZRAM] Child
class z_ram_pop(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # self["background"] = "#333333"
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 280
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")

        def z_ram_install():

            if distro_get == "ubuntu":
                popen(
                    f"xterm -e 'bash -c \"{legit} apt install zram-config ; exec bash\"'"
                )
            else:
                popen(
                    f"xterm -e 'bash -c \"{legit} apt install zram-tools; exec bash\"'"
                )

            Notification(
                title="ZRAMr\n",
                description="ZRAM has been installed",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # ää
        def z_ram_uninstall():

            if distro_get == "ubuntu":
                popen(
                    f"xterm -e 'bash -c \"{legit} apt remove zram-config ; exec bash\"'"
                )
            else:
                popen(
                    f"xterm -e 'bash -c \"{legit} apt remove zram-tools; exec bash\"'"
                )

            Notification(
                title="ZRAMr\n",
                description="ZRAM has been uninstalled",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        GLabel_804 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.ip03
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "ZRAM"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Zram is a Linux kernel module that allows\nyou to set up compressed filesystems in RAM.\nzram-tools uses this module to set up compressed \nswap space.\nThis is useful on systems with low memory or servers\nrunning a large amount of services with data that's\neasily swappable but that you may wish to swap back\nfast without sacrificing disk bandwidth.\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = z_ram_install

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = z_ram_uninstall


# [Tuning] Tab
class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        # Current OV settings
        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def generate_lines_that_equal(string, fp):
            for line in fp:
                if line == string:
                    yield line

        def info_tuning_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Tuning Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/tuning_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def tuning_legende():
            tu_le = Tuning_Legende(self)
            tu_le.grab_set()

        def z_ram():
            z_ram = z_ram_pop(self)
            z_ram.grab_set()

        def expert_mode():
            x_mode = Overclocking_Expert(self)
            x_mode.grab_set()

        # BG + Icons

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.rm_ov_icon = PhotoImage(file=r"images/icons/PiGroOV_rm.png")
        self.ov1_icon = PhotoImage(file=r"images/icons/PiGroOV1.png")
        self.ov2_icon = PhotoImage(file=r"images/icons/PiGroOV2.png")
        self.ov3_icon = PhotoImage(file=r"images/icons/PiGroOV3.png")
        self.ov4_icon = PhotoImage(file=r"images/icons/PiGroOV4.png")
        self.ov5_icon = PhotoImage(file=r"images/icons/PiGroOV5.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")
        self.tu_legend_ico = PhotoImage(file=r"images/icons/legende.png")
        self.zram_icon = PhotoImage(file=r"images/icons/zram.png")

        # OV Notifications

        def done_msg():
            d_msg = Done_Reboot(self)
            d_msg.grab_set()

        # overclocking_default/reset

        def set_default():
            os.system(
                f"xterm -e 'bash -c \"{legit} {Application_path}/scripts/rm_ov.sh && exit; exec bash\"'"
            )
            done_msg()
            tu_btn1.config(state=NORMAL)
            tu_btn2.config(state=NORMAL)
            tu_btn3.config(state=NORMAL)
            tu_btn4.config(state=NORMAL)

            pigro_t_display.config(text="not nonfigured", fg="green")
            arm_f_display.config(text="not configured")
            gpu_f_display.config(text="not configured")
            gpu_m_display.config(text="not configured")
            over_v_display.config(text="not configured")
            force_t_display.config(text="not configured")

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
                f"""{legit} sh -c 'echo "#Pigro_Overclocking1\narm_freq=2000\ngpu_freq=750\nover_voltage=6\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
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
                f"""{legit} sh -c 'echo "#Pigro_Overclocking2\narm_freq=2147\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
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

            popen(f"mpg123 {Application_path}/scripts/HOLYPiT.mp3")

        # overclocking_2200

        def ov_2200():
            os.system(
                f"""{legit} sh -c 'echo "#Pigro_Overclocking3\narm_freq=2200\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )
            popen(f"mpg123 {Application_path}/scripts/over9000.mp3")
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
                f"""{legit} sh -c 'echo "#Pigro_Overclocking4\narm_freq=2300\ngpu_freq=700\nover_voltage=14\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )
            popen(f"mpg123 {Application_path}/scripts/over9000.mp3")
            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2300\ngpu_fequ = 700\nover_voltage = 14\nforce_turbo = 1",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        # OV_Button_Frame
        self.ov_buttons = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
            padx=20,
        )
        self.ov_buttons.pack(side=LEFT, pady=20, padx=20, fill=BOTH)
        self.ov_buttons["background"] = "#222222"

        # Overclocking State Main Frame
        self.ov_state_display_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.ov_state_display_frame.pack(
            anchor="n", padx=10, pady=20, fill=BOTH, expand=True
        )
        self.ov_state_display_frame["background"] = "#222222"

        self.settings_header = Label(
            self.ov_state_display_frame,
            text="Current Settings",
            highlightthickness=0,
            borderwidth=2,
            background="#222222",
            foreground="#d4244d",
            font=("Helvetica", 16),
            justify="left",
        ).pack(pady=20)

        # Overclocking Values Frame
        self.ov_display_frame = Frame(
            self.ov_state_display_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=5,
            pady=5,
        )
        self.ov_display_frame.pack(anchor="n")
        self.ov_display_frame["background"] = "#222222"

        # ZRAM Button
        self.tu_zbtn = Button(
            self.ov_state_display_frame,
            image=self.zram_icon,
            text="Install ZRAM",
            font=("Helvetica", 12),
            anchor="w",
            command=z_ram,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            compound=LEFT,
            foreground="#d4244d",
        ).pack(pady=20)

        # Additional Infos

        self.ov_helps_frame = Frame(
            self.ov_state_display_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.ov_helps_frame.pack(padx=20)
        self.ov_helps_frame["background"] = "#222222"

        # Overclocking Stats

        # Tuning_Button_Frame
        pigro_t_label = Label(
            self.ov_display_frame,
            anchor="e",
            justify=RIGHT,
            text="PiGro Berry: ",
            highlightthickness=0,
            borderwidth=2,
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="green",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
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
            background="#222222",
            foreground="white",
            font=("Helvetica", 12, "bold"),
            width=25,
        )
        force_t_display.grid(column=1, row=6)

        self.tu_info = Label(
            self.ov_helps_frame,
            text="Settings tested with:\nRaspberry Pi 4B 8 GB Rev.1.4\nRaspberry Pi 4B 4 GB Rev.1.1\n+ Ice Tower Cooler & Pi400.\nI take no responsibility if\nyour Pi is damaged.\nPlease click on the Info Button\nto learn more",
            font=("Helvetica", 8),
            highlightthickness=0,
            borderwidth=2,
            background="#222222",
            foreground="yellow",
        ).pack()

        # Tuning_Button_Frame
        self.tuning_options = Label(
            self.ov_buttons,
            text="Overclocking Options",
            highlightthickness=0,
            borderwidth=2,
            background="#222222",
            foreground="#d4244d",
            font=("Helvetica", 16),
            justify="left",
        ).grid(column=0, row=1, pady=10)

        self.tu_reset = Button(
            self.ov_buttons,
            justify="left",
            image=self.rm_ov_icon,
            text="Reset Overclocking",
            anchor="w",
            command=set_default,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
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
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
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
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
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
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
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
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        tu_btn4.grid(column=0, row=9, pady=10)

        global tu_btn5
        tu_btn5 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov5_icon,
            text="I really like typing\nin random numbers and\nsee what happens!",
            command=expert_mode,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        tu_btn5.grid(column=0, row=10, pady=10)

        self.tu_legende = Button(
            self.ov_buttons,
            text="Legende",
            font=("Helvetica", 8),
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="yellow",
            command=tuning_legende,
            image=self.tu_legend_ico,
        ).grid(column=0, row=11, pady=10)

        def ov_display():
            # Overclock Display Functions
            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking1", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="Crank It Up",
                            fg="yellow",
                            bg="#222222",
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
                            text="Need A Fan!",
                            fg="red",
                            bg="#222222",
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
                            fg="pink",
                            bg="#222222",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)

            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking4", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="Honey,the fuse blew again!",
                            fg="purple",
                            bg="#222222",
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
                        fg="white",
                        bg="#222222",
                        font=("Helvetica", 12, "bold"),
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
                        fg="white",
                        bg="#222222",
                        font=("Helvetica", 12, "bold"),
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
                        fg="white",
                        bg="#222222",
                        font=("Helvetica", 12, "bold"),
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
                        fg="white",
                        bg="#222222",
                        font=("Helvetica", 12, "bold"),
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
                        fg="white",
                        bg="#222222",
                        font=("Helvetica", 12, "bold"),
                    )

        def refresh_OV_stats():
            ov_display()
            self.after(3000, refresh_OV_stats)

        refresh_OV_stats()

        self.info_tuning_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_tuning_tab,
        )
        self.info_tuning_btn.place(x=900, y=700)


# [Links] Tab
class Frame7(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def down_twist():
            popen("xdg-open https://twisteros.com/")

        def down_NCP():
            popen("xdg-open https://ownyourbits.com/nextcloudpi/")

        def down_puppy():
            popen("xdg-open https://puppylinux.com/")

        def down_diet():
            popen("xdg-open https://dietpi.com/")

        def down_mx():
            popen(
                "xdg-open https://mxlinux.org/blog/fluxbox-raspberrypi-respin-ragout-beta/"
            )

        def down_fy():
            popen("xdg-open https://releases.fydeos.io/11.4/rpi4-fydeos")

        def down_kk():
            popen("xdg-open https://konstakang.com/devices/rpi4/")

        def down_bb():
            popen("xdg-open https://berryboot.alexgoldcheidt.com/images")

        def link_mankier():
            popen("xdg-open https://mankier.com")

        def link_guake():
            popen("xdg-open https://github.com/Guake/guake")

        def link_onBoard():
            popen("xdg-open https://wiki.ubuntuusers.de/Barrierefreiheit/onBoard/")

        def link_drac():
            popen("xdg-open https://draculatheme.com/")

        def link_star():
            popen("xdg-open https://starship.rs/")

        def lern_l():
            popen("xdg-open https://www.learnlinux.tv/")

        def rb_tv():
            popen("xdg-open https://rocketbeans.tv/")

        def l4_e():
            popen("xdg-open http://www.lcdwiki.com/Main_Page")

        def fitwo_p():
            popen("xdg-open https://www.52pi.com/")

        def ubi_bubi():
            popen("xdg-open https://ubuntu.com/download/raspberry-pi")

        def popo_bubi():
            popen("xdg-open https://pop.system76.com/")

        def six4_berry():
            popen("xdg-open https://downloads.raspberrypi.org/raspios_arm64/images/")

        def pi_doc():
            popen("xdg-open https://www.raspberrypi.com/documentation/")

        def pi_tuto():
            popen("xdg-open https://tutorials-raspberrypi.com/")

        def vis_tk():
            popen("xdg-open https://visualtk.com/")

        def papirus_nord():
            popen("xdg-open https://github.com/Adapta-Projects/Papirus-Nord")

        # äö
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.di01 = PhotoImage(file=r"images/icons/TwisterOSLogo-Large-New3.png")
        self.di02 = PhotoImage(file=r"images/icons/Puppy_Linux_Logo.png")
        self.di03 = PhotoImage(file=r"images/icons/dietpi.png")
        self.di04 = PhotoImage(file=r"images/icons/MX-icon.png")
        self.di05 = PhotoImage(file=r"images/icons/fydeos.png")
        self.di06 = PhotoImage(file=r"images/icons/android.png")
        self.di06 = PhotoImage(file=r"images/icons/android.png")
        self.di07 = PhotoImage(file=r"images/icons/logo_berryserver.png")
        self.di08 = PhotoImage(file=r"images/icons/NCP.png")
        self.pop_os_ico = PhotoImage(file=r"images/icons/popo_os_icon.png")
        self.ubu_os_ico = PhotoImage(file=r"images/icons/Logo-ubuntu_.png")
        self.pi64_os_ico = PhotoImage(file=r"images/icons/Raspberry_Pi_Logo.png")

        self.rahmen = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            padx=10,
            pady=20,
        )
        self.rahmen.grid(row=0, rowspan=11, column=0, pady=20, padx=40)
        self.rahmen["background"] = "#333333"

        sys_btn2 = Label(
            self.rahmen,
            text="Distros",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 16, "bold"),
        )
        sys_btn2.pack()

        self.dist_btn1 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di01,
            anchor="w",
            text="Twister OS ",
            command=down_twist,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn2 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di02,
            anchor="w",
            text="Puppy Linux",
            command=down_puppy,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn3 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di03,
            anchor="w",
            text="DietPi     ",
            command=down_diet,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn4 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di04,
            anchor="w",
            text="MX Linux   ",
            command=down_mx,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn5 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di05,
            anchor="w",
            text="FydeOS     ",
            command=down_fy,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn6 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di06,
            anchor="w",
            text="Android    ",
            command=down_kk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn7 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di07,
            anchor="w",
            text="Berryserver",
            command=down_bb,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn8 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di08,
            anchor="w",
            text="NextCloudPi",
            command=down_NCP,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn9 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.ubu_os_ico,
            anchor="w",
            text="Ubuntu",
            command=ubi_bubi,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn10 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.pop_os_ico,
            anchor="w",
            text="Pop_OS",
            command=popo_bubi,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.fast_sec_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=3,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
        )
        self.fast_sec_frame.grid(row=0, column=1, pady=20)
        self.fast_sec_frame["background"] = "#333333"

        sys_btn2 = Label(
            self.fast_sec_frame,
            text=" Other ",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 14, "bold"),
        )
        sys_btn2.pack()

        self.choice_link1 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Mankier.com (Commandline Database)",
            command=link_mankier,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Guake (Drop Down Terminal)",
            command=link_guake,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="OnBoard (Onscreen Keyboard)",
            command=link_onBoard,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Draculatheme.com",
            command=link_drac,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Starship (Cross-Shell-Promt)",
            command=link_star,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link1 = Button(
            sys_btn2,
            width=50,
            text="LernLinux.tv",
            anchor="w",
            command=lern_l,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Rocket Beans(ger.)",
            anchor="w",
            command=rb_tv,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="52Pi",
            anchor="w",
            command=fitwo_p,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="LCD Wiki",
            anchor="w",
            command=l4_e,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Offical Raspberry Pi Documentation",
            anchor="w",
            command=pi_doc,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Raspberry Pi Tutorials",
            anchor="w",
            command=pi_tuto,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="VisualTk.com",
            anchor="w",
            command=vis_tk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Papirus Nord Icon Theme",
            anchor="w",
            command=papirus_nord,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()


# [Poll] Tab
class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.auto_start = PhotoImage(file=r"images/icons/actionschnitzel_logo.png")

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        def poll():
            popen("xdg-open http://www.actionschnitzel.de/Pig-Grow-Poll/")

        def wpaps():
            popen("xdg-open http://www.actionschnitzel.de/Wallpapers/")

        def wiki():
            popen("xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki")

        def red_bub():
            popen(
                "xdg-open https://www.redbubble.com/de/people/Actionschnitzel/shop?asc=u"
            )

        self.rahmen102 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=2, pady=10, padx=10
        )
        self.rahmen102.pack(fill=BOTH, padx=50, pady=20)
        self.rahmen102["background"] = "#333333"

        self.actn_shn = Label(
            self.rahmen102,
            image=self.auto_start,
            background="#333333",
        ).pack(pady=20)

        self.poke_pig_21 = Label(
            self.rahmen102,
            justify="left",
            text="I never thought that so many people would use Pigro.\nAs open source lives from community,I want you to have a say in that too.\nIf you click on poll, you can vote on what else I should add to Pigro.\nSo ... let's fatten up the hog! xD\nIf you want to support me, click on the RedBubble button below.\nHere you can get Pi / Linux design from me.\n\nBest regards\n\nTimo\n\nQuestions or suggestions?:",
            font=("Helvetica", 12),
            background="#333333",
            fg="white",
            padx=5,
            pady=3,
        ).pack()

        self.mail = Entry(self.rahmen102, bd=5, width=31, borderwidth=1)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.rahmen101 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2)
        self.rahmen101.pack(fill=BOTH, padx=50, pady=20)
        self.rahmen101["background"] = "#333333"

        self.pig_btn_1 = Button(
            self.rahmen101,
            text="User Poll",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#2FFC05",
            command=poll,
            font=(("Helvetica,bold"), "12", "bold"),
        ).pack()

        self.pig_btn_2 = Button(
            self.rahmen101,
            text="Wallpapers",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#EBFC05",
            command=wpaps,
            font=(("Helvetica,bold"), "12", "bold"),
        ).pack()

        self.pig_btn_3 = Button(
            self.rahmen101,
            text="PiGro Manuel",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#053AFC",
            command=wiki,
            font=(("Helvetica,bold"), "12", "bold"),
        ).pack()

        self.pig_btn_4 = Button(
            self.rahmen101,
            text="Redbubble.com",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#FC05A0",
            command=red_bub,
            font=(("Helvetica,bold"), "12", "bold"),
        ).pack()



# [Cam] Tab
class Frame9(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def photo1():
            photo = str(entry.get())
            popen(f"libcamera-jpeg -o {home}/{photo}.jpg")

        def video1():
            video = str(entry.get())
            rec_time = str(sec_entry.get() + "000")
            popen(f"libcamera-vid -t {rec_time} -o {home}/{video}.h264")


        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg, bg="#333333")
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.rahmen101 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=5, pady=20, padx=10
        )
        self.rahmen101.pack(pady=50)
        self.rahmen101["background"] = "#333333"

        self.btn_frame = Frame(self.rahmen101, bg="#333333")
        self.btn_frame.pack()
        self.label = Label(
            self.btn_frame,
            text="#NOTE: This is experimentel\nDon't know it will be continued ;-)\nand it works with the new camlibs",
            bg="#333333",
            fg="white",
        )
        self.label.pack()

        self.welcome_icon = PhotoImage(file=r"~/PiGro-Aid-/images/icons/Pi-Camera.png")
        self.head_frame = Frame(self.rahmen101, bg="#333333")
        self.head_frame.pack()
        self.header_label = Label(
            self.head_frame, image=self.welcome_icon, bg="#333333"
        )
        self.header_label.pack(pady=20)

        # Clicker_Frame
        self.btn_frame = Frame(self.rahmen101, bg="#333333")
        self.btn_frame.pack()
        self.label = Label(
            self.btn_frame,
            text=f"Files will be saved in:\n{home}\n\nGive it a Name:",
            bg="#333333",
            fg="white",
        )
        self.label.pack()

        entry = Entry(self.btn_frame, bd=5, width=31, borderwidth=1)
        entry.pack()
        photo_btn = Button(
            self.btn_frame,
            text="Take A Photo",
            command=photo1,
            bg="#333333",
            fg="white",
            highlightthickness=0,
        )
        photo_btn.pack(pady=10)

        video_btn = Button(
            self.btn_frame,
            text="Take A Video",
            command=video1,
            bg="#333333",
            fg="white",
            highlightthickness=0,
        )
        video_btn.pack()

        sec_ent_label = Label(
            self.btn_frame,
            text="REC time in seconds:",
            bg="#333333",
            fg="white",
        )
        sec_ent_label.pack()

        sec_entry = Entry(self.btn_frame, bd=5, width=5, borderwidth=1)
        sec_entry.pack()




# [Error Massage] Child
class Error_Mass(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
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

        error_frame = Frame(self, bg="#333333")
        error_frame.pack(pady=10)

        error_img = Label(error_frame, image=self.e_m, bg="#333333")
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(error_frame, text="Y U MAKE ERROR?", fg="white", bg="#333333")
        error_y.grid(row=0, column=1)

        error_y2 = Label(
            error_frame, text="You did not enter a value", fg="white", bg="#333333"
        )
        error_y2.grid(row=1, column=1)

        error_btn = Button(
            error_frame, text="OK OK OK!", fg="white", bg="#333333", command=cu_error
        )
        error_btn.grid(row=3, column=1)


# [TOOLTIPZ]
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text="widget info"):
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
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


# [THROBBER]
class Loading_Throbber(Label):
    def __init__(self, master, filename):
        im = Image.open(filename)
        seq = []
        try:
            while 1:
                seq.append(im.copy())
                im.seek(len(seq))  # skip to next frame
        except EOFError:
            pass  # we're done

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
