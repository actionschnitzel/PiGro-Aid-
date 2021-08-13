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
from playsound import playsound
import distro


##################################################MAIN

popen('find /home/pi/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;')

###################################Main_Settings

main = Tk()
main.title("PiGro Xtrmo - Just Click It!")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#333333'
main.resizable(0, 0)


app_width = 850
app_height = 545

screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)

main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

main.wait_visibility(main)
main.wm_attributes('-alpha', 0.95, )


###########################################TABCONT




#Notebook Style
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", borderwidth=0, background="#333333", tabposition='wn',highlightthickness=0)
noteStyler.configure("TNotebook.Tab", borderwidth=0, background="#333333", foreground="white",font=("Helvetica",16),width=10,highlightthickness=0)
noteStyler.configure("TFrame", background="#333333")


noteStyler.map("TNotebook.Tab", background=[("selected", "#333333")], foreground=[("selected", "#d4244d")]);
#noteStyler.configure("TNotebook.Tab", background="#383c4a", foreground="white");

tab_control = ttk.Notebook(main)

tab1 = ttk.Frame(tab_control)
tab11 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)
tab4 = ttk.Frame(tab_control)
tab5 = ttk.Frame(tab_control)
tab6 = ttk.Frame(tab_control)
tab7 = ttk.Frame(tab_control)
tab8 = ttk.Frame(tab_control)
tab9 = ttk.Frame(tab_control)
tab10 = ttk.Frame(tab_control)

########################
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



########################################
tab_control.add(tab1, compound=LEFT, text='Start', image=tp01)
tab_control.add(tab11, compound=LEFT, text='Updater', image=tp012)
tab_control.add(tab2, compound=LEFT, text='System', image=tp02)
tab_control.add(tab3, compound=LEFT, text='Installer', image=tp03)
tab_control.add(tab4, compound=LEFT, text='Look', image=tp04)
tab_control.add(tab6, compound=LEFT, text='Tuning', image=tp06)
tab_control.add(tab8, compound=LEFT, text='Links', image=bp0111)
tab_control.add(tab9, compound=LEFT, text='Holy Grail', image=tp09)
tab_control.add(tab10, compound=LEFT, text='Pig-Grow', image=tp10)



################################################DEF/BUTTONZ

def changelog():
    global pop_changelog
    pop_changelog=Toplevel()
    pop_changelog.geometry("650x600")
    text = Text(pop_changelog)
    text.insert(INSERT, """
####AugustFix#################################################################
##############################################################################

The vacation is over and I finally have my Pi in front of me again.
Programming on a laptop while sunbathing is something nice xD

Changes:

- Splaaaash Screeeen :-)
- new unique icons (I am now a GIMP PRO xD)
- Uniform fonts (Helvetica)
- XFCE settings are marked with a symbol
- "Distro display" at System Info
- New Stuff in the Shop (Icon is ugly .. I'll patch it soon ;-)
    - Vulkan 32/64 installer
    - Tetris CLI
- Overlocking to 2200 Ghz
- More usefull links
- * NEW * Pig-Grow Tab


Cheers

Timo
##############################################################################
##############################################################################
""")
    text.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )
################################
def readf():
    global pop_readf
    pop_readf=Toplevel()
    pop_readf.geometry("650x600")
    text = Text(pop_readf)
    text.insert(INSERT, """
##############################################################################
##############################################################################
PiGro is getting more and more complex. In general,
PiGro should work with all Debian derivatives.
Nevertheless, despite Debian as the basis, there are many differences.

For Raspberry Pi OS users this means:

- Only nano config.txt instead of mousepad config.txt

- Notification Sounds are not working

If you installed PiGro via pi-apps (On RaspiOS) please run:

sudo apt-get install xterm -y
sudo apt-get install python3-pil python3-pil.imagetk -y
sudo apt install python3-pip -y
pip3 install playsound

that should fix most of the bugs ;-)

If you use Twister you shouldn't have any problem :-P

I'll do a pull request to pi-apps soon to fix all.

Cheers

Timo
##############################################################################
##############################################################################
""")
    text.pack(anchor=N, fill=BOTH, expand=True, side=LEFT )


#################################

def upDater_button():
    popen("python3 updater.py")

def pi_configbutton():
    popen("xterm -e 'bash -c \"sudo raspi-config; exec bash\"'")

def pi_configbutton2():
    popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")

def pi_appear():
    popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")
    
def opbox_button():
    popen("sudo obconf")    

def lxap_button():
    popen("sudo lxappearance")

def xfceappear_button():
    popen("xfce4-appearance-settings")
    
def kiss_button():
    popen("xterm -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'")

def compiz_button():
    popen("xterm -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")

def contxt_button():
    popen("sudo xdg-open /boot/config.txt")

def neofetch_button():
    popen("xterm -e 'bash -c \"neofetch; exec bash\"'")

def tasksel_button():
    popen("xterm -e 'bash -c \"sudo tasksel; exec bash\"'")

def arc_inst():
    popen("xterm -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")

def breeze_inst():
    popen("xterm -e 'bash -c \"sudo apt-get install breeze-cursor-theme; exec bash\"'")

def papi_inst():
    popen("xterm -e 'bash -c \"sudo apt-get install papirus-icon-theme; exec bash\"'")

def gparted_inst():
    popen("xterm -e 'bash -c \"sudo apt-get install gparted; exec bash\"'")

def gparted_exec():
    popen("sudo gparted")

def xfcefix():
    popen("xterm -e 'bash -c \"sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'")

def xfcefix2():
    popen("xterm -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'")

def actionhome():
    popen("xdg-open https://www.actionschnitzel.de/PiGro/")
    
def xfcelook_f():
    popen("xdg-open https://www.xfce-look.org/browse/cat/")

def web_OVC():
    popen("xdg-open https://www.gnome-look.org/p/1158321/")

def ch_desk():
    popen("xterm -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")

def w_app():
    popen("xterm -e 'bash -c \"sudo snap install kesty-whatsapp; exec bash\"'")

def onc_ben():
    popen("sudo xdg-open ~")

def inst_bleach():
    popen("xterm -e 'bash -c \"sudo apt-get install bleachbit ; exec bash\"'")

def button_lk():
    popen("xterm -e 'bash -c \"sudo BRANCH=next rpi-update; exec bash\"'")

def inst_ima():
    popen("xterm -e 'bash -c \"sudo apt install rpi-imager; exec bash\"'")

def inst_neo():
    popen("xterm -e 'bash -c \"sudo apt-get install neofetch; exec bash\"'")

def button_dpfc():
    popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

def button_xf4s():
    popen("xfwm4-settings")

def button_xfwm():
    popen("xterm -e 'bash -c \"sudo update-alternatives --config x-window-manager; exec bash\"'")

def button_boot():
    popen("xterm -e 'bash -c \"dmesg; exec bash\"'")

def btswitch_64():
    popen("xterm -e 'bash -c \"sudo apt-get install -y raspbian-nspawn-64; exec bash\"'")
    
def z_ram():
    popen("xterm -e 'bash -c \"sudo apt-get install zram-tools; exec bash\"'")
    
def rm_vsc():
    popen("xterm -e 'bash -c \"sudo rm /etc/apt/sources.list.d/vscode.list & echo DONE!; exec bash\"'")

def reboot_n():
    popen("sudo reboot")
    
def theme_f():
    popen("sudo xdg-open /usr/share/themes/")
    
