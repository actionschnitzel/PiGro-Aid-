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
    os.system("lxterminal -e 'bash -c \"sudo apt-get update; exec bash\"'")
   
    
def button_action1():
    os.system("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")    
    
def button_action2():
   os.system ("lxterminal -e 'bash -c \"sudo apt-get update -y && sudo apt-get full-upgrade -y && sudo apt-get dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean; exec bash\"'")
    
def button_action3():
    os.system ("lxterminal -e 'bash -c \"~/PiGro-Aid-/scripts/lxappearance.sh; exec bash\"'")
    
def button_action4():
    os.system ("lxterminal -e 'bash -c \"sudo nano /etc/apt/sources.list; exec bash\"'")
    
def button_action5():   
    os.system ("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'")

def button_action6():   
    os.system ("lxterminal -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")
    
def button_action7():   
    os.system ("lxterminal -e 'bash -c \"sudo nano /boot/config.txt; exec bash\"'")
    
def button_action8():   
    os.system ("lxterminal -e 'bash -c \"neofetch; exec bash\"'")
    
def button_action9():   
    os.system ("lxterminal -e 'bash -c \"sudo tasksel; exec bash\"'")

def button_action10():   
    os.system ("lxterminal -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")
    
def button_action11():   
    os.system ("lxterminal -e 'bash -c \"raspistill -o image.jpg; exec bash\"'")
    
#############################################################################
#MAIN
    
main = Tk()
main.title("PiGro+Aid+")
main.geometry("620x510")
main['background']='grey10'
##############################################################################
photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/emblem-debian.png") 
photoimage = photo.subsample(2,2) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/picam.png") 
photoimage2 = photo.subsample(5,4) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/879px-Bleachbit_logo.svg.png") 
photoimage3 = photo.subsample(30,25)

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/logo_pikiss_400.png") 
photoimage4 = photo.subsample(12,12)

photo = PhotoImage(file = r"/home/pi/DEV/PiGro-Aid-/icons/neofetch.png") 
photoimage5 = photo.subsample(7,5) 

i=Image.open('/home/pi/DEV/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(main,image = p)
l.image = p
l.place(x=100, y=260)
l['background']='grey10'
#########################################################################
sys_label = Label(main, text="System", fg="white")
sys_label.configure(font=("Impact", 16,"italic"))
sys_label['background']='grey10'

#######
look_label = Label(main, text="Appearance", fg="white")
look_label.configure(font=("Impact", 16,"italic"))
look_label['background']='grey10'
#######
tool_label = Label(main, text="Tools", fg="white")
tool_label.configure(font=("Impact", 16,"italic"))
tool_label['background']='grey10'


########################################################################
button0 = Button(main, anchor="w", image = photoimage, text="Update",foreground="white", command=button_action, compound = LEFT,width=170)
button0['background']='grey10'
button1 = Button(main, anchor="w",compound = LEFT, image = photoimage, text="Raspi-Config",foreground="white", command=button_action1,width=170)
button1['background']='grey10'
button2 = Button(main, anchor="w",compound = LEFT, image = photoimage, text ="Upgrade", foreground="white", command=button_action2,width=170)
button2['background']='grey10'
button3 = Button(main, anchor="w",compound = LEFT, image = photoimage, text="Change PiXEL Theme",foreground="white", command=button_action3,width=170)
button3['background']='grey10'
button4 = Button(main, anchor="w",compound = LEFT,text="Edit Source",foreground="white", command=button_action4, image = photoimage,width=170)
button4['background']='grey10'
button5 = Button(main, anchor="w",compound = LEFT,text="Install Pikiss",foreground="white", command=button_action5, image = photoimage4,width=170)
button5['background']='grey10'
button6 = Button(main, anchor="w",compound = LEFT,text="Install Compiz",foreground="white", command=button_action6, image = photoimage,width=170)
button6['background']='grey10'
button7 = Button(main, anchor="w",compound = LEFT,text="Nano Config.txt",foreground="white", command=button_action7, image = photoimage,width=170)
button7['background']='grey10'
button8 = Button(main, anchor="w",compound = LEFT,text="Neofetch",foreground="white", command=button_action8, image = photoimage,width=170)
button8['background']='grey10'
button9 = Button(main, anchor="w",compound = LEFT,text="Tasksel",foreground="white", command=button_action9, image = photoimage,width=170)
button9['background']='grey10'
button10 = Button(main, anchor="w",compound = LEFT,text="Change Desktop \nEnvironment",foreground="white", command=button_action10, image = photoimage,width=170)
button10['background']='grey10'
button11 = Button(main, anchor="w",compound = LEFT,text="Take A Photo",foreground="white", command=button_action10, image = photoimage2,width=170)
button11['background']='grey10'
#####
#newwin




####mainwin
sys_label.grid(row=0, column=1)
look_label.grid(row=0, column=2)
tool_label.grid(row=0, column=3)
button0.grid(padx=5, row=1, column=1)
button2.grid(row=2, column=1)
button1.grid(row=3, column=1)
button3.grid(row=1, column=2)
button4.grid(row=4, column=1)
button5.grid(padx=5,row=1, column=3)
button6.grid(row=2, column=2)
button7.grid(row=6, column=1)
button8.grid(row=2, column=3)
button9.grid(row=4, column=2)
button10.grid( row=3, column=2)
button11.grid(row=3, column=3)

###################################################################################################
main.mainloop()


