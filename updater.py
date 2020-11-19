#PiGro UpDater ############################################################
#Author: Timo Westphal ####################################################
#Date: NOV.2020 ###########################################################
#Version: 1.0 #############################################################
###########################################################################
##### Y U LOOK MY CODE? xD ################################################
###########################################################################

from tkinter import *
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

updater = Tk()
updater.title("PiGro UpDater")
icon = tk.PhotoImage(file="/home/pi/PiGro-Aid-/PiGroLogoslim.png")
updater.tk.call('wm', 'iconphoto', updater._w, icon)
updater.geometry("900x310")
updater['background']='grey39'
updater.resizable(0, 0)
#############################################
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






def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))

def button_action():
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/update.sh &' % wid)
    
def button_action2():
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/upgrade.sh &' % wid)

def button_action16():   
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/autoremove.sh &' % wid)

def button_action17():   
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &' % wid)
    
def save_list():
    os.system('sudo chmod 777 -R /etc/apt/sources.list')
    text_file=open("/etc/apt/sources.list",'w')
    text_file.write(s_list.get(1.0,END))
    m_text = "\
\n\
\n\
Sources List has been saved\n\
\n\
\n\
"
    messagebox.showinfo(message=m_text, title = "Infos")
        
#Notebook Style
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", background="grey39", borderwidth=0)
noteStyler.configure("TNotebook.Tab", background="grey39")
noteStyler.configure("TFrame", background="grey39")




#Notebook
tab_control = ttk.Notebook(updater,style='TNotebook')
tab1 = ttk.Frame(tab_control, style='TFrame')
tab_control.add(tab1, text='Update & Settings',)
tab_control.pack(expand=1, fill='both')



termf = Frame(tab1, height=20, width=20)
wid = termf.winfo_id()
os.system('xterm -into %d -geometry 120x20  &' % wid)
termf['background']='grey39'


i=Image.open('/home/pi/PiGro-Aid-/pigropi.png')
p=ImageTk.PhotoImage(i)
l=Label(tab1,image = p)
l['background']='grey39'
l.image = p



s_list = Text(tab1, width=90, height=10)
text_file=open("/etc/apt/sources.list",'r')
stuff=text_file.read() 
s_list.insert(END,stuff)
text_file.close()
s_list.pack(anchor='w')

update_button=Button(tab1,text="Update",width=15,anchor='w', command=button_action,background="grey39",foreground="white")
update_button.place(x=730, y=0,)

upgrade_button=Button(tab1,text="Upgrade",width=15,anchor='w', command=button_action2,background="grey39",foreground="white")
upgrade_button.place(x=730, y=30)

auth_button=Button(tab1,text="Allow Sources",width=15,anchor='w', command=button_action17,background="grey39",foreground="white")
auth_button.place(x=730, y=60)

rm_button=Button(tab1,text="Remove Config Files",width=15,anchor='w', command=button_action16,background="grey39",foreground="white")
rm_button.place(x=730, y=90)


sv_button=Button(tab1,text="Save Source List",width=15,anchor='w', command=save_list,background="grey39",foreground="white")
sv_button.place(x=730, y=145)

hiddn_button=Button(tab1,width=15,anchor='w',background="grey39",foreground="grey39", borderwidth=0, highlightbackground="grey39" )
hiddn_button.place(x=730, y=280)
hiddn_button_ttp = CreateToolTip(hiddn_button, \
   "oh my fucking god, you found the hidden button !!!! I don't give a fuck about spelling, okay? This tool was created in 6 weeks of corona quarantine and quite honestly I think it's really cool. if it wasn't open source, I'd be a fucking millionaire now .... fuuuuuuuuuuuuuuuuuuuu. love you for using my tool: - * C YA")



termf.pack(fill=BOTH, expand=NO)
l.pack()


updater.mainloop()