def icon_f():
    popen("sudo xdg-open /usr/share/icons/")
    
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def gnome_pie():
    popen("xterm -e 'bash -c \"sudo apt-get install gnome-pie; exec bash\"'")
    
def pi_apps():
    popen("xterm -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'")
    
def inst_lutis():
    popen("sudo chmod +x /home/pi/PiGro-Aid-/scripts/lutris.sh")
    popen("xterm -e 'bash -c \"sudo /home/pi/PiGro-Aid-/scripts/lutris.sh; exec bash\"'")
    
def vulk_32():
    popen("xterm -e 'bash -c \"sudo /home/pi/PiGro-Aid-/scripts/vulkan_32.sh; exec bash\"'")
    
def vulk_64():
    popen("xterm -e 'bash -c \"sudo /home/pi/PiGro-Aid-/scripts/vulkan_64.sh; exec bash\"'")
    
def tetris_cli():
    popen("xterm -e 'bash -c \"sudo /home/pi/PiGro-Aid-/scripts/tetris_cli.sh; exec bash\"'")
#####################################TOOLTIPZ
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
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
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()




####################################
def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor





#################TAB_BGs
i = Image.open('icons/pigronew.png')
p = ImageTk.PhotoImage(i)
l = Label(tab1, image=p)
l.image = p
l['background'] = '#383c4a'
l.place(x=-1, y=-1)

itab11 = Image.open('icons/pigro_bg.png')
ptab11 = ImageTk.PhotoImage(itab11)
ltab11 = Label(tab11, image=ptab11)
ltab11.image = ptab11
ltab11['background'] = '#383c4a'
ltab11.place(x=-1, y=-1)

itab2 = Image.open('icons/pigro_bg.png')
ptab2 = ImageTk.PhotoImage(itab2)
ltab2 = Label(tab2, image=ptab2)
ltab2.image = ptab2
ltab2['background'] = '#383c4a'
ltab2.place(x=-1, y=-1)

itab3 = Image.open('icons/pigro_bg.png')
ptab3 = ImageTk.PhotoImage(itab3)
ltab3 = Label(tab3, image=ptab3)
ltab3.image = ptab3
ltab3['background'] = '#383c4a'
ltab3.place(x=-1, y=-1)

itab4 = Image.open('icons/pigro_bg.png')
ptab4 = ImageTk.PhotoImage(itab4)
ltab4 = Label(tab4, image=ptab4)
ltab4.image = ptab4
ltab4['background'] = '#383c4a'
ltab4.place(x=-1, y=-1)

itab5 = Image.open('icons/pigro_bg.png')
ptab5 = ImageTk.PhotoImage(itab5)
ltab5 = Label(tab5, image=ptab5)
ltab5.image = ptab5
ltab5['background'] = '#383c4a'
ltab5.place(x=-1, y=-1)

itab6 = Image.open('icons/pigro_bg.png')
ptab6 = ImageTk.PhotoImage(itab6)
ltab6 = Label(tab6, image=ptab6)
ltab6.image = ptab6
ltab6['background'] = '#383c4a'
ltab6.place(x=-1, y=-1)

itab7 = Image.open('icons/pigro_bg.png')
ptab7 = ImageTk.PhotoImage(itab7)
ltab7 = Label(tab7, image=ptab7)
ltab7.image = ptab7
ltab7['background'] = '#383c4a'
ltab7.place(x=-1, y=-1)

itab8 = Image.open('icons/pigro_bg.png')
ptab8 = ImageTk.PhotoImage(itab8)
ltab8 = Label(tab8, image=ptab8)
ltab8.image = ptab8
ltab8['background'] = '#383c4a'
ltab8.place(x=-1, y=-1)

itab9 = Image.open('icons/pigro_bg.png')
ptab9 = ImageTk.PhotoImage(itab9)
ltab9 = Label(tab9, image=ptab9)
ltab9.image = ptab9
ltab9['background'] = '#383c4a'
ltab9.place(x=-1, y=-1)

itab10 = Image.open('icons/pigro_bg.png')
ptab10 = ImageTk.PhotoImage(itab10)
ltab10 = Label(tab10, image=ptab10)
ltab10.image = ptab10
ltab10['background'] = '#383c4a'
ltab10.place(x=-1, y=-1)


#############################################TAB1
def paypal():
    popen("xdg-open https://www.paypal.com/paypalme/actionschnitzel?locale.x=de_DE")
    
    
tab1.counter = 0


def clicked():
    playsound('scripts/kuba-yo.mp3')
    popen("xterm -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/kuba-yo!.sh && exit; exec bash\"'")
    tab1.counter += 1
    L['text'] = str(tab1.counter)


L = Label(tab1, text="", font=("Helvetica", 20), background='#333333', fg="white")
L.place(y=447, x=315)

###############StartClick
i9 = Image.open('icons/click.png')
p9 = ImageTk.PhotoImage(i9)
l9 = Label(image=p9)

ip9 = Image.open('icons/pay.png')
pp9 = ImageTk.PhotoImage(ip9)
lp9 = Label(image=pp9)

readfbutton = Button(tab1, text="Read First", borderwidth=0, background='green',highlightthickness=1, command=readf,font=(("Helvetica,bold"),"11")).place(x=80,y=400)

clc_btn0 = Button(tab1, image=p9, borderwidth=0, background='white',highlightthickness=0, command=clicked)
clc_btn0.place(x=470, y=156)
clc_btn0tt= CreateToolTip(clc_btn0, \
                                 "You found the hidden button ! Release hell/Kill cute puppies")

Chl = Button(tab1, text="Change Log", font="50", width=10, highlightthickness=0, borderwidth=0, background='#333333',
             foreground="white", command=changelog).place(x=550, y=445)

aclabel=Label(tab1,text="JULY FIX of the Fix:",font=("Helvetica", 12), bg="#333333",fg="#d4244d").place(x=410, y=447)

author = tk.Label(tab1, text="Author: Timo Westphal\nVersion: 6.0", foreground="white",font=20,compound=LEFT)
author.place(x=450, y=360)

paypal = Button(tab1, image=pp9, borderwidth=0, background='#333333',highlightthickness=0, command=paypal).place(x=505, y=400)

al = tk.Label(tab1, text=r"https://www.actionschnitzel.de/PiGro/", fg="blue", cursor="hand2")
al.place(x=410, y=425)
al.bind("<Button-1>", callback)

author['background'] = '#333333'
al['background'] = '#333333'


############################################################################################################tab11######updater

rahmen11 = Frame(tab11, relief=GROOVE, borderwidth=0)
rahmen11.pack(padx=45, pady=20, anchor=W)
rahmen11['background'] = '#333333'



class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text='widget info'):
        self.waittime = 500  # miliseconds
        self.wraplength = 180  # pixels
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
                         wraplength=self.wraplength)
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()



def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))


def button_action():
    os.popen('xterm -into %d -bg Grey37 -geometry 120x25 -e \"sudo apt update && read -p PRESS_ENTER && exit; exec bash\"' % wid);

def button_action2():
    os.popen('xterm -into %d -bg Grey37 -geometry 120x25 -e \"sudo apt-get update -y && sudo apt-get full-upgrade -y && sudo apt-get dist-upgrade -y && sudo apt autoremove -y && sudo apt autoclean && read -p PRESS_ENTER && exit ; exec bash\"' % wid);
    
