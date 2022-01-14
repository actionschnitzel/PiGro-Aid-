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



#MAIN
main = Tk()
main.title("PiGro - Colpo Diretto")
icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
main.tk.call('wm', 'iconphoto', main._w, icon)
main['background'] = '#333333'
main.resizable(0, 0)
app_width = 1000
app_height = 700
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()
x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)
main.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
main.wait_visibility(main)
main.wm_attributes('-alpha', 0.95, )



#Notebook Style
noteStyler = ttk.Style(main)
noteStyler.configure("TNotebook",borderwidth=0, background="#333333", tabposition='w',highlightthickness=0)
noteStyler.configure("TNotebook.Tab",borderwidth=0, background="#333333", foreground="white",font=("Helvetica",16),width=13,highlightthickness=0)
noteStyler.configure("TFrame", background="#333333")
noteStyler.map("TNotebook.Tab", background=[("selected", "#333333")], foreground=[("selected", "#d4244d")]);


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

#Sidebar theme
tabi = Image.open('icons/side_bar.png')
tabp = ImageTk.PhotoImage(tabi)
tabl = Label(tab_control,image=tabp)
tabl.image = tabp
tabl['background'] = '#333333'
tabl.place(x=-2, y=-1) 

tab2i = Image.open('icons/side_bar2.png')
tab2p = ImageTk.PhotoImage(tab2i)
tab2l = Label(tab_control,image=tab2p)
tab2l.image = tab2p
tab2l['background'] = '#333333'
tab2l.place(x=-2, y=630) 



#Tab_Icons
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

tab_tpu = Image.open('icons/ubuntu_logo.png')
tpU = ImageTk.PhotoImage(tab_tpu)
tlU = Label(image=tpU)

tab_tpinf = Image.open('icons/info_button.png')
tpinf = ImageTk.PhotoImage(tab_tpinf)
tlinf = Label(image=tpinf)

tab_tpinfp = Image.open('icons/info_button_p.png')
tpinfp = ImageTk.PhotoImage(tab_tpinfp)
tlinfp = Label(image=tpinfp)

tab_tpinfm = Image.open('icons/info_m.png')
tpinfm = ImageTk.PhotoImage(tab_tpinfm)
tlinfm = Label(image=tpinfm)

ico_1 = Image.open('icons/gui_icon.png')
ico_m = ImageTk.PhotoImage(ico_1)
ico_win = Label(image=ico_m)

ico_2 = Image.open('icons/weblink_icon.png')
ico_m2 = ImageTk.PhotoImage(ico_2)
ico_win2 = Label(image=ico_m2)

#Tab_contal_look
tab_control.add(tab1, compound=LEFT, text='Start', image=tp01)
tab_control.add(tab11, compound=LEFT, text='Updater', image=tp012)
tab_control.add(tab2, compound=LEFT, text='System', image=tp02)
tab_control.add(tab3, compound=LEFT, text='Installer', image=tp03)
tab_control.add(tab4, compound=LEFT, text='Look', image=tp04)
tab_control.add(tab6, compound=LEFT, text='Tuning', image=tp06)
tab_control.add(tab8, compound=LEFT, text='Links', image=bp0111)
#tab_control.add(tab9, compound=LEFT, text='Xfce', image=tp09)
tab_control.add(tab10, compound=LEFT, text='Pig-Grow', image=tp10)

#####################################TOOLTIPZs
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


#changelog popup
def changelog():
    global pop_changelog
    pop_changelog=Toplevel()
    pop_changelog.geometry("1000x1000")
    pop_changelog.title("Changelog")
    scrollbar = Scrollbar(pop_changelog)
    scrollbar.pack( side = RIGHT, fill = Y )
    s_list = Text(pop_changelog, yscrollcommand = scrollbar.set )
    text_file = open("changelog.txt")
    stuff = text_file.read()
    s_list.insert(END, stuff)
    text_file.close()
    s_list.pack(anchor='w', fill=BOTH, expand=True)
    scrollbar.config( command = mylist.yview )
    
def net_set():
    popen("nm-connection-editor")

def pi_configbutton():
    popen("xterm -e 'bash -c \"sudo raspi-config; exec bash\"'")

def pi_configbutton2():
    popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")

def pi_appear():
    popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")
    
def opbox_button():
    popen("sudo obconf")    

def lxap_button():
    popen("lxappearance")

def xfceappear_button():
    popen("xfce4-appearance-settings")

def lx_task():
    popen("lxtask")

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

def actionhome():
    popen("xdg-open https://www.actionschnitzel.de/PiGro/")
    
def snapcraft():
    popen("xdg-open https://snapcraft.io/store")

def flatflat():
    popen("xdg-open https://flathub.org/")

def xfcelook_f():
    popen("xdg-open https://www.xfce-look.org/browse/cat/")

def web_OVC():
    popen("xdg-open https://www.gnome-look.org/p/1158321/")

def ch_desk():
    popen("xterm -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")

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

def z_inst():
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
    
def pi_apps():
    popen("xterm -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'")
    
def button_auto():
    popen('xfce4-session-settings')
    
def button_xsett():
    popen('xfce4-settings-manager')
    
def xfcefix():
    popen("xterm -e 'bash -c \"sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'")

def xfcefix2():
    popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'")
    
def xfce_make():
    popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")
    
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

#help button popups
def info_update_tab():
    global pop_info_update
    pop_info_update=Toplevel()
    up_box = Text(
    pop_info_update)
    message ='''
    The first frame contains the source list. This can be edited immediately. 
    Do not worry! 
    The changes are only adopted if you press the "SAVE SOURCE LIST" button. 
    I installed this emergency brake on purpose so that 
    I don't mess around and accidentally break everything.
    Linux users should know the other buttons. They do exactly what it says.
    The GPK button is super cool, it opens the GPK update viewer, 
    which is AMAZINGLY preinstalled but is not displayed in the menu. 
    Question is .. Why ??? !!!!!
    The big gray box is xterm. it shows you what's going on right now.
    Xterm is ancient but great for embedding in programs. 
    You will come across it more often. 
    My guiding principle is "less terminal more click!" but 
    I think it's good and important to see what happens.'''


    up_box.pack(expand=True)
    up_box.insert('end', message)
    up_box.config(fill=BOTH, expand=True)


