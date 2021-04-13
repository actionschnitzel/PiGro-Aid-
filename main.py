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

##################################################MAIN


main = Tk()
main.title("PiGro Xtrmo - Just Click It")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#404552'
main.resizable(0, 0)
main.geometry("750x550")
main.wait_visibility(main)
main.wm_attributes('-alpha', 0.9)

###########################################TABCONT


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


# Notebook Style
noteStyler = ttk.Style()
noteStyler.configure("TNotebook", borderwidth=2, background="#383c4a")
noteStyler.configure("TNotebook.Tab", tabforeground="red", borderwidth=0, background="#383c4a", foreground="white", font="bold")
noteStyler.configure("TFrame", background="#383c4a")


########################
tab_tp1 = Image.open('icons/Logotab.png')
tp01 = ImageTk.PhotoImage(tab_tp1)
tl01 = Label(image=tp01)

tab_tp12 = Image.open('icons/updatetab.png')
tp012 = ImageTk.PhotoImage(tab_tp12)
tl012 = Label(image=tp012)

tab_tp2 = Image.open('icons/bum.png')
tp02 = ImageTk.PhotoImage(tab_tp2)
tl02 = Label(image=tp02)

tab_tp3 = Image.open('icons/mate-panel-window-menu.png')
tp03 = ImageTk.PhotoImage(tab_tp3)
tl03 = Label(image=tp03)

tab_tp4 = Image.open('icons/com.github.cassidyjames.palette.png')
tp04 = ImageTk.PhotoImage(tab_tp4)
tl04 = Label(image=tp04)

tab_tp6 = Image.open('icons/tuning.png')
tp06 = ImageTk.PhotoImage(tab_tp6)
tl06 = Label(image=tp06)

tab_tp7 = Image.open('icons/org.gnome.OfficeRunner.png')
tp07 = ImageTk.PhotoImage(tab_tp7)
tl07 = Label(image=tp07)

tab_tp8 = Image.open('icons/org.gnome.OfficeRunner.png')
tp08 = ImageTk.PhotoImage(tab_tp8)
tl08 = Label(image=tp07)

sys_bp9 = Image.open('icons/iconfinder_linux_tux_337128.png')
bp09 = ImageTk.PhotoImage(sys_bp9)
bl09 = Label(image=bp09)

########################################
tab_control.add(tab1, compound=LEFT, text='Start', image=tp01)
tab_control.add(tab11, compound=LEFT, text='Updater', image=tp012)
tab_control.add(tab2, compound=LEFT, text='System', image=tp02)
tab_control.add(tab3, compound=LEFT, text='Installer', image=tp03)
tab_control.add(tab4, compound=LEFT, text='Look', image=tp04)
tab_control.add(tab6, compound=LEFT, text='Tuning', image=tp06)
tab_control.add(tab8, compound=LEFT, text='Distros', image=bp09)
tab_control.add(tab7, compound=LEFT, text='Info', image=tp07)



################################################DEF/BUTTONZ

def changelog():
    popen("python3 updateinfo.py")


def upDater_button():
    popen("python3 updater.py")


def pi_configbutton():
    popen("lxterminal -e 'bash -c \"sudo raspi-config; exec bash\"'")


def pi_configbutton2():
    popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")


def lxap_button():
    popen("sudo lxappearance")


def kiss_button():
    popen("lxterminal -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'")


def compiz_button():
    popen("lxterminal -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")


def contxt_button():
    popen("lxterminal -e 'bash -c \"sudo nano /boot/config.txt; exec bash\"'")


def neofetch_button():
    popen("lxterminal -e 'bash -c \"neofetch; exec bash\"'")


def tasksel_button():
    popen("lxterminal -e 'bash -c \"sudo tasksel; exec bash\"'")


def arc_inst():
    popen("lxterminal -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")


def breeze_inst():
    popen("lxterminal -e 'bash -c \"sudo apt-get install breeze-cursor-theme; exec bash\"'")


def papi_inst():
    popen("lxterminal -e 'bash -c \"sudo apt-get install papirus-icon-theme; exec bash\"'")


def gparted_inst():
    popen("lxterminal -e 'bash -c \"sudo apt-get install gparted; exec bash\"'")


def gparted_exec():
    popen("sudo gparted")


def xfcefix():
    popen(
        "lxterminal -e 'bash -c \"sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'")


def xfcefix2():
    popen("lxterminal -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'")


def actionhome():
    popen("chromium-browser https://www.actionschnitzel.de/PiGro/")


def ch_desk():
    popen("lxterminal -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")


def w_app():
    popen("lxterminal -e 'bash -c \"sudo snap install kesty-whatsapp; exec bash\"'")


def onc_ben():
    popen("lxterminal -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/fmsudo.sh; exec bash\"'")