def button_action16():
    os.popen('xterm -into %d -bg Grey37 -geometry 120x25 -e \"sudo apt autoremove -y && sudo apt clean && sudo apt-get purge -y && read -p PRESS_ENTER && exit ; exec bash\"' % wid)

def button_action17():
    os.popen("xterm -into %d -bg Grey37 -geometry 120x25 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &" % wid)

def button_auto():
    popen('xfce4-session-settings')
    
def button_xsett():
    popen('xfce4-settings-manager')
    
def button_gpk():
    popen('sudo pi-gpk-update-viewer')

def save_list():
    os.system('sudo chmod 777 -R /etc/apt/sources.list')
    text_file = open("/etc/apt/sources.list", 'w')
    text_file.write(s_list.get(1.0, END))
    m_text = "\
\n\
\n\
Sources List has been saved\n\
\n\
\n\
"
    messagebox.showinfo(message=m_text, title="Infos")


#ft

termf = Frame(tab11, height=270, width=600, padx=10, highlightthickness=1)
wid = termf.winfo_id()
# os.system('xterm -into %d -bg SteelBlue4 -geometry 120x100  &' % wid)
termf['background'] = '#383c4a'

s_list = Text(rahmen11, width=100, height=5, highlightthickness=1, borderwidth=0)
text_file = open("/etc/apt/sources.list", 'r')
stuff = text_file.read()
s_list.insert(END, stuff)
text_file.close()
s_list.pack(anchor='w')

shadowcolor = "yellow"


# yyyy
rahmen112 = Frame(tab11, borderwidth=0, relief=GROOVE, highlightthickness=1)
rahmen112.pack(padx=45, anchor='w')
rahmen112['background'] = '#333333'

