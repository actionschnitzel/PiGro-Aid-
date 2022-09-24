#!/usr/bin/python3
from curses.textpad import Textbox
from distutils.filelist import translate_pattern
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
from turtle import width
import re
import uuid


# Say Hallo!
global user
user = os.getlogin()
print(f"[Info]: Hi,{user} waz uuuuup?!")

# Define Home
global home
home = str(Path.home())
print(f"[Info]: {home} is your home directory!")

# Gets path to PiGro
global Application_path
Application_path = str(os.getcwd())
print(f"[Info]: PiGro directory is {Application_path}")

# Makes all .sh files in /sripts executable if PiGro in $HOME
if Application_path == f"{home}/PiGro-Aid-":
    popen('find ~/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;')
    print(f"[Info]: All files executable")

# Checks if settings folder exists
pigro_conf_folder = os.path.isdir(f"{home}/.pigro")  # Need full path
if pigro_conf_folder == False:
    print("[Info]: Folder:.pigro not found will created")
    os.mkdir(f"{home}/.pigro")
    open(f"{home}/.pigro/apt_cache.list", "a").close()
    open(f"{home}/.pigro/autostart.list", "a").close()
    open(f"{home}/.pigro/packages.list", "a").close()
    open(f"{home}/.pigro/pi-apps_list.list", "a").close()
if pigro_conf_folder == True:
    print("[Info]: Folder: .pigro exsists")

# Checks if pigro.conf exists
pigro_conf_file = os.path.exists(f"{home}/.pigro/pigro.conf")  # Need full path
if pigro_conf_file == False:
    open(f"{home}/.pigro/pi-apps_list.list", "a")
    with open(f"{home}/.pigro/pigro.conf", "a") as p_file:
        p_file.write(
            "[PiGro - Just Click It! Configs]\n\nfirst_run = true\ntheme = dark\ntransparency = 1.00"
        )
        p_file.close()
    print("[Info]: pigro.conf created")
if pigro_conf_file == True:
    print("[Info]: pigro.conf exsists")


# Checks if pigro bin exists
popen(f"{Application_path}/scripts/check_bin.sh ")

# Gets list of all pakages avaleble on APT
os.system(
    f"xterm > /dev/null 2>&1 -e 'bash -c \"apt-cache pkgnames > /home/{user}/.pigro/apt_cache.list && exit; exec bash\"'"
)
print("[Info]: APT-CACHE loaded")

# Gets list of all installed pakages
os.system(
    f"xterm > /dev/null 2>&1 -e 'bash -c \"dpkg --get-selections > /home/{user}/.pigro/packages.list && sed -e s/install//g -i /home/{user}/.pigro/packages.list && exit; exec bash\"'"
)
print("[Info]: Instaled pakages loaded")

# Get Distro
distro_get = distro.id()
print("[Info]: Your Distro is: " + str(distro_get))

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
print("[Info]: Your DE is: " + str(get_de))

# Checks if pi-apps exists
global piapps_path
piapps_path = os.path.isdir(f"{home}/pi-apps")  # Need full path
if piapps_path == False:
    print("[Info]: Pi-Apps not found")
if piapps_path == True:
    print("[Info]: Pi-Apps is installed list will be added")
    popen(f"ls ~/pi-apps/apps/ > /home/{user}/.pigro/pi-apps_list.list")


# Checks if snapd exists
if os.path.isfile("/bin/snap"):
    print("[Info]: Snap is installed")
else:
    print("[Info]: Snap is not installed")

# Checks if flatpak exists
if os.path.isfile("/bin/flatpak"):
    print("[Info]: Flatpak is installed")
else:
    print("[Info]: Flatpak is not installed")

# Checks if pigro.conf exists
if os.path.isfile(f"{home}/.pigro/pigro.conf"):
    print("[Info]: pigro.conf exists")
else:
    print("[Info]: pigro.conf not found")
    with open(f"{home}/.pigro/pigro.conf", "a") as myfile:
        myfile.write(
            "[PiGro - Just Click It! Configs]\n\nfirst_run = true\ntheme = dark"
        )
        print("[Info]: pigro.conf was created")


conf_file = open(f"{home}/.pigro/pigro.conf", "r")
loglist = conf_file.readlines()
conf_file.close()

for line in loglist:
    # Dark Theme Settings
    if str("theme = dark") in line:
        print("[Info]: Dark Theme")
        global maincolor
        maincolor = "#404040"
        global nav_color
        nav_color = "#353535"
        global frame_color
        frame_color = "#404040"
        global main_font
        main_font = "white"
        global info_color
        info_color = "yellow"
        global ext_btn
        ext_btn = "#0075b7"

    # Dark Theme Settings
    if str("theme = light") in line:
        print("[Info]: Light Theme")
        maincolor = "#ededed"
        nav_color = "#b6b6b3"
        frame_color = "#ededed"
        main_font = "black"
        info_color = "#0075b7"
        ext_btn = "#b6b6b3"

# Transparency Settings
conf_file = open(f"{home}/.pigro/pigro.conf", "r")
loglist = conf_file.readlines()
conf_file.close()

for line in loglist:

    if str("transparency = 1.00") in line:
        print("[Info]: No Transparency")
        global translate_p
        translate_p = "1.00"

    if str("transparency = 0.95") in line:
        translate_p = "0.95"
        print("[Info]: Transparency 5%")


# [Main Window / Notebook Config]
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        """defines the look of the app"""

        # Window Basics
        self.title("PiGro - Just Click It! (Perche sei cosi serio?)")
        self.icon = tk.PhotoImage(file="images/icons/pigro_icons/256x256.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self["background"] = maincolor
        self.resizable(0, 0)
        app_width = 1200
        app_height = 800
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.wait_visibility(self)
        self.wm_attributes("-alpha", translate_p)

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
        self.Frame14 = Frame14(self.notebook)
        self.Frame10 = Frame10(self.notebook)

        # Notebook Icons
        self.status_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/com.github.hannesschulze.optimizer.png"
        )
        self.system_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/kcontrol.png")
        self.update_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/aptdaemon-upgrade.png"
        )
        self.install_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/softwarecenter.png"
        )
        self.look_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/com.github.cassidyjames.palette.png"
        )
        self.tuning_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/blackmagicraw-speedtest.png"
        )
        self.links_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/applications-webapps.png"
        )
        self.support_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/4137_winhlp32.0.png"
        )
        self.cam_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/gtkam-camera.png")
        self.ubuntu_icon = PhotoImage(
            file=r"images/icons//papirus/48x48/distributor-logo-ubuntu.png"
        )
        self.auto_start = PhotoImage(
            file=r"images/icons//papirus/48x48/cs-startup-programs.png"
        )
        self.kill_proc = PhotoImage(
            file=r"images/icons//papirus/48x48/appimagekit-gqrx.png"
        )
        self.git_more = PhotoImage(
            file=r"images/icons//papirus/48x48/git-dag.png")

        # Puts tabs in nav bar
        self.notebook.add(
            self.Frame1, compound=LEFT, text="Dashboard", image=self.status_icon
        )

        self.notebook.add(
            self.Frame3, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.Frame12, compound=LEFT, text="System", image=self.system_icon
        )

        self.notebook.add(
            self.Frame2, compound=LEFT, text="Update", image=self.update_icon
        )

        self.notebook.add(
            self.Frame5, compound=LEFT, text="Look & Feel", image=self.look_icon
        )

        self.notebook.add(
            self.Frame13, compound=LEFT, text="Autostart", image=self.auto_start
        )

        self.notebook.add(
            self.Frame14, compound=LEFT, text="Tasks", image=self.kill_proc
        )

        self.notebook.add(
            self.Frame4, compound=LEFT, text="Software", image=self.install_icon
        )

        self.notebook.add(
            self.Frame10, compound=LEFT, text="Git & More", image=self.git_more
        )

        self.notebook.add(
            self.Frame6, compound=LEFT, text="Tuning", image=self.tuning_icon
        )

        self.notebook.add(
            self.Frame9, compound=LEFT, text="Pi Camera", image=self.cam_icon
        )
        self.notebook.hide(self.Frame9)

        self.notebook.add(
            self.Frame7, compound=LEFT, text="Links", image=self.links_icon
        )

        self.notebook.add(
            self.Frame8, compound=LEFT, text="About", image=self.support_icon
        )

        self.notebook.pack(fill="both", expand=True, anchor=W)

        if distro_get == "debian" or distro_get == "raspbian":
            self.notebook.hide(self.Frame12)

        if distro_get == "ubuntu":
            self.notebook.hide(self.Frame3)
            self.notebook.hide(self.Frame5)
            self.notebook.hide(self.Frame9)

        # Notebook Theming
        global noteStyler
        noteStyler = ttk.Style(self)
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
            font=("Sans", 16),
            width=13,
            highlightthickness=0,
        )
        noteStyler.configure("TFrame", background=maincolor)
        noteStyler.map(
            "TNotebook.Tab",
            background=[("selected", nav_color)],
            foreground=[("selected", "#d4244d")],
        )
        noteStyler.configure(
            "red.Horizontal.TProgressbar", foreground="red", background="green"
        )
        noteStyler.configure("Line.TSeparator", background="grey")


# [Changelog] Child
class Change_Log(tk.Toplevel):
    """ "child window to display the changelog"""

    def __init__(
        self,
        parent,
    ):
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
        self.update_info_btn = PhotoImage(
            file=r"images/icons/pigro_icons/128x128.png")
        logo_lbl = Label(
            self,
            image=self.update_info_btn,
            text="Changelog",
            highlightthickness=0,
            borderwidth=0,
            compound=TOP,
            font=("Sans", 20, "bold"),
        )
        logo_lbl.pack(pady=20)
        changelog_label = Label(
            self,
            justify="left",
            anchor=W,
            text="#Light/Dark Mode (matches RPiOS Theme & Linux Mint Dark Theme)\n#Moste Icons are taken from Papirus Icon Theme\n#Main Frames are replaced with LabelFrames\n#Welcome Tab is now Dashboard\n#Added: User Name to Dashboard\n#Added: MAC Address to Dashboard\n#Added: Hide Sensitiv Data Button\n#System Settings are now categorized\n#Added: dpkg --configure -a button\n#Look Tab is now Look & Feel\n#Buttons for Backup, Restore & Restart lxpanel\n#Added: Light/Dark Theme option\n#Added: Transparacy option\n#Changed: Moved all apps from shop that are in the\nRepo as instant installer to Software tab\n#Added: New Tab Git & More\n#This tab containes stuff from github ore else where\n#Is now About\n#Backgrounds, Pi-Cam Tab",
        )
        changelog_label.pack()


