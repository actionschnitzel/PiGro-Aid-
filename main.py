
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
#############################################################################
#MAIN
    
main = Tk()
main.title("PiGro+Aid+")
main.geometry("455x300")
main['background']='grey10'

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/emblem-debian.png") 
photoimage = photo.subsample(3,3) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/rpi-logo.png") 
photoimage2 = photo.subsample(2,2) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/879px-Bleachbit_logo.svg.png") 
photoimage3 = photo.subsample(30,25)

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/logo_pikiss_400.png") 
photoimage4 = photo.subsample(15,15) 

i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(main,image = p)
l.image = p
l.place(x = 200, y = 0,width=250, height=250)
l['background']='grey10'


button0 = Button(main,compound = LEFT, image = photoimage, text="Update your OS           ",foreground="white", command=button_action)
button0['background']='grey10'
button1 = Button(main, text="Raspi-Config                ",foreground="white", command=button_action1, image = photoimage2, compound = LEFT)
button1['background']='grey10'
button2 = Button(main, text ="Upgrade your OS         ", foreground="white", command=button_action2, image = photoimage, compound = LEFT)
button2['background']='grey10'
button3 = Button(main,text="Change PiXEL Theme  ",foreground="white", command=button_action3, image = photoimage2, compound = LEFT)
button3['background']='grey10'
button4 = Button(main,text="Edit Source                  ",foreground="white", command=button_action4, image = photoimage ,compound = LEFT)
button4['background']='grey10'
button5 = Button(main,text="Install Pikiss                 ",foreground="white", command=button_action5, image = photoimage4 ,compound = LEFT)
button5['background']='grey10'
button6 = Button(main,text="Install Compiz             ",foreground="white", command=button_action6, image = photoimage ,compound = LEFT)
button6['background']='grey10'
button7 = Button(main,text="Nano Config.txt           ",foreground="white", command=button_action7, image = photoimage2 ,compound = LEFT)
button7['background']='grey10'

#####
#newwin




####mainwin
button0.place(x = 0, y = 0, width=200, height=30)
button2.place(x = 0, y = 30, width=200, height=30)
button1.place(x = 0, y = 60, width=200, height=30)
button3.place(x = 0, y = 90, width=200, height=30)
button4.place(x = 0, y = 120, width=200, height=30)
button5.place(x = 0, y = 150, width=200, height=30)
button6.place(x = 0, y = 180, width=200, height=30)
button7.place(x = 0, y = 210, width=200, height=30)
###################################################################################################
main.mainloop()


