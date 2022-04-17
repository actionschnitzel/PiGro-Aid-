import os
import os.path
import tkinter as tk
from tkinter.dialog import DIALOG_ICON
from turtle import width
import tkinter.font as tkFont
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
from gpiozero import CPUTemperature
from pathlib import Path
from cgitb import enable
from pynotifier import Notification
from subprocess import check_call, CalledProcessError
from threading import Thread
from concurrent.futures import thread



# Say Hallo!
global user
user = os.environ.get('LOGNAME')
print(f"Hi,{user} waz uuuuup?!")

# Define Home
global home
home = str(Path.home())
print(f"{home} is your home directory!")

# Get Desktop Environment
global get_de
get_de = os.environ.get("XDG_CURRENT_DESKTOP")
print("You are using: " + get_de)

class App:
    def __init__(self, root):
        #setting title
        root.title("Go Xfce")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)


        wiper_icon=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        wiper_icon["font"] = ft
        wiper_icon["fg"] = "#333333"
        wiper_icon["justify"] = "center"
        wiper_icon["text"] = "wiper_icon"
        wiper_icon.place(x=30,y=40,width=70,height=25)

        global pix_entry
        pix_entry=tk.Entry(root)
        pix_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Helvetica',size=10)
        pix_entry["font"] = ft
        pix_entry["fg"] = "#333333"
        pix_entry["justify"] = "center"
        pix_entry["text"] = "Entry"
        pix_entry.place(x=30,y=410,width=411,height=30)

        global verifier
        verifier = pix_entry.get()


        killer_btn=tk.Button(root)
        killer_btn["bg"] = "#efefef"
        ft = tkFont.Font(family='Helvetica',size=10)
        killer_btn["font"] = ft
        killer_btn["fg"] = "#000000"
        killer_btn["justify"] = "center"
        killer_btn["text"] = "Ok!"
        killer_btn.place(x=470,y=410,width=81,height=30)
        killer_btn["command"] = self.killer_btn_command

        pix_info_text=tk.Label(root)
        ft = tkFont.Font(family='Helvetica',size=10)
        pix_info_text["font"] = ft
        pix_info_text["fg"] = "#333333"
        pix_info_text["justify"] = "left"
        pix_info_text["text"] = "#Note:\n\nYou use it at your own risk.\nA clean installation of Xfce4 and lightDM is done:\n\nxfce4 xfce4-terminal xfce4-goodies lightdm slick-greeter bluetooth\npulseaudio-module-bluetooth blueman bluez-firmware\nnetwork-manager-gnome\n\nIf you continue,\nall PIXEL and LXDE desktop elements will be permanently removed:\n\nlxde* pipanel lxpanel openbox* obconf\n\n\nTo continue,\ntype 'Yes, do as I say!' in the field and click Ok!"
        pix_info_text.place(x=130,y=50,width=422,height=325)

    def killer_btn_command(self):
        if pix_entry.get() == "Yes, do as I say!":
            popen("xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/hallo_xfce.sh; exec bash\"'")

        else:
            pix_entry.delete(0,'end')
            pix_entry.insert(0,"Nope, try again!")
            

            
        

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