update_button = Button(rahmen112, text="Update", width=15, anchor='w', command=button_action, highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white")
update_button.grid(column=0, row=0)

upgrade_button = Button(rahmen112, text="Upgrade", width=15, anchor='w', command=button_action2, highlightthickness=0,
                        borderwidth=0, background='#333333', foreground="white")
upgrade_button.grid(column=0, row=1)

auth_button = Button(rahmen112, text="Allow Sources", width=15, anchor='w', command=button_action17,
                     highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
auth_button.grid(column=1, row=0)

rm_button = Button(rahmen112, text="Remove Config Files", width=15, anchor='w', command=button_action16,
                   highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
rm_button.grid(column=1, row=1)

gpk_button = Button(rahmen112, text="GPK UpdateViewer", width=15, anchor='w', command=button_gpk,
                    highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
gpk_button.grid(column=0, row=2)

sv_button = Button(rahmen112, text="Save Source List", width=15, anchor='w', command=save_list, highlightthickness=0,
                   borderwidth=1, background='#333333', foreground="#d4244d")
sv_button.grid(column=1, row=2)

hiddn_button = Button(tab11, width=15, anchor='w', borderwidth=0)
# hiddn_button.place(x=730, y=280)
hiddn_button_ttp = CreateToolTip(hiddn_button, \
                                 "oh my fucking god, you found the hidden button !!!! I don't give a fuck about spelling, okay? This tool was created in 6 weeks of corona quarantine and quite honestly I think it's really cool. if it wasn't open source, I'd be a fucking millionaire now .... fuuuuuuuuuuuuuuuuuuuu. love you for using my tool: - * C YA")



termf.pack(padx=10,pady=20)




#####################################################INSTALLER Tab3###############################


rahmen3 = Frame(tab3, relief=GROOVE, padx=42, pady=20,borderwidth=0, highlightthickness=1)
rahmen3.pack(pady=20,anchor=N)
rahmen3['background'] = '#333333'


#########inst tab2
#########inst tab2
inst1_p1=""" xterm -e 'bash -c \"sudo apt-get install """
inst1_p2="""; exec bash\"' """

def inst_btn1():
    entry_text = eingabefeld1.get()
    popen(inst1_p1 + entry_text + inst1_p2)

def uninst_btn1():
        popen("sudo synaptic")
        
def inst_syn():
        popen("xterm -e 'bash -c \"sudo apt-get install synaptic; exec bash\"'")




i4 = Image.open('icons/apt-get.png')
p4 = ImageTk.PhotoImage(i4)
l4 = Label(image=p4)

welcome_label1 = Label(rahmen3)
eingabefeld1 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button1 = Button(rahmen3, text="install", command=inst_btn1, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
welcom_button1_ttp = CreateToolTip(welcom_button1, \
                                   'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.')

uninst_button = Button(rahmen3, text="Synaptic/Uninstaller", command=uninst_btn1, highlightthickness=1, borderwidth=0,background='#333333', foreground="white")
uninst_button_ttp = CreateToolTip(uninst_button, \
                                  'If nothing happens you must install Synaptic')

my_label = Label(rahmen3, image=p4, fg="white")
my_label['background'] = '#333333'
my_label.grid(column=0, row=0, pady=10)
eingabefeld1.grid(column=2, row=0)
welcom_button1.grid(column=1, row=0)
uninst_button.grid(column=2, row=6)


######DEFZ####inst3###pi-apps
inst3_p1=""" xterm -e 'bash -c \"~/pi-apps/manage install """
inst3_p2="""; exec bash\"' """

def inst_pi_apps():
    entry_text = eingabefeld3.get()
    popen(inst3_p1 + entry_text + inst3_p2)


uninst3_p1=""" xterm -e 'bash -c \"~/pi-apps/manage uninstall """
uninst3_p2="""; exec bash\"' """

def uninst_pi_apps():
    entry_text = eingabefeld3.get()
    popen(uninst3_p1 + entry_text + uninst3_p2)

def pi_apps_list():
    popen("xterm -e 'bash -c \"ls /home/pi/pi-apps/apps/ ; exec bash\"'")

ia6 = Image.open('icons/pi-app.png')
pa6 = ImageTk.PhotoImage(ia6)
la6 = Label(image=pa6)

apps_inst_btn = Label(rahmen3, image=pa6, text="piapps install", fg="white")
apps_inst_btn ['background'] = '#333333'

welcome_label2 = Label(rahmen3)
eingabefeld3 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button3 = Button(rahmen3, text="install", command=inst_pi_apps, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

welcom_button33 = Button(rahmen3, text="list all pi-apps", command=pi_apps_list, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

welcom_button4 = Button(rahmen3, text="uninstall", command=inst_pi_apps, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white")

apps_inst_btn.grid(column=0, row=3)
eingabefeld3.grid(column=2, row=3)
welcom_button3.grid(column=1, row=3)
welcom_button33.grid(column=1, row=4)
welcom_button4.grid(column=1, row=5)

######DEFZ####inst2###

inst2_p1=""" xterm -e 'bash -c \"sudo snap install """
inst2_p2="""; exec bash\"' """

def inst_btn2():
    entry_text = eingabefeld2.get()
    popen(inst2_p1 + entry_text + inst2_p2)


i6 = Image.open('icons/snap.png')
p6 = ImageTk.PhotoImage(i6)
l6 = Label(image=p6)

my_label2 = Label(rahmen3, image=p6, text="Snap install", fg="white")
my_label2['background'] = '#333333'

welcome_label2 = Label(rahmen3)
eingabefeld2 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button2 = Button(rahmen3, text="install", command=inst_btn2, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
welcom_button2_ttp = CreateToolTip(welcom_button2, \
                                   '*to use snap install, you must\napt-get install snapd xD lol')

my_label2.grid(column=0, row=1)
eingabefeld2.grid(column=2, row=1)
welcom_button2.grid(column=1, row=1)

tab_ip3 = Image.open('icons/download_ico.png')
ip03 = ImageTk.PhotoImage(tab_ip3)
il03 = Label(image=ip03)


###################shop Tab3
def shop():
    global pop_shop
    pop_shop=Toplevel()
    #pop_shop.geometry("+300+300")
    pop_shop['background'] = '#333333'



    shop_btn01 = Button(pop_shop, width=120, image=ip03, text="Whatsapp\n(Snap)", anchor="w", command=w_app, highlightthickness=0,
                  borderwidth=0, background='#d4244d',foreground="white", compound=LEFT).grid(column=0, row=1)

    shop_btn1_ttp = CreateToolTip(sys_btn6, \
                                      'This is a SNAP')

    shop_lbl011 = Label(pop_shop,width=50, text="... is... you know Whatsapp", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=1)

    shop_btn2 = Button(pop_shop, width=120, image=ip03, text="Compiz", anchor="w", command=compiz_button,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=2)

    shop_lbl21 = Label(pop_shop,width=50, text="When I was young it was cool You know it as wobbly windows", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=2)

    
    shop_btn3 = Button(pop_shop, width=120, image=ip03, text="Gparted", anchor="w", command=gparted_inst,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=3)


    shop_btn31 = Label(pop_shop,width=50, text="A Partition Manager", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=3)


    shop_btn4 = Button(pop_shop, width=120, image=ip03, text="NeoFetch", anchor="w", command=inst_neo, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=4)


    shop_btn41 = Label(pop_shop,width=50, text="Shows system specs you already know but ... uhhm...", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=4)


    shop_btn5 = Button(pop_shop, width=120, image=ip03, text="PiKiss", anchor="w", command=kiss_button, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=5)


    shop_btn51 = Label(pop_shop,width=50, text="Bow down!", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=5)


    shop_btn6 = Button(pop_shop, width=120, image=ip03, text="Bleach Bit", anchor="w", command=inst_bleach,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=6)

    
    shop_btn61 = Label(pop_shop,width=50, text="Cleans the System", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=6)


    shop_btn7 = Button(pop_shop, width=120, image=ip03, text="Pi Imager", anchor="w", command=inst_ima, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=7)

    
    shop_btn71 = Label(pop_shop,width=50, text="Pi-Imager on RaspiOS is like the Replicants from Stargate... o,o", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=7)

    
    shop_btn8 = Button(pop_shop, width=120, image=ip03, text="Synaptic", anchor="w", command=inst_syn, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=8)

    
    shop_btn81 = Label(pop_shop,width=50, text="THE Pakegemanager", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=8)


    shop_btn9 = Button(pop_shop, width=120, image=ip03, text="Gnome-Pie", anchor="w", command=gnome_pie, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=9)


    shop_btn91 = Label(pop_shop,width=50, compound=LEFT, text="When you tell peolpe i3 is god but you need a hidden menu cuz\nyou dont cope with it", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=1, row=9)


    shop_btn10 = Button(pop_shop, width=120, image=ip03, text="Pi-Apps", anchor="w", command=pi_apps, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=10)

    
    shop_btn101 = Label(pop_shop,width=50, text="DOWNLOAD IT!!!!!11", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=10)

    
    shop_btn11 = Button(pop_shop, width=120, image=ip03, text="Lutris", anchor="w", command=inst_lutis, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=11)

    
    shop_btn111 = Label(pop_shop,width=50, text="Game installer", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=11)
    
    
    shop_btn13 = Button(pop_shop, width=120, image=ip03, text="Vulkan 32 bit\n ", anchor="w", command=vulk_32, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=2, row=1)

    shop_btn113 = Label(pop_shop,width=50, text="Uninstall: sudo rm -r /home/pi/mesa_vulkan", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=3, row=1)   
    
    shop_btn14 = Button(pop_shop, width=120, image=ip03, text="Vulkan 64 bit", anchor="w", command=vulk_64, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=2, row=2)

    shop_btn114 = Label(pop_shop,width=50, text="Uninstall: sudo rm -r /home/pi/mesa_vulkan", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=3, row=2)     

    shop_btn15 = Button(pop_shop, width=120, image=ip03, text="Tetris-CLI", anchor="w", command=tetris_cli, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=2, row=3)

    shop_btn115 = Label(pop_shop,width=50, text="Uninstall: sudo rm -r /home/pi/tetris", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=3, row=3)     


#####################
tab_shop = Image.open('icons/shop.png')
ipshop = ImageTk.PhotoImage(tab_shop)
ilshop = Label(image=ipshop)

rahmen_shop = Frame(tab3,borderwidth=0, highlightthickness=1)
rahmen_shop.pack(padx=40, pady=20)
rahmen_shop['background'] = '#333333'


shop_click = Button(rahmen_shop,image=ipshop, anchor="w", command=shop, highlightthickness=1,
                  borderwidth=0, background='#7f1b57', foreground="white", compound=LEFT)
shop_click.pack()





###########################################System####################tab2#######################################




####################
# icons
sys_bp1 = Image.open('icons/raspberry-pi-logo.png')
bp01 = ImageTk.PhotoImage(sys_bp1)
bl01 = Label(image=bp01)

sys_bp2 = Image.open('icons/raspberry-pi-logo.png')
bp02 = ImageTk.PhotoImage(sys_bp2)
bl02 = Label(image=bp02)

sys_bp3 = Image.open('icons/terminal.png')
bp03 = ImageTk.PhotoImage(sys_bp3)
bl03 = Label(image=bp03)

sys_bp33 = Image.open('icons/terminal3.png')
bp033 = ImageTk.PhotoImage(sys_bp33)
bl033 = Label(image=bp033)

sys_bp4 = Image.open('icons/gparted.png')
bp04 = ImageTk.PhotoImage(sys_bp4)
bl04 = Label(image=bp04)

sys_bp5 = Image.open('icons/indicator-cpufreq.png')
bp05 = ImageTk.PhotoImage(sys_bp5)
bl05 = Label(image=bp05)

sys_bp6 = Image.open('icons/folder.png')
bp06 = ImageTk.PhotoImage(sys_bp6)
bl06 = Label(image=bp06)

sys_bp7 = Image.open('icons/links.png')
bp07 = ImageTk.PhotoImage(sys_bp7)
bl07 = Label(image=bp07)

#########################################FRAMETAB2
#########################################
rahmen2 = Frame(tab2,borderwidth=0, highlightthickness=1, relief=GROOVE,padx=10)
rahmen2.pack(padx=10,pady=20)
rahmen2['background'] = '#333333'

###
#env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui


sys_btn6 = Button(rahmen2, image=bp01, text="Raspi-Config CLI", command=pi_configbutton,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn6.grid(row=0,column=0)

sys_btn1 = Button(rahmen2, image=bp01, text="Raspi-Config GUI", command=pi_configbutton2,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn1.grid(row=0,column=1)


sys_btn2 = Button(rahmen2, image=bp03, text="Nano Config.txt", command=contxt_button,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn2.grid(row=0,column=2)

sys_btnvs = Button(rahmen2, image=bp03, text="rm vscode.list ", command=rm_vsc,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btnvs.grid(row=0,column=3)

sys_btn3 = Button(rahmen2, image=bp04, text="Gparted", command=gparted_exec,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn3.grid(row=1,column=0)

sys_btn4 = Button(rahmen2, image=bp05, text="NeoFetch", command=neofetch_button,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn4.grid(row=1,column=1)

sys_btn5 = Button(rahmen2, image=bp06, text="FM God Mode", command=onc_ben, highlightthickness=0,
                  borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn5.grid(row=1,column=2)
sys_btn5_ttp = CreateToolTip(sys_btn5, \
                                   "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)")


sys_btn6 = Button(rahmen2, image=bp07, text="Upgrade Linux Kernel", command=button_lk,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn6.grid(row=1,column=3)

sys_btn7 = Button(rahmen2, image=bp03, text="DeskpiPro Control", command=button_dpfc,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn7.grid(row=2,column=0)

sys_btn8 = Button(rahmen2, image=bp03, text="Boot Log", command=button_boot,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn8.grid(row=2,column=1)

sys_btn9 = Button(rahmen2, image=bp033, text="Xfce Autostarts", command=button_auto,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn9.grid(row=2,column=2)

sys_btn9 = Button(rahmen2, image=bp033, text="Xfce Settings", command=button_xsett,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP, anchor="w")
sys_btn9.grid(row=2,column=3)


####################################################


rahmen21 = Frame(tab2,borderwidth=0, highlightthickness=1, relief=GROOVE,pady=10,padx=20)
rahmen21.pack()
rahmen21['background'] = '#333333'







deblogo = Image.open('icons/deb_logo.png')
dl = ImageTk.PhotoImage(deblogo)
dl01 = Label(image=dl)

deblogo2 = Image.open('icons/lmint.png')
dl2 = ImageTk.PhotoImage(deblogo2)
dl012 = Label(image=dl2)




        
pid = os.getpid()
ps = psutil.Process(pid)
my_system = platform.uname()
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
distro = distro.id()




#xxx

sysinf0 = Label(rahmen21, text="System Info", compound=LEFT, anchor='n',font=("Helvetica",16), highlightthickness=0, borderwidth=0,
                background='#333333', foreground="#d4244d",pady=20)
sysinf0.grid(column=1, row=0)

sysinf0 = Label(rahmen21,image=dl, highlightthickness=0, borderwidth=0,
                background='#333333', foreground="#d4244d",pady=20,padx=20)
sysinf0.grid(column=0, row=0,rowspan=6)

sysinf0 = Label(rahmen21, text=f"System: {my_system.system}", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#333333', foreground="white", width=20,padx=10)
sysinf0.grid(column=1, row=1)

sysinfd = Label(rahmen21, text=f"Distro: {distro}", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#333333', foreground="white", width=20)
sysinfd.grid(column=1, row=2)

sysinf1 = Label(rahmen21, text=f"Node Name: {my_system.node}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20)
sysinf1.grid(column=1, row=3)
sysinf2 = Label(rahmen21, text=f"Kernel: {my_system.release}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20)
sysinf2.grid(column=1, row=4)
sysinf3 = Label(rahmen21, text=f"Machine: {my_system.machine}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20)
sysinf3.grid(column=1, row=5)
sysinf3 = Label(rahmen21, text="", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20)
sysinf3.grid(column=2, row=0)
sysinf3 = Label(rahmen21, text=f"RAM Total: {get_size(svmem.total)}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25)
sysinf3.grid(column=2, row=1)
sysinf3 = Label(rahmen21, text=f"SWAP Total: {get_size(swap.total)}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25)
sysinf3.grid(column=2, row=2)

sysinf6 = Label(rahmen21, text=f"CPU Max Freq: {cpufreq.max:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25)
sysinf6.grid(column=2, row=3)
sysinf7 = Label(rahmen21, text=f"CPU Min Freq: {cpufreq.min:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25)
sysinf7.grid(column=2, row=4)
sysinf8 = Label(rahmen21, text=f"Current CPU Freq: {cpufreq.current:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25)
sysinf8.grid(column=2, row=5)


##########################################LOOK

# xx
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def xfce_make():
    popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

tab_ip1 = Image.open('icons/download_ico.png')
ip01 = ImageTk.PhotoImage(tab_ip1)
il01 = Label(image=ip01)

tab_ip2 = Image.open('icons/fix1i.png')
ip02 = ImageTk.PhotoImage(tab_ip2)
il02 = Label(image=ip02)

rahmen4 = Frame(tab4,borderwidth=0, highlightthickness=1, relief=GROOVE, pady=10, padx=5)
rahmen4.pack(pady=20)
rahmen4['background'] = '#333333'



in_btn1 = Button(rahmen4, text="Tasksel", command=tasksel_button, font=120, highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white")
in_btn1.grid(column=0, row=0, padx=5)

in_btn2 = Button(rahmen4, text="Change Desktop", command=ch_desk, font=120, highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white")
in_btn2.grid(column=1, row=0, padx=5)

in_btn3 = Button(rahmen4, text="Change Win-Manager", command=button_xfwm, font=120, highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white")
in_btn3.grid(column=2, row=0, padx=5)

in_btn7 = Button(rahmen4, text="Theme Folder", compound=LEFT, anchor="w", width=10,
                 command=theme_f, highlightthickness=2, borderwidth=0, background='#333333', foreground="white")
in_btn7.grid(column=3, row=1)

in_btn7 = Button(rahmen4, text="Icon Folder", compound=LEFT, anchor="w", width=10,
                 command=icon_f, highlightthickness=2, borderwidth=0, background='#333333', foreground="white")
in_btn7.grid(column=3, row=2)

in_btn7 = Button(rahmen4, text="Xfce_look", compound=LEFT, anchor="w", width=10,
                 command=xfcelook_f, highlightthickness=2, borderwidth=0, background='#333333', foreground="white")
in_btn7.grid(column=3, row=0)

in_btn8 = Button(rahmen4, text="Make-Me-Xfce (Tutorial)", compound=LEFT, anchor="w",
                 command=xfce_make, highlightthickness=2, borderwidth=0, background='#333333', foreground="white")
in_btn8.grid(column=1, row=2)


###########################################


rahmen41 = Frame(tab4,borderwidth=0, highlightthickness=1, relief=GROOVE,pady=10,padx=15)
rahmen41.pack()
rahmen41['background'] = '#333333'


xfce = Label(rahmen41, text="Xfce Tweaks",font=("Helvetica",14), background='#333333', foreground="#d4244d", anchor="w")
xfce.grid(column=0, row=0)

in_btn3 = Button(rahmen41, text="Xfwm4 Settings", image=ip02, compound=LEFT, anchor="w",
                 command=button_xf4s, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", width=150)
in_btn3.grid(column=1, row=0, padx=5)

in_btn5 = Button(rahmen41, text="WiFi Fix", image=ip02, compound=LEFT, anchor="w",
                 command=xfcefix2, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", width=100)
in_btn5.grid(column=3, row=0)

in_btn5 = Button(rahmen41, text="Bluetooth Fix", image=ip02, compound=LEFT, anchor="w",
                 command=xfcefix, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", width=150)
in_btn5.grid(column=2, row=0)

in_btn5 = Button(rahmen41, text="Xfce4 Appearance", image=ip02, compound=LEFT, anchor="w",
                 command=xfceappear_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", width=150)
in_btn5.grid(column=1, row=1)

##################################################

rahmen42 = Frame(tab4,borderwidth=0, highlightthickness=1, relief=GROOVE,pady=10,padx=16)
rahmen42.pack(padx=10, pady=20)
rahmen42['background'] = '#333333'

lxde = Label(rahmen42, text="Pixel Tweaks",font=("Helvetica",14), background='#333333', foreground="#d4244d", anchor="w")
lxde.grid(column=0, row=0)

lx_btn0 = Button(rahmen42, text="LXAppearace", image=ip02, compound=LEFT, anchor="w",
                 command=lxap_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
lx_btn0.grid(column=1, row=0)

lxde = Button(rahmen42, text="OpenBox Conf", image=ip02, compound=LEFT, anchor="w",
                 command=opbox_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
lxde.grid(column=2, row=0)

lxde = Button(rahmen42, text="Pi Appeariance", image=ip02, compound=LEFT, anchor="w",
                 command=pi_appear, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
lxde.grid(column=3, row=0)

##################################################

rahmen43 = Frame(tab4,borderwidth=0, highlightthickness=1, relief=GROOVE,pady=10,padx=15)
rahmen43.pack(padx=8)
rahmen43['background'] = '#333333'


lxde = Label(rahmen43, text="Suggestions ",font=("Helvetica",14), background='#333333', foreground="#d4244d", anchor="w")
lxde.grid(column=0, row=0)

in_btn3 = Button(rahmen43, text="Install Arc Theme", image=ip01, compound=LEFT, anchor="w", width=220, command=arc_inst,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
in_btn3.grid(column=1, row=0)

in_btn4 = Button(rahmen43, text="Install Breeze Cursor Theme", image=ip01, compound=LEFT, anchor="w", width=220,
                 command=breeze_inst, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
in_btn4.grid(column=2, row=0)

in_btn5 = Button(rahmen43, text="Install Papirus Icon Theme", image=ip01, compound=LEFT, anchor="w", width=220,
                 command=papi_inst, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
in_btn5.grid(column=1, row=1)

#in_btn6 = Button(rahmen43, text="PiGro Wallpapers(Web)", image=ip01, compound=LEFT, anchor="w", width=220,
#                 command=web_wall, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
#in_btn6.grid(column=2, row=1)

in_btn7 = Button(rahmen43, text="Overwatch Cursor", image=ip01, compound=LEFT, anchor="w", width=220,
                 command=web_OVC, highlightthickness=0, borderwidth=0, background='#333333', foreground="white")
in_btn7.grid(column=1, row=3)






############################################Tuning





tu_tp1 = Image.open('icons/PiGroOV2.png')
tu01 = ImageTk.PhotoImage(tu_tp1)
tul01 = Label(image=tu01)

tu_tp2 = Image.open('icons/PiGroOV.png')
tu02 = ImageTk.PhotoImage(tu_tp2)
tul02 = Label(image=tu02)

tu_tp3 = Image.open('icons/PiGroOV3.png')
tu03 = ImageTk.PhotoImage(tu_tp3)
tul03 = Label(image=tu03)

tu_tp4 = Image.open('icons/PiGroOV4.png')
tu04 = ImageTk.PhotoImage(tu_tp4)
tul04 = Label(image=tu04)


#########################################tuning_def
def pop_dest():
    pop_default.destroy()

def pop_dest1():
    pop_2147.destroy()

def pop_dest2():
    pop_2000.destroy()
    
def pop_dest3():
    pop_2200.destroy()
    
def reboot_n():
    popen("sudo reboot")
######################################pop_2000
def ov_2000():
    popen("xterm -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/ov_1.sh && exit; exec bash\"'")
    
    global pop_2000
    pop_2000=Toplevel(main)
    pop_2000.config(bg='#333333')
    
    frame_pop_2000 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
    frame_pop_2000.pack()
    frame_pop_2000['background'] = '#333333'

    frame_pop_2000_1 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
    frame_pop_2000_1.pack(pady=10)
    frame_pop_2000_1['background'] = '#333333'

    
    pop_lbl_2000=Label(frame_pop_2000,anchor="w", text="Done !",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
    pop_lbl_2000.grid(column=1, row=1,pady=10,padx=10)
    pop_btn_2000=Button(frame_pop_2000_1,text="Continue", anchor="w", command=pop_dest2,
                           highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
    pop_btn_2000.grid(column=1, row=2)
    pop_btn_shut=Button(frame_pop_2000_1,text="Reboot", anchor="w", command=reboot_n,
                           highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
    pop_btn_shut.grid(column=2, row=2)
    
    #tl0m = Label(frame_pop_2000,image=tp0m, background='#333333').grid(column=0, row=1)
    
    
######################################pop_2147        
def ov_2147():
    popen("xterm -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/ov_2.sh && exit; exec bash\"'")
    playsound('scripts/HOLYPiT.mp3')
    global pop_2147
    pop_2147=Toplevel(main)
    pop_2147.config(bg='#333333')
    
    frame_pop_2147 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
    frame_pop_2147.pack()
    frame_pop_2147['background'] = '#333333'

    frame_pop_2147_1 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
    frame_pop_2147_1.pack(pady=10)
    frame_pop_2147_1['background'] = '#333333'

    
    pop_lbl_2147=Label(frame_pop_2147,anchor="w", text="Done !",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
    pop_lbl_2147.grid(column=1, row=1,pady=10,padx=10)
    pop_btn_2147=Button(frame_pop_2147_1,text="Continue", anchor="w", command=pop_dest1,
                           highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
    pop_btn_2147.grid(column=1, row=2)
    pop_btn_shut=Button(frame_pop_2147_1,text="Reboot", anchor="w", command=reboot_n,
                           highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
    pop_btn_shut.grid(column=2, row=2)
    
    #tl0m = Label(frame_pop_2147,image=tp0m, background='#333333').grid(column=0, row=1)
##########################pop_default
def set_default():
    popen("xterm -e 'bash -c \"sudo chmod +x /home/pi/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
    popen("xterm -e 'bash -c \"sudo /home/pi/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
    global pop_default
    pop_default=Toplevel(main)
    pop_default.config(bg='#333333')
    
    frame_pop_de = Frame(pop_default, borderwidth=0, relief=GROOVE)
    frame_pop_de.pack()
    frame_pop_de['background'] = '#333333'

    frame_pop_de1 = Frame(pop_default, borderwidth=0, relief=GROOVE)
    frame_pop_de1.pack(pady=10)
    frame_pop_de1['background'] = '#333333'

    pop_lbl_default=Label(frame_pop_de,anchor="w", text="Settings Restored",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
    pop_lbl_default.grid(column=1, row=1,pady=10,padx=10)
    pop_btn_default=Button(frame_pop_de1,text="Continue", anchor="w", command=pop_dest,
                           highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
    pop_btn_default.grid(column=1, row=2)
    pop_btn_shut=Button(frame_pop_de1,text="Reboot", anchor="w", command=reboot_n,
                           highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
    pop_btn_shut.grid(column=2, row=2)
    
    #tl0m = Label(frame_pop_de,image=tp0m, background='#333333').grid(column=0, row=1)


######################################pop_2147        
def ov_2200():
    popen("xterm -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/ov_3.sh && exit; exec bash\"'")
    playsound('scripts/HOLYPiT.mp3')
    global pop_2200
    pop_2200=Toplevel(main)
    pop_2200.config(bg='#333333')
    
    frame_pop_2200 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
    frame_pop_2200.pack()
    frame_pop_2200['background'] = '#333333'

    frame_pop_2200_1 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
    frame_pop_2200_1.pack(pady=10)
    frame_pop_2200_1['background'] = '#333333'

    
    pop_lbl_2200=Label(frame_pop_2200,anchor="w", text="Done !",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
    pop_lbl_2200.grid(column=1, row=1,pady=10,padx=10)
    pop_btn_2200=Button(frame_pop_2200_1,text="Continue", anchor="w", command=pop_dest3,
                           highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
    pop_btn_2200.grid(column=1, row=2)
    pop_btn_shut=Button(frame_pop_2200_1,text="Reboot", anchor="w", command=reboot_n,
                           highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
    pop_btn_shut.grid(column=2, row=2)
    
    #tl0m = Label(frame_pop_2200,image=tp0m, background='#333333').grid(column=0, row=1)
##########################pop_default

 ##########################################   
rahmen6 = Frame(tab6,borderwidth=0, highlightthickness=1, relief=GROOVE, pady=20)
rahmen6.pack(padx=10, pady=20, anchor=N)
rahmen6['background'] = '#333333'

rahmen622 = Frame(tab6,borderwidth=0, highlightthickness=1, relief=GROOVE, padx=100, pady=10)#
rahmen622.pack(padx=10)
rahmen622['background'] = '#333333'

rahmen61 = Frame(rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=30, pady=10)#
rahmen61.pack(side=LEFT)
rahmen61['background'] = '#333333'

rahmen62 = Frame(rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=10, pady=10)#
rahmen62.pack(padx=10, side=LEFT)
rahmen62['background'] = '#333333'

tu_lb1 = Label(rahmen6, text="Crank It Up", font='20', highlightthickness=0, borderwidth=2, background='#333333',
               foreground="#d4244d").grid(column=1, row=0)

tu_btn1 = Button(rahmen6, image=tu01, text="Arm_Freq = 2000\nGpu_Freq = 750\nOver_Voltage = 6", anchor="w", command=ov_2000,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=1)

tu_lb2 = Label(rahmen6, text="You Sir... Need A Fan! ", font='20', highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d").grid(column=2, row=0)

tu_btn2 = Button(rahmen6, image=tu02, text="Arm_Freq = 2147\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2147,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=2, row=1)

tu_lb3 = Label(rahmen6, text="Reset Overclocking", font='20', highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d").grid(column=0, row=0)

tu_btn3 = Button(rahmen6, image=tu03,text="Arm_Freq = 1500\nGpu_Freq = 500", anchor="w", command=set_default,
                highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=0, row=1)

tu_lb4 = Label(rahmen6, text="\nTake It To The Max!", font='20', highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d").grid(column=1, row=2)

tu_btn4 = Button(rahmen6, image=tu04,text="Arm_Freq = 2200\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2200,
                highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=3)

tu_info = Label(rahmen6, text="Settings tested with\nPi4 + Ice Tower Cooler and Pi400.\nI take no responsibility if\nyour Pi is damaged.", font=("Helvetica", 8), highlightthickness=0, borderwidth=2,
               background='#333333', foreground="yellow").grid(column=1, row=4)



tu_zb1 = Label(rahmen61, text="ZRAM", font='20', highlightthickness=0, borderwidth=2, background='#333333',foreground="#d4244d").grid(column=0, row=0)


tu_zbtn = Button(rahmen61, text="Install Zram\n\nCommands:\nswapon -s\nservice zramswap stop\nservice zramswap start\n ", anchor="w", command=z_ram,highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica", 8)).grid(column=0, row=1)
################


tu_bb1=Label(rahmen62, text="64 Bit Mode", font='20', highlightthickness=0, borderwidth=2, background='#333333',foreground="#d4244d").grid(column=0, row=0)

tu_bbtn=Button(rahmen62, text="Install 64 Bit Mode\n\nHow To:\nActivate via Menu\nor\n Type:ds64-shell\nThen install what ever you want", anchor="w", command=btswitch_64,highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica", 8)).grid(column=0, row=1)


#####################################Links
def down_twist():
    popen("xdg-open https://twisteros.com/")
    
def down_NCP():
    popen("xdg-open https://ownyourbits.com/nextcloudpi/")

def down_puppy():
    popen("xdg-open https://puppylinux.com/")
    
def down_diet():
    popen("xdg-open https://dietpi.com/")
    
def down_mx():
    popen("xdg-open https://mxlinux.org/blog/fluxbox-raspberrypi-respin-ragout-beta/")

def down_fy():
    popen("xdg-open https://releases.fydeos.io/11.4/rpi4-fydeos")

def down_kk():
    popen("xdg-open https://konstakang.com/devices/rpi4/")
    
def down_bb():
    popen("xdg-open https://berryboot.alexgoldcheidt.com/images")

def link_mankier():
    popen("xdg-open https://mankier.com")
    
def link_guake():
    popen("xdg-open https://github.com/Guake/guake")
    
def link_onBoard():
    popen("xdg-open https://wiki.ubuntuusers.de/Barrierefreiheit/onBoard/")
    
def link_drac():
    popen("xdg-open https://draculatheme.com/")    

def link_star():
    popen("xdg-open https://starship.rs/")    



rahmen81 = Frame(tab8,borderwidth=0, highlightthickness=1, relief=GROOVE)
rahmen81.pack(padx=20, pady=20)
rahmen81['background'] = '#333333'

rahmen82 = Frame(tab8,borderwidth=0, highlightthickness=1, relief=GROOVE,padx=20, pady=20)
rahmen82.pack(padx=20, pady=20)
rahmen82['background'] = '#333333'

tab8_dist1 = Image.open('icons/TwisterOSLogo-Large-New3.png')
di01 = ImageTk.PhotoImage(tab8_dist1)
dl01 = Label(image=di01)

tab8_dist2 = Image.open('icons/Puppy_Linux_Logo.png')
di02 = ImageTk.PhotoImage(tab8_dist2)
dl02 = Label(image=di02)

tab8_dist3 = Image.open('icons/dietpi.png')
di03 = ImageTk.PhotoImage(tab8_dist3)
dl03 = Label(image=di03)

tab8_dist4 = Image.open('icons/MX-icon.png')
di04 = ImageTk.PhotoImage(tab8_dist4)
dl04 = Label(image=di04)

tab8_dist5 = Image.open('icons/fydeos.png')
di05 = ImageTk.PhotoImage(tab8_dist5)
dl05 = Label(image=di05)

tab8_dist6 = Image.open('icons/android.png')
di06 = ImageTk.PhotoImage(tab8_dist6)
dl06 = Label(image=di06)

tab8_dist7 = Image.open('icons/logo_berryserver.png')
di07 = ImageTk.PhotoImage(tab8_dist7)
dl07 = Label(image=di07)

tab8_dist8 = Image.open('icons/NCP.png')
di08 = ImageTk.PhotoImage(tab8_dist8)
dl08 = Label(image=di08)

dist_btn1 = Button(rahmen81, compound=LEFT, image=di01, text="Get: Twister OS", anchor="w", command=down_twist,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).grid(column=0, row=0)

dist_btn2 = Button(rahmen81,compound=LEFT, image=di02, text="Get: Puppy Linux", anchor="w", command=down_puppy,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).grid(column=1, row=0)

dist_btn3 = Button(rahmen81, image=di03, text="Get: DietPi", anchor="w", command=down_diet,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=3, row=0)

dist_btn4 = Button(rahmen81, image=di04, text="Get: MX Linux", anchor="w", command=down_mx,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=0, row=1)

dist_btn5 = Button(rahmen81, image=di05, text="Get: FydeOS", anchor="w", command=down_fy,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=1, row=1)

dist_btn6 = Button(rahmen81, image=di06, text="Get: Android", anchor="w", command=down_kk,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=3, row=1)

dist_btn7 = Button(rahmen81, image=di07, text="Get: Berryserver", anchor="w", command=down_bb,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=0, row=2)

dist_btn8 = Button(rahmen81,image=di08, text="Get: NextCloudPi", anchor="w", command=down_NCP,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,width=150).grid(column=1, row=2)
##################

hedd = Label (rahmen82, text="Good Sites [No payed promo/Just stuff I like]",
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="#d4244d",font=("Helvetica",16)).grid(column=0, row=0,columnspan=3,pady=10)

choice_link1=Button(rahmen82, anchor="w", width=20,text="Mankiere.com (Commandline Database)", command=link_mankier,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=1)

choice_link2=Button(rahmen82,anchor="w",width=20,text="Guake (Drop Down Terminal)",  command=link_guake,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=2)

choice_link2=Button(rahmen82,anchor="w",width=20,text="OnBoard (Onscreen Keyboard)",  command=link_onBoard,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=3)

choice_link2=Button(rahmen82, anchor="w",width=20,text="Draculatheme.com", command=link_drac,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=4)

choice_link2=Button(rahmen82, anchor="w",width=20,text="Starship (Cross-Shell-Promt)", command=link_star,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=5)
######column1
#####################################
##############################################

def lern_l():
    popen("xdg-open https://www.learnlinux.tv/")
    
def rb_tv():
    popen("xdg-open https://rocketbeans.tv/")
    
def l4_e():
    popen("xdg-open http://www.lcdwiki.com/Main_Page")
    
def fitwo_p():
    popen("xdg-open https://www.52pi.com/")    
    


choice_link1=Button(rahmen82,width=20,text="LernLinux.tv", anchor="w", command=lern_l,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=2, row=1)

choice_link2=Button(rahmen82,width=20,text="Rocket Beans(ger.)", anchor="w", command=rb_tv,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=2, row=2)

choice_link2=Button(rahmen82,width=20,text="52Pi", anchor="w", command=fitwo_p,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=2, row=3)

choice_link2=Button(rahmen82,width=20,text="LCD Wiki", anchor="w", command=l4_e,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=2, row=4)

#####################################INFO


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


def callback2(event):
    xterm.open_new(event.widget.cget("entry_text"))




###########################################################HOLY_GRAIL!!!!!1111


###########################
def holy_backup():
    popen("xterm -e 'bash -c \"dpkg --get-selections > /home/pi/packages.list & echo Done!; exec bash\"'")
    
def holy_dselect():
    popen("xterm -e 'bash -c \"sudo apt update & sudo apt install dselect; exec bash\"'")
    
def holy_recovery():
    popen("xterm -e 'bash -c \"sudo dselect update & dpkg --get-selections < /home/pi/packages.list & sudo apt-get dselect-upgrade; exec bash\"'")    
#############################


rahmen92 = Frame(tab9,borderwidth=0, highlightthickness=1, relief=GROOVE,
               background='#383c4a',padx=80)
rahmen92.pack(padx=20,pady=20)
rahmen92['background'] = '#333333'

grail_text=Label(rahmen92,text="Creates a packages.list (in: /home/pi/) of all .deb files\non your system.\nCopy it to a fresh system to auto install your packages.\nDo sudo apt-get/apt at first!",
                 background='#333333',font=("Helvetica",12), foreground="white")
grail_text.pack(pady=10)

grail_botn=Button(rahmen92,text="Backup", highlightthickness=1,background='#333333',
                       borderwidth=0, foreground="white",command=holy_backup)
grail_botn.pack(pady=10)
grail_botn_ttp = CreateToolTip(grail_botn, \
                                 "This also kills kitten remotely...\nRight now...\nAs you clicked...\nMuhahahaha!!!")

grail_text2=Label(rahmen92,text="On the  fresh system install dselect and press RECOVER.",
                 background='#333333',font=("Helvetica",12), foreground="white")
grail_text2.pack(pady=10)


#############################
rahmen93 = Frame(rahmen92,borderwidth=0, highlightthickness=0, relief=GROOVE)
rahmen93.pack(padx=20)
rahmen93['background'] = '#333333'

grail_botn2=Button(rahmen93,text="dselect", highlightthickness=1,background='#333333',
                       borderwidth=0, foreground="white",command=holy_dselect)
grail_botn2.grid(column=0, row=0)

grail_botn2=Label(rahmen93,text="              ",
                 background='#333333', highlightthickness=0,
                       borderwidth=0, foreground="white")
grail_botn2.grid(column=1, row=0)

grail_botn3=Button(rahmen93,text="Recover", highlightthickness=1,
                       borderwidth=0, background='#333333', foreground="white",command=holy_recovery)
grail_botn3.grid(column=2, row=0)

grail_text3=Label(rahmen92,text="Or: sudo apt install dselect\nsudo dselect updat\nsudo dpkg --set-selections < packages.listn\nsudo apt-get dselect-upgrade",
                 background='#333333',font=("Helvetica",8), foreground="white")
grail_text3.pack(pady=10)


##########################################pig-grow
pig_x = Image.open('icons/poke_pig.jpg')
pg0x = ImageTk.PhotoImage(pig_x)
pl0x = Label(image=pg0x)


def pick_at_you():
    global pop_pig
    pop_pig=Toplevel()
    pop_pig['background'] = 'white'
    
    poke_pig = Label(pop_pig,image=pg0x,background='#333333').pack()

    playsound('scripts/poke_pig.mp3')

    poke_pig1 = Label(pop_pig,text="Moral: Never post funny things about Pigro on forums!\nI could come up with even more stupid ideas\nand incorporate them into PiGro xD",background='white', fg="red").pack()


################################
def poll():
    popen("xdg-open http://www.actionschnitzel.de/Pig-Grow-Poll/")
    
def wpaps():
    popen("xdg-open http://www.actionschnitzel.de/Wallpapers/")
    
def wiki():
    popen("xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki")    
    
pig_1 = Image.open('icons/pigpi_btn.png')
pg01 = ImageTk.PhotoImage(pig_1)
pl01 = Label(image=pg01)

pig_logo = Button(tab10,image=pg01,background='#333333', command=pick_at_you).pack(pady=20)


rahmen102 = Frame(tab10, borderwidth=0, relief=GROOVE, highlightthickness=1)
rahmen102.pack()
rahmen102['background'] = '#333333'

poke_pig_21 = Label(rahmen102,text="I never thought that so many people would use Pigro.\nAs open source lives from community,I want you to have a say in that too.\nIf you click on poll, you can vote on what else I should add to Pigro.\nSo ... let's fatten up the hog! xD",font=("Helvetica",14),background='#333333', fg="white",padx=5,pady=20).pack()




rahmen101 = Frame(tab10, borderwidth=0, relief=GROOVE, highlightthickness=1)
rahmen101.pack(padx=45,pady=20)
rahmen101['background'] = '#333333'



pig_btn_1 = Button(rahmen101,text="User Poll", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white", command=poll).grid(column=0,row=0,pady=20, padx=20)

pig_btn_2 = Button(rahmen101,text="Wallpapers", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white", command=wpaps).grid(column=1,row=0,pady=20)

pig_btn_3 = Button(rahmen101,text="PiGro Manuel", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white",command=wiki).grid(column=2,row=0,pady=20, padx=20)



###########################################################Games

################################################################
tab_control.pack(expand=1, fill='both')

main.mainloop()

