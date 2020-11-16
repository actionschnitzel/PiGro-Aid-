#Author: Timo Westphal#######################################################
#Date: 11.11.2020###########################################################
#Version: 2.0###############################################################
###########################################################################
##### Y U LOOK MY CODE? xD ################################################
###########################################################################
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import os
import sys
from os import popen
from os import system as cmd
import subprocess
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser
#######################

###########################################################################
#DEFINITIONS
fenster = Tk()
fenster.title("PiGro - Just Click It")
icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
fenster.tk.call('wm', 'iconphoto', fenster._w, icon)
fenster.geometry("440x450")
fenster['background']='grey10'
##################################################




################################################
def button_action20():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Name of the App?")
    else:
        entry_text = "sudo apt-get install " + entry_text 
        #welcome_label.config(text=entry_text)
        #welcome_label.config(command=callback2)
        
        #print(entry_text)
        #entry_text = popen("lxterminal") + entry_text
        #button_action20(command=callback2)
        f=open("/home/pi/PiGro-Aid-/buttoninst.sh","w+")
        for i in range(1):
             f.write(entry_text)
        popen("lxterminal -e 'bash -c \"sudo chmod +x /home/pi/PiGro-Aid-/buttoninst.sh && /home/pi/PiGro-Aid-/buttoninst.sh ; exec bash\"'")
        #popen("lxterminal -e 'bash -c \"sudo rm /home/pi/PiGro-Aid-/buttoninst.sh && exit ; exec bash\"'")
        
        
        
my_label = Label(fenster, text="sudo apt-get install(>NAME<)", fg="white")
my_label['background']='grey10'

welcome_label = Label(fenster)

eingabefeld = Entry(fenster, bd=5, width=40)

welcom_button = Button(fenster, text="Install", command=button_action20)

exit_button = Button(fenster, text="Beenden", command=fenster.quit)

################################################
def callback(event):
       webbrowser.open_new(event.widget.cget("text"))
       
def callback2(event):
       lxterminal.open_new(event.widget.cget("entry_text"))

def button_action():
    #popen("lxterminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/update.sh &' % wid)
    
    
def button_action1():
    popen("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")    
    
def button_action2():
    #popen ("lxterminal -e 'bash -c \"sudo apt-get update -y && sudo apt-get full-upgrade -y && sudo apt-get dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/upgrade.sh &' % wid)
    
def button_action3():
    popen ("sudo lxappearance")
    
def button_action4():
    popen ("lxterminal -e 'bash -c \"sudo nano /etc/apt/sources.list; exec bash\"'")
    
def button_action5():   
    popen ("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'") 

def button_action6():   
    #popen ("lxterminal -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e sudo apt-get install compiz &' % wid)
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

def button_action12():   
    #popen ("lxterminal -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e sudo apt-get install arc-theme &' % wid)
def button_action13():   
    #popen ("lxterminal -e 'bash -c \"sudo apt-get install breeze; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e sudo apt-get install breeze &' % wid)
def button_action14():   
    #popen ("lxterminal -e 'bash -c \"sudo apt-get install gparted; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e sudo apt-get install gparted &' % wid)
def button_action15():   
    popen ("sudo gparted")

def button_action16():   
    #popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/autoremove.sh; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/autoremove.sh &' % wid)
def button_action17():   
    #popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/addunsignedrepo.sh; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &' % wid)
def button_action18():   
    #popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/xfce4fix.sh ; exec bash\"'")    
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/xfce4fix.sh &' % wid)
def button_action19():   
    popen ("chromium-browser https://www.actionschnitzel.de/PiGro/PiGro-HowTo-s/")    
#CSB#

 
def create_window1():
    infofenster1 = tk.Toplevel(fenster)
    infofenster1.title("CSB Freakin' Alpha")    
    icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
    infofenster1.tk.call('wm', 'iconphoto', infofenster1._w, icon)
    infofenster1.geometry("600x500")
    
    def open_txt():
        text_file = filedialog.askopenfilename()
        text_file = open(text_file,'r')
        stuff = text_file.read()
        my_text.insert(END, stuff)
        text_file.close()
        
    def save_txt():
        text_file = filedialog.askopenfilename()
        text_file = open(text_file,'w')
        text_file.write(my_text.get(1.0, END))
        
    my_text = Text(infofenster1, width=390, heigh=20)
    my_text.pack()
    
    open_button = Button(infofenster1, text="Open File", command=open_txt)
    open_button.pack(padx=5, pady=0, side=LEFT)
    
    save_button = Button(infofenster1, text="Save File", command=save_txt) 
    save_button.pack(padx=5, pady=0, side=LEFT)
    
    
    termf = Frame(infofenster1)
    termf.pack(fill=BOTH, expand=YES) 
    wid = termf.winfo_id()
    os.system('xterm -into %d -geometry 390x80  &' % wid)
    infofenster1['background']='grey10'

    