def info_installer_tab():
    global pop_info_installer
    pop_info_installer=Toplevel()
    inst_box = Text(
    pop_info_installer)
    message ='''
    Do you know RAMBO III?

    What's that? ... It's blue light. ..... What does it do? 
    ..... It turns blue.
    So, here you can install programs .....
    The special thing here is that you only have to enter the program name
    without SUDO APT-GET INSTALL BLA BAL BLA ...
    In general, the installer is designed like this:
    Without having to do a lot of tinkering and digging,
    you can quickly install a program. no extras.
    Set up quickly!
    
    To use snap and flatpaks you have to install them beforehand ;-)
    command:
    - sudo apt install snapd
    - sudo apt install flatpak 
        + flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

    If you want to know which programs are available click on: 
    / snapcraft.io / list of all pi-apps / Flathub / 
    
    
    
    '''

    inst_box.pack(expand=True)
    inst_box.insert('end', message)
    inst_box.config(fill=BOTH, expand=True)

def info_system_tab():
    global pop_info_system
    pop_info_system=Toplevel()
    sys_box = Text(
    pop_info_system)
    message ='''
    I think the buttons here are also self-explanatory. 
    There are a few things to watch out for.
    If you delete vcode.list, 
    you can no longer install vscode. which is a really cool tool. 
    Microsoft, Amazon and Google already know everything about you ;-)
    Gparted, Neofetch, Deskpi and the Xfce tools only 
    work if you have installed it. I
    'm not installing anything behind your back here.
    FM God Mode opens your file browser with sudo so be careful.
    Update Kernel makes an upgrade to the latest. 
    It can be that everything doesn't run so smoothly anymore (can be)
    System info is unfortunately not yet in real time, 
    but I'm working on it.'''

    sys_box.pack(expand=True)
    sys_box.insert('end', message)
    sys_box.config(fill=BOTH, expand=True)


def info_look_tab():
    global pop_info_look
    pop_info_look=Toplevel()
    luk_box = Text(
    pop_info_look)
    message ='''
    I love this TAB!
    Why? Because I've read thousands of articles on how to 
    change the desktop under RaspiOS. 
    The articles and forum posts were like kilometers long.
    And I compressed the whole thing into a tab. .... 
    A man's praise in his own mouth stinks. :-P
    I think everything is well structured and in an understandable way.
    I have added a guideline especially for XFCE. (Make-Me-XFCE)
    Tasksel basically does most of the work.
    The suggestions are again stuff that I use. 
    I think Twister OS does a good job when it comes to desktop themes. 
    So I don't have to try to reinvent the wheel.
    If you want to make an iOS out of vanilla raspi OS 
    you have to handle so many dependencies ... 
    that it is faster to install Twister.
    With the Look tab, I just want to fully expand your options.
    Tasksel:
    Install the desktop environment of your choice with all dependencies.

    Change Desktop:
    Switch to a specific desktop after the reboot.

    Change win manager:
    Change the window manager

    e.g gdm (Gnome), xfwm4 (XFCE)

    Xfce_look:
    Opens your webbrowser to xfce-looks.org

    Theme folder:
    Opens the theme folder as SUDO so that the new themes can be thrown in.

    Icon folder:
    Same same here

    Xfwm4 Settings:
    Quick access to the Xfce settings

    Bluetooth fix:
    If you have no bluetooth connectivity after installing Xfce

    WiFi Fix:
    If you have no Wifi connectivity after installing Xfce

    Xfce4 Appearance:
    Change the color scheme, icons etc.'''

    luk_box.pack(expand=True)
    luk_box.insert('end', message)
    luk_box.config(fill=BOTH, expand=True)

def info_tuning_tab():
    global pop_info_tuning
    pop_info_tuning=Toplevel()
    tun_box = Text(
    pop_info_tuning)
    message ='''
    I have to admit, I was lazy programming. 
    If you are using the Tuning Berrys, 
    you should check beforehand whether there is a space between 
    the equals of your previous tuning settings.

    example:
    Valid: (arm_freq = over9000)
    No Valid: (arm_freq=over9000)

    Note that over9000 is a DBZ reference ;-) Never overclock to 9000 
    ... NEVER

    Zram: This creates a compressing block device right in the computer's memory. 
    However, zRam is only used when the main memory is full: 
    the kernel first uses the entire available RAM, 
    then it tries to compress parts of it into zRam. 
    In this way, more data can be kept in memory. 
    In practice, this means that the system does not have to move to a slower 
    hard drive so quickly, 
    but the price is a slightly higher processor load.

    64 bit mode adds the 64 bit kernel to your system. 
    You can see how it works on the button ;-) 
    Important !!!!! Kernel means KERNEL not distro. 
    You will need to run a separate apt update / upgrade. 
    64 bit apps can only be installed in the 64 bit container. 
    You will also have to install a few things, 
    e.g. you have to install cmake additionally, 
    even if it is already installed under 32 bit. 
    And ..... yeeeees Box64 you have to install over the 64 container.'''

    tun_box.pack(expand=True)
    tun_box.insert('end', message)
    tun_box.config(fill=BOTH, expand=True)

#def info_holy_tab():
#    global pop_info_holy
#    pop_info_holy=Toplevel()
#    hol_box = Text(
#    pop_info_holy)
#    message ='''
#    I bought the book from the guy here -> LernLinux.tv 
#    and was so excited about it. 
#    Saw dselcet there. 
#    I've been using Linux since I was 15 years old, 
#    but "dselect" completely passed me by. 
#    The thing is: when I use timeshift, 
#    I still have all the trash on the HDD. 
#    Dselect only downloads all saved .DEBs. 
#    You get a fresh system with all the programs you love.
#    '''
#
#    hol_box.pack(expand=True)
#    hol_box.insert('end', message)
#    hol_box.config(fill=BOTH, expand=True)




#TAB_BG       
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

#Start_Tab
Chl = Button(tab1, image=tpinfp,font=(("Helvetica,bold"),"11"), highlightthickness=0, borderwidth=0, background='#cdac61',
             foreground="white", command=changelog).place(x=110, y=400)


al = tk.Label(tab1, text=r"https://www.actionschnitzel.de/PiGro/", fg="blue", cursor="hand2")
al.place(x=480, y=645)
al.bind("<Button-1>", callback)

al['background'] = '#333333'

al2 = tk.Label(tab1, text=r"https://github.com/actionschnitzel/PiGro-Aid-", fg="blue", cursor="hand2")
al2.place(x=480, y=670)
al2.bind("<Button-1>", callback)

al2['background'] = '#333333'


#Updater_Tab
rahmen11 = Frame(tab11, relief=GROOVE, borderwidth=0)
rahmen11.pack(padx=45, pady=40, anchor=W)
rahmen11['background'] = '#333333'

def send_entry_to_terminal(*args):
    """*args needed since callback may be called from no arg (button)
   or one arg (entry)
   """
    cmd("%s" % (BasicCovTests))

def update_btn():
    os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/update.sh && read -p PRESS_ENTER && exit; exec bash\"' % wid);

