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
                print(pkg+" is installed")
                return True
            else:
                print(pkg+" is NOT installed")
                return False
        except KeyError:
            print("ERROR: there is no package called '"+pkg+"'!")
    def install(self, pkg):
        command='sudo apt install -y '+pkg
        cmd(command)
    def installIfNotInstalled(self, pkg):
        if not self.find(pkg):
            self.install(pkg)
def pip_install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

def install_depends():
    global isInstalling
    isInstalling=True
    c = aptFind()
    c.installIfNotInstalled('xterm')
    c.installIfNotInstalled('python3-pil')
    c.installIfNotInstalled('python3-pil.imagetk')
    c.installIfNotInstalled('python3-pip')
    c.installIfNotInstalled('mpg123')
    c.installIfNotInstalled('lolcat')
    pip_install('distro')
    isInstalling=False
def isConnected(url, timeout):
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

splash = Tk()
splash['background'] = '#333333'

app_width = 499
app_height = 299

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
splash.overrideredirect(True)



tab_tp1 = Image.open('icons/splash.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)

spl_png = Label(image=tp01).place(x=-1,y=-1)


list = ["Whoaa...\nSplash Screen....\nSoooo professionel","Sono pigro","Wer\nanderen eine Bratwurst brät,\n hat ein Bratwurstbratgerät.","I love Ubuntu... Server...","I DID NOTHING!\nTHE PAVEMENT\nWAS HIS ENEMY!","GO GO Power Rangers!","1 + 1 = 3", "It’s time to kick ass\nand chew bubble gum", "It’s a-me, Mario!", "Do a barrel roll!", "I need TP for my ...", "Splash screens suck!", "Snake? Snake? SNAKE!", "I like shorts! They’re comfy and easy to wear!", "Frostmourne hungers", "It's alive! It's alive!", "Hello, gorgeous", "I feel the need - the need for speed!", "They call it a Royale with cheese.", "Yo, Adrian!", "My precious.", "Go ahead, make my day.","My Little Pony is not for Children", "Mama says, 'Stupid is as stupid does."]
item = random.choice(list)
#print(item)
info_splash_txt = Label(text="Checked Dependencies - Lets GO!!!", bg="#333333",fg="white").pack(side=TOP)

dump_splash_txt = Label(text=item,font=("Arial", 16), bg="#333333",fg="white").pack(pady=20,side=BOTTOM)


def loop():
    while isInstalling == True:
        pass
    splash.destroy()

if isConnected('https://github.com', 5):
    t = threading.Thread(target=install_depends)
    splash.after(3000, loop)
    t.start()
else:
    print("\033[1;33mWARNING: not connected to the internet!\033[0m") #print in bold yellow
    splash.after(3000, splash.destroy)

mainloop()
