from tkinter import *
import time
import random
from PIL import ImageTk, Image
import os
from os import popen
from os import system as cmd


splash = Tk()
splash['background'] = '#333333'

app_width = 499
app_height = 299

screen_width = splash.winfo_screenwidth()
screen_height = splash.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

splash.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
splash.overrideredirect(True)

popen("pip3 install distro && exit"

tab_tp1 = Image.open('icons/splash.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)

spl_png = Label(image=tp01).place(x=-1,y=-1)


list = ["Whoaa...\nSplash Screen....\nSoooo professionel","Sono pigro","Wer\nanderen eine Bratwurst brät,\n hat ein Bratwurstbratgerät.","I love Ubuntu... Server...","I DID NOTHING!\nTHE PAVEMENT\nWAS HIS ENEMY!","GO GO Power Rangers!","1 + 1 = 3", "It’s time to kick ass\nand chew bubble gum", "It’s a-me, Mario!", "Do a barrel roll!", "I need TP for my ...", "Splash screens suck!", "Snake? Snake? SNAKE!", "I like shorts! They’re comfy and easy to wear!", "Frostmourne hungers", "It's alive! It's alive!", "Hello, gorgeous", "I feel the need - the need for speed!", "They call it a Royale with cheese.", "Yo, Adrian!", "My precious.", "Go ahead, make my day.","My Little Pony is not for Children", "Mama says, 'Stupid is as stupid does."]
item = random.choice(list)
#print(item)
info_splash_txt = Label(text="Checking dependencies", bg="#333333",fg="white").pack(side=TOP)

dump_splash_txt = Label(text=item,font=("Arial", 16), bg="#333333",fg="white").pack(pady=20,side=BOTTOM)

#popen("sudo apt-get install xterm -y")
#popen("sudo apt-get install python3-pil python3-pil.imagetk -y")
#popen("sudo apt install python3-pip -y")
#popen("pip3 install playsound")


splash.after(3000, splash.destroy)

mainloop()