def upgrade_btn():
    os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/upgrade.sh && read -p PRESS_ENTER && exit; exec bash\"' % wid);

def full_upgrade_btn():
    os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/full_upgrade.sh && read -p PRESS_ENTER && exit; exec bash\"' % wid);
    
def autoremove_btn():
    os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"sudo apt autoremove -y && sudo apt clean && sudo apt-get purge -y && read -p PRESS_ENTER && exit ; exec bash\"' % wid)

def add_unsi_btn():
    os.popen("xterm -into %d -bg Grey1 -geometry 120x25 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &" % wid)
    
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




termf = Frame(tab11, height=270, width=700, padx=10, highlightthickness=2, borderwidth=0)
wid = termf.winfo_id()
termf['background'] = '#333333'

s_list = Text(rahmen11, width=1550, height=10, highlightthickness=1)
text_file = open("/etc/apt/sources.list", 'r')
stuff = text_file.read()
s_list.insert(END, stuff)
text_file.close()
s_list.pack(anchor='w')

shadowcolor = "yellow"


rahmen112 = Frame(tab11, borderwidth=0, relief=GROOVE, highlightthickness=2,padx=5,pady=5)
rahmen112.pack(padx=45, anchor='w')
rahmen112['background'] = '#333333'

update_button = Button(rahmen112, text="Update", width=15, anchor='w', command=update_btn, highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
update_button.grid(column=0, row=0)

update_button = Button(rahmen112, text="Upgrade", width=15, anchor='w', command=upgrade_btn, highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
update_button.grid(column=0, row=1)

fupgrade_button = Button(rahmen112, text="Full Upgrade", width=15, anchor='w', command=full_upgrade_btn, highlightthickness=0,
                        borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
fupgrade_button.grid(column=0, row=2)

gpk_button = Button(rahmen112, text="GPK UpdateViewer", width=15, anchor='w', command=button_gpk,
                    highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
gpk_button.grid(column=0, row=3)

auth_button = Button(rahmen112, text="Allow Sources", width=20, anchor='w', command=add_unsi_btn,
                     highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
auth_button.grid(column=1, row=0)

rm_button = Button(rahmen112, text="Remove Config Files", width=20, anchor='w', command=autoremove_btn,
                   highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
rm_button.grid(column=1, row=1)

sv_button = Button(rahmen112, text="Save Source List", width=20, anchor='w', command=save_list, highlightthickness=0,
                   borderwidth=0, background='#333333', foreground="#d4244d",font=("Helvetica",12,"bold"))
sv_button.grid(column=1, row=2)


termf.pack(padx=45,pady=20, anchor=W)

info_up_btn = Button(tab11, image=tpinfm,highlightthickness=0,
                   borderwidth=0,command=info_update_tab)
info_up_btn.place(x=650,y=320)


#INSTALLER_Tab
def w_app():
    popen("xterm -e 'bash -c \"sudo snap install kesty-whatsapp; exec bash\"'")

def compiz_button():
    popen("xterm -e 'bash -c \"sudo apt-get install compiz; exec bash\"'")

def kiss_button():
    popen("xterm -e 'bash -c \"curl -sSL https://git.io/JfAPE | bash; exec bash\"'")
    
def gnome_pie():
    popen("xterm -e 'bash -c \"sudo apt-get install gnome-pie; exec bash\"'")    
    
def pi_apps():
    popen("xterm -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'")
        
def p_lank():
    popen("xterm -e 'bash -c \"sudo apt-get install -y plank; exec bash\"'")     
    
def inst_tilix():
    popen("xterm -e 'bash -c \"sudo apt-get install -y tilix; exec bash\"'")    
    
def goodstuff():
    global pop_goodstuff
    pop_goodstuff=Toplevel()
    pop_goodstuff['background'] = '#333333'
    
    shop_btn01 = Button(pop_goodstuff, width=120, image=ip03, text="Whatsapp\n(Snap)", anchor="w", command=w_app, highlightthickness=0,borderwidth=0, background='#d4244d',foreground="white", compound=LEFT).grid(column=0, row=1)
    shop_btn1_ttp = CreateToolTip(sys_btn6, \
                                      'This is a SNAP')
    shop_lbl011 = Label(pop_goodstuff,width=60, text="... is... you know Whatsapp", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=1)

    shop_btn2 = Button(pop_goodstuff, width=120, image=ip03, text="Compiz", anchor="w", command=compiz_button,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=2)

    shop_lbl21 = Label(pop_goodstuff,width=60, text="When I was young it was cool You know it as wobbly windows", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=2)
    
    shop_btn3 = Button(pop_goodstuff, width=120, image=ip03, text="Gparted", anchor="w", command=gparted_inst,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=3)

    shop_btn31 = Label(pop_goodstuff,width=60, text="A Partition Manager", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=3)

    shop_btn4 = Button(pop_goodstuff, width=120, image=ip03, text="NeoFetch", anchor="w", command=inst_neo, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=4)

    shop_btn41 = Label(pop_goodstuff,width=60, text="Shows system specs you already know but ... uhhm...", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=4)

    shop_btn5 = Button(pop_goodstuff, width=120, image=ip03, text="PiKiss", anchor="w", command=kiss_button, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=5)

    shop_btn51 = Label(pop_goodstuff,width=60, text="Bow down!", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=5)

    shop_btn6 = Button(pop_goodstuff, width=120, image=ip03, text="Bleach Bit", anchor="w", command=inst_bleach,
                      highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=6)
    
    shop_btn61 = Label(pop_goodstuff,width=60, text="Cleans the System", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=6)

    shop_btn7 = Button(pop_goodstuff, width=120, image=ip03, text="Pi Imager", anchor="w", command=inst_ima, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=7)
    
    shop_btn71 = Label(pop_goodstuff,width=60, text="Pi-Imager on RaspiOS is like the Replicants from Stargate... o,o", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=7)
    
    shop_btn8 = Button(pop_goodstuff, width=120, image=ip03, text="Synaptic", anchor="w", command=inst_syn, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=8)
    
    shop_btn81 = Label(pop_goodstuff,width=60, text="THE Pakegemanager", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=8)

    shop_btn9 = Button(pop_goodstuff, width=120, image=ip03, text="Gnome-Pie", anchor="w", command=gnome_pie, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=9)

    shop_btn91 = Label(pop_goodstuff,width=60, compound=LEFT, text="When you tell peolpe i3 is god but you need a hidden menu cuz\nyou dont cope with it", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=1, row=9)

    shop_btn10 = Button(pop_goodstuff, width=120, image=ip03, text="Pi-Apps", anchor="w", command=pi_apps, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=10)
    
    shop_btn101 = Label(pop_goodstuff,width=60, text="DOWNLOAD IT!!!!!11", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=10)

    shop_btn18 = Button(pop_goodstuff, width=120, image=ip03, text="Plank", anchor="w", command=p_lank, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=11)

    shop_btn118 = Label(pop_goodstuff,width=60, text="It's a Dock!", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=11)     

    shop_btn20 = Button(pop_goodstuff, width=120, image=ip03, text="Tilix", anchor="w", command=inst_tilix, highlightthickness=0,
                      borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=12)

    shop_btn120 = Label(pop_goodstuff,width=60, text="Multi-Tiling-Super-Terminal-Emulator", anchor="w",
                      highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=12)


def shop():
    os.system("python3 ~/PiGro-Aid-/PDL.py")


tab_shop = Image.open('icons/shop.png')
ipshop = ImageTk.PhotoImage(tab_shop)
ilshop = Label(image=ipshop)

tab_finst = Image.open('icons/fast_install.png')
ipfinst = ImageTk.PhotoImage(tab_finst)
ilfinst = Label(image=ipfinst)

rahmen_shop = Frame(tab3,borderwidth=0, highlightthickness=1)
rahmen_shop.pack(padx=40, pady=40)
rahmen_shop['background'] = '#333333'


shop_click = Button(rahmen_shop,image=ipshop, command=shop, highlightthickness=1, borderwidth=5, background='green', foreground="white", compound=LEFT,width=500)
shop_click.pack()

rahmen3x = Frame(tab3, relief=GROOVE,borderwidth=1, highlightthickness=1,pady=10,padx=10)
rahmen3x['background'] = 'green'
rahmen3x.pack()

sysinf0 = Label(rahmen3x,image=ipfinst, compound=LEFT, anchor='n',font=("Helvetica",16), highlightthickness=0, borderwidth=0,background='green', foreground="white",pady=20)
sysinf0.pack()


rahmen3 = Frame(rahmen3x, relief=GROOVE,borderwidth=0, highlightthickness=1, padx=42, pady=20)
rahmen3.pack()
rahmen3['background'] = '#333333'


#apt-get_entry
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
eingabefeld1.insert(0,"Enter Package Name")
welcom_button1 = Button(rahmen3, text="install", command=inst_btn1, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
welcom_button1_ttp = CreateToolTip(welcom_button1, \
                                   'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.')



my_label = Label(rahmen3, image=p4, fg="white")
my_label['background'] = '#333333'
my_label.grid(column=0, row=0, )
eingabefeld1.grid(column=2, row=0)
welcom_button1.grid(column=1, row=0)



#pi-apps_entry
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
    popen("xterm -e 'bash -c \"ls ~/pi-apps/apps/ ; exec bash\"'")

ia6 = Image.open('icons/pi-app.png')
pa6 = ImageTk.PhotoImage(ia6)
la6 = Label(image=pa6)

apps_inst_btn = Label(rahmen3, image=pa6, text="piapps install", fg="white")
apps_inst_btn ['background'] = '#333333'

welcome_label2 = Label(rahmen3)
eingabefeld3 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button3 = Button(rahmen3, text="install", command=inst_pi_apps, highlightthickness=0, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))



apps_inst_btn.grid(column=0, row=3)
eingabefeld3.grid(column=2, row=3)
welcom_button3.grid(column=1, row=3)


#snap_entry
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




#flat_entry
inst4_p1=""" xterm -e 'bash -c \"sudo flatpak install flathub """
inst4_p2="""; exec bash\"' """

def inst_btn4():
    entry_text = eingabefeld4.get()
    popen(inst4_p1 + entry_text + inst4_p2)


i66 = Image.open('icons/flathub.png')
p66 = ImageTk.PhotoImage(i66)
l66 = Label(image=p66)

my_label4 = Label(rahmen3, image=p66, text="Snap install", fg="white")
my_label4['background'] = '#333333'

welcome_label4 = Label(rahmen3)
eingabefeld4 = Entry(rahmen3, bd=5, width=31, borderwidth=1)
welcom_button44 = Button(rahmen3, text="install", command=inst_btn4, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
welcom_button44_ttp = CreateToolTip(welcom_button44, \
                                   '*past without--->>>flatpak install flathub<<< org.mozilla.firefox')

my_label4.grid(column=0, row=7)
eingabefeld4.grid(column=2, row=7)
welcom_button44.grid(column=1, row=7)

frame311 = Frame(tab3, relief=GROOVE,borderwidth=0, highlightthickness=1,pady=5,padx=36,bg="green")
frame311.pack(pady=10)

snapstore_btn = Button(frame311, text="snapcraft.io", command=snapcraft, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

welcom_button33 = Button(frame311, text="list all pi-apps", command=pi_apps_list, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

uninst_button = Button(frame311, text="Synaptic", command=uninst_btn1, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
uninst_button_ttp = CreateToolTip(uninst_button, \
                                  'If nothing happens you must install Synaptic')

goodstuff_btn = Button(frame311, text="Must Haves", command=goodstuff, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

flat_btn = Button(frame311, text="Flathub", command=flatflat, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))


snapstore_btn.grid(column=0, row=6)
welcom_button33.grid(column=1, row=6)
uninst_button.grid(column=2, row=6)
goodstuff_btn.grid(column=4, row=6)
flat_btn.grid(column=3, row=6)


info_inst_btn = Button(tab3, image=tpinfm,highlightthickness=0,
                   borderwidth=0,command=info_installer_tab)
info_inst_btn.place(x=700,y=620)

#System_Tab
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


rahmen2 = Frame(tab2,borderwidth=0, highlightthickness=2, relief=GROOVE,padx=60,pady=10)
rahmen2.pack(padx=40, pady=20, fill='both')
rahmen2['background'] = '#333333'

sys_btn6 = Button(rahmen2, image=bp01, text="Raspi-Config CLI", command=pi_configbutton,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn6.grid(row=0,column=0)

sys_btn1 = Button(rahmen2, image=bp01, text="Raspi-Config GUI", command=pi_configbutton2,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn1.grid(row=0,column=1)

sys_btn2 = Button(rahmen2, image=ico_m, text="Config.txt", command=contxt_button,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn2.grid(row=0,column=2)

sys_btnvs = Button(rahmen2, image=bp03, text="rm vscode.list ", command=rm_vsc,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btnvs.grid(row=0,column=3)

sys_btn3 = Button(rahmen2, image=bp04, text="Gparted", command=gparted_exec,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn3.grid(row=1,column=0)

sys_btn4 = Button(rahmen2, image=bp05, text="NeoFetch", command=neofetch_button,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn4.grid(row=1,column=1)

sys_btn5 = Button(rahmen2, image=bp06, text="FM God Mode", command=onc_ben, highlightthickness=0,
                  borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn5.grid(row=1,column=2)
sys_btn5_ttp = CreateToolTip(sys_btn5, \
                                   "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)")

sys_btn6 = Button(rahmen2, image=bp07, text="Upgrade Linux Kernel", command=button_lk,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn6.grid(row=1,column=3)

sys_btn7 = Button(rahmen2, image=bp03, text="DeskpiPro Control", command=button_dpfc,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn7.grid(row=2,column=0)

sys_btn8 = Button(rahmen2, image=bp03, text="Boot Log", command=button_boot,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn8.grid(row=2,column=1)

sys_btn9 = Button(rahmen2, image=bp033, text="Xfce Autostarts", command=button_auto,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn9.grid(row=2,column=2)

sys_btn9 = Button(rahmen2, image=bp033, text="Xfce Settings", command=button_xsett,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn9.grid(row=2,column=3)

sys_btn10 = Button(rahmen2, image=ico_m, text="Network Settings", command=net_set,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn10.grid(row=3,column=0)

sys_btn11 = Button(rahmen2, image=ico_m, text="Taskmanager", command=lx_task,
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
sys_btn11.grid(row=3,column=1)





#Parameters for System
pid = os.getpid()
ps = psutil.Process(pid)
my_system = platform.uname()
cpufreq = psutil.cpu_freq()
svmem = psutil.virtual_memory()
swap = psutil.swap_memory()
distro = distro.id()



#status_frame
rahmen21 = Frame(tab2,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=20)
rahmen21.pack(padx=40, pady=20, fill='both')
rahmen21['background'] = '#333333'

deblogo = Image.open('icons/deb_logo.png')
dl = ImageTk.PhotoImage(deblogo)
dl01 = Label(image=dl)

deblogo2 = Image.open('icons/lmint.png')
dl2 = ImageTk.PhotoImage(deblogo2)
dl012 = Label(image=dl2)

sysinf0 = Label(rahmen21, text="System Info", compound=LEFT, anchor='n',font=("Helvetica",16), highlightthickness=0, borderwidth=0,
                background='#333333', foreground="#d4244d",pady=20)
sysinf0.grid(column=1, row=0)
sysinf0 = Label(rahmen21,image=dl, highlightthickness=0, borderwidth=0,
                background='#333333', foreground="#d4244d",pady=20,padx=20)
sysinf0.grid(column=0, row=0,rowspan=6)
sysinf0 = Label(rahmen21, text=f"System: {my_system.system}", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#333333', foreground="white", width=20,padx=10,font=("Helvetica",10,"bold"))
sysinf0.grid(column=1, row=1)
sysinfd = Label(rahmen21, text=f"Distro: {distro}", compound=LEFT, anchor=W, highlightthickness=0,
                borderwidth=0, background='#333333', foreground="white", width=20,font=("Helvetica",10,"bold"))
sysinfd.grid(column=1, row=2)
sysinf1 = Label(rahmen21, text=f"Node Name: {my_system.node}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20,font=("Helvetica",10,"bold"))
sysinf1.grid(column=1, row=3)
sysinf2 = Label(rahmen21, text=f"Kernel: {my_system.release}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20,font=("Helvetica",10,"bold"))
sysinf2.grid(column=1, row=4)
sysinf3 = Label(rahmen21, text=f"Machine: {my_system.machine}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20,font=("Helvetica",10,"bold"))
sysinf3.grid(column=1, row=5)
sysinf3 = Label(rahmen21, text="", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=20,font=("Helvetica",10,"bold"))
sysinf3.grid(column=2, row=0)
sysinf3 = Label(rahmen21, text=f"RAM Total: {get_size(svmem.total)}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25,font=("Helvetica",10,"bold"))
sysinf3.grid(column=2, row=1)
sysinf3 = Label(rahmen21, text=f"SWAP Total: {get_size(swap.total)}", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25,font=("Helvetica",10,"bold"))
sysinf3.grid(column=2, row=2)
sysinf6 = Label(rahmen21, text=f"CPU Max Freq: {cpufreq.max:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25,font=("Helvetica",10,"bold"))
sysinf6.grid(column=2, row=3)
sysinf7 = Label(rahmen21, text=f"CPU Min Freq: {cpufreq.min:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
                foreground="white", width=25,font=("Helvetica",10,"bold"))
sysinf7.grid(column=2, row=4)

sysinf8 = Label(rahmen21, text=f"Current CPU Freq: {cpufreq.current:.2f}Mhz", compound=LEFT, anchor=W, background='#333333',
            foreground="white", width=25,font=("Helvetica",10,"bold"))
sysinf8.grid(column=2, row=5)

info_sys_btn = Button(tab2, image=tpinfm,highlightthickness=0,
                   borderwidth=0,command=info_system_tab)
info_sys_btn.place(x=700,y=620)

    

#LOOK_Tab
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def xfce_make():
    popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

tab_ip1 = Image.open('icons/download_ico.png')
ip01 = ImageTk.PhotoImage(tab_ip1)
il01 = Label(image=ip01)

rahmen4 = Frame(tab4,borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10, padx=10,width=300)
rahmen4.pack(pady=40,padx=40 , fill='both' )#
rahmen4['background'] = '#333333'

tab_loktt = Image.open('icons/tuxterm.png')
ttp01 = ImageTk.PhotoImage(tab_loktt)
ttl01 = Label(image=ttp01)

guitweaks = Label(rahmen4, text="GUI Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d", anchor="w")
guitweaks.grid(column=0, row=0)

in_btn1 = Button(rahmen4,image=ttp01, text="Tasksel",font=("Helvetica",10,"bold"), command=tasksel_button, highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
in_btn1.grid(column=1, row=0, padx=5)

in_btn2 = Button(rahmen4,image=ttp01, text="Change Desktop", command=ch_desk,font=("Helvetica",10,"bold"), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
in_btn2.grid(column=1, row=1, padx=5)

in_btn3 = Button(rahmen4,image=ttp01, text="Change Win-Manager", command=button_xfwm,font=("Helvetica",10,"bold"), highlightthickness=0, borderwidth=0,
                 background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
in_btn3.grid(column=1, row=2, padx=5)

in_btn7 = Button(rahmen4,image=bp06, text="Theme Folder",font=("Helvetica",10,"bold"),
                 command=theme_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=200)
in_btn7.grid(column=2, row=0, padx=5,pady=5)

in_btn7 = Button(rahmen4,image=bp06, text="Icon Folder",font=("Helvetica",10,"bold"),
                 command=icon_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=200)
in_btn7.grid(column=2, row=1, padx=5)

xfcelook_ttp = CreateToolTip(in_btn7, \
                                   '*download the themes extract em and throw it into Theme/Icon Folder')


tab_ip2 = Image.open('icons/fix1i.png')
ip02 = ImageTk.PhotoImage(tab_ip2)
il02 = Label(image=ip02)


#xfce_tweaks
rahmen41 = Frame(tab4,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=15)
rahmen41.pack(padx=40, pady=20, fill='both')
rahmen41['background'] = '#333333'

xfce = Label(rahmen41, text="Xfce Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d",width=10)
xfce.grid(column=0, row=0)

in_btn3 = Button(rahmen41,image=ico_m,justify="left", text="Xfwm4 Settings",
                 command=button_xf4s, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=160,font=("Helvetica",10,"bold"))
in_btn3.grid(column=1, row=0, padx=5)

in_btn5 = Button(rahmen41,image=bp03,justify="left", text="WiFi Fix", compound=LEFT,
                 command=xfcefix2, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
in_btn5.grid(column=3, row=0)

in_btn5 = Button(rahmen41,image=bp03,justify="left", text="Bluetooth Fix", compound=LEFT,
                 command=xfcefix, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", anchor='w',width=160,font=("Helvetica",10,"bold"))
in_btn5.grid(column=2, row=0)

in_btn5 = Button(rahmen41,image=ico_m,justify="left", text="Xfce4 Appearance", compound=LEFT,
                 command=xfceappear_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", anchor='w',width=160,font=("Helvetica",10,"bold"))
in_btn5.grid(column=1, row=1)

in_btn7 = Button(rahmen41,image=ico_m2,justify="left", text="Xfce_look", compound=LEFT,
                 command=xfcelook_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
in_btn7.grid(column=2, row=1)

in_btn8 = Button(rahmen41,image=ico_m2,justify="left", text="Make-Me-Xfce", compound=LEFT,
                 command=xfce_make, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
in_btn8.grid(column=3, row=1)



#gui_tweaks
rahmen42 = Frame(tab4,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=15)
rahmen42.pack(padx=40, pady=20, fill='both')
rahmen42['background'] = '#333333'

lxde = Label(rahmen42, text="Pixel Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d")
lxde.grid(column=0, row=0)

lx_btn0 = Button(rahmen42,image=ico_m,justify="left", text="LXAppearace", compound=LEFT,
                 command=lxap_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
lx_btn0.grid(column=1, row=0)

lxde = Button(rahmen42,image=ico_m,justify="left", text="OpenBox Conf", compound=LEFT,
                 command=opbox_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
lxde.grid(column=2, row=0)

lxde = Button(rahmen42,image=ico_m,justify="left", text="Pi Appeariance", compound=LEFT,
                 command=pi_appear, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
lxde.grid(column=3, row=0)


#Suggestions
rahmen43 = Frame(tab4,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=15)
rahmen43.pack(padx=40, pady=20, fill='both')
rahmen43['background'] = '#333333'

lxde = Label(rahmen43, text="Suggestions ",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d", anchor="w")
lxde.grid(column=0, row=0)

in_btn3 = Button(rahmen43, text="Install Arc Theme", compound=LEFT, command=arc_inst,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",10,"bold"))
in_btn3.grid(column=1, row=0)

in_btn4 = Button(rahmen43, text="Install Breeze Cursor Theme", compound=LEFT,command=breeze_inst, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",10,"bold"))
in_btn4.grid(column=2, row=0)

in_btn5 = Button(rahmen43, text="Install Papirus Icon Theme", compound=LEFT,
                 command=papi_inst, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",10,"bold"))
in_btn5.grid(column=1, row=1)

in_btn7 = Button(rahmen43, text="Overwatch Cursor", compound=LEFT,
                 command=web_OVC, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",10,"bold"))
in_btn7.grid(column=1, row=3)

info_look_btn = Button(tab4, image=tpinfm,highlightthickness=0,
                   borderwidth=0,command=info_look_tab)
info_look_btn.place(x=700,y=620)





#Tuning_Tab
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





#overclocking
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
    
    

#overclocking_2000    
def ov_2000():
    popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/ov_1.sh && exit; exec bash\"'")
    
    global pop_2000
    pop_2000=Toplevel(main)
    pop_2000.config(bg='#333333')
    app_width = 300
    app_height = 100
    screen_width = pop_2000.winfo_screenwidth()
    screen_height = pop_2000.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    pop_2000.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
    
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
    
    
    
#overclocking_2147    
def ov_2147():
    popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/ov_2.sh && exit; exec bash\"'")
    popen("mpg123 ~/PiGro-Aid-/scripts/HOLYPiT.mp3")
    
    global pop_2147
    pop_2147=Toplevel(main)
    pop_2147.config(bg='#333333')
    app_width = 300
    app_height = 100
    screen_width = pop_2147.winfo_screenwidth()
    screen_height = pop_2147.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    pop_2147.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

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
    

#overclocking_default/reset      
def set_default():
    popen("xterm -e 'bash -c \"sudo chmod +x ~/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
    popen("xterm -e 'bash -c \"sudo ~/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
    

    global pop_default
    pop_default=Toplevel(main)
    pop_default.config(bg='#333333')
    app_width = 300
    app_height = 100
    screen_width = pop_default.winfo_screenwidth()
    screen_height = pop_default.winfo_screenheight()
    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)
    pop_default.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

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
    


#overclocking_2200    
def ov_2200():
    popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/ov_3.sh && exit; exec bash\"'")
    popen("mpg123 ~/PiGro-Aid-/scripts/over9000.mp3")
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
    


rahmen6 = Frame(tab6,borderwidth=0, highlightthickness=2, relief=GROOVE, pady=20,padx=50)
rahmen6.pack(padx=40, pady=20, fill='both')
rahmen6['background'] = '#333333'

rahmen622 = Frame(tab6,borderwidth=0, highlightthickness=2, relief=GROOVE, padx=100, pady=10)#
rahmen622.pack(padx=40, pady=20, fill='both')
rahmen622['background'] = '#333333'

rahmen61 = Frame(rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=30, pady=10)#
rahmen61.pack(side=LEFT)
rahmen61['background'] = '#333333'

rahmen62 = Frame(rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=10, pady=10)#
rahmen62.pack(padx=10, side=LEFT)
rahmen62['background'] = '#333333'



tu_lb0 = Label(rahmen6,justify="left", text="Pi4 Overclocking", highlightthickness=0, borderwidth=2,
               background='#333333', foreground="white",font=("Helvetica",18),pady=5).grid(column=0, row=0)

tu_lb3 = Label(rahmen6, text="\nReset Overclocking", highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d",font=("Helvetica",14),justify="left").grid(column=0, row=1)

tu_btn3 = Button(rahmen6,justify="left", image=tu03,text="Base Clock       \n1.5 / 1.8 Ghz       ", anchor="w", command=set_default,
                highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=0, row=2)

tu_lb1 = Label(rahmen6,justify="left", text="\nCrank It Up", highlightthickness=0, borderwidth=2, background='#333333',
               foreground="#d4244d",font=("Helvetica",14)).grid(column=0, row=3)

tu_btn1 = Button(rahmen6,justify="left", image=tu01, text="Arm_Freq = 2000\nGpu_Freq = 750\nOver_Voltage = 6", anchor="w", command=ov_2000,
                 highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=0, row=4)

tu_lb2 = Label(rahmen6,justify="left", text="\nYou Sir... Need A Fan! ", highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d",font=("Helvetica",14)).grid(column=0, row=5)

tu_btn2 = Button(rahmen6,justify="left", image=tu02, text="Arm_Freq = 2147\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2147,
                 highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=0, row=6)

tu_lb4 = Label(rahmen6,justify="left", text="\nTake It To The Max!", highlightthickness=0, borderwidth=2,
               background='#333333', foreground="#d4244d",font=("Helvetica",14)).grid(column=0, row=7)

tu_btn4 = Button(rahmen6,justify="left", image=tu04,text="Arm_Freq = 2200\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2200,
                highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=0, row=8)

tu_info = Label(rahmen6, text="Settings tested with\nPi4 + Ice Tower Cooler and Pi400.\nI take no responsibility if\nyour Pi is damaged.", font=("Helvetica", 8), highlightthickness=0, borderwidth=2,
              background='#333333', foreground="yellow").grid(column=1, row=8)




def z_ram():
    global z_ram_pop
    z_ram_pop=Toplevel()
    z_ram_pop['background'] = '#333333'
    
    def top_inst():
        os.system("xterm -e 'bash -c \"~/PiGro-Aid-/essentials/bpytop/install.sh; exec bash\"'")
    def top_uninst():
        os.system("xterm -e 'bash -c \"~/PiGro-Aid-/essentials/bpytop/uninstall.sh; exec bash\"'")

    logo = Label(z_ram_pop, image=ip03, text="ZRAM",font=("Helvetica",16), anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    bt_inst = Button(z_ram_pop, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                     highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=z_inst).grid(column=0, row=1)
    
    bt_info = Label(z_ram_pop, text="\nzram is a Linux kernel feature and userspace tools for creating compressible RAM-based block devices.\nIt has been included as a module of the mainline Linux since kernel version 3.14. \nStarting with kernel version 3.15, zram supports multiple compression streams and the ability to change \nthe compression algorithms without a system restart.",justify="left", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0)




def btswitch_64():
    global six4_mode_pop
    six4_mode_pop=Toplevel()
    six4_mode_pop['background'] = '#333333'
    
    def top_inst():
        os.system("xterm -e 'bash -c \"sudo apt-get install -y raspbian-nspawn-64; exec bash\"'")
    logo = Label(six4_mode_pop, image=ip03, text="64-Bit\nMode",font=("Helvetica",16), anchor="w",
                    highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
    
    bt_inst = Button(six4_mode_pop, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                     highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=z_inst).grid(column=0, row=1)
    
    bt_info = Label(six4_mode_pop, text="\nAdds 64 bit support.\nRun >ds64-shell< in terminal.\nBut I recommend using the RPi OS 64 bit.\nYou can find the link under LINK TAB",justify="left", anchor="w",
                  highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0)


tu_zbtn = Button(rahmen61, text="ZRAM",font=("Helvetica",16), anchor="w", command=z_ram,highlightthickness=0, borderwidth=0, background='#333333', compound=LEFT,foreground="#d4244d").grid(column=0, row=1)

tu_bbtn=Button(rahmen62, text="64 Bit Mode",font=("Helvetica",16), anchor="w", command=btswitch_64,highlightthickness=0, borderwidth=0, background='#333333', foreground="#d4244d", compound=LEFT).grid(column=0, row=1)

info_tuning_btn = Button(tab6, image=tpinfm,highlightthickness=0,
                   borderwidth=0,command=info_tuning_tab)
info_tuning_btn.place(x=665,y=40)

#Links_Tab
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
    
def lern_l():
    popen("xdg-open https://www.learnlinux.tv/")
    
def rb_tv():
    popen("xdg-open https://rocketbeans.tv/")
    
def l4_e():
    popen("xdg-open http://www.lcdwiki.com/Main_Page")
    
def fitwo_p():
    popen("xdg-open https://www.52pi.com/") 

def pi64_ld():
    popen("xdg-open https://downloads.raspberrypi.org/raspios_arm64/images/")




rahmen81 = Frame(tab8,borderwidth=0, highlightthickness=2, relief=GROOVE,padx=90,pady=10)
rahmen81.pack(padx=40, pady=20, fill='both')
rahmen81['background'] = '#333333'

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


rahmen82 = Frame(tab8,borderwidth=0, highlightthickness=2, relief=GROOVE,padx=50, pady=20,width=800)
rahmen82.pack(padx=40, pady=20, fill='both')
rahmen82['background'] = '#333333'

hedd = Label (rahmen82, text="Good Sites [No payed promo/Just stuff I like]",
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="#d4244d",font=("Helvetica",16)).grid(column=0, row=0,columnspan=3,pady=10)

choice_link1=Button(rahmen82, anchor="w", width=50,text="Mankiere.com (Commandline Database)", command=link_mankier,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=1)

choice_link2=Button(rahmen82,anchor="w",width=50,text="Guake (Drop Down Terminal)",  command=link_guake,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=2)

choice_link2=Button(rahmen82,anchor="w",width=50,text="OnBoard (Onscreen Keyboard)",  command=link_onBoard,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=3)

choice_link2=Button(rahmen82, anchor="w",width=50,text="Draculatheme.com", command=link_drac,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=4)

choice_link2=Button(rahmen82, anchor="w",width=50,text="Starship (Cross-Shell-Promt)", command=link_star,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=5)

choice_link1=Button(rahmen82,width=50,text="LernLinux.tv", anchor="w", command=lern_l,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=6)

choice_link2=Button(rahmen82,width=50,text="Rocket Beans(ger.)", anchor="w", command=rb_tv,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=7)

choice_link2=Button(rahmen82,width=50,text="52Pi", anchor="w", command=fitwo_p,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=8)

choice_link2=Button(rahmen82,width=50,text="LCD Wiki", anchor="w", command=l4_e,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=9)

choice_link3=Button(rahmen82,width=50,text="RasPi OS 64 bit", anchor="w", command=pi64_ld,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=0, row=10)

def callback(event):
    webbrowser.open_new(event.widget.cget("text"))

def callback2(event):
    xterm.open_new(event.widget.cget("entry_text"))


#HOLY_GRAIL_Tab
#def holy_backup():
    #popen("xterm -e 'bash -c \"dpkg --get-selections > ~/packages.list & echo Done!; exec bash\"'")
    
#def holy_dselect():
    #popen("xterm -e 'bash -c \"sudo apt update & sudo apt install dselect; exec bash\"'")
    
#def holy_recovery():
    #popen("xterm -e 'bash -c \"sudo dselect update & dpkg --get-selections < ~/packages.list & sudo apt-get dselect-upgrade; exec bash\"'")
    

    
#rahmen92 = Frame(tab9,borderwidth=0, highlightthickness=2, relief=GROOVE,background='#383c4a',padx=80,pady=10)
#rahmen92.pack(padx=20,pady=40)
#rahmen92['background'] = '#333333'

#grail_text=Label(rahmen92,text="Creates a packages.list (in: ~/) of all .deb files\non your system.\nCopy it to a fresh system to auto install your packages.\nDo sudo apt-get/apt at first!",
                 #background='#333333',font=("Helvetica",12), foreground="white")
#grail_text.pack(pady=10)

#grail_botn=Button(rahmen92,text="Backup", highlightthickness=1,background='#333333',
                       #borderwidth=0, foreground="white",command=holy_backup)
#grail_botn.pack(pady=10)
#grail_botn_ttp = CreateToolTip(grail_botn, \
                                # "This also kills kitten remotely...\nRight now...\nAs you clicked...\nMuhahahaha!!!")

#grail_text2=Label(rahmen92,text="On the  fresh system install dselect and press RECOVER.",
                 #background='#333333',font=("Helvetica",12), foreground="white")
#grail_text2.pack(pady=10)


#rahmen93 = Frame(rahmen92,borderwidth=0, highlightthickness=0, relief=GROOVE)
#rahmen93.pack(padx=20)
#rahmen93['background'] = '#333333'

#grail_botn2=Button(rahmen93,text="dselect", highlightthickness=1,background='#333333',
                       #borderwidth=0, foreground="white",command=holy_dselect)
#grail_botn2.grid(column=0, row=0)

#grail_botn2=Label(rahmen93,text="              ",
                # background='#333333', highlightthickness=0,
                      # borderwidth=0, foreground="white")
#grail_botn2.grid(column=1, row=0)

#grail_botn3=Button(rahmen93,text="Recover", highlightthickness=1,
                       #borderwidth=0, background='#333333', foreground="white",command=holy_recovery)
#grail_botn3.grid(column=2, row=0)

#grail_text3=Label(rahmen92,text="Or: sudo apt install dselect\nsudo dselect updat\nsudo dpkg --set-selections < packages.listn\nsudo apt-get dselect-upgrade",
                 #background='#333333',font=("Helvetica",8), foreground="white")
#grail_text3.pack(pady=10)


#info_holy_btn = Button(tab9, image=tpinfm,highlightthickness=0,
                   #borderwidth=0,command=info_holy_tab)
#info_holy_btn.place(x=700,y=620)


#Pig-Grow_Tab
pig_x = Image.open('icons/poke_pig.jpg')
pg0x = ImageTk.PhotoImage(pig_x)
pl0x = Label(image=pg0x)


def pick_at_you():
    global pop_pig
    pop_pig=Toplevel()
    pop_pig['background'] = 'white'
    
    poke_pig = Label(pop_pig,image=pg0x,background='#333333').pack()

    popen("mpg123  ~/PiGro-Aid-/scripts/poke_pig.mp3")

    poke_pig1 = Label(pop_pig,text="Moral: Never post funny things about Pigro on forums!\nI could come up with even more stupid ideas\nand incorporate them into PiGro xD",background='white', fg="red").pack()
    
def poll():
    popen("xdg-open http://www.actionschnitzel.de/Pig-Grow-Poll/")
    
def wpaps():
    popen("xdg-open http://www.actionschnitzel.de/Wallpapers/")
    
def wiki():
    popen("xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki")
    
def red_bub():
    popen("xdg-open https://www.redbubble.com/de/people/Actionschnitzel/shop?asc=u") 





pig_1 = Image.open('icons/pigpi_btn.png')
pg01 = ImageTk.PhotoImage(pig_1)
pl01 = Label(image=pg01)

pig_logo = Button(tab10,image=pg01,background='#333333', command=pick_at_you).pack(pady=40)

rahmen102 = Frame(tab10, borderwidth=0, relief=GROOVE, highlightthickness=2)
rahmen102.pack(padx=40, pady=20, fill='both')
rahmen102['background'] = '#333333'


poke_pig_21 = Label(rahmen102,justify="left",text="I never thought that so many people would use Pigro.\nAs open source lives from community,I want you to have a say in that too.\nIf you click on poll, you can vote on what else I should add to Pigro.\nSo ... let's fatten up the hog! xD\nIf you want to support me, click on the RedBubble button below.\nHere you can get Pi / Linux design from me.\n\nBest regards\n\nTimo\n\nQuestions or suggestions?:",font=("Helvetica",12),background='#333333', fg="white",padx=5,pady=3).pack()


mail = Entry(rahmen102, bd=5, width=31, borderwidth=1)
mail.insert(END,"pigroxtrmo@gmail.com")
mail.pack(pady=5)


rahmen101 = Frame(tab10, borderwidth=0, relief=GROOVE, highlightthickness=2)
rahmen101.pack(padx=40, pady=20, fill='both')
rahmen101['background'] = '#333333'





pig_btn_1 = Button(rahmen101,text="User Poll", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="#2FFC05", command=poll,font=(("Helvetica,bold"),"12","bold")).grid(column=0,row=0,pady=20, padx=20)

pig_btn_2 = Button(rahmen101,text="Wallpapers", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="#EBFC05", command=wpaps,font=(("Helvetica,bold"),"12","bold")).grid(column=1,row=0,pady=20)

pig_btn_3 = Button(rahmen101,text="PiGro Manuel", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="#053AFC",command=wiki,font=(("Helvetica,bold"),"12","bold")).grid(column=2,row=0,pady=20, padx=20)

pig_btn_4 = Button(rahmen101,text="Redbubble.com", highlightthickness=0,
                       borderwidth=0, background='#333333', foreground="#FC05A0",command=red_bub,font=(("Helvetica,bold"),"12","bold")).grid(column=3,row=0,pady=20, padx=20)









#########################################END
tab_control.pack(expand=1, fill='both')
main.mainloop()
