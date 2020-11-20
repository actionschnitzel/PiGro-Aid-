#PiGro ####################################################################
#Author: Timo Westphal ####################################################
#Date: NOV.2020 ###########################################################
#Version: 2.5 #############################################################
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
##########################################################################

###########################################################################
#DEFINITIONS
fenster = Tk()
fenster.title("PiGro - Just Click It")
icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
fenster.tk.call('wm', 'iconphoto', fenster._w, icon)
fenster.geometry("385x430")
fenster['background']='grey10'
fenster.resizable(0, 0)
################################################
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """
    def __init__(self, widget, text='widget info'):
        self.waittime = 500     #miliseconds
        self.wraplength = 180   #pixels
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
        label = tk.Label(self.tw, text=self.text, justify='left',
                       background="#ffffff", relief='solid', borderwidth=1,
                       wraplength = self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw= None
        if tw:
            tw.destroy()




################################################
def button_action20():
    entry_text = eingabefeld.get()
    if (entry_text == ""):
        welcome_label.config(text="Name of the App?")
    else:
        entry_text = "sudo apt-get install " + entry_text 
        
        f=open("/home/pi/PiGro-Aid-/buttoninst.sh","w+")
        for i in range(1):
             f.write(entry_text)
        popen("lxterminal -e 'bash -c \"sudo chmod +x /home/pi/PiGro-Aid-/buttoninst.sh && /home/pi/PiGro-Aid-/buttoninst.sh ; exec bash\"'")       
        
my_label = Label(fenster, text="sudo apt-get install:", fg="white")
my_label['background']='grey10'

welcome_label = Label(fenster)
eingabefeld = Entry(fenster, bd=5, width=31)
welcom_button = Button(fenster, text="Install", command=button_action20)
welcom_button_ttp = CreateToolTip(welcom_button, \
   'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.')


################################################
def callback(event):
       webbrowser.open_new(event.widget.cget("text"))
       
def callback2(event):
       lxterminal.open_new(event.widget.cget("entry_text"))

def button_action():
    popen("python3 /home/pi/PiGro-Aid-/updater.py")
    
    
def button_action1():
    popen("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")    
    
def button_action3():
    popen ("sudo lxappearance")
    
def button_action4():
    popen ("lxterminal -e 'bash -c \"sudo nano /etc/apt/sources.list; exec bash\"'")
    
def button_action5():   
    popen ("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'") 

def button_action6():   
    popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install compiz &' % wid)
    
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
    popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install arc-theme &' % wid)
    
def button_action13():   
    popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install breeze &' % wid)
    
def button_action14():   
    popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install gparted &' % wid)
    
def button_action15():   
    popen ("sudo gparted")

def button_action18():   
    popen ('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/xfce4fix.sh &' % wid)
    
def button_action19():   
    popen ("chromium-browser https://www.actionschnitzel.de/PiGro/")
    
    
    
def create_window():
    infofenster = tk.Toplevel(fenster)
    infofenster.title("Good Pi-Websites")    
    icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
    infofenster.tk.call('wm', 'iconphoto', infofenster._w, icon)
    infofenster.geometry("400x250")
    


    
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
    
    lbl2 = tk.Label(infofenster, text=r"https://www.lcdwiki.com/Main_Page", fg="blue", cursor="hand2")
    lbl2.pack()
    lbl2.bind("<Button-1>", callback)

####################################################
def action_get_info_dialog():
    m_text = "\
************************\n\
Author: Timo Westphal\n\
Date: Nov. 2020\n\
Version: 2.5\n\
************************"
    messagebox.showinfo(message=m_text, title = "Infos")
        

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
system_menu.add_command(label="Update & Settings", command=button_action)
system_menu.add_separator()
system_menu.add_command(label="Raspi-Config", command=button_action1)
system_menu.add_command(label="Nano Config.txt", command=button_action7)
system_menu.add_separator()
system_menu.add_command(label="Gparted", command=button_action15)
system_menu.add_command(label="NeoFetch", command=button_action8)
system_menu['background']='snow'
#
#
#
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

#
#

#Help ....I need somebody... HELP!
help_menu.add_command(label="Good Pi-Websites", command=create_window)
help_menu.add_command(label="Support / Me, tryna figure out wtf is wrong ;-)", command=button_action19)
help_menu.add_command(label="Info", command=action_get_info_dialog)
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
l_ttp = CreateToolTip(l, \
   "Don't forget to git pull PiGro from time to time to be up to date")

my_label.place(x=5, y=0)
eingabefeld.place(x=5, y=20)
welcom_button.place(x=310, y=20)
l.pack(anchor='w',pady=55)


###################################################################
def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))


termf = Frame(fenster, height=20, width=440)
termf.pack(fill=BOTH, expand=NO)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 100x100  &' % wid)



fenster.config(menu=menuleiste)



fenster.mainloop()
