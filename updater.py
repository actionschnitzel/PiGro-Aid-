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

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))

def button_action():
    #popen("lxterminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/update.sh &' % wid)
    
def button_action2():
    #popen ("lxterminal -e 'bash -c \"sudo apt-get update -y && sudo apt-get full-upgrade -y && sudo apt-get dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/upgrade.sh &' % wid)

def button_action16():   
    #popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/autoremove.sh; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/autoremove.sh &' % wid)

def button_action17():   
    #popen ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/addunsignedrepo.sh; exec bash\"'")
    os.system('xterm -into %d -geometry 100x20 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &' % wid)
    
def save_list():
    #os.system('xterm -into %d -geometry 100x20 -e chmod +rwx /etc/apt/sources.list &' % wid)
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
#tab2 = ttk.Frame(tab_control, style='TFrame')
#lbl2 = Label(tab2, text= "This updater is inspired by the Ub**tu software updater. No ads here. xDDD")
#lbl2.grid(column=0, row=0)
tab_control.add(tab1, text='Update & Settings',)


#tab_control.add(tab2, text='Info')



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

termf.pack(fill=BOTH, expand=NO)
l.pack()


updater.mainloop()