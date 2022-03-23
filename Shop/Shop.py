# https://visualtk.com/

import tkinter.font as tkFont
import os
import tkinter as tk
import webbrowser
from os import popen
from os import system as cmd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import platform
import psutil
from collections import namedtuple
from datetime import datetime
import distro
import socket
import subprocess


# from gpiozero import CPUTemperature
from pathlib import Path


class App:
    def __init__(self, root):
        # setting title
        root.title("Shop")
        icon = tk.PhotoImage(file="~/PiGro-Aid-/images/icons/pdl_ico.png")
        root.tk.call("wm", "iconphoto", root._w, icon)
        root["background"] = "#333333"

        # setting window size
        width = 625
        height = 500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        self.albert_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Albert/icon.png")
        self.argon_icon = PhotoImage(
            file=r"~/PiGro-Aid-/Shop/Argon_One_Driver/icon.png"
        )
        self.bleach_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Bleach_Bit/icon.png")
        self.bpytop_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/bpytop/icon.png")
        self.commanderpi_icon = PhotoImage(
            file=r"~/PiGro-Aid-/Shop/CommanderPi/icon.png"
        )
        self.compiz_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Compiz/icon.png")
        self.deskpi_icon = PhotoImage(
            file=r"~/PiGro-Aid-/Shop/DeskPi_Pro_Driver/icon.png"
        )
        self.fanshim_icon = PhotoImage(
            file=r"~/PiGro-Aid-/Shop/FanShim_Driver/icon.png"
        )
        self.gnomepie_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Gnome-Pie/icon.png")
        self.gparted_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Gparted/icon.png")
        self.neofetch_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/NeoFetch/icon.png")
        self.piapps_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Pi-Apps/icon.png")
        self.pi_imager_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Pi_Imager/icon.png")
        self.pi_kiss_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Pikiss/icon.png")
        self.plank_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Plank/icon.png")
        self.sub_text_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Sublime_Text/icon.png")
        self.sub_merge_icon = PhotoImage(
            file=r"~/PiGro-Aid-/Shop/Sublime_Merge/icon.png"
        )
        self.tetris_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Tetris-CLI/icon.png")
        self.tilix_icon = PhotoImage(file=r"~/PiGro-Aid-/Shop/Tilix/icon.png")

        Albert_BTN = tk.Button(root)
        Albert_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        Albert_BTN["font"] = ft
        Albert_BTN["fg"] = "#000000"
        Albert_BTN["justify"] = "center"
        Albert_BTN["text"] = "Albert"
        Albert_BTN["image"] = self.albert_icon
        Albert_BTN["compound"] = "top"
        Albert_BTN.place(x=20, y=30, width=100, height=100)
        Albert_BTN["command"] = self.Albert_BTN_command

        ARGON_BTN = tk.Button(root)
        ARGON_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        ARGON_BTN["font"] = ft
        ARGON_BTN["fg"] = "#000000"
        ARGON_BTN["justify"] = "center"
        ARGON_BTN["text"] = "Argon One"
        ARGON_BTN["image"] = self.argon_icon
        ARGON_BTN["compound"] = "top"
        ARGON_BTN.place(x=140, y=30, width=100, height=100)
        ARGON_BTN["command"] = self.ARGON_BTN_command

        BLEACH_BTN = tk.Button(root)
        BLEACH_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        BLEACH_BTN["font"] = ft
        BLEACH_BTN["fg"] = "#000000"
        BLEACH_BTN["justify"] = "center"
        BLEACH_BTN["text"] = "Bleach Bit"
        BLEACH_BTN["image"] = self.bleach_icon
        BLEACH_BTN["compound"] = "top"
        BLEACH_BTN.place(x=260, y=30, width=100, height=100)
        BLEACH_BTN["command"] = self.BLEACH_BTN_command

        BPYTOP_BTN = tk.Button(root)
        BPYTOP_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        BPYTOP_BTN["font"] = ft
        BPYTOP_BTN["fg"] = "#000000"
        BPYTOP_BTN["justify"] = "center"
        BPYTOP_BTN["text"] = "BpyTop"
        BPYTOP_BTN["image"] = self.bpytop_icon
        BPYTOP_BTN["compound"] = "top"
        BPYTOP_BTN.place(x=380, y=30, width=100, height=100)
        BPYTOP_BTN["command"] = self.BPYTOP_BTN_command

        CMNDR_BTN = tk.Button(root)
        CMNDR_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        CMNDR_BTN["font"] = ft
        CMNDR_BTN["fg"] = "#000000"
        CMNDR_BTN["justify"] = "center"
        CMNDR_BTN["text"] = "Commander Pi"
        CMNDR_BTN["image"] = self.commanderpi_icon
        CMNDR_BTN["compound"] = "top"
        CMNDR_BTN.place(x=500, y=30, width=100, height=100)
        CMNDR_BTN["command"] = self.CMNDR_BTN_command

        COMPIZ_BTN = tk.Button(root)
        COMPIZ_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        COMPIZ_BTN["font"] = ft
        COMPIZ_BTN["fg"] = "#000000"
        COMPIZ_BTN["justify"] = "center"
        COMPIZ_BTN["text"] = "Compiz"
        COMPIZ_BTN["image"] = self.compiz_icon
        COMPIZ_BTN["compound"] = "top"
        COMPIZ_BTN.place(x=20, y=150, width=100, height=100)
        COMPIZ_BTN["command"] = self.COMPIZ_BTN_command

        DESKPI_BTN = tk.Button(root)
        DESKPI_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        DESKPI_BTN["font"] = ft
        DESKPI_BTN["fg"] = "#000000"
        DESKPI_BTN["justify"] = "center"
        DESKPI_BTN["text"] = "DeskPi"
        DESKPI_BTN["image"] = self.deskpi_icon
        DESKPI_BTN["compound"] = "top"
        DESKPI_BTN.place(x=140, y=150, width=100, height=100)
        DESKPI_BTN["command"] = self.DESKPI_BTN_command

        FanShim_BTN = tk.Button(root)
        FanShim_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        FanShim_BTN["font"] = ft
        FanShim_BTN["fg"] = "#000000"
        FanShim_BTN["justify"] = "center"
        FanShim_BTN["text"] = "FanShim"
        FanShim_BTN["image"] = self.fanshim_icon
        FanShim_BTN["compound"] = "top"
        FanShim_BTN.place(x=260, y=150, width=100, height=100)
        FanShim_BTN["command"] = self.FanShim_BTN_command

        GNOMEPI_BTN = tk.Button(root)
        GNOMEPI_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GNOMEPI_BTN["font"] = ft
        GNOMEPI_BTN["fg"] = "#000000"
        GNOMEPI_BTN["justify"] = "center"
        GNOMEPI_BTN["text"] = "Gnome-Pie"
        GNOMEPI_BTN["image"] = self.gnomepie_icon
        GNOMEPI_BTN["compound"] = "top"
        GNOMEPI_BTN.place(x=380, y=150, width=100, height=100)
        GNOMEPI_BTN["command"] = self.GNOMEPI_BTN_command

        GPARTED_BTN = tk.Button(root)
        GPARTED_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GPARTED_BTN["font"] = ft
        GPARTED_BTN["fg"] = "#000000"
        GPARTED_BTN["justify"] = "center"
        GPARTED_BTN["text"] = "GParted"
        GPARTED_BTN["image"] = self.gparted_icon
        GPARTED_BTN["compound"] = "top"
        GPARTED_BTN.place(x=500, y=150, width=100, height=100)
        GPARTED_BTN["command"] = self.GPARTED_BTN_command

        NEOFETCH_BTN = tk.Button(root)
        NEOFETCH_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        NEOFETCH_BTN["font"] = ft
        NEOFETCH_BTN["fg"] = "#000000"
        NEOFETCH_BTN["justify"] = "center"
        NEOFETCH_BTN["text"] = "NeoFetch"
        NEOFETCH_BTN["image"] = self.neofetch_icon
        NEOFETCH_BTN["compound"] = "top"
        NEOFETCH_BTN.place(x=20, y=270, width=100, height=100)
        NEOFETCH_BTN["command"] = self.NEOFETCH_BTN_command

        PIIMAGER_BTN = tk.Button(root)
        PIIMAGER_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        PIIMAGER_BTN["font"] = ft
        PIIMAGER_BTN["fg"] = "#000000"
        PIIMAGER_BTN["justify"] = "center"
        PIIMAGER_BTN["text"] = "Pi-Imager"
        PIIMAGER_BTN["image"] = self.pi_imager_icon
        PIIMAGER_BTN["compound"] = "top"
        PIIMAGER_BTN.place(x=140, y=270, width=100, height=100)
        PIIMAGER_BTN["command"] = self.PIIMAGER_BTN_command

        PIKISS_BTN = tk.Button(root)
        PIKISS_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        PIKISS_BTN["font"] = ft
        PIKISS_BTN["fg"] = "#000000"
        PIKISS_BTN["justify"] = "center"
        PIKISS_BTN["text"] = "piKISS"
        PIKISS_BTN["image"] = self.pi_kiss_icon
        PIKISS_BTN["compound"] = "top"
        PIKISS_BTN.place(x=260, y=270, width=100, height=100)
        PIKISS_BTN["command"] = self.PIKISS_BTN_command

        PLANK_BTN = tk.Button(root)
        PLANK_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        PLANK_BTN["font"] = ft
        PLANK_BTN["fg"] = "#000000"
        PLANK_BTN["justify"] = "center"
        PLANK_BTN["text"] = "Plank"
        PLANK_BTN["image"] = self.plank_icon
        PLANK_BTN["compound"] = "top"
        PLANK_BTN.place(x=380, y=270, width=100, height=100)
        PLANK_BTN["command"] = self.PLANK_BTN_command

        SUB_TEXT_BTN = tk.Button(root)
        SUB_TEXT_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        SUB_TEXT_BTN["font"] = ft
        SUB_TEXT_BTN["fg"] = "#000000"
        SUB_TEXT_BTN["justify"] = "center"
        SUB_TEXT_BTN["text"] = "Sublime Text"
        SUB_TEXT_BTN["image"] = self.sub_text_icon
        SUB_TEXT_BTN["compound"] = "top"
        SUB_TEXT_BTN.place(x=500, y=270, width=100, height=100)
        SUB_TEXT_BTN["command"] = self.SUB_TEXT_BTN_command

        SUB_MERGE_BTN = tk.Button(root)
        SUB_MERGE_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        SUB_MERGE_BTN["font"] = ft
        SUB_MERGE_BTN["fg"] = "#000000"
        SUB_MERGE_BTN["justify"] = "center"
        SUB_MERGE_BTN["text"] = "Sublime Merge"
        SUB_MERGE_BTN["image"] = self.sub_merge_icon
        SUB_MERGE_BTN["compound"] = "top"
        SUB_MERGE_BTN.place(x=20, y=390, width=100, height=100)
        SUB_MERGE_BTN["command"] = self.SUB_MERGE_BTN_command

        TETRIS_BTN = tk.Button(root)
        TETRIS_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        TETRIS_BTN["font"] = ft
        TETRIS_BTN["fg"] = "#000000"
        TETRIS_BTN["justify"] = "center"
        TETRIS_BTN["text"] = "Tetris CLI"
        TETRIS_BTN["image"] = self.tetris_icon
        TETRIS_BTN["compound"] = "top"
        TETRIS_BTN.place(x=140, y=390, width=100, height=100)
        TETRIS_BTN["command"] = self.TETRIS_BTN_command

        TILIX_BTN = tk.Button(root)
        TILIX_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        TILIX_BTN["font"] = ft
        TILIX_BTN["fg"] = "#000000"
        TILIX_BTN["justify"] = "center"
        TILIX_BTN["text"] = "Tilix Terminal"
        TILIX_BTN["image"] = self.tilix_icon
        TILIX_BTN["compound"] = "top"
        TILIX_BTN.place(x=260, y=390, width=100, height=100)
        TILIX_BTN["command"] = self.TILIX_BTN_command

        PIAPPS_BTN = tk.Button(root)
        PIAPPS_BTN["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        PIAPPS_BTN["font"] = ft
        PIAPPS_BTN["fg"] = "#000000"
        PIAPPS_BTN["justify"] = "center"
        PIAPPS_BTN["text"] = "Pi-Apps"
        PIAPPS_BTN["image"] = self.piapps_icon
        PIAPPS_BTN["compound"] = "top"
        PIAPPS_BTN.place(x=380, y=390, width=220, height=100)
        PIAPPS_BTN["command"] = self.PIAPPS_BTN_command

    #
    #         GButton_762=tk.Button(root)
    #         GButton_762["bg"] = "#efefef"
    #         ft = tkFont.Font(family='Helvetica',size=10)
    #         GButton_762["font"] = ft
    #         GButton_762["fg"] = "#000000"
    #         GButton_762["justify"] = "center"
    #         GButton_762["text"] = "Button"
    #         GButton_762.place(x=500,y=390,width=100,height=100)
    #         GButton_762["command"] = self.GButton_762_command

    # Albert
    def Albert_BTN_command(self):
        global albert_pop
        albert_pop = Toplevel()
        # setting title
        albert_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = albert_pop.winfo_screenwidth()
        screenheight = albert_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        albert_pop.geometry(alignstr)
        albert_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(albert_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.albert_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(albert_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Albert for Debian Buster"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(albert_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Albert is a desktop agnostic launcher.\nIts goals are usability and beauty, performance and extensibility.\nIt is written in C++ and based on the Qt framework."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(albert_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.albert_install

        GButton_585 = tk.Button(albert_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.albert_uninstall

    def albert_install(self):
        popen("xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Albert/install.sh; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Albert has been installed"]
        )

    def albert_uninstall(self):
        popen("xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Albert/uninstall.sh; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Albert has been uninstalled"]
        )

    # Argon One
    def ARGON_BTN_command(self):
        global argon_pop
        argon_pop = Toplevel()
        # setting title
        argon_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = argon_pop.winfo_screenwidth()
        screenheight = argon_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        argon_pop.geometry(alignstr)
        argon_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(argon_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.argon_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(argon_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Argon One /M.2 Driver"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(argon_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Drivers for the Argon One Case"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(argon_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.argon_install

        GButton_585 = tk.Button(argon_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.argon_uninstall

    def argon_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Argon_One_Driver/install.sh; exec bash\"'"
        )
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Argon One Driver has been installed",
            ]
        )

    def argon_uninstall(self):
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Please use Argons native uninstaller!",
            ]
        )

    # Blech Bit
    def BLEACH_BTN_command(self):
        global bleach_pop
        bleach_pop = Toplevel()
        # setting title
        bleach_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = bleach_pop.winfo_screenwidth()
        screenheight = bleach_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        bleach_pop.geometry(alignstr)
        bleach_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(bleach_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.bleach_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(bleach_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Blech Bit"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(bleach_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "When your computer is getting full,\nBleachBit quickly frees disk space.\nWhen your information is only your business,\nBleachBit guards your privacy.\nWith BleachBit you can free cache, delete cookies,\nclear Internet history, shred temporary files, delete logs,\nand discard junk you didn't know was there. "
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(bleach_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.bleach_install

        GButton_585 = tk.Button(bleach_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.bleach_uninstall

    def bleach_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install bleachbit -y && exit; exec bash\"'"
        )
        self.subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Bleach Bit has been installed"]
        )

    def bleach_uninstall(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get remove bleachbit -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Bleach Bit has been uninstalled"]
        )

    # BpyTop
    def BPYTOP_BTN_command(self):
        global bpytop_pop
        bpytop_pop = Toplevel()
        # setting title
        bpytop_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = bpytop_pop.winfo_screenwidth()
        screenheight = bpytop_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        bpytop_pop.geometry(alignstr)
        bpytop_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(bpytop_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.bpytop_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(bpytop_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "BpyTop"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(bpytop_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Easy to use, with a game inspired menu system.\nFull mouse support, all buttons with a highlighted\nkey is clickable and mouse scroll works in process\n list and menu boxes.\nFast and responsive UI with UP, DOWN keys process selection.\nFunction for showing detailed stats for selected process.\nAbility to filter processes, multiple filters can be entered.\nEasy switching between sorting options.\nSend SIGTERM, SIGKILL, SIGINT to selected process.\nUI menu for changing all config file options.\nAuto scaling graph for network usage.\nShows message in menu if new version is available\nShows current read and write speeds for disks\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(bpytop_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.bpytop_install

        GButton_585 = tk.Button(bpytop_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.bpytop_uninstall

    def bpytop_install(self):
        popen("xterm -e 'bash -c \"pip3 install bpytop && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "BpyTop has been installed"]
        )

    def bpytop_uninstall(self):
        popen("xterm -e 'bash -c \"pip3 uninstall bpytop && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "BpyTop has been uninstalled"]
        )

    # Commander Pi
    def CMNDR_BTN_command(self):
        global commanderpi_pop
        commanderpi_pop = Toplevel()
        # setting title
        commanderpi_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = commanderpi_pop.winfo_screenwidth()
        screenheight = commanderpi_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        commanderpi_pop.geometry(alignstr)
        commanderpi_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(commanderpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.commanderpi_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(commanderpi_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "CommanderPi"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(commanderpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "-Check your system information (CPU temperature, CPU usage,\nKernel version,etc)\nwith an user friendly menu.\n\n-Easy overclocking!\n\n-Checks the actual bootloader\nconfiguration and setup your own!\n\n-Switch between the 64bit and 32bit Linux Kernel!\n(EXPERIMENTAL)\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(commanderpi_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.commanderpi_install

        GButton_585 = tk.Button(commanderpi_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.commanderpi_uninstall

    def commanderpi_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/CommanderPi/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Commander Pi has been installed"]
        )

    def commanderpi_uninstall(self):
        print("command")
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Please use Commander Pis nativ uninstaller",
            ]
        )

    # Compiz
    def COMPIZ_BTN_command(self):
        global compiz_pop
        compiz_pop = Toplevel()
        # setting title
        compiz_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = compiz_pop.winfo_screenwidth()
        screenheight = compiz_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        compiz_pop.geometry(alignstr)
        compiz_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(compiz_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.compiz_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(compiz_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Compiz"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(compiz_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Compiz is an OpenGL compositing manager\nthat use GLX_EXT_texture_from_pixmap for\nbinding redirected top-level windows\nto texture objects.\nIt has a flexible plug-in system and\nit is designed to run well on\nmost graphics hardware."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(compiz_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.compiz_install

        GButton_585 = tk.Button(compiz_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.compiz_uninstall

    def compiz_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install compiz -y && exit; exec bash\"'"
        )
        # subprocess.call(['notify-send','PiGro - Just Click It!','Compiz has been installed'])

    def compiz_uninstall(self):
        popen("xterm -e 'bash -c \"sudo apt-get remove compiz -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Compiz has been uninstalled"]
        )

    # Deskpi Pro
    def DESKPI_BTN_command(self):
        global deskpi_pop
        deskpi_pop = Toplevel()
        # setting title
        deskpi_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = deskpi_pop.winfo_screenwidth()
        screenheight = deskpi_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        deskpi_pop.geometry(alignstr)
        deskpi_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.deskpi_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "DeskPi Pro Driver"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Drivers for the DeskPi Pro Case"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(deskpi_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.deskpi_install

        GButton_585 = tk.Button(deskpi_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.deskpi_uninstall

    def deskpi_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/DeskPi_Pro_Driver/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "DeskPi Driver has been installed",
            ]
        )

    def deskpi_uninstall(self):
        print("command")
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Please use DeskPis nativ uninstaller",
            ]
        )

    # FanShim
    def FanShim_BTN_command(self):
        global deskpi_pop
        deskpi_pop = Toplevel()
        # setting title
        deskpi_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = deskpi_pop.winfo_screenwidth()
        screenheight = deskpi_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        deskpi_pop.geometry(alignstr)
        deskpi_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.deskpi_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "deskpi"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(deskpi_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Drivers for the FanShim"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(deskpi_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.deskpi_install

        GButton_585 = tk.Button(deskpi_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.deskpi_uninstall

    def deskpi_install(self):
        print("command")

    def deskpi_uninstall(self):
        print("command")

    # Gnome-Pie
    def GNOMEPI_BTN_command(self):
        global gnomepie_pop
        gnomepie_pop = Toplevel()
        # setting title
        gnomepie_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = gnomepie_pop.winfo_screenwidth()
        screenheight = gnomepie_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        gnomepie_pop.geometry(alignstr)
        gnomepie_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(gnomepie_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.gnomepie_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(gnomepie_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Gnome-Pie"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(gnomepie_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Gnome-Pie is a circular application\nlauncher for Linux.\nt is made of several pies, each consisting\nof multiple slices. The user presses a key stroke\nwhich opens the desired pie.\nBy activating one of its slices,\napplications may be launched,\nkey presses may be simulated or\nfiles can be opened."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(gnomepie_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.gnomepie_install

        GButton_585 = tk.Button(gnomepie_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.gnomepie_uninstall

    def gnomepie_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install gnome-pie -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Gnome-Pie has been installed"]
        )

    def gnomepie_uninstall(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get remove gnome-pie -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Gnome-Pie has been uninstalled"]
        )

    # Gparted
    def GPARTED_BTN_command(self):
        global gparted_pop
        gparted_pop = Toplevel()
        # setting title
        gparted_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = gparted_pop.winfo_screenwidth()
        screenheight = gparted_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        gparted_pop.geometry(alignstr)
        gparted_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(gparted_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.gparted_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(gparted_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Gparted"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(gparted_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "GParted is a GTK front-end to GNU Parted\nand an official GNOME partition-editing application.\nGParted is used for creating, deleting, resizing,\nmoving, checking, and copying disk partitions and their\nfile systems. This is useful for creating space\nfor new operating systems, reorganizing disk usage,\ncopying data residing on hard disks,\nand mirroring one partition with another."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(gparted_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.gparted_install

        GButton_585 = tk.Button(gparted_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.gparted_uninstall

    def gparted_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install gparted -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Gparted has been installed"]
        )

    def gparted_uninstall(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get remove gparted -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Gparted has been uninstalled"]
        )

    # NeoFetch
    def NEOFETCH_BTN_command(self):
        global neofetch_pop
        neofetch_pop = Toplevel()
        # setting title
        neofetch_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = neofetch_pop.winfo_screenwidth()
        screenheight = neofetch_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        neofetch_pop.geometry(alignstr)
        neofetch_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(neofetch_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.neofetch_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(neofetch_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Neofetch"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(neofetch_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Neofetch is a command-line system information\ntool written in bash 3.2+ .\nNeofetch displays information\nabout your operating system,\nsoftware and hardware ..."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(neofetch_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.neofetch_install

        GButton_585 = tk.Button(neofetch_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.neofetch_uninstall

    def neofetch_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install neofetch -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Neofetch has been installed"]
        )

    def neofetch_uninstall(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get remove neofetch -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Neofetch has been uninstalled"]
        )

    # Pi-Imager
    def PIIMAGER_BTN_command(self):
        global pi_imager_pop
        pi_imager_pop = Toplevel()
        # setting title
        pi_imager_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = pi_imager_pop.winfo_screenwidth()
        screenheight = pi_imager_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        pi_imager_pop.geometry(alignstr)
        pi_imager_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(pi_imager_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.pi_imager_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(pi_imager_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Pi_Imager"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(pi_imager_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Flash an OS to SD"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(pi_imager_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.pi_imager_install

        GButton_585 = tk.Button(pi_imager_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.pi_imager_uninstall

    def pi_imager_install(self):
        popen(
            "xterm -e 'bash -c \"sudo apt-get install imager -y && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Pi Imager has been installed"]
        )

    def pi_imager_uninstall(self):
        popen("xterm -e 'bash -c \"sudo apt-get remove imager -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Pi Imager has been uninstalled"]
        )

    # PiKiss
    def PIKISS_BTN_command(self):
        global pi_kiss_pop
        pi_kiss_pop = Toplevel()
        # setting title
        pi_kiss_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = pi_kiss_pop.winfo_screenwidth()
        screenheight = pi_kiss_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        pi_kiss_pop.geometry(alignstr)
        pi_kiss_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(pi_kiss_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.pi_kiss_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(pi_kiss_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Pi_Kiss"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(pi_kiss_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Install Tools & Games, Config Your Pi"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(pi_kiss_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.pi_kiss_install

        GButton_585 = tk.Button(pi_kiss_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.pi_kiss_uninstall

    def pi_kiss_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Pikiss/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "PiKiss has been installed"]
        )

    def pi_kiss_uninstall(self):
        print("command")
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Please use PiKiss nativ uninstaller",
            ]
        )

    # Plank
    def PLANK_BTN_command(self):
        global plank_pop
        plank_pop = Toplevel()
        # setting title
        plank_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = plank_pop.winfo_screenwidth()
        screenheight = plank_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        plank_pop.geometry(alignstr)
        plank_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(plank_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.plank_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(plank_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Plank"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(plank_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Plank is meant to be the simplest dock on the planet.\nThe goal is to provide just what a dock needs\nand absolutely nothing more.\nIt is, however,\na library which can be extended to create other\ndock programs with more advanced features."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(plank_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.plank_install

        GButton_585 = tk.Button(plank_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.plank_uninstall

    def plank_install(self):
        popen("xterm -e 'bash -c \"sudo apt-get install plank -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Plank has been installed"]
        )

    def plank_uninstall(self):
        popen("xterm -e 'bash -c \"sudo apt-get remove plank -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Plank has been uninstalled"]
        )

    # Sub Text
    def SUB_TEXT_BTN_command(self):
        global sub_text_pop
        sub_text_pop = Toplevel()
        # setting title
        sub_text_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = sub_text_pop.winfo_screenwidth()
        screenheight = sub_text_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        sub_text_pop.geometry(alignstr)
        sub_text_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(sub_text_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.sub_text_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(sub_text_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Sublime Text for aarch64"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(sub_text_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Sublime Text is a sophisticated text editor for code,\nmarkup and prose. "
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(sub_text_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.sub_text_install

        GButton_585 = tk.Button(sub_text_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.sub_text_uninstall

    def sub_text_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Sublime_Text/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Sublime Text has been installed"]
        )

    def sub_text_uninstall(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Sublime_Text/uninstall.sh && exit; exec bash\"'"
        )
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Sublime Text has been uninstalled",
            ]
        )

    # Sub Merge
    def SUB_MERGE_BTN_command(self):
        global sub_merge_pop
        sub_merge_pop = Toplevel()
        # setting title
        sub_merge_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = sub_merge_pop.winfo_screenwidth()
        screenheight = sub_merge_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        sub_merge_pop.geometry(alignstr)
        sub_merge_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(sub_merge_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.sub_merge_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(sub_merge_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Sublime Merge for aarch64"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(sub_merge_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Graphical Git Client"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(sub_merge_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.sub_merge_install

        GButton_585 = tk.Button(sub_merge_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.sub_merge_uninstall

    def sub_merge_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Sublime_Merge/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Sublime Merge has been installed",
            ]
        )

    def sub_merge_uninstall(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Sublime_Merge/uninstall.sh && exit; exec bash\"'"
        )
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Sublime Merge has been uninstalled",
            ]
        )

    # Tetris
    def TETRIS_BTN_command(self):
        global tetris_pop
        tetris_pop = Toplevel()
        # setting title
        tetris_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = tetris_pop.winfo_screenwidth()
        screenheight = tetris_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        tetris_pop.geometry(alignstr)
        tetris_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(tetris_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.tetris_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(tetris_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Tetris"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(tetris_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29["text"] = "Tetris in Terminal"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(tetris_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.tetris_install

        GButton_585 = tk.Button(tetris_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.tetris_uninstall

    def tetris_install(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Tetris-CLI/install.sh && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Tetris has been installed"]
        )

    def tetris_uninstall(self):
        popen(
            "xterm -e 'bash -c \"~/PiGro-Aid-/Shop/Tetris-CLI/uninstall.sh && exit; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Tetris has been uninstalled"]
        )

    # Tilix
    def TILIX_BTN_command(self):
        global tilix_pop
        tilix_pop = Toplevel()
        # setting title
        tilix_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = tilix_pop.winfo_screenwidth()
        screenheight = tilix_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        tilix_pop.geometry(alignstr)
        tilix_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(tilix_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.tilix_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(tilix_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Tilix"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(tilix_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Tilix is an advanced GTK3\ntiling terminal emulator\nthat follows the Gnome Human Interface\nGuidelines."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(tilix_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.tilix_install

        GButton_585 = tk.Button(tilix_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.tilix_uninstall

    def tilix_install(self):
        popen("xterm -e 'bash -c \"sudo apt-get install tilix -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Tilix has been installed"]
        )

    def tilix_uninstall(self):
        popen("xterm -e 'bash -c \"sudo apt-get remove tilix -y && exit; exec bash\"'")
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Tilix has been uninstalled"]
        )

    def PIAPPS_BTN_command(self):
        global piapps_pop
        piapps_pop = Toplevel()
        # setting title
        piapps_pop.title("")
        # setting window size
        width = 552
        height = 280
        screenwidth = piapps_pop.winfo_screenwidth()
        screenheight = piapps_pop.winfo_screenheight()
        alignstr = "%dx%d+%d+%d" % (
            width,
            height,
            (screenwidth - width) / 2,
            (screenheight - height) / 2,
        )
        piapps_pop.geometry(alignstr)
        piapps_pop.resizable(width=False, height=False)

        GLabel_804 = tk.Label(piapps_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.piapps_icon
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(piapps_pop)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "Pi-Apps"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(piapps_pop)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Introducing Pi-Apps, a well-maintained collection of\napp installation-scripts that you can run with one click.\nPi-Apps now serves over 1,000,000 people\nand hosts nearly 200 apps."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(piapps_pop)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = self.piapps_install

        GButton_585 = tk.Button(piapps_pop)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = self.piapps_uninstall

    def piapps_install(self):
        popen(
            "xterm -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'"
        )
        subprocess.call(
            ["notify-send", "PiGro - Just Click It!", "Pi-Apps has been uninstalled"]
        )

    def piapps_uninstall(self):
        print("command")
        subprocess.call(
            [
                "notify-send",
                "PiGro - Just Click It!",
                "Please use PiKiss nativ uninstaller",
            ]
        )


#    def GButton_762_command(self):
#        print("command")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
