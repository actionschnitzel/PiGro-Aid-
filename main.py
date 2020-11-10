from tkinter import *
import os
import sys
from os import popen
import subprocess
from PIL import ImageTk, Image
from tkinter import messagebox
###########################################################################
#DEFINITIONS






def button_action():
    popen("lxterminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    
def button_action1():
    popen("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")    
    
def button_action2():
   popen ("lxterminal -e 'bash -c \"sudo apt-get update -y && sudo apt-get full-upgrade -y && sudo apt-get dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean; exec bash\"'")
    
def button_action3():
    popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/lxappearance.sh; exec bash\"'")
    
def button_action4():
    popen ("lxterminal -e 'bash -c \"sudo nano /etc/apt/sources.list; exec bash\"'")
    
def button_action5():   
    popen ("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'")

def button_action6():   
    popen ("lxterminal -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")
    
def button_action7():   
    popen ("lxterminal -e 'bash -c \"sudo nano /boot/config.txt; exec bash\"'")
    
def button_action8():   
    popen ("lxterminal -e 'bash -c \"neofetch; exec bash\"'")
    
def button_action9():   
    popen ("lxterminal -e 'bash -c \"sudo tasksel; exec bash\"'")

def button_action10():   
    popen ("lxterminal -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")
    
def button_action11():   
    popen ("lxterminal -e 'bash -c \"raspistill -o image.jpg; exec bash\"'")
        
def action_get_info_dialog():
    m_text = "\
************************\n\
Autor: Timo Westphal\n\
Date: 11.11.2020\n\
Version: 2.0\n\
************************"
    messagebox.showinfo(message=m_text, title = "Infos")
        

        
        
fenster = Tk()
fenster.title("PiGro - Don't Cry Little Pi")
fenster.geometry("400x250")
fenster['background']='grey10'



# Menüleiste 
menuleiste = Menu(fenster)
menuleiste['background']='snow'
# Menüeinträge
system_menu = Menu(menuleiste, tearoff=0)
appearance_menu = Menu(menuleiste, tearoff=0)
tools_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# System
# 
system_menu.add_command(label="Update", command=button_action)
system_menu.add_command(label="Upgrade", command=button_action2)
system_menu.add_separator() 
system_menu.add_command(label="Raspi-Config", command=button_action1)
system_menu.add_command(label="Edit Source List", command=button_action4)
system_menu.add_command(label="Nano Config.txt", command=button_action7)
system_menu['background']='snow'
#system_menu.add_command(label="Exit", command=fenster.quit)
#
#Appear
appearance_menu.add_command(label="LXAppearance", command=button_action3)
appearance_menu.add_command(label="Compiz", command=button_action6)
appearance_menu.add_separator() 
appearance_menu.add_command(label="Tasksel", command=button_action9)
appearance_menu.add_command(label="Change Desktop Env.", command=button_action10)
appearance_menu['background']='snow'
#
#
#Tools
tools_menu.add_command(label="Install/Start PiKiss", command=button_action5)
tools_menu.add_command(label="NeoFetch", command=button_action8)
tools_menu.add_separator() 
tools_menu.add_command(label="Take A Photo", command=button_action11)
tools_menu['background']='snow'
#
#
#Help ....I need somebody... HELP!
help_menu.add_command(label="Info!", command=action_get_info_dialog)
help_menu['background']='snow'
# 
# "Drop-Down-Menü"
menuleiste.add_cascade(label="System", menu=system_menu)
menuleiste.add_cascade(label="Appearance", menu=appearance_menu)
menuleiste.add_cascade(label="Tools", menu=tools_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(fenster,image = p)
l.image = p
l['background']='grey10'
l.grid(row=0, column=1)

# 
fenster.config(menu=menuleiste)          

fenster.mainloop()
