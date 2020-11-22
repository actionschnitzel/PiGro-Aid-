from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import os
import sys
from tkinter import ttk
from os import popen
from os import system as cmd
import subprocess
from PIL import ImageTk, Image
from tkinter import messagebox
import webbrowser


##################################################MAIN
main = Tk()

main.title("PiGro Xtremo - TESTING v3.0")
icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)

#main['background']='grey20'
main.resizable(0, 0)

main.geometry("500x315")

###########################################TABCONT
tab_control = ttk.Notebook(main)



tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)

#Notebook Style
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", borderwidth=0)
#noteStyler.configure("TNotebook.Tab", background="grey20")
#noteStyler.configure("TFrame", background="grey20")

tab_control.add(tab1, text='Start')
tab_control.add(tab2, text='System')
tab_control.add(tab3, text='Installer')
tab_control.add(tab4, text='Appearance')
#tab_control.add(tab5, text='Tools')
tab_control.add(tab6, text='Help')

lbl1 = Label(tab3, text= '*to use snap install, you must\napt-get install snapd xD lol')
lbl1.grid(column=1, row=3)

lbl2 = Label(tab3, text= 'Suggestions', font=16, pady=20)
lbl2.grid(column=0, row=5)

################################################DEF/BUTTONZ


def upDater_button():
    popen("python3 /home/pi/PiGro-Aid-/updater.py")  
    
def pi_configbutton():
    popen("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")    
    
def lxap_button():
    popen ("sudo lxappearance")
    
def kiss_button():   
    popen ("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'") 

def compiz_button():   
    popen ("lxterminal -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")
    
def contxt_button():   
    popen ("lxterminal -e 'bash -c \"sudo nano /boot/config.txt; exec bash\"'")
    
def neofetch_button():   
    popen ("lxterminal -e 'bash -c \"neofetch; exec bash\"'")
    
def tasksel_button():   
    popen ("lxterminal -e 'bash -c \"sudo tasksel; exec bash\"'")

def arc_inst():   
    #popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install arc-theme &' % wid)
    popen ("lxterminal -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")
def breeze_inst():   
    popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install breeze &' % wid)
    
def gparted_inst():   
    #popen ('xterm -into %d -geometry 100x20 -e sudo apt-get install gparted &' % wid)
    popen ("lxterminal -e 'bash -c \"sudo apt-get install gparted; exec bash\"'")
def gparted_exec():   
    popen ("sudo gparted")

def xfcefix():   
    #popen ('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/xfce4fix.sh &' % wid)
    popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'")

def actionhome():   
    popen ("chromium-browser https://www.actionschnitzel.de/PiGro/")

def ch_desk():   
    popen ("lxterminal -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")
    
def w_app():
    popen ("lxterminal -e 'bash -c \"sudo snap install kesty-whatsapp; exec bash\"'")

#####################################TOOLTIPZ
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


######DEFZ####inst1###############################################################
def inst_btn1():
    entry_text = eingabefeld1.get()
    if (entry_text == ""):
        welcome_label.config(text="Name of the App?")
    else:
        entry_text = "sudo apt-get install " + entry_text 
        
        f=open("/home/pi/PiGro-Aid-/buttoninst.sh","w+")
        for i in range(1):
             f.write(entry_text)
        popen("lxterminal -e 'bash -c \"sudo chmod +x /home/pi/PiGro-Aid-/buttoninst.sh && /home/pi/PiGro-Aid-/buttoninst.sh ; exec bash\"'")       
                
        
my_label1 = Label(tab3, text="Apt-Get install", fg="white")
#my_label1['background']='grey20'

welcome_label1 = Label(tab3)
eingabefeld1 = Entry(tab3, bd=5, width=31, borderwidth=1 )
welcom_button1 = Button(tab3, text="install", command=inst_btn1)


######DEFZ####inst2##############################################################
def inst_btn2():
    entry_text = eingabefeld2.get()
    if (entry_text == ""):
        welcome_label2.config(text="Name of the App?")
    else:
        entry_text = "sudo snap install " + entry_text 
        
        f=open("/home/pi/PiGro-Aid-/buttoninst.sh","w+")
        for i in range(1):
             f.write(entry_text)
        popen("lxterminal -e 'bash -c \"sudo chmod +x /home/pi/PiGro-Aid-/buttoninst.sh && /home/pi/PiGro-Aid-/buttoninst.sh ; exec bash\"'")       
        
my_label2 = Label(tab3, text="Snap install", fg="white")
#my_label2['background']='grey20'