def inst_bleach():
    popen("lxterminal -e 'bash -c \"sudo apt-get install bleachbit ; exec bash\"'")


def m_alien():
    popen("chromium-browser https://github.com/actionschnitzel/Matemorph")


def button_lk():
    popen("lxterminal -e 'bash -c \"sudo BRANCH=next rpi-update; exec bash\"'")


def inst_ima():
    popen("lxterminal -e 'bash -c \"sudo apt install rpi-imager; exec bash\"'")


def inst_neo():
    popen("lxterminal -e 'bash -c \"sudo apt-get install neofetch; exec bash\"'")


def changelog():
    popen("chromium-browser https://github.com/actionschnitzel/PiGro-Aid-")


def button_dpfc():
    popen("lxterminal -e 'bash -c \"deskpi-config; exec bash\"'")


def button_xf4s():
    popen("xfwm4-settings")


def button_xfwm():
    popen("lxterminal -e 'bash -c \"sudo update-alternatives --config x-window-manager; exec bash\"'")


def button_boot():
    popen("lxterminal -e 'bash -c \"dmesg; exec bash\"'")

def btswitch_64():
    popen("lxterminal -e 'bash -c \"sudo apt-get install -y raspbian-nspawn-64; exec bash\"'")
    
def z_ram():
    popen("lxterminal -e 'bash -c \"sudo apt-get install zram-tools; exec bash\"'")
    
def rm_vsc():
    popen("lxterminal -e 'bash -c \"sudo rm /etc/apt/sources.list.d/vscode.list & echo DONE!; exec bash\"'")

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


#############################################TAB1


#################LOGO
i = Image.open('icons/pigrox.png')
p = ImageTk.PhotoImage(i)
l = Label(tab1, image=p)
l.image = p
l['background'] = '#383c4a'
l.place(x=30, y=10)

iac = Image.open('icons/Schwarzenschnitzel.png')
pac = ImageTk.PhotoImage(iac)
lac = Label(tab1, image=pac)
lac.image = p
lac['background'] = '#383c4a'
lac.place(x=575, y=280)



aclabel=Label(tab1,text="Hey man, I'm Actionschnitzel!\nI'll be your guide.\nSo what's new?!\n1. ToolTips\n2. Nothin'",font=("Arial", 8), bg="white",).place(x=590, y=300)


tab1.counter = 0


def clicked():
    tab1.counter += 1
    L['text'] = str(tab1.counter)


L = Label(tab1, text="", font="50", background='#404552', fg="white")
L.place(y=495, anchor=W)

###############StartClick
i9 = Image.open('icons/click.png')
p9 = ImageTk.PhotoImage(i9)
l9 = Label(image=p9)



clc_btn0 = Button(tab1, image=p9, borderwidth=0, command=clicked)
clc_btn0.place(x=225, y=220)



Chl = Button(tab1, text="Change Log", width=10, highlightthickness=0, borderwidth=0, background='#404552',
             foreground="white", command=changelog).place(x=50, y=480)


############################################################################################################tab11######updater

rahmen11 = Frame(tab11, borderwidth=2, relief=GROOVE)
rahmen11.pack(padx=10, pady=20, anchor=NW)
rahmen11['background'] = '#404552'



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


lac_ttp = CreateToolTip(lac, \
                                   "Ok, Ok ... I'll admit that the updates always come after I've seen the latest leepsp video. I have no own ideas xD. And yes ... I'm just too lazy to port PiGro to Ubuntu, because it's an ass full of work. And BTW the Click! button is a real button. R U brave enough?")

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))


def button_action():
    os.system('xterm -into %d -bg SteelBlue4 -geometry 120x25 -e ~/PiGro-Aid-/scripts/update.sh &' % wid);


def button_action2():
    os.system('xterm -into %d -bg SteelBlue4 -geometry 120x25 -e ~/PiGro-Aid-/scripts/upgrade.sh &' % wid)


def button_action16():
    os.system('xterm -into %d -bg SteelBlue4 -geometry 120x25 -e ~/PiGro-Aid-/scripts/autoremove.sh &' % wid)


def button_action17():
    os.system('xterm -into %d -bg SteelBlue4 -geometry 120x25 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &' % wid)


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

termf = Frame(tab11, height=270, width=680, padx=10)
wid = termf.winfo_id()
# os.system('xterm -into %d -bg SteelBlue4 -geometry 120x100  &' % wid)
termf['background'] = '#383c4a'

s_list = Text(rahmen11, width=100, height=5)
text_file = open("/etc/apt/sources.list", 'r')
stuff = text_file.read()
s_list.insert(END, stuff)
text_file.close()
s_list.pack(anchor='w')

shadowcolor = "yellow"


