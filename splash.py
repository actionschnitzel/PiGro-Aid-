from tkinter import *
import subprocess
import sys
import pkg_resources
import time
import random
from PIL import ImageTk, Image
import os
from os import popen
from os import system as cmd
import apt
import threading
import requests


class aptFind(apt.Cache):
    def __init__(self):
        super().__init__()

    def find(self, pkg):
        try:
            if self[pkg].is_installed:
                print(pkg + " is installed")
                return True
            else:
                print(pkg + " is NOT installed")
                return False
        except KeyError:
            print("ERROR: there is no package called '" + pkg + "'!")

    def install(self, pkg):
        command = "sudo apt install -y " + pkg
        cmd(command)

    def installIfNotInstalled(self, pkg):
        if not self.find(pkg):
            self.install(pkg)


def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])


def install_depends():
    global isInstalling
    isInstalling = True
    c = aptFind()
    c.installIfNotInstalled("xterm")
    c.installIfNotInstalled("python3-pil")
    c.installIfNotInstalled("python3-pil.imagetk")
    c.installIfNotInstalled("python3-pip")
    c.installIfNotInstalled("mpg123")
    c.installIfNotInstalled("lolcat")
    pip_install("distro")
    pip_install("psutil")
    # pip_install("pystray")
    isInstalling = False


def isConnected(url, timeout):
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


splash = Tk()
splash["background"] = "grey"

app_width = 499
app_height = 299
screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
splash.overrideredirect(True)

bg = PhotoImage(file="images/backgrounds/splash.png")

splash_canvas = Canvas(splash, width=499, height=299, highlightthickness=0)
splash_canvas.pack(fill="both", expand=True)

splash_canvas.create_image(0, 0, image=bg, anchor="nw")


list = [
    "Kamehameha\nwas the first king of\nHawaii",
    "Run PiGro in\nTerminal by:\n'pigro' ;-)",
    "Sono pigro",
    "Heidi Ho Winslow!",
    "I love Ubuntu... Server...",
    "I DID NOTHING!\nTHE PAVEMENT\nWAS HIS ENEMY!",
    "GO GO Power Rangers!",
    "It’s time to kick ass\nand chew bubble gum",
    "Splash screens suck!",
    "Snake? Snake? SNAKE!",
    "Frostmourne hungers",
    "It's alive! It's alive!",
    "They call it a Royale with cheese.",
    "Yo, Adrian!",
    "Go ahead, make my day.",
    "My Little Pony\nis not for Children",
    "Try the New\nMUST HAVES on Installer TAB",
]
item = random.choice(list)
# print(item)
splash_canvas.create_text(
    130,
    20,
    text="Checked Dependencies - Lets GO!!!",
    font=("Helvetica", 11, "bold"),
    fill="white",
)

splash_canvas.create_text(
    250, 250, text=item, font=("Helvetica", 18, "bold"), fill="white"
)


def loop():
    while isInstalling == True:
        pass
    splash.destroy()


if isConnected("https://github.com", 5):
    t = threading.Thread(target=install_depends)
    splash.after(3000, loop)
    t.start()
else:
    print(
        "\033[1;33mWARNING: not connected to the internet!\033[0m"
    )  # print in bold yellow
    splash.after(3000, splash.destroy)


popen('find ~/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;')
popen("~/PiGro-Aid-/scripts/check_bin.sh")
os.system(
    "xterm -e 'bash -c \"apt-cache pkgnames > ~/PiGro-Aid-/scripts/apt_cache.list && exit; exec bash\"'"
)

mainloop()