# [Dashboard] Tab
class Frame1(ttk.Frame):
    """shows system stats, user name, an changelog"""

    def __init__(
        self,
        container,
    ):
        super().__init__()

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

        # Hide/Show sensetiv data
        def Simpletoggle():
            if self.toggle_button.config("text")[-1] == "ON":
                self.toggle_button.config(text="OFF")
                self.sysinfn.config(text=f"User Name: {user}")
                self.sysinf_ip.config(text=f"IP Address: {IPAddr}")
                self.sysinf_ma.config(text=f"MAC Address: {get_mac}")
                self.toggle_button.config(background=ext_btn)
            else:
                self.toggle_button.config(text="ON")
                self.sysinfn.config(text="User Name: XXXXXXXXXXXXX")
                self.sysinf_ip.config(text=f"IP Address: XXXXXXXXXXXXX")
                self.sysinf_ma.config(text=f"MAC Address: XXXXXXXXXXXXX")
                self.toggle_button.config(background="green")

        # MAC Address
        get_mac = ":".join(re.findall("..", "%012x" % uuid.getnode()))

        # HDD usage
        obj_Disk = psutil.disk_usage("/")

        # Hide/Show Butten & Label
        self.sensitiv = Label(
            self,
            text=f"Hide Sensitiv Data:",
            justify="left",
            background=maincolor,
            foreground=main_font,
            font=("Sans", 10),
            anchor=W,
        ).place(x=120, y=762)

        self.toggle_button = Button(
            text="OFF",
            font=("Sans", 10),
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            width=10,
            command=Simpletoggle,
        )
        self.toggle_button.place(x=500, y=760)

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

        # Main frame for system stats

        self.sys_logo = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="#d4244d",
            relief=GROOVE,
            pady=20,
            padx=30,
        )

        self.sys_logo.pack()
        self.sys_logo["background"] = maincolor

        self.raspi_img = ImageTk.PhotoImage(
            Image.open("images/icons/pi4b.png"))
        self.pigro_img = ImageTk.PhotoImage(
            Image.open("images/icons/pigro_icons/pigrologo.png")
        )

        # Sys Info Labels
        self.sysinf_btn = Label(
            self.sys_logo,
            image=self.pigro_img,
            borderwidth=0,
            bg=maincolor,
            highlightthickness=0,
        )
        self.sysinf_btn.pack(pady=20)



        self.info_main_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="#d4244d",
            relief=GROOVE,
            pady=20,
            padx=30,
        )

        self.info_main_frame.pack()
        self.info_main_frame["background"] = maincolor


        self.sys_info_main_frame = Frame(
            self.info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="#d4244d",
            relief=GROOVE,
            pady=20,
            padx=30,
        )

        self.sys_info_main_frame.pack(side=LEFT)
        self.sys_info_main_frame["background"] = maincolor

        self.sys_info_main_frame2 = Frame(
            self.info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="#d4244d",
            relief=GROOVE,
            pady=20,
            padx=30,
        )

        self.sys_info_main_frame2.pack(side=LEFT)
        self.sys_info_main_frame2["background"] = maincolor


        # Contains all stats

        self.sys_frame_1 = LabelFrame(
            self.sys_info_main_frame,text="System Info",font=("Sans",16,),foreground="#d4244d", borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=10
        )
        self.sys_frame_1.pack(pady=5,padx=5)
        self.sys_frame_1["background"] = nav_color

        self.sys_frame_2 = LabelFrame(
        self.sys_info_main_frame,text="CPU",font=("Sans",16,),foreground="#d4244d", borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=10
        )
        self.sys_frame_2.pack(pady=5,padx=5)
        self.sys_frame_2["background"] = nav_color

        self.sys_frame_3 = LabelFrame(
        self.sys_info_main_frame2,text="Memory",font=("Sans",16,),foreground="#d4244d", borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=10
        )
        self.sys_frame_3.pack(pady=5,padx=5)
        self.sys_frame_3["background"] = nav_color

        self.sys_frame_4 = LabelFrame(
        self.sys_info_main_frame2,text="Network",font=("Sans",16,),foreground="#d4244d", borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=10
        )
        self.sys_frame_4.pack(pady=5,padx=5)
        self.sys_frame_4["background"] = nav_color

        self.sys_frame_5 = LabelFrame(
        self.sys_info_main_frame2,text="Disk",font=("Sans",16,),foreground="#d4244d", borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=10
        )
        self.sys_frame_5.pack(pady=5,padx=5)
        self.sys_frame_5["background"] = nav_color

        self.sys_frame_left = Frame(
            self.sys_info_main_frame, borderwidth=0, highlightthickness=0, relief=GROOVE
        )





        self.sysinf0 = Label(
            self.sys_frame_1,
            text=f"Platform: {my_system.system}",
            font=(
                "Sans",
                12,
            ),
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=nav_color,
            foreground=main_font,
            width=40,
            anchor=W,
        ).pack()

        self.sysinfd = Label(
            self.sys_frame_1,
            text=f"Distro: {distro}",
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_de = Label(
            self.sys_frame_1,
            text=f"Desktop: {get_de}",
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf2 = Label(
            self.sys_frame_1,
            text=f"Kernel: {my_system.release}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_a = Label(
            self.sys_frame_1,
            text=f"Architecture: {my_system.machine}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinfn = Label(
            self.sys_frame_1,
            text=f"User Name: {user}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        )
        self.sysinfn.pack()

        self.sysinf1 = Label(
            self.sys_frame_1,
            text=f"Device Name: {my_system.node}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_1,
            text=f"Board: {Pi_Model.read()}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf8 = Label(
            self.sys_frame_2,
            text="",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        )
        self.sysinf8.pack()

        self.sysinf6 = Label(
            self.sys_frame_2,
            text=f"CPU Max Freq: {cpufreq.max:.0f} Mhz",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf7 = Label(
            self.sys_frame_2,
            text=f"CPU Min Freq: {cpufreq.min:.0f} Mhz",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf10 = Label(
            self.sys_frame_2,
            text="",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        )
        self.sysinf10.pack()

        self.sysinf3 = Label(
            self.sys_frame_3,
            text=f"RAM Total: {get_size(svmem.total)}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_st = Label(
            self.sys_frame_3,
            text=f"SWAP Total: {get_size(swap.total)}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_ip = Label(
            self.sys_frame_4,
            text=f"IP Address: {IPAddr}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        )
        self.sysinf_ip.pack()

        self.sysinf_ma = Label(
            self.sys_frame_4,
            text=f"MAC Address: {get_mac}",
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        )
        self.sysinf_ma.pack()

        self.sysinf_hdd_t = Label(
            self.sys_frame_5,
            text=("Total Disk Space: %d GiB" % (total // (2**30))),
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_hdd_u = Label(
            self.sys_frame_5,
            text=("Used Disk Space: %d GiB" % (used // (2**30))),
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_hdd_f = Label(
            self.sys_frame_5,
            text=("Free Disk Space: %d GiB" % (free // (2**30))),
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        self.sysinf_hdd_u_p = Label(
            self.sys_frame_5,
            text=(f"Used Disk Space: {obj_Disk.percent} %"),
            justify="left",
            background=nav_color,
            foreground=main_font,
            width=40,
            font=(
                "Sans",
                12,
            ),
            anchor=W,
        ).pack()

        def step():
            self.pb1["value"] = obj_Disk.percent

        self.pb1 = ttk.Progressbar(
            self.sys_frame_5,
            style="red.Horizontal.TProgressbar",
            orient=HORIZONTAL,
            length=200,
            mode="determinate",
        )
        self.pb1.pack(expand=True, anchor="w")
        step()

        def refresh_sys_stats():

            # Parameters for System
            pid = os.getpid()
            ps = psutil.Process(pid)
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            cpu = CPUTemperature()
            # print(cpu)

            self.sysinf8.configure(
                text=f"Current CPU Freq: {cpufreq.current:.0f} Mhz")
            self.sysinf10.configure(
                text=f"CPU Temp: {cpu.temperature:.1f} °C")
            self.after(1000, refresh_sys_stats)

        refresh_sys_stats()


# [Update] Tab
class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def update_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/update.sh && exit ; exec bash"'
                % self.wid
            )

        def upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/upgrade.sh && exit; exec bash"'
                % self.wid
            )

        def full_upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/full_upgrade.sh && exit; exec bash"'
                % self.wid
            )

        def autoremove_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/auto_remove.sh && exit ; exec bash"'
                % self.wid
            )

        def add_unsi_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/addunsignedrepo.sh && exit; exec bash"'
                % self.wid
            )

        def dpgk_conf_btn():
            os.popen(
                f'xterm -into %d -bg Grey11 -geometry 1000x25 -e "{Application_path}/scripts/config_a.sh && exit; exec bash"'
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

        self.background = maincolor

        self.source_list_frame = Frame(self, relief=GROOVE, borderwidth=0)
        self.source_list_frame.pack(padx=45, pady=40, anchor="w", fill=BOTH)
        self.source_list_frame["background"] = maincolor

        self.termf = Frame(
            self, height=270, width=700, padx=10, highlightthickness=0, borderwidth=0
        )
        self.wid = self.termf.winfo_id()
        self.termf["background"] = maincolor

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
            highlightthickness=0,
            padx=5,
            pady=5,
        )
        self.update_btn_frame.pack(padx=45, anchor="w")
        self.update_btn_frame["background"] = maincolor

        self.update_button = Button(
            self.update_btn_frame,
            text="Update",
            width=15,
            anchor="w",
            command=update_btn,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.update_button.grid(column=0, row=0, padx=5, pady=5)

        self.update_button = Button(
            self.update_btn_frame,
            text="Upgrade",
            width=15,
            anchor="w",
            command=upgrade_btn,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.fupgrade_button.grid(column=0, row=2, padx=5, pady=5)

        self.gpk_button = Button(
            self.update_btn_frame,
            text="GPK UpdateViewer",
            width=20,
            anchor="w",
            command=button_gpk,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.gpk_button.grid(column=1, row=0)

        self.auth_button = Button(
            self.update_btn_frame,
            text="Allow Sources",
            width=20,
            anchor="w",
            command=add_unsi_btn,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.auth_button.grid(column=1, row=1, padx=5, pady=5)

        self.rm_button = Button(
            self.update_btn_frame,
            text="Remove Config Files",
            width=20,
            anchor="w",
            command=autoremove_btn,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.rm_button.grid(column=1, row=2)

        self.sv_button = Button(
            self.update_btn_frame,
            text="Save Source List",
            width=20,
            anchor="w",
            command=save_list,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.sv_button.grid(column=2, row=0, padx=5, pady=5)

        self.sv_button = Button(
            self.update_btn_frame,
            text="Open Sources.list.d",
            width=20,
            anchor="w",
            command=button_list,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.sv_button.grid(column=2, row=1)

        self.dpkg_button = Button(
            self.update_btn_frame,
            text="dpkg --configure -a",
            width=20,
            anchor="w",
            command=dpgk_conf_btn,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.dpkg_button.grid(column=2, row=1)

        self.reboot_button = Button(
            self.update_btn_frame,
            text="Reboot",
            width=20,
            anchor="w",
            command=reboot_n,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
        )
        self.reboot_button.grid(column=2, row=2, padx=5, pady=5)

        self.termf.pack(padx=45, pady=20, anchor=W, fill=BOTH)


# [System] Tab
class Frame3(ttk.Frame):
    """standard system tab for all rpi os distros"""

    def __init__(self, container):
        super().__init__()

        def source_sett():
            popen("pi-gpk-prefs")

        def screen_sett():
            popen("lxrandr")

        def desk_sett():
            popen("pcmanfm --desktop-pref")

        def printer_sett():
            popen("system-config-printer")

        def menu_sett():
            popen("alacarte")

        def mouse_key_sett():
            popen("lxinput")

        def button_boot():
            popen("xterm -e 'bash -c \"dmesg; exec bash\"'")

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

            print("[Info]: With great power comes great responsibility")
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
                    f"xterm -e 'bash -c \"{legit} BRANCH=next rpi-update; exec bash\"'"
                )
                print("[Info]: Kernel Upgrade GO!")
                pop_kernel.destroy()

            frame_pop_kernel = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel.pack()
            frame_pop_kernel["background"] = maincolor

            frame_pop_kernel_1 = Frame(
                pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel_1.pack()
            frame_pop_kernel_1["background"] = maincolor

            pop_lbl_2000 = Label(
                frame_pop_kernel,
                anchor="w",
                text="Do you really want to Upgrade the Kernel?",
                font=("Sans", 12),
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

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def button_auto():
            popen("xfce4-session-settings")

        def button_xsett():
            popen("xfce4-settings-manager")

        def bash_log():
            popen(f"xdg-open {home}/.bash_history")

        def rename_user():
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
                popen(f"{legit} rename-user")
                print("[Info]: Name will be changed")
                pop_u_name.destroy()

            frame_pop_u_name = Frame(pop_u_name, borderwidth=0, relief=GROOVE)
            frame_pop_u_name.pack()
            frame_pop_u_name["background"] = maincolor

            frame_pop_u_name_1 = Frame(
                pop_u_name, borderwidth=0, relief=GROOVE)
            frame_pop_u_name_1.pack()
            frame_pop_u_name_1["background"] = maincolor

            pop_lbl_2000 = Label(
                frame_pop_u_name,
                anchor="w",
                text="Do you really want to change the user name?\nrename-user will run on reboot.",
                font=("Sans", 12),
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
                background="#2246c4",
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
        self.gparted_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gparted.png")
        self.mouse_keyboard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gnome-settings-keybinding.png"
        )
        self.deskpipro_icon = PhotoImage(
            file=r"images/icons/pigro_icons/deskpi.png")
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
        self.neofetch_icon = PhotoImage(
            file=r"images/icons/pigro_icons/neofetch.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )
        self.kernel_2_latest_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-madlinux.png"
        )
        self.boot_log_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/bash.png")
        self.xfce_autostarts_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.xfce_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.taskmanager_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.bash_history_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/bash.png")
        self.cron_job_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/mousepad.png")
        self.alacard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/classicmenu-indicator-light.png"
        )
        self.source_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )

        # Raspberry Pi Settings
        self.pi_set = LabelFrame(
            self,
            text="Raspberry Pi Settings",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.pi_set.pack(pady=40, padx=40, fill="both")  #
        self.pi_set["background"] = maincolor

        sys_rc_cli_btn = Button(
            self.pi_set,
            image=self.raspi_config_cli_icon,
            width=140,
            height=100,
            text="Raspi-Config CLI",
            command=pi_configbutton,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_rc_cli_btn.grid(row=0, column=0)

        sys_rc_gui_btn = Button(
            self.pi_set,
            image=self.raspi_config_gui_icon,
            width=140,
            height=100,
            text="Raspi-Config GUI",
            command=pi_configbutton2,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_rc_gui_btn.grid(row=0, column=1)

        rename_user_btn = Button(
            self.pi_set,
            image=self.rename_user_icon,
            width=140,
            height=100,
            text="Rename User",
            command=rename_user,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        rename_user_btn.grid(row=0, column=2)

        sys_conf_btn = Button(
            self.pi_set,
            image=self.edit_config_txt_icon,
            width=140,
            height=100,
            text="Edit Config.txt",
            command=contxt_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_conf_btn.grid(row=0, column=3)

        # Device Settings
        self.dev_set = LabelFrame(
            self,
            text="Device Settings",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.dev_set.pack(pady=0, padx=40, fill="both")  #
        self.dev_set["background"] = maincolor

        sys_gparted_btn = Button(
            self.dev_set,
            image=self.gparted_icon,
            width=140,
            height=100,
            text="Gparted",
            command=gparted_exec,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_gparted_btn.grid(row=0, column=0)

        if os.path.isfile("/usr/sbin/gparted"):
            print("[Info]: Gparted is installed")
            sys_gparted_btn.configure(state=NORMAL)
        else:
            print("[Info]: Gparted is not installed")
            sys_gparted_btn.configure(state=DISABLED)

        mouse_key_sett_btn = Button(
            self.dev_set,
            image=self.mouse_keyboard_icon,
            width=140,
            height=100,
            text="Mouse & Keyboard",
            command=mouse_key_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        mouse_key_sett_btn.grid(row=0, column=1)

        sys_dpp_btn = Button(
            self.dev_set,
            image=self.deskpipro_icon,
            width=140,
            height=100,
            text="DeskpiPro Control",
            command=button_dpfc,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_dpp_btn.grid(row=0, column=2)

        sys_netset_btn = Button(
            self.dev_set,
            image=self.network_icon,
            width=140,
            height=100,
            text="Network Settings",
            command=net_set,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_netset_btn.grid(row=0, column=3)

        sys_sd_btn = Button(
            self.dev_set,
            image=self.sd_card_copier_icon,
            width=140,
            height=100,
            text="SD Card Copier",
            command=sd_copy,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_sd_btn.grid(row=0, column=4)

        sys_printer_sett_btn = Button(
            self.dev_set,
            image=self.printer_settings_icon,
            width=140,
            height=100,
            text="Printer Settings",
            command=printer_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_printer_sett_btn.grid(row=1, column=0)

        desk_sett_btn = Button(
            self.dev_set,
            image=self.desktop_settings_icon,
            width=140,
            height=100,
            text="Desktop Settings",
            command=desk_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        desk_sett_btn.grid(row=1, column=1)

        screen_sett_btn = Button(
            self.dev_set,
            image=self.screen_settings_icon,
            width=140,
            height=100,
            text="Screen Settings",
            command=screen_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        screen_sett_btn.grid(row=1, column=2)

        sys_neo_btn = Button(
            self.dev_set,
            image=self.neofetch_icon,
            width=140,
            height=100,
            text="NeoFetch",
            command=neofetch_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_neo_btn.grid(row=1, column=3)

        if os.path.isfile("/bin/neofetch"):
            print("[Info]: Neofetch is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("[Info]: Neofetch is not installed")
            sys_neo_btn.configure(state=DISABLED)

        # OS Settings
        self.os_set = LabelFrame(
            self,
            text="Operating System",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.os_set.pack(pady=10, padx=40, fill="both")  #
        self.os_set["background"] = maincolor

        sys_FMGM_btn = Button(
            self.os_set,
            image=self.fm_godmode_icon,
            width=140,
            height=100,
            text="FM God Mode",
            command=onc_ben,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_FMGM_btn.grid(row=0, column=0)
        sys_FMGM_btn = CreateToolTip(
            sys_FMGM_btn,
            "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)",
        )

        sys_kernel_btn = Button(
            self.os_set,
            image=self.kernel_2_latest_icon,
            width=140,
            height=100,
            text="Upgrade Linux Kernel",
            command=button_lk,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_kernel_btn.grid(row=0, column=1)

        sys_b_log_btn = Button(
            self.os_set,
            image=self.boot_log_icon,
            width=140,
            height=100,
            text="Boot Log",
            command=button_boot,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_b_log_btn.grid(row=0, column=2)

        sys_xf_auto_btn = Button(
            self.os_set,
            image=self.xfce_autostarts_icon,
            width=140,
            height=100,
            text="Xfce Autostarts",
            command=button_auto,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_xf_auto_btn.grid(row=0, column=3)
        sys_xf_auto_btn.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_xf_auto_btn.configure(state=NORMAL)

        sys_xf_sett_btn = Button(
            self.os_set,
            image=self.xfce_settings_icon,
            width=140,
            height=100,
            text="Xfce Settings",
            command=button_xsett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_xf_sett_btn.grid(row=0, column=4)
        sys_xf_sett_btn.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_xf_sett_btn.configure(state=NORMAL)

        sys_task_btn = Button(
            self.os_set,
            image=self.taskmanager_icon,
            width=140,
            height=100,
            text="Taskmanager",
            command=lx_task,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_task_btn.grid(row=1, column=0)

        sys_bash_btn = Button(
            self.os_set,
            image=self.bash_history_icon,
            width=140,
            height=100,
            text="Bash History",
            command=bash_log,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_bash_btn.grid(row=1, column=1)

        sys_cron_btn = Button(
            self.os_set,
            image=self.cron_job_icon,
            width=140,
            height=100,
            text="Cron Job",
            command=cron_job,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_cron_btn.grid(row=1, column=2)

        menu_sett_btn = Button(
            self.os_set,
            image=self.alacard_icon,
            width=140,
            height=100,
            text="Menu Settings\nAlacart",
            command=menu_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        menu_sett_btn.grid(row=1, column=3)

        source_sett_btn = Button(
            self.os_set,
            image=self.source_settings_icon,
            width=140,
            height=100,
            text="Source Settings",
            command=source_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        source_sett_btn.grid(row=1, column=4)


# [System For Ubuntu] Tab
class Frame12(ttk.Frame):
    """system tab for ubuntu"""

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
            print("[Info]: With great power comes great responsibility")
            Notification(
                title="Sudo File Manager\n",
                description="With great power comes great responsibility\n\n                          - Oncle Ben",
                icon_path=f"{Application_path}/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def bash_log():
            popen(f"xdg-open {home}/.bash_history")

        def gX_web():
            popen("xdg-open https://extensions.gnome.org/")

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
        self.gparted_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gparted.png")
        self.mouse_keyboard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/gnome-settings-keybinding.png"
        )
        self.deskpipro_icon = PhotoImage(
            file=r"images/icons/pigro_icons/deskpi.png")
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
        self.neofetch_icon = PhotoImage(
            file=r"images/icons/pigro_icons/neofetch.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )
        self.kernel_2_latest_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/distributor-logo-madlinux.png"
        )
        self.boot_log_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/bash.png")
        self.xfce_autostarts_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.xfce_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.taskmanager_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.bash_history_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/bash.png")
        self.cron_job_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/mousepad.png")
        self.alacard_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/classicmenu-indicator-light.png"
        )
        self.source_settings_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )

        # Button Set/Frame1
        self.rahmen2 = Frame(
            self, borderwidth=0, highlightthickness=0, relief=GROOVE, padx=60, pady=10
        )
        self.rahmen2.pack(padx=40, pady=20, fill="both")
        self.rahmen2["background"] = maincolor

        sys_rc_cli_btn = Button(
            self.rahmen2,
            image=self.bp01,
            text="Raspi-Config CLI",
            command=pi_configbutton,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_rc_cli_btn.grid(row=0, column=0)

        if os.path.isfile("/bin/raspi-config"):
            print("[Info]: Raspi-Config is installed")
            sys_rc_cli_btn.configure(state=NORMAL)
        else:
            print("[Info]: Raspi-Config is not installed")
            sys_rc_cli_btn.configure(state=DISABLED)

        sys_ubu_pref_btn = Button(
            self.rahmen2,
            image=self.raspi_config_cli_icon,
            text="Ubuntu Settings",
            command=ubu_prefs,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_ubu_pref_btn.grid(row=0, column=1)

        sys_conf_btn = Button(
            self.rahmen2,
            image=self.raspi_config_cli_icon,
            text="Config.txt",
            command=contxt_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_conf_btn.grid(row=0, column=2)

        sys_neo_btn = Button(
            self.rahmen2,
            image=self.neofetch_icon,
            text="NeoFetch",
            command=neofetch_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_neo_btn.grid(row=0, column=3)

        if os.path.isfile("/bin/neofetch"):
            print("[Info]: Neofetch is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("[Info]: Neofetch is not installed")
            sys_neo_btn.configure(state=DISABLED)

        sys_dpp_btn = Button(
            self.rahmen2,
            image=self.deskpipro_icon,
            text="DeskpiPro Control",
            command=button_dpfc,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_dpp_btn.grid(row=0, column=4)

        sys_bash_btn = Button(
            self.rahmen2,
            image=self.bash_history_icon,
            text="Bash History",
            command=bash_log,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_bash_btn.grid(row=1, column=1)

        g_tweaks_btn = Button(
            self.rahmen2,
            image=self.source_settings_icon,
            text="Gnome Tweaks",
            command=g_tweaks,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        g_tweaks_btn.grid(row=1, column=2)

        if os.path.isfile("/bin/gnome-tweaks"):
            print("[Info]: gnome-tweaks is installed")
            sys_neo_btn.configure(state=NORMAL)
        else:
            print("[Info]: gnome-tweaks is not installed")
            g_tweaks_btn.configure(state=DISABLED)

        menu_sett_btn = Button(
            self.rahmen2,
            image=self.alacard_icon,
            text="Menu Settings\nAlacart",
            command=menu_sett,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        menu_sett_btn.grid(row=1, column=3)

        if os.path.isfile("/bin/alacarte"):
            print("[Info]: alacarte is installed")
            menu_sett_btn.configure(state=NORMAL)
        else:
            print("[Info]: Gparted is not installed")
            menu_sett_btn.configure(state=DISABLED)

        sys_gparted_btn = Button(
            self.rahmen2,
            image=self.gparted_icon,
            text="Gparted",
            command=gparted_exec,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_gparted_btn.grid(row=1, column=4)

        if os.path.isfile("/usr/sbin/gparted"):
            print("[Info]: Gparted is installed")
            sys_gparted_btn.configure(state=NORMAL)
        else:
            print("[Info]: Gparted is not installed")
            sys_gparted_btn.configure(state=DISABLED)

        sys_FMGM_btn = Button(
            self.rahmen2,
            image=self.fm_godmode_icon,
            text="FM God Mode",
            command=onc_ben,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_FMGM_btn.grid(row=1, column=0)
        sys_FMGM_btn = CreateToolTip(
            sys_FMGM_btn,
            "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)",
        )

        sys_gX_btn = Button(
            self.rahmen2,
            image=self.source_settings_icon,
            text="Gnome Extensions",
            command=gX_web,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=TOP,
            font=(
                "Sans",
                10,
            ),
        )
        sys_gX_btn.grid(row=2, column=0)


# [Autostarts] Tab
class Frame13(ttk.Frame):
    """displays all files in the autostart folder in a listbox"""

    def __init__(self, container):
        super().__init__()

        def add_auto():
            add_child = Add_Autostart(self)
            add_child.grab_set()

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

        onlyfiles = [
            f
            for f in listdir(f"{home}/.config/autostart")
            if isfile(join(f"{home}/.config/autostart", f))
        ]

        # print(onlyfiles)

        with open(f"/home/{user}/.pigro/autostart.list", "w") as f:
            for item in onlyfiles:
                f.write("%s\n" % item)

        auto_main_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            background=maincolor,
            pady=20,
            padx=20,
        )
        auto_main_frame.pack(pady=20)

        auto_button_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background=maincolor,
            highlightthickness=0,
            pady=10,
        )
        auto_button_frame.pack(side="left", anchor="n", fill=BOTH, expand=True)

        auto_select_frame = Frame(
            auto_main_frame,
            borderwidth=0,
            background=maincolor,
            highlightthickness=0,
            pady=10,
        )
        auto_select_frame.pack()

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
            pop_del_entry.geometry(
                f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_del_entry.resizable(0, 0)

            def yes_btn_command():
                os.remove(
                    f"/home/{user}/.config/autostart/{auto_selected.get()}")
                auto_list.delete(tk.ACTIVE)
                pop_del_entry.destroy()

            def no_btn_command():
                pop_del_entry.destroy()

            yes_btn = tk.Button(pop_del_entry)
            yes_btn["bg"] = maincolor
            ft = tkFont.Font(family="Sans", size=10)
            yes_btn["borderwidth"] = 0
            yes_btn["highlightthickness"] = 1
            yes_btn["font"] = ft
            yes_btn["fg"] = "white"
            yes_btn["justify"] = "center"
            yes_btn["text"] = "Yes"
            yes_btn.place(x=70, y=120, width=70, height=25)
            yes_btn["command"] = yes_btn_command

            no_btn = tk.Button(pop_del_entry)
            no_btn["bg"] = maincolor
            ft = tkFont.Font(family="Sans", size=10)
            no_btn["borderwidth"] = 0
            no_btn["highlightthickness"] = 1
            no_btn["font"] = ft
            no_btn["fg"] = "white"
            no_btn["justify"] = "center"
            no_btn["text"] = "No"
            no_btn.place(x=180, y=120, width=70, height=25)
            no_btn["command"] = no_btn_command

            del_label = tk.Label(pop_del_entry)
            ft = tkFont.Font(family="Sans", size=10)
            del_label["font"] = ft
            del_label["bg"] = maincolor
            del_label["fg"] = "white"
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

        fo3 = open(f"/home/{user}/.pigro/autostart.list", "r")
        content3 = fo3.readlines()
        # print(content3)

        inst_btn3 = Label(
            auto_button_frame,
            text="Selected: \n",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground="#d4244d",
            font=(("Sans,bold"), "14"),
        )
        inst_btn3.pack(anchor="n")

        inst_btn3 = Button(
            auto_button_frame,
            text="Delete",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            command=del_enrty,
        )
        inst_btn3.pack(anchor="s")

        uninst_btn3 = Button(
            auto_button_frame,
            text="Add",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            command=add_auto,
        )
        uninst_btn3.pack(anchor="s")

        uninst_btn3 = Button(
            auto_button_frame,
            text="Details/\nEdit",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            command=edit_auto,
        )
        uninst_btn3.pack(anchor="s")

        # Create an entry box
        global auto_selected
        auto_selected = Entry(auto_select_frame, font=("Sans", 12), width=60)
        auto_selected.pack()

        note_lbl = Label(
            auto_select_frame,
            text="double click to select",
            background=maincolor,
            foreground=info_color,
            font=("Sans", 14),
        )
        note_lbl.pack(pady=5)

        global auto_list
        auto_list = Listbox(auto_select_frame, width=60, height=30)
        auto_list.pack()

        fo3 = open(f"/home/{user}/.pigro/autostart.list", "r")
        content3 = fo3.readlines()
        for i3, s3 in enumerate(content3):
            content3[i3] = s3.strip()
        # print(content3)

        # Add toppings
        update3(content3)

        # Create binding
        auto_list.bind("<<ListboxSelect>>", fillout3)
        auto_selected.bind("<KeyRelease>", check3)


# [Autostart Edit Entry Child]
class Edit_Autostart(tk.Toplevel):
    """child window for editing a .desktopfile in autostart folder"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 630
        app_height = 500
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
            # open file
            with open(
                f"/home/{user}/.config/autostart/{auto_selected.get()}", "w"
            ) as file:
                # write to file
                file.writelines(
                    [
                        f"Name={name_entry.get()}\n",
                        f"Exec={exec_entry.get()}\n",
                        f"Icon={icon_entry.get()}\n",
                        f"Terminal={terminal_entry.get()}\n",
                        f"Type={type_entry.get()}\n",
                        f"X-GNOME-Autostart-enabled={x_g_entry.get()}\n",
                        f"Hidden={hidden_entry.get()}\n",
                        f"NoDisplay={no_display_entry.get()}\n",
                    ]
                )
            done_edit()

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

        # App Exec#
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

        # App Icon
        icon_label = Label(
            self,
            text="Icon:",
            justify="left",
            anchor="w",
            width=15,
            background=maincolor,
            foreground=main_font,
        )
        icon_label.grid(column=0, row=2, padx=5, pady=5, sticky="w")

        icon_entry = Entry(self, width=50)
        icon_entry.grid(column=1, row=2, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "Icon=" in line:
                icon_entry.insert(0, line[5:-1])

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
        hidden_label.grid(column=0, row=6, padx=5, pady=5, sticky="w")

        hidden_entry = Entry(self, width=50)
        hidden_entry.grid(column=1, row=6, padx=5, pady=5, sticky="w")

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
        no_display_label.grid(column=0, row=7, padx=5, pady=5, sticky="w")

        no_display_entry = Entry(self, width=50)
        no_display_entry.grid(column=1, row=7, padx=5, pady=5, sticky="w")

        with open(f"/home/{user}/.config/autostart/{auto_selected.get()}") as pi_conf:
            datafile = pi_conf.readlines()
        for line in datafile:
            if "NoDisplay=" in line:
                no_display_entry.insert(0, line[10:-1])

        set_btn = Button(
            self,
            text="Apply",
            width=10,
            background=maincolor,
            foreground=main_font,
            command=edit_entries,
        )
        set_btn.grid(column=0, row=8, padx=5, pady=5, sticky="w")

        close_butn = Button(
            self,
            text="Close",
            width=10,
            background=maincolor,
            foreground=main_font,
            command=self.destroy,
        )
        close_butn.grid(column=0, row=9, padx=5, pady=5, sticky="w")


# [Autostart Add Entry Child]
class Add_Autostart(tk.Toplevel):
    """child window for creating a .desktopfile in autostart folder"""

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
        self["background"] = maincolor

        def error_mass():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def add_enrty():

            if add_name.get() == "" or add_path.get() == "":
                error_mass()
            else:
                file_name = f"/home/{user}/.config/autostart/{add_name.get()}.desktop"
                f = open(file_name, "a+")  # open file in append mode
                f.write(
                    f"[Desktop Entry]\nName={add_name.get()}\nExec={add_path.get()}\nTerminal=false\nType=Application\nX-GNOME-Autostart-enabled=true\nHidden=false\n"
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

        add_name = Entry(add_frame, width=45)
        add_name.grid(row=0, column=1)

        add_path = Entry(add_frame, width=45)
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
            background=maincolor,
            foreground=main_font,
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
            background=maincolor,
            foreground=main_font,
            highlightthickness=1,
            borderwidth=0,
            highlightcolor="white",
        )
        cancel_add.grid(row=4, column=0, pady=5)


# [Overclocking_Legend Popup] Child
class Tuning_Legende(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
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
            foreground="#d4244d",
            font=("Sans", 14),
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
            foreground="#d4244d",
            font=("Sans", 14),
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
            foreground="#d4244d",
            font=("Sans", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=("Sans", 9),
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
            foreground="#d4244d",
            font=("Sans", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=("Sans", 9),
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
            foreground="#d4244d",
            font=("Sans", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=0)

        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=("Sans", 9),
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

        self.tu_main_frame2 = Frame(self, bg=maincolor)
        self.tu_main_frame2.pack(pady=20)


# [Done Popup] Child
class Done_Restart_P(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
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
        ft = tkFont.Font(family="Sans", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = main_font
        cont_btn["bg"] = maincolor
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 2
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Got It!"
        cont_btn.pack()
        cont_btn["command"] = self.destroy


# [Done Popup] Child
class Done_(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
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
        ft = tkFont.Font(family="Sans", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = main_font
        cont_btn["bg"] = maincolor
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 2
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        global done_label
        done_label = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=14)
        done_label["font"] = ft
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)


# [Done_Reboot Popup] Child
class Done_Reboot(tk.Toplevel):
    """a custom massagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done! Reboot?")
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
        ft = tkFont.Font(family="Sans", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = main_font
        cont_btn["bg"] = maincolor
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 2
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        rebt_btn = tk.Button(self)
        rebt_btn["bg"] = "#efefef"
        ft = tkFont.Font(family="Sans", size=10)
        rebt_btn["font"] = ft
        rebt_btn["fg"] = main_font
        rebt_btn["bg"] = maincolor
        rebt_btn["justify"] = "center"
        rebt_btn["highlightthickness"] = 2
        rebt_btn["borderwidth"] = 0
        rebt_btn["text"] = "Reboot"
        rebt_btn.place(x=160, y=130, width=70, height=25)
        rebt_btn["command"] = self.rebt_btn_command

        done_label = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=14)
        done_label["font"] = ft
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)

    def rebt_btn_command(self):
        popen(f"{legit} reboot")


# [Overclocking_Expert Popup] Child
class Overclocking_Expert(tk.Toplevel):
    """entry fields to custom configure config.txt"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/arm_freq/d' config.txt")
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/gpu_freq/d' config.txt")
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/gpu_mem/d' config.txt")
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/over_voltage/d' config.txt")
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/disable_splash/d' config.txt")
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
                os.popen(
                    f" cd /boot/ && {legit} sed -i '/force_turbo/d' config.txt")
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
        arm_freq_entry = Entry(
            x_mode_frame, borderwidth=0, highlightthickness=2)
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
            font=("Sans", 12, "bold"),
            text="Reboot",
            bg=maincolor,
            foreground=main_font,
            borderwidth=0,
            highlightthickness=2,
            command=reboot_n,
        )
        reboot_e.pack()


# [APT Installer Popup] Child
class APT_Installer_Popup(tk.Toplevel):
    """child window that makes the the install process graphicle"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"Installing ... {apt_inst_combo_box.get()}")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 500
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
            foreground=main_font,
        )
        inst_show.pack(pady=20)

        anim = Loading_Throbber(self, "images/icons/loading.gif")
        anim["borderwidth"] = "0"
        anim.pack()

        def stop_it():
            anim.after_cancel(anim.cancel)

        self.apt_inst_termf = Frame(
            self, height=300, width=600, highlightthickness=0, borderwidth=0
        )

        self.apt_inst_wid = self.apt_inst_termf.winfo_id()

        self.apt_inst_termf["background"] = "#333333"
        self.apt_inst_termf.pack(padx=45, pady=20)

        def install_parameter():

            if distro_get == "ubuntu":

                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "pkexec apt install -y {apt_inst_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!", font=(
                    ("Sans,bold"), "12"))  # äöl
                GButton_9161.place_forget()
            else:
                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "sudo apt install -y {apt_inst_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )

                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")
                GButton_9161.place_forget()

        # place the progressbar

        def GButton_916_command():
            APT_Installer_Popup.destroy(self)

        GButton_916 = tk.Button(self)
        GButton_916["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        GButton_916["font"] = ft
        GButton_916["fg"] = "white"
        GButton_916["justify"] = "center"
        GButton_916["bg"] = "#333333"
        GButton_916["text"] = "Close"
        GButton_916.place(x=580, y=450, width=70, height=25)
        GButton_916["command"] = GButton_916_command
        GButton_916.configure(state=DISABLED)

        GButton_9161 = tk.Button(self)
        GButton_9161["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        GButton_9161["font"] = ft
        GButton_9161["fg"] = "white"
        GButton_9161["justify"] = "center"
        GButton_9161["bg"] = "#333333"
        GButton_9161["text"] = "Cancel"
        GButton_9161.place(x=500, y=450, width=70, height=25)
        GButton_9161["command"] = GButton_916_command

        Thread(target=install_parameter).start()


# [APT Uninstaller Popup] Child
class APT_Uninstaller_Popup(tk.Toplevel):
    """child window that makes the the install process graphicle"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"Removing ... {apt_un_combo_box.get()}")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 500
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
            foreground=main_font,
        )
        inst_show.pack(pady=20)

        anim = Loading_Throbber(self, "images/icons/loading.gif")
        anim["borderwidth"] = "0"
        anim.pack()

        def stop_it():
            anim.after_cancel(anim.cancel)

        self.apt_inst_termf = Frame(
            self, height=300, width=600, highlightthickness=0, borderwidth=0
        )

        self.apt_inst_wid = self.apt_inst_termf.winfo_id()

        self.apt_inst_termf["background"] = "#333333"
        self.apt_inst_termf.pack(padx=45, pady=20)

        def install_parameter():
            if distro_get == "ubuntu":
                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "pkexec apt remove -y {apt_un_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!", font=(("Sans,bold"), "12"))
                GButton_9161.place_forget()

            else:
                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "sudo apt remove -y {apt_un_combo_box.get()} && exit ; exec bash"'
                    % self.apt_inst_wid
                )
                stop_it()
                anim.forget()
                GButton_916.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")
                GButton_9161.place_forget()

        # place the progressbar

        def GButton_916_command():
            APT_Installer_Popup.destroy(self)

        GButton_916 = tk.Button(self)
        GButton_916["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        GButton_916["font"] = ft
        GButton_916["fg"] = "white"
        GButton_916["justify"] = "center"
        GButton_916["bg"] = "#333333"
        GButton_916["text"] = "Close"
        GButton_916.place(x=580, y=450, width=70, height=25)
        GButton_916["command"] = GButton_916_command
        GButton_916.configure(state=DISABLED)

        GButton_9161 = tk.Button(self)
        GButton_9161["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        GButton_9161["font"] = ft
        GButton_9161["fg"] = "white"
        GButton_9161["justify"] = "center"
        GButton_9161["bg"] = "#333333"
        GButton_9161["text"] = "Cancel"
        GButton_9161.place(x=500, y=450, width=70, height=25)
        GButton_9161["command"] = GButton_916_command

        Thread(target=install_parameter).start()


# [Custom_Installer Popup] Child
class Custom_Installer(tk.Toplevel):
    """child window that makes the the install process graphicle"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title(f"Installing ... {pigro_skript_name}")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 500
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
            text="",  # {cust_inst_combo_box.get()}
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

            if distro_get == "ubuntu":

                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "pkexec {pigro_skript}; exec bash"'
                    % self.cust_inst_wid
                )
                stop_it()
                anim.forget()
                close_btn.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")
                cancel_btn.place_forget()
            else:
                os.system(
                    f'xterm -into %d -bg Grey11 -geometry 120x25 -e "sudo {pigro_skript} -y; exec bash"'
                    % self.cust_inst_wid
                )

                stop_it()
                anim.forget()
                close_btn.configure(state=NORMAL)
                self.title(f"Done!")
                inst_show.configure(text="Done!")
                cancel_btn.place_forget()

        # place the progressbar

        def close_btn_command():
            Custom_Installer.destroy(self)

        close_btn = tk.Button(self)
        close_btn["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        close_btn["font"] = ft
        close_btn["fg"] = "white"
        close_btn["justify"] = "center"
        close_btn["bg"] = "#333333"
        close_btn["text"] = "Close"
        close_btn.place(x=580, y=450, width=70, height=25)
        close_btn["command"] = close_btn_command
        close_btn.configure(state=DISABLED)

        cancel_btn = tk.Button(self)
        cancel_btn["bg"] = "#e9e9ed"
        ft = tkFont.Font(family="Sans", size=12)
        cancel_btn["font"] = ft
        cancel_btn["fg"] = "white"
        cancel_btn["justify"] = "center"
        cancel_btn["bg"] = "#333333"
        cancel_btn["text"] = "Cancel"
        cancel_btn.place(x=500, y=450, width=70, height=25)
        cancel_btn["command"] = close_btn_command

        Thread(target=install_parameter).start()


# [Software] Tab
class Frame4(ttk.Frame):
    def __init__(self, container):
        """lets you install apps via APT, snap, pi-apps and flatpak in one single window"""
        super().__init__()

        def pi_apps_list():
            global pop_pi_apps_list
            pop_pi_apps_list = Toplevel()
            pop_pi_apps_list.geometry("700x800")
            pop_pi_apps_list.title("pi_apps_list")
            scrollbar = Scrollbar(pop_pi_apps_list)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_pi_apps_list, yscrollcommand=scrollbar.set)
            text_file = open(f"/home/{user}/.pigro/pi-apps_list.list")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def snapcraft():
            popen("xdg-open https://snapcraft.io/store")

        def flatflat():
            popen("xdg-open https://flathub.org/")

        def neofetch_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install neofetch -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def bleacbit_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install bleachbit -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def bpytop_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install bpytop -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def compiz_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install neofetch -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def gnomepie_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install compiz -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def gparted_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install gparted -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def imager_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install imager -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def plank_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install plank && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        def xfce4screen_installer():
            global pigro_skript_name
            pigro_skript_name = "Neofetch"
            global pigro_skript
            pigro_skript = "apt install xfce4-screenshooter -y && exit"
            custom_pop = Custom_Installer(self)
            custom_pop.grab_set()

        # Fast_Installer Main_Frame
        self.fast_main_frame = LabelFrame(
            self,
            text="Fast Installer",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=10,
        )
        self.fast_main_frame["background"] = maincolor
        self.fast_main_frame.pack(
            pady=20,
        )

        # Sec Fast Frame
        self.fast_sec_frame = Frame(
            self.fast_main_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            padx=42,
            pady=0,
        )
        self.fast_sec_frame.pack()
        self.fast_sec_frame["background"] = maincolor

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=20)

        # apt-get_entry
        self.apt_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.apt_frame.pack()
        self.apt_frame["background"] = maincolor

        fo = open(f"/home/{user}/.pigro/apt_cache.list", "r")
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
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            width=10,
        )
        self.apt_inst_btn_ttp = CreateToolTip(
            self.apt_inst_btn,
            'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.',
        )

        self.apt_ico = Label(
            self.apt_frame,
            text="Apt-Get",
            foreground="#d4244d",
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.apt_ico["background"] = maincolor
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
        self.un_apt_frame["background"] = maincolor

        ua_fo = open(f"/home/{user}/.pigro/packages.list", "r")
        un_content = ua_fo.readlines()
        for i, s in enumerate(un_content):
            un_content[i] = s.strip()

        def check_input(event):
            value = event.widget.get()

            if value == "":
                apt_un_combo_box["values"] = un_content
            else:
                data = []
                for item in un_content:
                    if value.lower() in item.lower():
                        data.append(item)
                apt_un_combo_box["values"] = data

        def un_inst_btn1():
            if apt_un_combo_box.get() == "":
                error_mass()
            else:
                uninst_pop = APT_Uninstaller_Popup(self)
                uninst_pop.grab_set()

        self.un_apt_ico = Label(
            self.un_apt_frame,
            text=" ",
            foreground="#d4244d",
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.un_apt_ico["background"] = maincolor
        self.un_apt_ico.grid(
            column=0,
            row=0,
        )

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
            background=maincolor,
            foreground="red",
            font=(("Sans,bold"), "12"),
            width=10,
        )

        self.un_apt_ico.grid(column=0, row=0, rowspan=2)
        apt_un_combo_box.grid(column=2, row=0)
        self.un_apt_inst_btn.grid(column=1, row=0)

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=20)

        # pi-apps_entry

        self.pi_apps = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.pi_apps.pack()
        self.pi_apps["background"] = maincolor

        def inst_pi_apps():
            if self.pi_apps_entry.get() == "":
                error_mass()
            else:
                popen(
                    f"xterm -e 'bash -c \"~/pi-apps/manage install {self.pi_apps_entry.get()}; exec bash\"'"
                )

        self.pi_apps_ico = Label(
            self.pi_apps,
            text="Pi-Apps",
            foreground="#d4244d",
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.pi_apps_ico["background"] = maincolor

        self.pi_apps_entry = Entry(self.pi_apps, bd=5, width=31, borderwidth=1)
        self.pi_apps_inst_btn = Button(
            self.pi_apps,
            text="install",
            command=inst_pi_apps,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            width=10,
        )

        self.pi_apps_inst_btn3 = Button(
            self.pi_apps,
            text="Search Pi-Apps",
            command=pi_apps_list,
            highlightthickness=0,
            borderwidth=0,
            width=33,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "9"),
        )

        if piapps_path == False:
            print("[Info]: Pi-Apps not found")
            self.pi_apps_entry.insert(0, "Pi-Apps is not installed")
            self.pi_apps_inst_btn.configure(state=DISABLED)

        self.pi_apps_ico.grid(column=0, row=0, rowspan=2)
        self.pi_apps_entry.grid(column=2, row=0)
        self.pi_apps_inst_btn.grid(column=1, row=0)
        self.pi_apps_inst_btn3.grid(column=2, row=1)

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=20)

        # snap_entry
        self.snap_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.snap_frame.pack()
        self.snap_frame["background"] = maincolor

        def inst_btn2():
            if self.snap_entry.get() == "":
                error_mass()
            else:
                popen(
                    f"xterm -e 'bash -c \"{legit} snap install {self.snap_entry.get()}; exec bash\"'"
                )

        self.snap_ico = Label(
            self.snap_frame,
            text="Snap",
            foreground="#d4244d",
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.snap_ico["background"] = maincolor

        self.snap_entry = Entry(self.snap_frame, bd=5, width=31, borderwidth=1)
        self.snap_inst_btn = Button(
            self.snap_frame,
            text="install",
            command=inst_btn2,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            width=10,
        )
        self.snap_inst_btn_ttp = CreateToolTip(
            self.snap_inst_btn,
            "*to use snap install, you must\napt-get install snapd xD lol",
        )

        self.snapstore_btn = Button(
            self.snap_frame,
            text="Search Snaps",
            command=snapcraft,
            highlightthickness=0,
            borderwidth=0,
            width=33,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "9"),
        )

        if os.path.isfile("/bin/snap"):
            self.snap_inst_btn.configure(state=NORMAL)
        else:
            self.snap_inst_btn.configure(state=DISABLED)
            self.snap_entry.insert(0, "Snap is not installed")

        self.snap_ico.grid(column=0, row=0, rowspan=2)
        self.snap_entry.grid(column=2, row=0)
        self.snap_inst_btn.grid(column=1, row=0)
        self.snapstore_btn.grid(column=2, row=1)

        self.ip03 = PhotoImage(
            file=r"images/icons/pigro_icons/download_ico.png")

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=20)

        # flat_entry
        self.flat_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.flat_frame.pack()
        self.flat_frame["background"] = maincolor

        def inst_btn4():
            if self.flat_entry.get() == "":
                error_mass()
            else:
                popen(
                    f" xterm -e 'bash -c \"{legit} flatpak install flathub {self.flat_entry.get()}; exec bash\"'"
                )

        self.flatp_ico = Label(
            self.flat_frame,
            text="Flatpak",
            foreground="#d4244d",
            width=15,
            font=(("Sans,bold"), "14"),
        )
        self.flatp_ico["background"] = maincolor

        self.flat_entry = Entry(self.flat_frame, bd=5, width=31, borderwidth=1)
        self.flatp_inst_btn = Button(
            self.flat_frame,
            text="install",
            command=inst_btn4,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(("Sans,bold"), "12"),
            width=10,
        )
        self.flatp_inst_btn_ttp = CreateToolTip(
            self.flatp_inst_btn,
            "*past without--->>>flatpak install flathub<<< org.mozilla.firefox",
        )

        self.flat_btn = Button(
            self.flat_frame,
            text="Search Flathub",
            command=flatflat,
            highlightthickness=0,
            width=33,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            font=(("Sans,bold"), "9"),
        )

        if os.path.isfile("/bin/flatpak"):
            self.flatp_inst_btn.configure(state=NORMAL)
        else:
            self.flatp_inst_btn.configure(state=DISABLED)
            self.flat_entry.insert(0, "Flatpak is not installed")

        self.flatp_ico.grid(column=0, row=0, rowspan=2)
        self.flat_entry.grid(column=2, row=0)
        self.flatp_inst_btn.grid(column=1, row=0)
        self.flat_btn.grid(column=2, row=1)

        # Separator Line
        self.separator = ttk.Separator(
            self.fast_sec_frame, orient=tk.VERTICAL, style="Line.TSeparator"
        )
        self.separator.pack(fill="x", pady=20)

        self.repo_main_frame = LabelFrame(
            self,
            text="From The Repository",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            pady=20,
            padx=10,
        )
        self.repo_main_frame["background"] = maincolor
        self.repo_main_frame.pack(
            pady=20,
        )

        self.bleach_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Bleach Bit",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=bleacbit_installer,
        ).grid(row=0, column=0, pady=5, padx=5)

        self.bpytop_inst = Button(
            self.repo_main_frame,
            width=20,
            text="BPYTop",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=bpytop_installer,
        ).grid(row=0, column=1, pady=5, padx=5)

        self.compiz_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Compiz",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=compiz_installer,
        ).grid(row=0, column=2, pady=5, padx=5)

        self.gnomepi_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Gnome-Pie",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=gnomepie_installer,
        ).grid(row=1, column=0, pady=5, padx=5)

        self.gparted_inst = Button(
            self.repo_main_frame,
            width=20,
            text="GParted",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=gparted_installer,
        ).grid(row=1, column=1, pady=5, padx=5)

        self.neo_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Neofetch",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=neofetch_installer,
        ).grid(row=1, column=2, pady=5, padx=5)

        self.imager_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Pi Imager",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=imager_installer,
        ).grid(row=2, column=0, pady=5, padx=5)

        self.plank_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Plank",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=plank_installer,
        ).grid(row=2, column=1, pady=5, padx=5)

        self.xfce_screen_inst = Button(
            self.repo_main_frame,
            width=20,
            text="Xfce4 Screenshooter",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=xfce4screen_installer,
        ).grid(row=2, column=2, pady=5, padx=5)

        self.warning_msg = Label(
            self.repo_main_frame,
            text="These applications will \nbe installed directly!",
            foreground=info_color,
            font=(("Sans"), "8", "bold"),
        )
        self.warning_msg["background"] = maincolor
        self.warning_msg.grid(row=3, column=1, pady=5, padx=5)


# [Git & More] Tab
class Frame10(ttk.Frame):
    def __init__(self, container):
        """lets you install apps via APT, snap, pi-apps and flatpak in one single window"""
        super().__init__()

        def xpad_neo():
            self.appname_header.config(text="Xpad Neo")
            self.app_disc.config(
                text="Advanced Linux Driver for\nXbox Wireless Gamepad\nAdds FULL support for all Xbox controlers"
            )
            self.web_link.config(text=r"https://github.com/atar-axis/xpadneo")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "sudo apt-get install dkms raspberrypi-kernel-headers\ngit clone https://github.com/atar-axis/xpadneo.git\ncd xpadneo\nsudo ./install.sh",
            )

        def desk_pi():
            self.appname_header.config(text="DeskPi Pro Driver")
            self.app_disc.config(
                text="Driver & Fan Control for the DeskPi Pro Case")
            self.web_link.config(text=r"https://github.com/DeskPi-Team/deskpi")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "cd ~\ngit clone https://github.com/DeskPi-Team/deskpi.git\ncd ~/deskpi/\nchmod +x install.sh\nsudo ./install.sh\n\n#Pi OS 64 Bit\nchmod +x install-raspios-64bit.sh\nsudo ./install-raspios-64bit.sh",
            )

        def pi_pa_po_piapps():
            self.appname_header.config(text="Pi-Apps")
            self.app_disc.config(
                text="The go to apps store when it comes to\nprograms that are not in repository."
            )
            self.web_link.config(text=r"https://pi-apps.io/")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash",
            )

        def albert():
            self.appname_header.config(text="Albert")
            self.app_disc.config(
                text="Desktop agnostic launcher\nAccess everything with virtually zero effort.\nRun applications, open files or their paths,\nopen bookmarks in your browser,\nsearch the web, calculate things and a lot more.\n\nDowload-Link:"
            )
            self.web_link.config(
                text=r"https://software.opensuse.org/download.html?project=home:manuelschneid3r&package=albert"
            )
            self.app_inst.forget()

        def argon():
            self.appname_header.config(text="Argon One/M.2 Case Driver")
            self.app_disc.config(text="Driver for the Argon One Case")
            self.web_link.config(
                text=r"https://www.waveshare.com/wiki/PI4-CASE-ARGON-ONE"
            )
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end", "curl https://download.argon40.com/argon1.sh | bash"
            )

        def papirus():
            self.appname_header.config(text="Papirus Icon Theme/Folders")
            self.app_disc.config(
                text="The popular icon theme plus the ability to change the order color"
            )
            self.web_link.config(
                text=r"https://github.com/PapirusDevelopmentTeam/papirus-icon-theme"
            )
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "Icon Theme:\nwget -qO- https://git.io/papirus-icon-theme-install | sh\n\nFolder Theme:\nwget -qO- https://git.io/papirus-folders-install | sh\n\nHow To:\nSelect the papirus icon theme then:\npapirus-folders -C brown --theme Papirus-Dark\n\nColors:\nadwaita,black,bluegrey,breeze,brown,carminecyan,darkcyan,\ndeeporange,green,grey,indigo,magenta,nordic,orange,palebrown,\npaleorange,pink,red,teal,violet,white,yaru,yellow",
            )

        def f_shim():
            self.appname_header.config(text="Fan Shim Driver")
            self.app_disc.config(text="Driver for the Pimoroni FanShim")
            self.web_link.config(
                text=r"https://learn.pimoroni.com/article/getting-started-with-fan-shim"
            )
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "git clone https://github.com/pimoroni/fanshim-python\ncd fanshim-python\nsudo ./install.sh",
            )

        def pi_kiss():
            self.appname_header.config(text="piKiss")
            self.app_disc.config(
                text="System Tweak Tool & Game Installer for ARM/Raspberry Pi"
            )
            self.web_link.config(text=r"https://github.com/jmcerrejon/PiKISS")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                "curl -sSL https://git.io/JfAPE | bash",
            )

        def sub_merge():
            self.appname_header.config(text="Sublime Merge aarch64")
            self.app_disc.config(text="Great Git GUI")
            self.web_link.config(text=r"https://www.sublimemerge.com/")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -\n\nsudo apt-get install apt-transport-https\n\necho "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list\n\nsudo apt-get update\nsudo apt-get install sublime-merge -y\n""",
            )

        def sub_text():
            self.appname_header.config(text="Sublime Text aarch64")
            self.app_disc.config(text="Very good Text Editor")
            self.web_link.config(text=r"https://www.sublimetext.com/")
            self.app_inst.pack(anchor="w")
            self.app_inst.delete("1.0", END)
            self.app_inst.insert(
                "end",
                """wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add -\n\nsudo apt-get install apt-transport-https\n\necho "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list\n\nsudo apt-get update\nsudo apt-get install sublime-text -y\n""",
            )

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

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

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Albert",
            command=albert,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Argon One Driver",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=argon,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=20,
            text="DeskPi Pro Driver",
            anchor="w",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=desk_pi,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=20,
            text="FanShim Driver",
            anchor="w",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=f_shim,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Papirus Icon Theme",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=papirus,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Pi-Apps",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=pi_pa_po_piapps,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="PiKiss",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=pi_kiss,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Sublime Merge aarch64",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=sub_merge,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Sublime Text aarch64",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            command=sub_text,
        ).pack(pady=5)

        self.choice_link1 = Button(
            self.link_left,
            anchor="w",
            width=20,
            text="Xpad-Neo",
            command=xpad_neo,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        # Right Frame
        self.link_right = Frame(
            self.link_main,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=20,
        )
        self.link_right.pack(side=LEFT, expand=True, fill=BOTH)
        self.link_right["background"] = maincolor

        self.appname_header = Label(
            self.link_right,
            text=" ",
            width=50,
            highlightthickness=0,
            borderwidth=2,
            background=maincolor,
            foreground=main_font,
            font=("Sans", 16),
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
            background=maincolor,
            foreground=main_font,
            font=("Sans", 12),
            anchor="w",
        )
        self.app_disc.pack(anchor="w")

        self.web_link = tk.Label(
            self.link_right,
            text=r" ",
            width=50,
            background=maincolor,
            foreground="blue",
            cursor="hand2",
            anchor="w",
        )
        self.web_link.pack(anchor="w", pady=10)
        self.web_link.bind("<Button-1>", callback)

        self.app_inst = Text(
            self.link_right,
            width=70,
            height=20,
        )


# [Look] Tab
class Frame5(ttk.Frame):
    """a tool collection to customize the debian desktop"""

    def __init__(self, container):
        super().__init__()

        def done_1():
            d_msg1 = Done_Restart_P(self)
            d_msg1.grab_set()

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def button_xf4s():
            popen("xfwm4-settings")

        def pi_appear():
            popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")

        def pi_panel_bak():
            popen("mv ~/.config/lxpanel lxpanel.bak")

        def pi_panel_restore():
            popen(
                f"cp /etc/xdg/lxpanel/LXDE-pi/panels/panel {home}/.config/lxpanel/LXDE-pi/panels/panel && lxpanelctl restart"
            )

        def pi_panel_restart():
            popen("lxpanelctl restart")

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

        def color_selected():
            if select_clicked.get() == "Light Theme":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("theme = dark", "theme = light")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()

                # messagebox.showinfo(title=None, message="Done! Please restart PiGro")
                done_1()

            if select_clicked.get() == "Dark Theme":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("theme = light", "theme = dark")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                # messagebox.showinfo(title=None, message="Done! Please restart PiGro")
                done_1()

        def trans_selected():
            if select_clicked1.get() == "None":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("transparency = 0.95",
                                    "transparency = 1.00")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                # messagebox.showinfo(title=None, message="Done! Please restart PiGro")
                done_1()

            if select_clicked1.get() == "0.95":
                file = open(f"{home}/.pigro/pigro.conf", "rt")
                data = file.read()
                data = data.replace("transparency = 1.00",
                                    "transparency = 0.95")
                file.close()
                file = open(f"{home}/.pigro/pigro.conf", "wt")
                file.write(data)
                file.close()
                # messagebox.showinfo(title=None, message="Done! Please restart PiGro")
                done_1()

        # Images/Icons

        self.bash_history_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/bash.png")
        self.fm_godmode_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png"
        )

        self.bp06 = PhotoImage(
            file=r"images/icons/papirus/48x48/folder-yellow.png")
        self.ico_m = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-interfacedesign.png"
        )
        self.bp03 = PhotoImage(file=r"images/icons/papirus/48x48/bash.png")
        self.ico_m2 = PhotoImage(
            file=r"images/icons/papirus/48x48/applications-webapps.png"
        )
        self.ip01 = PhotoImage(
            file=r"images/icons/pigro_icons/download_ico.png")

        self.bluetooth = PhotoImage(
            file=r"images/icons/papirus/48x48/blueman.png")
        self.wifi = PhotoImage(
            file=r"images/icons/papirus/48x48/kali-wireless-attacks-trans.png"
        )

        # Frame/Button Set
        self.rahmen4 = LabelFrame(
            self,
            text="GUI Tweaks",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.rahmen4.pack(pady=40, padx=40, fill="both")  #
        self.rahmen4["background"] = maincolor

        self.in_btn1 = Button(
            self.rahmen4,
            image=self.bash_history_icon,
            text="Tasksel",
            font=(
                "Sans",
                10,
            ),
            command=tasksel_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn1.grid(column=0, row=0, padx=5)

        self.in_btn2 = Button(
            self.rahmen4,
            image=self.bash_history_icon,
            text="Change Desktop",
            command=ch_desk,
            font=(
                "Sans",
                10,
            ),
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn2.grid(column=1, row=0, padx=5)

        self.in_btn3 = Button(
            self.rahmen4,
            image=self.bash_history_icon,
            text="Change Win-Manager",
            command=button_xfwm,
            font=(
                "Sans",
                10,
            ),
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn3.grid(column=2, row=0, padx=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.fm_godmode_icon,
            text="Theme Folder",
            font=(
                "Sans",
                10,
            ),
            command=theme_f,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn7.grid(column=0, row=1, padx=5, pady=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.fm_godmode_icon,
            text="Icon Folder",
            font=(
                "Sans",
                10,
            ),
            command=icon_f,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
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
            font=(
                "Sans",
                10,
            ),
            command=web_OVC,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn7.grid(column=2, row=1, padx=5)

        # xfce_tweaks
        self.rahmen41 = LabelFrame(
            self,
            text="Xfce Tweaks",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=15,
        )
        self.rahmen41.pack(padx=40, pady=20, fill="both")
        self.rahmen41["background"] = maincolor

        self.in_btn3 = Button(
            self.rahmen41,
            image=self.ico_m,
            justify="left",
            text="Xfwm4 Settings",
            command=button_xf4s,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            compound=LEFT,
            anchor="w",
            width=160,
            font=(
                "Sans",
                10,
            ),
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
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
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
            background=maincolor,
            foreground=main_font,
            anchor="w",
            width=160,
            font=(
                "Sans",
                10,
            ),
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
            background=maincolor,
            foreground=main_font,
            anchor="w",
            width=160,
            font=(
                "Sans",
                10,
            ),
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
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
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
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
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
            text="Pixel Tweaks",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=FLAT,
            pady=10,
            padx=15,
        )
        self.rahmen42.pack(padx=40, pady=20, fill="both")
        self.rahmen42["background"] = maincolor

        self.lx_btn0 = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="LXAppearace",
            compound=LEFT,
            command=lxap_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.lx_btn0.grid(column=0, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="OpenBox Conf",
            compound=LEFT,
            command=opbox_button,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.lxde.grid(column=1, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Pi Appeariance",
            compound=LEFT,
            command=pi_appear,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.lxde.grid(column=2, row=0)

        self.set_wp_btn = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Set Wallpaper",
            compound=LEFT,
            command=set_wp,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.set_wp_btn.grid(column=3, row=0)

        self.set_wp_btn = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Backup Panel\nSettings",
            compound=LEFT,
            command=pi_panel_bak,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.set_wp_btn.grid(column=0, row=1)

        self.set_wp_btn = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Restore\nDefault Panel ",
            compound=LEFT,
            command=pi_panel_restore,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.set_wp_btn.grid(column=1, row=1)

        self.set_wp_btn = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Restart\nPanel",
            compound=LEFT,
            command=pi_panel_restart,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            width=160,
            anchor="w",
            font=(
                "Sans",
                10,
            ),
        )
        self.set_wp_btn.grid(column=2, row=1)

        # pigrotweaks
        self.rahmen43 = LabelFrame(
            self,
            text="Pigro Tweaks",
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=FLAT,
            pady=10,
            padx=15,
        )
        self.rahmen43.pack(padx=40, pady=20, fill="both")
        self.rahmen43["background"] = maincolor

        # Theme Selction Dropdown Menu
        theme_select_frame = Frame(
            self.rahmen43, highlightthickness=0, borderwidth=0, background=maincolor
        )
        theme_select_frame.pack(side=LEFT)
        options = [
            "Dark Theme",
            "Light Theme",
        ]
        global select_clicked
        select_clicked = StringVar()
        select_clicked.set("Select Theme")
        drop = OptionMenu(
            theme_select_frame,
            select_clicked,
            *options,
        )
        drop.grid(column=0, row=0)
        drop.config(
            bg=maincolor,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
        )
        drop["menu"].config(
            bg=maincolor,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
        )

        select_theme_btn = Button(
            theme_select_frame,
            text="Select",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
            command=color_selected,
        )
        select_theme_btn.grid(column=1, row=0)

        # Transparency Selction Dropdown Menu
        trasp_select_frame = Frame(
            self.rahmen43, highlightthickness=0, borderwidth=0, background=maincolor
        )
        trasp_select_frame.pack()
        options = [
            "None",
            "0.95",
        ]
        global select_clicked1
        select_clicked1 = StringVar()
        select_clicked1.set("Select transparency")
        drop = OptionMenu(
            trasp_select_frame,
            select_clicked1,
            *options,
        )
        drop.grid(column=0, row=0)
        drop.config(
            bg=maincolor,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
        )
        drop["menu"].config(
            bg=maincolor,
            fg=main_font,
            activebackground=maincolor,
            activeforeground=main_font,
        )

        select_trasp_btn = Button(
            trasp_select_frame,
            text="Select",
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
            command=trans_selected,
        )
        select_trasp_btn.grid(column=1, row=0)


# [ZRAM] Child
class z_ram_pop(tk.Toplevel):
    """child window that lets one install zram"""

    def __init__(self, parent):
        super().__init__(parent)
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
        ft = tkFont.Font(family="Sans", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = maincolor
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.ip03
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = maincolor
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "ZRAM"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = maincolor
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Zram is a Linux kernel module that allows\nyou to set up compressed filesystems in RAM.\nzram-tools uses this module to set up compressed \nswap space.\nThis is useful on systems with low memory or servers\nrunning a large amount of services with data that's\neasily swappable but that you may wish to swap back\nfast without sacrificing disk bandwidth.\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Sans", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = z_ram_install

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Sans", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = z_ram_uninstall


# [Tuning] Tab
class Frame6(ttk.Frame):
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
            z_ram = z_ram_pop(self)
            z_ram.grab_set()

        def expert_mode():
            x_mode = Overclocking_Expert(self)
            x_mode.grab_set()

        # BG + Icons
        self.rm_ov_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV_rm.png")
        self.ov1_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV1.png")
        self.ov2_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV2.png")
        self.ov3_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV3.png")
        self.ov4_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV4.png")
        self.ov5_icon = PhotoImage(
            file=r"images/icons/pigro_icons/PiGroOV5.png")
        self.ip03 = PhotoImage(
            file=r"images/icons/pigro_icons/download_ico.png")
        self.tu_legend_ico = PhotoImage(
            file=r"images/icons/papirus/48x48/io.otsaloma.nfoview.png"
        )
        self.zram_icon = PhotoImage(
            file=r"images/icons/papirus/48x48/device_mem.png")

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

            pigro_t_display.config(text="not nonfigured", foreground="green")
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

        # overclocking_2200

        def ov_2200():
            os.system(
                f"""{legit} sh -c 'echo "#Pigro_Overclocking3\narm_freq=2200\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
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
                f"""{legit} sh -c 'echo "#Pigro_Overclocking4\narm_freq=2300\ngpu_freq=750\nover_voltage=14\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
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
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
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
            font=(
                "Sans",
                16,
            ),
            foreground="#d4244d",
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=10,
            pady=10,
        )
        self.ov_display_frame.pack(anchor="n")
        self.ov_display_frame["background"] = nav_color

        # Additional Infos

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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground="green",
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
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
            background=nav_color,
            foreground=main_font,
            font=(
                "Sans",
                12,
            ),
            width=25,
        )
        force_t_display.grid(column=1, row=6)

        self.tu_info = Label(
            self.ov_helps_frame,
            text="\n\n\n\n\n\n\n\nSettings tested with:\nRaspberry Pi 4B 8 GB Rev.1.4\nRaspberry Pi 4B 4 GB Rev.1.1\n+ Ice Tower Cooler & Pi400.\nI take no responsibility if\nyour Pi is damaged.\nPlease click on the Info Button\nto learn more",
            font=("Sans", 8, "bold"),
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=info_color,
        ).pack()

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
            font=(
                "Sans",
                10,
            ),
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
            font=(
                "Sans",
                10,
            ),
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
            font=(
                "Sans",
                10,
            ),
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
            font=(
                "Sans",
                10,
            ),
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
            font=(
                "Sans",
                10,
            ),
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
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
            compound=LEFT,
            font=(
                "Sans",
                10,
            ),
            width=200,
        )
        tu_btn5.grid(column=0, row=10, pady=10)

        # ZRAM Button
        self.tu_zbtn = Button(
            self.ov_buttons,
            image=self.zram_icon,
            justify="left",
            text="Install ZRAM",
            font=("Sans", 12),
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
            font=("Sans", 8),
            highlightthickness=0,
            borderwidth=0,
            background=nav_color,
            foreground=info_color,
            command=tuning_legende,
            image=self.tu_legend_ico,
        ).grid(column=0, row=13, pady=10)

        self.pigro_t_info = Label(
            self.ov_buttons,
            anchor="w",
            justify=LEFT,
            text="To unlock the overclocking options\non 'first use' click on:\nReset Overclocking",
            highlightthickness=0,
            borderwidth=2,
            background=maincolor,
            foreground=info_color,
            font=("Sans", 8, "bold"),
        )
        self.pigro_t_info.grid(column=0, row=14)

        def ov_display():
            # Overclock Display Functions
            with open(f"{config_path}", "r") as fp:
                for line in lines_that_contain("#Pigro_Overclocking1", fp):
                    # print(line)
                    if line:
                        pigro_t_display.config(
                            text="Crank It Up",
                            foreground="yellow",
                            bg=maincolor,
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
                    # print(line)
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
                        font=(
                            "Sans",
                            12,
                        ),
                    )
                    tu_btn1.config(state=DISABLED)
                    tu_btn2.config(state=DISABLED)
                    tu_btn3.config(state=DISABLED)
                    tu_btn4.config(state=DISABLED)
                if "#arm_freq=800" in line:
                    arm_f_display.config(
                        text="not configured",
                        foreground=main_font,
                        font=(
                            "Sans",
                            12,
                        ),
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
                        font=(
                            "Sans",
                            12,
                        ),
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
                        font=(
                            "Sans",
                            12,
                        ),
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
                        font=(
                            "Sans",
                            12,
                        ),
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
                        font=(
                            "Sans",
                            12,
                        ),
                    )

        def refresh_OV_stats():
            ov_display()
            self.after(3000, refresh_OV_stats)

        refresh_OV_stats()


# [Links] Tab
class Frame7(ttk.Frame):
    """a tab that display lot of links to cool websites"""

    def __init__(self, container):
        super().__init__()

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

        def rb_tv():
            popen("xdg-open https://linuxcommandlibrary.com/")

        def l4_e():
            popen("xdg-open http://www.lcdwiki.com/Main_Page")

        def pi_doc():
            popen("xdg-open https://www.raspberrypi.com/documentation/")

        def pi_tuto():
            popen("xdg-open https://tutorials-raspberrypi.com/")

        def vis_tk():
            popen("xdg-open https://visualtk.com/")

        def papirus_nord():
            popen("xdg-open https://github.com/Adapta-Projects/Papirus-Nord")

        def wave_share():
            popen("xdg-open  https://www.waveshare.com/wiki/Main_Page")

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

        self.choice_link1 = Button(
            self.link_left,
            anchor="w",
            width=50,
            text="Mankier.com (Commandline Database)",
            command=link_mankier,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=50,
            text="Guake (Drop Down Terminal)",
            command=link_guake,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=50,
            text="OnBoard (Onscreen Keyboard)",
            command=link_onBoard,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=50,
            text="Draculatheme.com",
            command=link_drac,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            anchor="w",
            width=50,
            text="Starship (Cross-Shell-Promt)",
            command=link_star,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link3 = Button(
            self.link_left,
            width=50,
            text="Linuxcommandlibrary.com",
            anchor="w",
            command=rb_tv,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="LCD Wiki",
            anchor="w",
            command=l4_e,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="Offical Raspberry Pi Documentation",
            anchor="w",
            command=pi_doc,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="Raspberry Pi Tutorials",
            anchor="w",
            command=pi_tuto,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="VisualTk.com",
            anchor="w",
            command=vis_tk,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="Papirus Nord Icon Theme",
            anchor="w",
            command=papirus_nord,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)

        self.choice_link2 = Button(
            self.link_left,
            width=50,
            text="WaveShare Wiki",
            anchor="w",
            command=wave_share,
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=main_font,
        ).pack(pady=5)


# [Runing Processes]
class ProcessTree(ttk.Frame):
    """sets up a treeview of all runnning processes"""

    def __init__(self, parent, *args, **kwargs):
        ttk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.tree = ttk.Treeview(self, columns=(
            "PID", "Name", "Memory"), height=30)
        self.tree.heading("#0", text="Process")
        self.tree.heading("#1", text="PID")
        self.tree.heading("#2", text="Memory")
        self.tree.column("#0", stretch=tk.YES)
        self.tree.column("#1", stretch=tk.YES)
        self.tree.column("#2", stretch=tk.YES)
        self.tree.grid(row=0, column=0, sticky="nsew")
        self.tree.bind("<Double-1>", self.OnDoubleClick)
        self.vsb = ttk.Scrollbar(
            self, orient="vertical", command=self.tree.yview)
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


# [Processes] Tab
class Frame14(ttk.Frame):
    """shows all running pocesses in a treeview"""

    def __init__(self, container, *args, **kwargs):
        super().__init__()

        self.proc_frame = Frame(
            self,
            bg=maincolor,
            highlightthickness=0,
            highlightcolor="white",
            pady=10,
            padx=10,
        )
        self.proc_frame.pack(pady=40)
        self.tree = ProcessTree(self.proc_frame)
        self.tree.pack(fill="both", expand=True)

        self.kill_button = Label(
            self.proc_frame,
            text="Double Click To Kill Process",
            bg=maincolor,
            foreground=info_color,
            borderwidth=0,
            highlightthickness=0,
        )
        self.kill_button.pack(side="left", pady=10)


# [About] Tab
class Frame8(ttk.Frame):
    """this tab contains infos and links to the devs website"""

    def __init__(self, container):
        super().__init__()

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def ch_log():
            c_log = Change_Log(self)
            c_log.grab_set()

        self.auto_start = PhotoImage(file=r"images/icons/logo_128x128.png")

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
            #justify="left",
            text="PiGro - Just Click It!\n(Perche sei cosi serio?)\nVersion: 9.0",
            font=("Sans", 18, "bold"),
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.change_log = Button(
            self.rahmen102,
            text="Changelog",
            font=("Sans", 10),
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
            # justify="left",
            text="\n\n\nDeveloped and maintained by:\n\nTimo Westphal\n(Actionschnitzel)\n\n\n\n\nContact:",
            font=("Sans", 12),
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.mail = Entry(self.rahmen102, bd=5, width=18, borderwidth=1)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.poke_pig_21 = Label(
            self.rahmen102,
            # justify="left",
            text="\n\n\n\n\n\n\n\nThis program comes with ABSOLUTELY NO WARRANTY!\nIt is licensed under the GNU General Public License v3.0\nIcons have been partially adopted and modified from the\nPapirus Icon Theme licensed under the\nGNU General Public License v3.0\n\n\n2022",
            font=("Sans", 9, "bold"),
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()


# [Cam] Tab
class Frame9(ttk.Frame):
    """basic gui for the raspberry pi camera functions"""

    def __init__(self, container):
        super().__init__()

        def photo1():
            photo = str(entry.get())
            popen(f"libcamera-jpeg -o {home}/{photo}.jpg")

        def video1():
            video = str(entry.get())
            rec_time = str(sec_entry.get() + "000")
            popen(f"libcamera-vid -t {rec_time} -o {home}/{video}.h264")

        self.rahmen101 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=0, pady=20, padx=10
        )
        self.rahmen101.pack(pady=50)
        self.rahmen101["background"] = maincolor

        self.btn_frame = Frame(self.rahmen101, bg=maincolor)
        self.btn_frame.pack()
        self.label = Label(
            self.btn_frame,
            text=" ",
            bg=maincolor,
            foreground=main_font,
        )
        self.label.pack()

        self.status_icon = PhotoImage(
            file="images/icons/pigro_icons/Pi-Camera.png")
        self.head_frame = Frame(self.rahmen101, bg=maincolor)
        self.head_frame.pack()
        self.header_label = Label(
            self.head_frame, image=self.status_icon, bg=maincolor)
        self.header_label.pack(pady=20)

        # Clicker_Frame
        self.btn_frame = Frame(self.rahmen101, bg=maincolor)
        self.btn_frame.pack()
        self.label = Label(
            self.btn_frame,
            text=f"Files will be saved in:\n{home}\n\nGive it a Name:",
            bg=maincolor,
            foreground=main_font,
        )
        self.label.pack()

        entry = Entry(self.btn_frame, bd=5, width=31, borderwidth=1)
        entry.pack()
        photo_btn = Button(
            self.btn_frame,
            text="Take A Photo",
            command=photo1,
            bg=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
        )
        photo_btn.pack(pady=10)

        video_btn = Button(
            self.btn_frame,
            text="Take A Video",
            command=video1,
            bg=ext_btn,
            foreground=main_font,
            highlightthickness=0,
            borderwidth=0,
        )
        video_btn.pack()

        sec_ent_label = Label(
            self.btn_frame,
            text="REC time in seconds:",
            bg=maincolor,
            foreground=main_font,
        )
        sec_ent_label.pack()

        sec_entry = Entry(self.btn_frame, bd=5, width=5, borderwidth=1)
        sec_entry.pack()


# [Error Massage] Child
class Error_Mass(tk.Toplevel):
    """opens a popup when entry field is empty"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
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

        self.e_m = PhotoImage(
            file=f"{Application_path}/images/backgrounds/yuno.png")

        error_frame = Frame(self, bg=maincolor)
        error_frame.pack(pady=10)

        error_img = Label(error_frame, image=self.e_m, bg=maincolor)
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(
            error_frame, text="Y U MAKE ERROR?", foreground=main_font, bg=maincolor
        )
        error_y.grid(row=0, column=1)

        error_y2 = Label(
            error_frame,
            text="You did not enter a value",
            foreground=main_font,
            bg=maincolor,
        )
        error_y2.grid(row=1, column=1)

        error_btn = Button(
            error_frame,
            text="...got IT!",
            foreground=main_font,
            borderwidth=0,
            highlightthickness=0,
            bg="red",
            command=cu_error,
        )
        error_btn.grid(row=3, column=1)


# [TOOLTIPZ]
class CreateToolTip(object):
    """create a tooltip for a given widget"""

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
    """This class animates the the .GIF in the install window"""

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
