# from tkinter import *
# from PIL import ImageTk,Image

import os
import tkinter as tk
import webbrowser
from os import popen
from os import system as cmd
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import ImageTk, Image
import platform
import psutil
from collections import namedtuple
import resource
import threading
from datetime import datetime
import distro
#####################################

#####################################
def start1():
    page4text.pack_forget()
    page3text.pack_forget()
    page2text.pack_forget()
    
    page1text.pack()

def updater2():
    page4text.pack_forget()
    page3text.pack_forget()
    page1text.pack_forget()
    page2text.pack()

def system3():
    page4text.pack_forget()
    page1text.pack_forget()
    page2text.pack_forget()
    page3text.pack()
def installer4():
    page1text.pack_forget()
    page3text.pack_forget()
    page2text.pack_forget()
    page4text.pack()

def exit666():
    main.destroy()

main = Tk()
main.title("PiGro - Colpo Diretto")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#333333'
main.resizable(0, 0)


app_width = 959
app_height = 700

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main.wait_visibility(main)
main.wm_attributes('-alpha', 0.95, )
#####################################

#####################################
tab_tp1 = Image.open('icons/Logotab.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)

tab_tp12 = Image.open('icons/updatetab.png')
tp012 = ImageTk.PhotoImage(tab_tp12)
tl012 = Label(image=tp012)

tab_tp2 = Image.open('icons/system.png')
tp02 = ImageTk.PhotoImage(tab_tp2)
tl02 = Label(image=tp02)

tab_tp3 = Image.open('icons/installer_ico.png')
tp03 = ImageTk.PhotoImage(tab_tp3)
tl03 = Label(image=tp03)

tab_tp4 = Image.open('icons/look.png')
tp04 = ImageTk.PhotoImage(tab_tp4)
tl04 = Label(image=tp04)

tab_tp6 = Image.open('icons/tuning.png')
tp06 = ImageTk.PhotoImage(tab_tp6)
tl06 = Label(image=tp06)


sys_bp9 = Image.open('icons/links.png')
bp09 = ImageTk.PhotoImage(sys_bp9)
bl09 = Label(image=bp09)

sys_bp111 = Image.open('icons/dm.png')
bp0111 = ImageTk.PhotoImage(sys_bp111)
bl0111 = Label(image=bp0111)

tab_tp9 = Image.open('icons/holy_grail_ico.png')
tp09 = ImageTk.PhotoImage(tab_tp9)
tl09 = Label(image=tp09)

tab_tp10 = Image.open('icons/pigpi.png')
tp10 = ImageTk.PhotoImage(tab_tp10)
tl10 = Label(image=tp10)

tab_tpX = Image.open('icons/xfce.png')
tpX = ImageTk.PhotoImage(tab_tpX)
tlX = Label(image=tpX)

tab_tpinf = Image.open('icons/info_button.png')
tpinf = ImageTk.PhotoImage(tab_tpinf)
tlinf = Label(image=tpinf)







def toggle_win():
    f1=Frame(main,width=300,height=600,bg='#FFFFFF')
    f1.place(x=0,y=0)


    #buttons
    def bttn(x,y,text,bcolor,fcolor,cmd):
     
        def on_entera(e):
            myButton1['background'] = bcolor #ffcc66
            myButton1['foreground']= '#262626'  #000d33

        def on_leavea(e):
            myButton1['background'] = fcolor
            myButton1['foreground']= '#262626'

        myButton1 = Button(f1,text=text,
                       width=42,
                       height=2,
                       fg='#262626',
                       border=0,
                       bg=fcolor,
                       activeforeground='#262626',
                       activebackground=bcolor,            
                        command=cmd)
                      
        myButton1.bind("<Enter>", on_entera)
        myButton1.bind("<Leave>", on_leavea)

        myButton1.place(x=x,y=y)

    bttn(0,80,'Start','#E95420','#FFFFFF',start1)
    bttn(0,117,'Updater','#E95420','#FFFFFF',updater2)
    bttn(0,154,'System','#E95420','#FFFFFF',system3)
    bttn(0,191,'Installer','#E95420','#FFFFFF',installer4)
    bttn(0,228,'Look','#E95420','#FFFFFF',None)
    bttn(0,265,'Xfce','#E95420','#FFFFFF',None)
    bttn(0,302,'Tuning','#E95420','#FFFFFF',None)
    bttn(0,339,'Links','#E95420','#FFFFFF',None)
    bttn(0,376,'Holy Grail','#E95420','#FFFFFF',None)
    bttn(0,413,'Pig-Grow','#E95420','#FFFFFF',None)
    bttn(0,480,'Exit','#E95420','#FFFFFF',exit666)
    #
    def dele():
        f1.destroy()

    global img2
    img2 = ImageTk.PhotoImage(Image.open("close.png"))

    Button(f1,
           image=img2,
           border=0,
           command=dele,
           bg='#FFFFFF',
           activebackground='#FFFFFF').place(x=5,y=10)
 
 

i = Image.open('icons/pigro_bull.png')
p = ImageTk.PhotoImage(i)
l = Label(main, image=p)
l.image = p
l['background'] = '#383c4a'
l.place(x=-1, y=-1)



#l1=Label(main,text='Python',fg='white',bg='#262626')
#l1.config(font=('Comic Sans MS',90))
#l1.pack(expand=True)

img1 = ImageTk.PhotoImage(Image.open("open.png"))

Button(main,image=img1,
       command=toggle_win,
       border=0,
       highlightthickness=0,
       bg='#333333',
       activebackground='#262626').place(x=5,y=10)








page1text = Label(main,image=tp012, text="Start",font=("Helvetica",20), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w')

page2text = Label(main,image=tp012, text="Updater",font=("Helvetica",20), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w')

page3text = Label(main,image=tp02, text="System",font=("Helvetica",20), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w')

page4text = Label(main,image=tp03, text="Installer",font=("Helvetica",20), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w')





# page1btn.pack()
# page2btn.pack()
# page1text.pack()

main.mainloop()