welcome_label2 = Label(tab3)
eingabefeld2 = Entry(tab3, bd=5, width=31, borderwidth=1)
welcom_button2 = Button(tab3, text="Install", command=inst_btn2,)


#################LOGO
i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(tab1,image = p)
l.image = p
#l['background']='grey20'
l.place(x=0, y=0)
###################################################Placement#inst1
my_label1.grid(column=0, row=0)
eingabefeld1.grid(column=1, row=0)
welcom_button1.grid(column=2, row=0)
###################################################Placement#inst2
my_label2.grid(column=0, row=1)
eingabefeld2.grid(column=1, row=1)
welcom_button2.grid(column=2, row=1)
########################################inst#btn#
in_btn0 = Button(tab3, text="Whatsapp",command=w_app)
in_btn0.grid(column=0, row=6)

in_btn1 = Button(tab3, text="Compiz", command=compiz_button)
in_btn1.grid(column=1, row=6)

in_btn2 = Button(tab3, text="PiKiss",command=kiss_button)
in_btn2.grid(column=2, row=6)
######DEFZ####tab1
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
        
my_label = Label(tab1, text="sudo apt-get install", fg="white")
my_label['background']='grey20'

#################LOGO
i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(tab1,image = p)
l.image = p

###########################################System

i1=Image.open('/home/pi/PiGro-Aid-/pigropi.png')
p1=ImageTk.PhotoImage(i1)
l1=Label(image = p1)

i2=Image.open('/home/pi/PiGro-Aid-/spacepi.png')
p2=ImageTk.PhotoImage(i2)
l2=Label(tab2, image = p2)
l2.place(x=200, y=100)

sys_btn0 = Button(tab2,image = p1,command=upDater_button)
sys_btn0.grid(column=1, row=0, pady= 20)

sys_btn1 = Button(tab2, text="Raspi-Config", width=10,command=pi_configbutton)
sys_btn1.grid(column=0, row=1,padx= 10)

sys_btn2 = Button(tab2, text="Nano Config.txt", width=10,command=contxt_button)
sys_btn2.grid(column=0, row=2,padx= 10,)

sys_btn3 = Button(tab2, text="Gparted", width=10,command=gparted_exec)
sys_btn3.grid(column=0, row=3,padx= 10)

sys_btn4 = Button(tab2, text="NeoFetch", width=10,command=neofetch_button)
sys_btn4.grid(column=0, row=4,padx= 10)

##########################################LOOK
in_btn0 = Button(tab4, text="LXAppearace",font=120,command=lxap_button)
in_btn0.grid(column=1, row=0, pady=10)

in_btn1 = Button(tab4, text="Tasksel", width=15,command=tasksel_button)
in_btn1.grid(column=0, row=1)

in_btn2 = Button(tab4, text="Change Desktop", width=15,command=ch_desk)
in_btn2.grid(column=1, row=1)

in_btn2 = Button(tab4, text="Xfce WiFi Fix", width=15,command=xfcefix)
in_btn2.grid(column=2, row=1)

in_btn2 = Button(tab4, text="Install Arc Theme", width=15,command=arc_inst)
in_btn2.grid(column=0, row=2)

in_btn2 = Button(tab4, text="Install Breeze Theme", width=15,command=breeze_inst)
in_btn2.grid(column=1, row=2)



######################################HELP
def callback(event):
       webbrowser.open_new(event.widget.cget("text"))
       
def callback2(event):
       lxterminal.open_new(event.widget.cget("entry_text"))

author = tk.Label(tab6,text="Author: Timo Westphal\nDate: Nov. 2020\nVersion: 3.X")
author.pack(pady=10)
al = tk.Label(tab6, text=r"https://www.actionschnitzel.de/PiGro/", fg="blue", cursor="hand2")
al.pack()
al.bind("<Button-1>", callback)


separator = Frame(tab6,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=5)

gws = Label(tab6, text="Good Websites")
gws.pack(pady=10)


lbl = tk.Label(tab6, text=r"https://www.raspberrypi.org", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
    
lbl0 = tk.Label(tab6, text=r"https://twisteros.com", fg="blue", cursor="hand2")
lbl0.pack()
lbl0.bind("<Button-1>", callback)
    
lbl1 = tk.Label(tab6, text=r"https://berryboot.alexgoldcheidt.com/images", fg="blue", cursor="hand2")
lbl1.pack()
lbl1.bind("<Button-1>", callback)
    
lbl2 = tk.Label(tab6, text=r"https://www.lcdwiki.com/Main_Page", fg="blue", cursor="hand2")
lbl2.pack()
lbl2.bind("<Button-1>", callback)




tab_control.pack(expand=1, fill='both')

main.mainloop()