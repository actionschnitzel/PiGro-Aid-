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
    os.system ("lxterminal -e 'bash -c \"neofetch; exec bash\"'")
#############################################################################
#MAIN
    
main = Tk()
main.title("PiGro+Aid+")
main.geometry("455x550")
main['background']='grey10'

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/emblem-debian.png") 
photoimage = photo.subsample(2,2) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/rpi-logo.png") 
photoimage2 = photo.subsample(2,2) 

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/879px-Bleachbit_logo.svg.png") 
photoimage3 = photo.subsample(30,25)

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/logo_pikiss_400.png") 
photoimage4 = photo.subsample(13,13)

photo = PhotoImage(file = r"/home/pi/PiGro-Aid-/icons/tux.png") 
photoimage5 = photo.subsample(15,15) 

i=Image.open('/home/pi/PiGro-Aid-/raspi-aid.png')
p=ImageTk.PhotoImage(i)
l=Label(main,image = p)
l.image = p
l.place(x = 200, y = 0,width=250, height=250)
l['background']='grey10'

w = Label(main, text="Don't Cry Little Pi")
w.place(x = 260, y = 250)
w['background']='grey10'
w['foreground']='white'



button0 = Button(main, anchor="w", image = photoimage, text="Update",foreground="white", command=button_action, compound = LEFT)
button0['background']='grey10'
button1 = Button(main, anchor="w",compound = LEFT, image = photoimage, text="Raspi-Config",foreground="white", command=button_action1)
button1['background']='grey10'
button2 = Button(main, anchor="w",compound = LEFT, image = photoimage, text ="Upgrade", foreground="white", command=button_action2)
button2['background']='grey10'
button3 = Button(main, anchor="w",compound = LEFT, image = photoimage, text="Change PiXEL Theme",foreground="white", command=button_action3)
button3['background']='grey10'
button4 = Button(main, anchor="w",compound = LEFT,text="Edit Source",foreground="white", command=button_action4, image = photoimage)
button4['background']='grey10'
button5 = Button(main, anchor="w",compound = LEFT,text="Install Pikiss",foreground="white", command=button_action5, image = photoimage4)
button5['background']='grey10'
button6 = Button(main, anchor="w",compound = LEFT,text="Install Compiz",foreground="white", command=button_action6, image = photoimage)
button6['background']='grey10'
button7 = Button(main, anchor="w",compound = LEFT,text="Nano Config.txt",foreground="white", command=button_action7, image = photoimage)
button7['background']='grey10'
button8 = Button(main, anchor="w",compound = LEFT,text="Neofetch",foreground="white", command=button_action8, image = photoimage5)
button8['background']='grey10'
button9 = Button(main, anchor="w",compound = LEFT,text="Tasksel",foreground="white", command=button_action9, image = photoimage)
button9['background']='grey10'
button10 = Button(main, anchor="w",compound = LEFT,text="Nothing Jet",foreground="white", command=button_action10, image = photoimage)
button10['background']='grey10'
#####
#newwin




####mainwin
button0.place(x = 0, y = 0, width=200, height=50)
button2.place(x = 0, y = 50, width=200, height=50)
button1.place(x = 0, y = 100, width=200, height=50)
button3.place(x = 0, y = 150, width=200, height=50)
button4.place(x = 0, y = 200, width=200, height=50)
button5.place(x = 0, y = 250, width=200, height=50)
button6.place(x = 0, y = 300, width=200, height=50)
button7.place(x = 0, y = 350, width=200, height=50)
button8.place(x = 0, y = 400, width=200, height=50)
button9.place(x = 0, y = 450, width=200, height=50)
button10.place(x = 0, y = 500, width=200, height=50)

###################################################################################################
main.mainloop()