def create_window():
    infofenster = tk.Toplevel(fenster)
    infofenster.title("Good Pi-Websites")    
    icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
    infofenster.tk.call('wm', 'iconphoto', infofenster._w, icon)
    infofenster.geometry("400x250")
    
##############################################

    
####################################################################
    lbl = tk.Label(infofenster, text=r"https://www.raspberrypi.org", fg="blue", cursor="hand2")
    lbl.pack()
    lbl.bind("<Button-1>", callback)
    
    lbl0 = tk.Label(infofenster, text=r"https://twisteros.com", fg="blue", cursor="hand2")
    lbl0.pack()
    lbl0.bind("<Button-1>", callback)
    
    lbl1 = tk.Label(infofenster, text=r"https://berryboot.alexgoldcheidt.com/images", fg="blue", cursor="hand2")
    lbl1.pack()
    lbl1.bind("<Button-1>", callback)
    
    lbl2 = tk.Label(infofenster, text=r"https://http://www.lcdwiki.com/Main_Page", fg="blue", cursor="hand2")
    lbl2.pack()
    lbl2.bind("<Button-1>", callback)


def action_get_info_dialog():
    m_text = "\
************************\n\
Author: Timo Westphal\n\
Date: Nov. 2020\n\
Version: 2.1\n\
************************"
    messagebox.showinfo(message=m_text, title = "Infos")
        

        
        




# Menüleiste 
menuleiste = Menu(fenster)
menuleiste['background']='snow'
# Menüeinträge
system_menu = Menu(menuleiste, tearoff=0)
appearance_menu = Menu(menuleiste, tearoff=0)
tools_menu = Menu(menuleiste, tearoff=0)
cheat_menu = Menu(menuleiste, tearoff=0)
help_menu = Menu(menuleiste, tearoff=0)

# System
# 
system_menu.add_command(label="Update", command=button_action)
system_menu.add_command(label="Upgrade", command=button_action2)
system_menu.add_separator()
system_menu.add_command(label="Remove Residual Configuration Files", command=button_action16)
system_menu.add_separator()
system_menu.add_command(label="Raspi-Config", command=button_action1)
system_menu.add_command(label="Edit Source List", command=button_action4)
system_menu.add_command(label="Allow All Unauthed Source", command=button_action17)
system_menu.add_command(label="Nano Config.txt", command=button_action7)
system_menu.add_separator()
system_menu.add_command(label="Gparted", command=button_action15)
system_menu.add_command(label="NeoFetch", command=button_action8)
system_menu['background']='snow'
#system_menu.add_command(label="Exit", command=fenster.quit)
#
#Appear
appearance_menu.add_command(label="LXAppearance", command=button_action3)
appearance_menu.add_command(label="Compiz", command=button_action6)
appearance_menu.add_separator() 
appearance_menu.add_command(label="Tasksel", command=button_action9)
appearance_menu.add_command(label="Change Desktop Env.", command=button_action10)
appearance_menu.add_command(label="Xfce-Wifi-Fix(rpiOS)", command=button_action18)
appearance_menu.add_separator() 
appearance_menu.add_command(label="Arc-Theme", command=button_action12)
appearance_menu.add_command(label="Breeze-Theme", command=button_action13)
appearance_menu['background']='snow'
#
#
#Tools
tools_menu.add_command(label="Install PiKiss", command=button_action5)
tools_menu.add_command(label="Install Gparted", command=button_action14)
tools_menu.add_separator() 
tools_menu.add_command(label="Take A Photo", command=button_action11)
tools_menu['background']='snow'
#
#
cheat_menu.add_command(label="Let's be super lazy ", command=create_window1)
#
#

#Help ....I need somebody... HELP!
help_menu.add_command(label="Good Pi-Websites", command=create_window)
help_menu.add_command(label="HowTo's", command=button_action19)
help_menu.add_command(label="Info", command=action_get_info_dialog)
help_menu['background']='snow'
# 
# "Drop-Down-Menü"
menuleiste.add_cascade(label="System", menu=system_menu)
menuleiste.add_cascade(label="Appearance", menu=appearance_menu)
menuleiste.add_cascade(label="Tools", menu=tools_menu)
menuleiste.add_cascade(label="CSB(ALPHA)",foreground="red", menu=cheat_menu)
menuleiste.add_cascade(label="Help", menu=help_menu)

i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(fenster,image = p)
l.image = p
l['background']='grey10'







#(row=4, column=0)

my_label.pack()
#grid(row = 0, column = 0)
eingabefeld.pack()
#(row = 1, column = 0)
welcom_button.pack()
#(row = 2, column = 0)
l.pack()  
#
def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))


termf = Frame(fenster, height=20, width=440)
termf.pack(fill=BOTH, expand=YES)
wid = termf.winfo_id()
#termf2=Frame(fenster)
#termf2.pack(fill=BOTH, expand=YES) 
#wid=termf2.winfo_id()
os.system('xterm -into %d -geometry 100x20  &' % wid)




fenster.config(menu=menuleiste)

fenster.mainloop()