# yyyy
rahmen112 = Frame(tab11, borderwidth=2, relief=GROOVE)
rahmen112.pack(padx=10, pady=5, anchor=W)
rahmen112['background'] = '#404552'

update_button = Button(rahmen112, text="Update", width=15, anchor='w', command=button_action, highlightthickness=0,
                       borderwidth=0, background='#404552', foreground="white")
update_button.grid(column=0, row=0)

upgrade_button = Button(rahmen112, text="Upgrade", width=15, anchor='w', command=button_action2, highlightthickness=0,
                        borderwidth=0, background='#404552', foreground="white")
upgrade_button.grid(column=0, row=1)

auth_button = Button(rahmen112, text="Allow Sources", width=15, anchor='w', command=button_action17,
                     highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
auth_button.grid(column=1, row=0)

rm_button = Button(rahmen112, text="Remove Config Files", width=15, anchor='w', command=button_action16,
                   highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
rm_button.grid(column=1, row=1)

gpk_button = Button(rahmen112, text="GPK UpdateViewer", width=15, anchor='w', command=button_gpk,
                    highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
gpk_button.grid(column=0, row=2)

sv_button = Button(rahmen112, text="Save Source List", width=15, anchor='w', command=save_list, highlightthickness=0,
                   borderwidth=0, background='#404552', foreground="red")
sv_button.grid(column=1, row=2)

hiddn_button = Button(tab11, width=15, anchor='w', borderwidth=0)
# hiddn_button.place(x=730, y=280)
hiddn_button_ttp = CreateToolTip(hiddn_button, \
                                 "oh my fucking god, you found the hidden button !!!! I don't give a fuck about spelling, okay? This tool was created in 6 weeks of corona quarantine and quite honestly I think it's really cool. if it wasn't open source, I'd be a fucking millionaire now .... fuuuuuuuuuuuuuuuuuuuu. love you for using my tool: - * C YA")

iu = Image.open('icons/aptdaemon-upgrade.png')
pu = ImageTk.PhotoImage(iu)
lu = Label(tab11, image=pu)
lu.image=pu
lu['background'] = '#383c4a'
lu.place(x=420, y=120)

termf.pack()




#####################################################INSTALLER Tab3###############################


rahmen3 = Frame(tab3, borderwidth=2, relief=GROOVE, padx=42, pady=20)
rahmen3.pack(pady=20,anchor=N)
rahmen3['background'] = '#404552'


#########inst tab2
def inst_btn1():
    entry_text = eingabefeld1.get()
    if (entry_text == ""):
        welcome_label.config(text="Name of the App?")
    else:
        entry_text = "sudo apt-get install " + entry_text

        f = open("buttoninst.sh", "w+")
        for i in range(1):
            f.write(entry_text)
        popen(
            "lxterminal -e 'bash -c \"sudo chmod +x ~/PiGro-Aid-/buttoninst.sh && ~/PiGro-Aid-/buttoninst.sh ; exec bash\"'")

def uninst_btn1():
        popen("sudo synaptic")
        
def inst_syn():
        popen("lxterminal -e 'bash -c \"sudo apt-get install synaptic; exec bash\"'")

    
i4 = Image.open('icons/apt-get.png')
p4 = ImageTk.PhotoImage(i4)
l4 = Label(image=p4)

welcome_label1 = Label(rahmen3)
eingabefeld1 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button1 = Button(rahmen3, text="install", command=inst_btn1, highlightthickness=0, borderwidth=0,
                        background='#404552', foreground="white")
welcom_button1_ttp = CreateToolTip(welcom_button1, \
                                   'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.')

uninst_button = Button(rahmen3, text="Synaptic/Uninstaller", command=uninst_btn1, highlightthickness=0, borderwidth=1,background='#404552', foreground="white")
uninst_button_ttp = CreateToolTip(uninst_button, \
                                  'If nothing happens you must install Synaptic')

my_label = Label(rahmen3, image=p4, fg="white")
my_label['background'] = '#404552'
my_label.grid(column=0, row=0, pady=10)
eingabefeld1.grid(column=2, row=0)
welcom_button1.grid(column=1, row=0)
uninst_button.grid(column=2, row=2)


######DEFZ####inst2###


def inst_btn2():
    entry_text = eingabefeld2.get()
    if (entry_text == ""):
        welcome_label2.config(text="Name of the App?")
    else:
        entry_text = "sudo snap install " + entry_text

        f = open("buttoninst.sh", "w+")
        for i in range(1):
            f.write(entry_text)
        popen(
            "lxterminal -e 'bash -c \"sudo chmod +x ~/PiGro-Aid-/buttoninst.sh && ~/PiGro-Aid-/buttoninst.sh ; exec bash\"'")


i6 = Image.open('icons/snap.png')
p6 = ImageTk.PhotoImage(i6)
l6 = Label(image=p6)

my_label2 = Label(rahmen3, image=p6, text="Snap install", fg="white")
my_label2['background'] = '#404552'

welcome_label2 = Label(rahmen3)
eingabefeld2 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button2 = Button(rahmen3, text="install", command=inst_btn2, highlightthickness=0, borderwidth=0,
                        background='#404552', foreground="white")
welcom_button2_ttp = CreateToolTip(welcom_button2, \
                                   '*to use snap install, you must\napt-get install snapd xD lol')

my_label2.grid(column=0, row=1)
eingabefeld2.grid(column=2, row=1)
welcom_button2.grid(column=1, row=1)

###################sugga Tab3


rahmen31 = Frame(tab3, borderwidth=2, relief=GROOVE)
rahmen31.pack(padx=40, pady=20)
rahmen31['background'] = '#404552'

tab_ip3 = Image.open('icons/mintsources-additional.png')
ip03 = ImageTk.PhotoImage(tab_ip3)
il03 = Label(image=ip03)
##xx
sys_btn6 = Button(rahmen31, width=110, image=ip03, text="Whatsapp", anchor="w", command=w_app, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn6.grid(column=0, row=0)
sys_btn6_ttp = CreateToolTip(sys_btn6, \
                                  'This is a SNAP')


sys_btn2 = Button(rahmen31, width=110, image=ip03, text="Compiz", anchor="w", command=compiz_button,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn2.grid(column=0, row=1)

sys_btn3 = Button(rahmen31, width=110, image=ip03, text="Gparted", anchor="w", command=gparted_inst,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn3.grid(column=1, row=0)

sys_btn4 = Button(rahmen31, width=110, image=ip03, text="NeoFetch", anchor="w", command=inst_neo, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn4.grid(column=1, row=1)

sys_btn5 = Button(rahmen31, width=110, image=ip03, text="PiKiss", anchor="w", command=kiss_button, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn5.grid(column=2, row=0)

sys_btn5 = Button(rahmen31, width=110, image=ip03, text="Bleach Bit", anchor="w", command=inst_bleach,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn5.grid(column=2, row=1)

sys_btn5 = Button(rahmen31, width=110, image=ip03, text="Pi Imager", anchor="w", command=inst_ima, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn5.grid(column=3, row=0)

sys_btn6 = Button(rahmen31, width=110, image=ip03, text="Synaptic", anchor="w", command=inst_syn, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn6.grid(column=3, row=1)



ix2 = Image.open('icons/shop.png')
px2 = ImageTk.PhotoImage(ix2)
lx2 = Label(tab3, image=px2)
lx2.image = px2
lx2['background'] = '#383c4a'
lx2.place(x=270, y=330)

###########################################System####################tab2#######################################


i1 = Image.open('icons/pigropiup.png')
p1 = ImageTk.PhotoImage(i1)
l1 = Label(image=p1)

####################
# icons
sys_bp1 = Image.open('icons/raspberry-pi-logo.png')
bp01 = ImageTk.PhotoImage(sys_bp1)
bl01 = Label(image=bp01)

sys_bp2 = Image.open('icons/raspberry-pi-logo.png')
bp02 = ImageTk.PhotoImage(sys_bp2)
bl02 = Label(image=bp02)

sys_bp3 = Image.open('icons/byobu.png')
bp03 = ImageTk.PhotoImage(sys_bp3)
bl03 = Label(image=bp03)

sys_bp4 = Image.open('icons/gparted.png')
bp04 = ImageTk.PhotoImage(sys_bp4)
bl04 = Label(image=bp04)

sys_bp5 = Image.open('icons/indicator-cpufreq.png')
bp05 = ImageTk.PhotoImage(sys_bp5)
bl05 = Label(image=bp05)

sys_bp6 = Image.open('icons/folder-cyan.png')
bp06 = ImageTk.PhotoImage(sys_bp6)
bl06 = Label(image=bp06)

sys_bp7 = Image.open('icons/iconfinder_linux_tux_337128.png')
bp07 = ImageTk.PhotoImage(sys_bp7)
bl07 = Label(image=bp07)

#########################################FRAMETAB2
#########################################
rahmen2 = Frame(tab2, borderwidth=2, relief=GROOVE, padx=10)
rahmen2.pack(padx=10, pady=20, anchor=N)
rahmen2['background'] = '#404552'

###
sys_btn6 = Button(rahmen2, width=150, image=bp01, text="Raspi-Config", anchor="w", command=pi_configbutton,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn6.grid(column=0, row=0)

sys_btn1 = Button(rahmen2, width=150, image=bp01, text="Raspi-Config GUI", anchor="w", command=pi_configbutton2,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn1.grid(column=0, row=1)

sys_btn2 = Button(rahmen2, width=150, image=bp03, text="Nano Config.txt", anchor="w", command=contxt_button,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn2.grid(column=0, row=2)

sys_btnvs = Button(rahmen2, width=150, image=bp03, text="rm vscode.list ", anchor="w", command=rm_vsc,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="red", compound=LEFT)
sys_btnvs.grid(column=0, row=3)

sys_btn3 = Button(rahmen2, width=150, image=bp04, text="Gparted", anchor="w", command=gparted_exec,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn3.grid(column=1, row=0)

sys_btn4 = Button(rahmen2, width=150, image=bp05, text="NeoFetch", anchor="w", command=neofetch_button,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn4.grid(column=1, row=1)

sys_btn5 = Button(rahmen2, width=150, image=bp06, text="FM God Mode", anchor="w", command=onc_ben, highlightthickness=0,
                  borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn5.grid(column=1, row=2)

sys_btn5_ttp = CreateToolTip(sys_btn5, \
                                   "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)")


sys_btn6 = Button(rahmen2, width=180, image=bp07, text="Update Linux Kernel", anchor="w", command=button_lk,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn6.grid(column=2, row=0)

sys_btn7 = Button(rahmen2, width=180, image=bp03, text="Deskpi Pro Fan Control", anchor="w", command=button_dpfc,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn7.grid(column=2, row=1)

sys_btn8 = Button(rahmen2, width=180, image=bp03, text="Boot Log", anchor="w", command=button_boot,
                  highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT)
sys_btn8.grid(column=2, row=2)





rahmen21 = Frame(tab2, borderwidth=2, relief=GROOVE,pady=20, padx=70)
rahmen21.pack(padx=10, pady=20)
rahmen21['background'] = '#404552'


pid = os.getpid()
ps = psutil.Process(pid)
my_system = platform.uname()
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()

# Disk Information
#print("="*40, "Disk Information", "="*40)
#print("Partitions and Usage:")
# get all disk partitions
#partitions = psutil.disk_partitions()
#for partition in partitions:
    #print(f"=== Device: {partition.device} ===")
    #print(f"  Mountpoint: {partition.mountpoint}")
    #print(f"  File system type: {partition.fstype}")
    #try:
      #  partition_usage = psutil.disk_usage(partition.mountpoint)
   # except PermissionError:
        # this can be catched due to the disk that
        # isn't ready
        #continue
   ##print(f"  Used: {get_size(partition_usage.used)}")
    #print(f"  Free: {get_size(partition_usage.free)}")
    #print(f"  Percentage: {partition_usage.percent}%")
# get IO statistics since boot
#disk_io = psutil.disk_io_counters()
#print(f"Total read: {get_size(disk_io.read_bytes)}")
#print(f"Total write: {get_size(disk_io.write_bytes)}")

    

sysinf0 = Label(rahmen21, text="System Info", compound=LEFT, anchor=W, font=20, highlightthickness=0, borderwidth=0,
                background='#404552', foreground="white", width=20)
sysinf0.grid(column=0, row=0)
sysinf0 = Label(rahmen21, text="", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#404552', foreground="white", width=20)
sysinf0.grid(column=0, row=1)
sysinf0 = Label(rahmen21, text=f"System: {my_system.system}", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#404552', foreground="white", width=20)
sysinf0.grid(column=0, row=2)
sysinf1 = Label(rahmen21, text=f"Node Name: {my_system.node}", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf1.grid(column=0, row=3)
sysinf2 = Label(rahmen21, text=f"Kernel: {my_system.release}", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf2.grid(column=0, row=4)
sysinf3 = Label(rahmen21, text=f"Machine: {my_system.machine}", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf3.grid(column=0, row=5)
sysinf3 = Label(rahmen21, text="", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf3.grid(column=0, row=6)
sysinf3 = Label(rahmen21, text=f"RAM Total: {get_size(svmem.total)}", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf3.grid(column=0, row=7)
sysinf3 = Label(rahmen21, text=f"SWAP Total: {get_size(swap.total)}", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=20)
sysinf3.grid(column=0, row=8)






sysinf6 = Label(rahmen21, text=f"CPU Max Freq: {cpufreq.max:.2f}Mhz", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=25)
sysinf6.grid(column=1, row=2)
sysinf7 = Label(rahmen21, text=f"CPU Min Freq: {cpufreq.min:.2f}Mhz", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=25)
sysinf7.grid(column=1, row=3)
sysinf8 = Label(rahmen21, text=f"Current CPU Freq: {cpufreq.current:.2f}Mhz", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=25)
sysinf8.grid(column=1, row=4)
sysinf8 = Label(rahmen21, text="", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=25)
sysinf8.grid(column=1, row=5)
sysinf8 = Label(rahmen21, text="", compound=LEFT, anchor=W, background='#404552',
                foreground="white", width=25)
sysinf8.grid(column=1, row=6)
#sysinf8 = Label(rahmen21, text=f"Disk Size: {get_size(partition_usage.total)}", compound=LEFT, anchor=W, background='#404552',
               # foreground="white", width=25)
#sysinf8.grid(column=1, row=7)
#sysinf8 = Label(rahmen21, text=f"Disk Used: {get_size(partition_usage.used)}", compound=LEFT, anchor=W, background='#404552',
                #foreground="white", width=25)
#sysinf8.grid(column=1, row=8)


##########################################LOOK

# xx
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


tab_ip1 = Image.open('icons/mintsources-additional.png')
ip01 = ImageTk.PhotoImage(tab_ip1)
il01 = Label(image=ip01)

tab_ip2 = Image.open('icons/deepin-repair-tools.png')
ip02 = ImageTk.PhotoImage(tab_ip2)
il02 = Label(image=ip02)

rahmen4 = Frame(tab4, borderwidth=2, relief=GROOVE, pady=10, padx=17)
rahmen4.pack(pady=20, anchor=N)
rahmen4['background'] = '#404552'

in_btn0 = Button(rahmen4, text="LXAppearace", font=120, command=lxap_button, highlightthickness=0, borderwidth=0,
                 background='#404552', foreground="white", width=15)
in_btn0.grid(column=0, row=0, padx=5, pady=5)

in_btn1 = Button(rahmen4, text="Tasksel", command=tasksel_button, font=120, highlightthickness=0, borderwidth=0,
                 background='#404552', foreground="white", width=15)
in_btn1.grid(column=1, row=0, padx=5)

in_btn2 = Button(rahmen4, text="Change Desktop", command=ch_desk, font=120, highlightthickness=0, borderwidth=0,
                 background='#404552', foreground="white", width=15)
in_btn2.grid(column=2, row=0, padx=5)

in_btn3 = Button(rahmen4, text="Xfwm4 Settings", command=button_xf4s, font=120, highlightthickness=0, borderwidth=0,
                 background='#404552', foreground="white", width=15)
in_btn3.grid(column=0, row=1, padx=5)

in_btn3 = Button(rahmen4, text="Change Win-Manager", command=button_xfwm, font=120, highlightthickness=0, borderwidth=0,
                 background='#404552', foreground="white", width=15)
in_btn3.grid(column=2, row=1, padx=5)

in_lab1 = Label(rahmen4, text="", font=120, highlightthickness=0, borderwidth=0, background='#404552',
                foreground="white", width=15)
in_lab1.grid(column=1, row=1, padx=5)



rahmen41 = Frame(tab4, borderwidth=2, relief=GROOVE,pady=20,padx=10)
rahmen41.pack(padx=10,pady=20)
rahmen41['background'] = '#404552'

Sugg2 = Label(rahmen41, text="Suggestions", font=20, background='#404552', foreground="white")
Sugg2.grid(column=0, row=0)

Sugg2 = Label(rahmen41, text="", font=20, background='#404552', foreground="white")
Sugg2.grid(column=0, row=1)

in_btn3 = Button(rahmen41, text="Install Arc Theme", image=ip01, compound=LEFT, anchor="w", width=220, command=arc_inst,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
in_btn3.grid(column=0, row=2)

in_btn4 = Button(rahmen41, text="Install Breeze Cursor Theme", image=ip01, compound=LEFT, anchor="w", width=220,
                 command=breeze_inst, highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
in_btn4.grid(column=0, row=3)

in_btn5 = Button(rahmen41, text="Install Papirus Icon Theme", image=ip01, compound=LEFT, anchor="w", width=220,
                 command=papi_inst, highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
in_btn5.grid(column=0, row=4)

xfce = Label(rahmen41, text="Xfce Tweaks", font=20, background='#404552', foreground="white", anchor="w")
xfce.grid(column=2, row=0)

xfce = Label(rahmen41, text="", font=20, background='#404552', foreground="white", anchor="w")
xfce.grid(column=2, row=1)

in_btn5 = Button(rahmen41, text="Post-Install WiFi Fix", image=ip02, compound=LEFT, anchor="w", width=220,
                 command=xfcefix2, highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
in_btn5.grid(column=2, row=2)

in_btn5 = Button(rahmen41, text="Post-Install Bluetooth Fix", image=ip02, compound=LEFT, anchor="w", width=220,
                 command=xfcefix, highlightthickness=0, borderwidth=0, background='#404552', foreground="white")
in_btn5.grid(column=2, row=3)

tip1 = Label(rahmen41,
             text="*I recommend Xfce. Gnome & KDE\nrun terribly as a desktop\n even with Overclock.",
             background='#404552', foreground="white")
tip1.config(font=('Arial', 7))
tip1.grid(column=2, row=5)

loklik = Label(rahmen41, compound=LEFT, text="\nMore:", background='#404552', foreground="white")
loklik.grid(column=2, row=6)

ll = tk.Label(rahmen41, text=r"https://www.pling.com/s/XFCE/browse", fg="blue", cursor="hand2")
ll.grid(column=2, row=7)
ll.bind("<Button-1>", callback)
ll['background'] = '#404552'

space = Label(rahmen41, compound=LEFT, background='#404552', foreground="white",
              text="                ")  # if you see this... yes this is not professional but is 0.44 A.M and I want to release this tomorrow xD
space.grid(column=1, row=6)


######################################TOUCH


############################################Tuning





tu_tp1 = Image.open('icons/PiGroOV2.png')
tu01 = ImageTk.PhotoImage(tu_tp1)
tul01 = Label(image=tu01)

tu_tp2 = Image.open('icons/PiGroOV.png')
tu02 = ImageTk.PhotoImage(tu_tp2)
tul02 = Label(image=tu02)


def ov_2000():
    popen("lxterminal -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/ov_1.sh; exec bash\"'")


def ov_2147():
    popen("lxterminal -e 'bash -c \"/home/pi/PiGro-Aid-/scripts/ov_2.sh; exec bash\"'")


rahmen6 = Frame(tab6, borderwidth=2, relief=GROOVE, padx=50, pady=20)
rahmen6.pack(padx=10, pady=20, anchor=N)
rahmen6['background'] = '#404552'

rahmen61 = Frame(tab6, borderwidth=2, relief=GROOVE, padx=10, pady=10)#
rahmen61.pack(padx=70,side=LEFT)
rahmen61['background'] = '#404552'

rahmen62 = Frame(tab6, borderwidth=2, relief=GROOVE, padx=10, pady=10)#
rahmen62.pack(padx=10, side=LEFT)
rahmen62['background'] = '#404552'

tu_lb1 = Label(rahmen6, text="Crank It Up", font='20', highlightthickness=0, borderwidth=2, background='#404552',
               foreground="white").grid(column=0, row=0)

tu_btn1 = Button(rahmen6, image=tu01, text="Arm_Freq = 2000\nGpu_Freq = 750\nOver_Voltage = 6", anchor="w", command=ov_2000,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=2)



tu_lb2 = Label(rahmen6, text="Take It To The Max", font='20', highlightthickness=0, borderwidth=2,
               background='#404552', foreground="white").grid(column=1, row=0)


tu_btn2 = Button(rahmen6, image=tu02, text="Arm_Freq = 2147\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2147,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=1, row=2)




tu_zb1 = Label(rahmen61, text="ZRAM", font='20', highlightthickness=0, borderwidth=2, background='#404552',foreground="white").grid(column=0, row=0)

tu_zbtn = Button(rahmen61, text="Install Zram\n\nCommands:\nswapon -s\nservice zramswap stop\nservice zramswap start\n ", anchor="w", command=z_ram,highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=1)
################


tu_bb1=Label(rahmen62, text="64 Bit Mode", font='20', highlightthickness=0, borderwidth=2, background='#404552',foreground="white").grid(column=0, row=0)

tu_bbtn=Button(rahmen62, text="Install 64 Bit Mode\n\nHow To:\nActivate via Menu\nor\n Type:ds64-shell\nThen install what ever you want", anchor="w", command=btswitch_64,highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=1)


#####################################Distros
def down_twist():
    popen("chromium-browser https://twisteros.com/")
    
def down_puppy():
    popen("chromium-browser https://puppylinux.com/")
    
def down_diet():
    popen("chromium-browser https://dietpi.com/")
    
def down_mx():
    popen("chromium-browser https://mxlinux.org/blog/fluxbox-raspberrypi-respin-ragout-beta/")

def down_fy():
    popen("chromium-browser https://releases.fydeos.io/11.4/rpi4-fydeos")

def down_kk():
    popen("chromium-browser https://konstakang.com/devices/rpi4/")
    
def down_bb():
    popen("chromium-browser https://berryboot.alexgoldcheidt.com/images")

#def webvew():
    #popen("chromium-browser https://pypi.org/project/pywebview/")




rahmen81 = Frame(tab8, borderwidth=2, relief=GROOVE)
rahmen81.pack(padx=60, pady=100, anchor=NW)
rahmen81['background'] = '#404552'

rahmen82 = Frame(tab8, borderwidth=2, relief=GROOVE)
rahmen82.pack(padx=70, pady=20, anchor=NW)
rahmen82['background'] = '#404552'

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

tab8_dist7 = Image.open('icons/logo_berryserver_website_2020_125x125_opt.png')
di07 = ImageTk.PhotoImage(tab8_dist7)
dl07 = Label(image=di07)



dist_btn1 = Button(rahmen81, compound=LEFT, image=di01, text="Get: Twister OS", anchor="w", command=down_twist,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white",width=180).grid(column=0, row=0)

dist_btn2 = Button(rahmen81,compound=LEFT, image=di02, text="Get: Puppy Linux", anchor="w", command=down_puppy,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white",width=180).grid(column=1, row=0)

dist_btn3 = Button(rahmen81, image=di03, text="Get: DietPi", anchor="w", command=down_diet,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT,width=180).grid(column=3, row=0)

dist_btn4 = Button(rahmen81, image=di04, text="Get: MX Linux", anchor="w", command=down_mx,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT,width=180).grid(column=0, row=1)

dist_btn5 = Button(rahmen81, image=di05, text="Get: FydeOS", anchor="w", command=down_fy,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT,width=180).grid(column=1, row=1)

dist_btn6 = Button(rahmen81, image=di06, text="Get: Android", anchor="w", command=down_kk,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT,width=180).grid(column=3, row=1)

dist_btn7 = Button(rahmen81, image=di07, text="Berryserver", anchor="w", command=down_bb,
                 highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT,width=180).grid(column=1, row=2)
##################

#other_btn1 = Button(rahmen82, text="Program start on boot", anchor="w", command=ov_2147,
                 #highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=0)

#other_btn2 = Button(rahmen82, text="Make a Webapp with Python", anchor="w", command=webvew,
                 #highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=1)

#other_btn2 = Button(rahmen82, text="Get: Twister OS", anchor="w", command=ov_2147,
                 #highlightthickness=0, borderwidth=0, background='#404552', foreground="white", compound=LEFT).grid(column=0, row=2)

#####################################INFO


def callback(event):
    webbrowser.open_new(event.widget.cget("text"))


def callback2(event):
    lxterminal.open_new(event.widget.cget("entry_text"))


author = tk.Label(tab7, text="Author: Timo Westphal\nDate: MARCH. 2021\nVersion: 4.3.0", foreground="white",font=20,compound=LEFT)
author.pack(pady=10)
al = tk.Label(tab7, text=r"https://www.actionschnitzel.de/PiGro/", fg="red", cursor="hand2")
al.pack()
al.bind("<Button-1>", callback)
author['background'] = '#383c4a'
al['background'] = '#383c4a'

don_txt1= StringVar()
don_txt1.set("XMR/Monero: 45rGHE93ExgQwiAEvujSTMW4WvFn8RNRPE8ugEV898JMgx7Ti72KUDGbZbCHf9rD29TVzJMYPnq2f1D3ccSqE3KN2mnv91f")

don_txt2= StringVar()
don_txt2.set("BTC/Bitcoin: 1HTzo4dBMQRbwrxuM5T2stJ5XLNTnCRFhC")

supp=Label(tab7,text="If you want to support my project:", foreground="white", background='#383c4a')
supp.pack(pady=20)

donate_ent1= Entry(tab7,font=("Helvetica",7), borderwidth=0, state="readonly", textvariable = don_txt1,width=120 )
donate_ent1.pack()

#donate_ent2= Entry(tab7,font=("Helvetica",7), borderwidth=0, state="readonly", textvariable = don_txt2,width=120 )
#donate_ent2.pack()



gws = Label(tab7, text="Good Websites", foreground="white", font=20)
gws.pack(pady=20)
gws['background'] = '#383c4a'



######ALL LINKS###########

lbl = tk.Label(tab7, text=r"https://www.raspberrypi.org", fg="blue", cursor="hand2")
lbl.pack()
lbl.bind("<Button-1>", callback)
lbl['background'] = '#383c4a'

lbl0 = tk.Label(tab7, text=r"https://twisteros.com", fg="blue", cursor="hand2")
lbl0.pack()
lbl0.bind("<Button-1>", callback)
lbl0['background'] = '#383c4a'

lbl1 = tk.Label(tab7, text=r"https://berryboot.alexgoldcheidt.com/images", fg="blue", cursor="hand2")
lbl1.pack()
lbl1.bind("<Button-1>", callback)
lbl1['background'] = '#383c4a'

lbl2 = tk.Label(tab7, text=r"https://www.lcdwiki.com/Main_Page", fg="blue", cursor="hand2")
lbl2.pack()
lbl2.bind("<Button-1>", callback)
lbl2['background'] = '#383c4a'

###########################################################
tab_control.pack(expand=1, fill='both')

main.mainloop()

