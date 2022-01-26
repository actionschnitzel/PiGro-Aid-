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
import time
import socket
from gpiozero import CPUTemperature #rpitemp





def actionhome():
    popen("xdg-open https://www.actionschnitzel.de/PiGro/")
    
def reboot_n():
    popen("sudo reboot")
        
def callback(event):
    webbrowser.open_new(event.widget.cget("text"))



#Main Winddow / Notebook Config
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PiGro - Vincitore_Fedele")
        self.icon = tk.PhotoImage(file="icons/PiGroLogoslim.png")
        self.tk.call('wm', 'iconphoto', self._w, self.icon)
        self['background'] = '#333333'
        self.resizable(0, 0)
        app_width = 1000
        app_height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
        self.wait_visibility(self)
        self.wm_attributes('-alpha', 0.95)
        
        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        self.Frame8 = Frame8(self.notebook)
        
        tabi = Image.open('icons/side_bar.png')
        tabp = ImageTk.PhotoImage(tabi)
        tabl = Label(self.notebook,image=tabp)
        tabl.image = tabp
        tabl['background'] = '#333333'
        tabl.place(x=-2, y=0) 
        
        tab2i = Image.open('icons/side_bar2.png')
        tab2p = ImageTk.PhotoImage(tab2i)
        tab2l = Label(self.notebook,image=tab2p)
        tab2l.image = tab2p
        tab2l['background'] = '#333333'
        tab2l.place(x=-2, y=630)


        self.tab_tp1 = Image.open('icons/Logotab.png')
        self.tp01 = ImageTk.PhotoImage(self.tab_tp1)
        self.tl01 = Label(image=self.tp01)
        
        self.tab_tp12 = Image.open('icons/updatetab.png')
        self.tp012 = ImageTk.PhotoImage(self.tab_tp12)
        self.tl012 = Label(image=self.tp012)
        
        self.tab_tp2 = Image.open('icons/system.png')
        self.tp02 = ImageTk.PhotoImage(self.tab_tp2)
        self.tl02 = Label(image=self.tp02)
        
        self.tab_tp3 = Image.open('icons/installer_ico.png')
        self.tp03 = ImageTk.PhotoImage(self.tab_tp3)
        self.tl03 = Label(image=self.tp03)
        
        self.tab_tp4 = Image.open('icons/look.png')
        self.tp04 = ImageTk.PhotoImage(self.tab_tp4)
        self.tl04 = Label(image=self.tp04)
        
        self.tab_tp6 = Image.open('icons/tuning.png')
        self.tp06 = ImageTk.PhotoImage(self.tab_tp6)
        self.tl06 = Label(image=self.tp06)

        self.sys_bp111 = Image.open('icons/dm.png')
        self.bp0111 = ImageTk.PhotoImage(self.sys_bp111)
        self.bl0111 = Label(image=self.bp0111)
        
        self.tab_tp10 = Image.open('icons/pigpi.png')
        self.tp10 = ImageTk.PhotoImage(self.tab_tp10)
        self.tl10 = Label(image=self.tp10)
        
        self.notebook.add(self.Frame1, compound=LEFT, text='Welcome', image=self.tp01)
        self.notebook.add(self.Frame3, compound=LEFT, text='System', image=self.tp02)
        self.notebook.add(self.Frame2, compound=LEFT, text='Update', image=self.tp012)
        self.notebook.add(self.Frame4, compound=LEFT, text='Installer', image=self.tp03)
        self.notebook.add(self.Frame5, compound=LEFT, text='Look', image=self.tp04)
        self.notebook.add(self.Frame6, compound=LEFT, text='Tuning', image=self.tp06)
        self.notebook.add(self.Frame7, compound=LEFT, text='Links', image=self.bp0111)
        self.notebook.add(self.Frame8, compound=LEFT, text='PiG-Grow', image=self.tp10)

        self.notebook.pack()
        
        self.noteStyler = ttk.Style(self)
        self.noteStyler.configure("TNotebook",borderwidth=0, background="#333333", tabposition='w',highlightthickness=0)
        self.noteStyler.configure("TNotebook.Tab",borderwidth=0, background="#333333", foreground="white",font=("Helvetica",16),width=13,highlightthickness=0)
        self.noteStyler.configure("TFrame", background="#333333")
        self.noteStyler.map("TNotebook.Tab", background=[("selected", "#333333")], foreground=[("selected", "#d4244d")]);


#Start Tab
class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        
        def changelog():
            global pop_changelog
            pop_changelog=Toplevel()
            pop_changelog.geometry("700x800")
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
        
        self.tab_tpinfp = Image.open('icons/info_button_p.png')
        self.tpinfp = ImageTk.PhotoImage(self.tab_tpinfp)
        self.tlinfp = Label(image=self.tpinfp)


        self.bg = PhotoImage(file="~/PiGro-Aid-/icons/pigronew.png")
        self.my_canvas = Canvas(self,width=900, height=700,highlightthickness=0)
        self.my_canvas.pack(fill="both", expand=True)
        self.my_canvas.create_image(0,0, image=self.bg, anchor="nw")
        
        self.al = tk.Label(self, text=r"https://www.actionschnitzel.de/PiGro/", fg="blue", cursor="hand2")
        self.al.place(x=480, y=645)
        self.al.bind("<Button-1>", callback)

        self.al['background'] = '#333333'

        self.al2 = tk.Label(self, text=r"https://github.com/actionschnitzel/PiGro-Aid-", fg="blue", cursor="hand2")
        self.al2.place(x=480, y=670)
        self.al2.bind("<Button-1>", callback)

        self.al2['background'] = '#333333'

        self.Chl = Button(self, image=self.tpinfp,font=(("Helvetica,bold"),"11"), highlightthickness=0, borderwidth=0, background='#d0a966',
                     foreground="white", command=changelog).place(x=110, y=400)


#Update Tab
class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def send_entry_to_terminal(*args):
            """*args needed since callback may be called from no arg (button)
        or one arg (entry)
        """
            cmd("%s" % (BasicCovTests))

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


        def update_btn():
            os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/update.sh && read -p PRESS_ENTER && exit; exec bash\"' % self.wid);

        def upgrade_btn():
            os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/upgrade.sh && read -p PRESS_ENTER && exit; exec bash\"' % self.wid);

        def full_upgrade_btn():
            os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"~/PiGro-Aid-/scripts/full_upgrade.sh && read -p PRESS_ENTER && exit; exec bash\"' % self.wid);
            
        def autoremove_btn():
            os.popen('xterm -into %d -bg Grey1 -geometry 120x25 -e \"sudo apt autoremove -y && sudo apt clean && sudo apt-get purge -y && read -p PRESS_ENTER && exit ; exec bash\"' % wid)

        def add_unsi_btn():
            os.popen("xterm -into %d -bg Grey1 -geometry 120x25 -e ~/PiGro-Aid-/scripts/addunsignedrepo.sh &" % self.wid)
            
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

        self.tab_tpinfm = Image.open('icons/info_m.png')
        self.tpinfm = ImageTk.PhotoImage(self.tab_tpinfm)
        self.tlinfm = Label(image=self.tpinfm)

        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.rahmen11 = Frame(self, relief=GROOVE, borderwidth=0)
        self.rahmen11.pack(padx=45, pady=40, anchor=W)
        self.rahmen11['background'] = '#333333'

        self.termf = Frame(self, height=270, width=700, padx=10, highlightthickness=2, borderwidth=0)
        self.wid = self.termf.winfo_id()
        self.termf['background'] = '#333333'

        s_list = Text(self.rahmen11, width=1550, height=10, highlightthickness=1)
        text_file = open("/etc/apt/sources.list", 'r')
        stuff = text_file.read()
        s_list.insert(END, stuff)
        text_file.close()
        s_list.pack(anchor='w')

        shadowcolor = "yellow"


        self.rahmen112 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2,padx=5,pady=5)
        self.rahmen112.pack(padx=45, anchor='w')
        self.rahmen112['background'] = '#333333'

        self.update_button = Button(self.rahmen112, text="Update", width=15, anchor='w', command=update_btn, highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.update_button.grid(column=0, row=0)

        self.update_button = Button(self.rahmen112, text="Upgrade", width=15, anchor='w', command=upgrade_btn, highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.update_button.grid(column=0, row=1)

        self.fupgrade_button = Button(self.rahmen112, text="Full Upgrade", width=15, anchor='w', command=full_upgrade_btn, highlightthickness=0,
                                borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.fupgrade_button.grid(column=0, row=2)

        self.gpk_button = Button(self.rahmen112, text="GPK UpdateViewer", width=15, anchor='w', command=button_gpk,
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.gpk_button.grid(column=0, row=3)

        self.auth_button = Button(self.rahmen112, text="Allow Sources", width=20, anchor='w', command=add_unsi_btn,
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.auth_button.grid(column=1, row=0)

        self.rm_button = Button(self.rahmen112, text="Remove Config Files", width=20, anchor='w', command=autoremove_btn,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",12,"bold"))
        self.rm_button.grid(column=1, row=1)

        self.sv_button = Button(self.rahmen112, text="Save Source List", width=20, anchor='w', command=save_list, highlightthickness=0,
                        borderwidth=0, background='#333333', foreground="#d4244d",font=("Helvetica",12,"bold"))
        self.sv_button.grid(column=1, row=2)

        self.termf.pack(padx=45,pady=20, anchor=W)

        self.info_up_btn = Button(self, image=self.tpinfm,highlightthickness=0,
                        borderwidth=0,command=info_update_tab)
        self.info_up_btn.place(x=650,y=320)


#System Tab
distro = distro.id()
class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def button_boot():
            popen("xterm -e 'bash -c \"dmesg; exec bash\"'")
        
        def rm_vsc():
            popen("xterm -e 'bash -c \"sudo rm /etc/apt/sources.list.d/vscode.list & echo DONE!; exec bash\"'")

        def net_set():
            popen("nm-connection-editor")
            
        def pi_configbutton():
            popen("xterm -e 'bash -c \"sudo raspi-config; exec bash\"'")

        def pi_configbutton2():
            popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")

        def lx_task():
            popen("lxtask")

        def contxt_button():
            popen("sudo mousepad /boot/config.txt")

        def neofetch_button():
            popen("xterm -e 'bash -c \"neofetch; exec bash\"'")

        def gparted_exec():
            popen("sudo gparted")

        def onc_ben():
            popen("sudo xdg-open ~")

        def button_lk():
            popen("xterm -e 'bash -c \"sudo BRANCH=next rpi-update; exec bash\"'")

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def button_auto():
            popen('xfce4-session-settings')
            
        def button_xsett():
            popen('xfce4-settings-manager')

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

        def extract_ip():
            st = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            try:       
                st.connect(('10.255.255.255', 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = '127.0.0.1'
            finally:
                st.close()
            return IP
        #print(extract_ip())

        #Icon Set
        self.sys_bp1 = Image.open('icons/raspberry-pi-logo.png')
        self.bp01 = ImageTk.PhotoImage(self.sys_bp1)
        self.bl01 = Label(image=self.bp01)

        self.sys_bp2 = Image.open('icons/raspberry-pi-logo.png')
        self.bp02 = ImageTk.PhotoImage(self.sys_bp2)
        self.bl02 = Label(image=self.bp02)

        self.sys_bp3 = Image.open('icons/terminal.png')
        self.bp03 = ImageTk.PhotoImage(self.sys_bp3)
        self.bl03 = Label(image=self.bp03)

        self.sys_bp33 = Image.open('icons/terminal3.png')
        self.bp033 = ImageTk.PhotoImage(self.sys_bp33)
        self.bl033 = Label(image=self.bp033)

        sys_bp4 = Image.open('icons/gparted.png')
        bp04 = ImageTk.PhotoImage(sys_bp4)
        bl04 = Label(image=bp04)

        self.sys_bp5 = Image.open('icons/indicator-cpufreq.png')
        self.bp05 = ImageTk.PhotoImage(self.sys_bp5)
        self.bl05 = Label(image=self.bp05)

        self.sys_bp6 = Image.open('icons/folder.png')
        self.bp06 = ImageTk.PhotoImage(self.sys_bp6)
        self.bl06 = Label(image=self.bp06)

        self.sys_bp7 = Image.open('icons/links.png')
        self.bp07 = ImageTk.PhotoImage(self.sys_bp7)
        self.bl07 = Label(image=self.bp07)
        
        self.sys_bp1 = Image.open('icons/raspberry-pi-logo.png')
        self.bp01 = ImageTk.PhotoImage(self.sys_bp1)
        self.bl01 = Label(image=self.bp01)

        self.sys_bp2 = Image.open('icons/raspberry-pi-logo.png')
        self.bp02 = ImageTk.PhotoImage(self.sys_bp2)
        self.bl02 = Label(image=self.bp02)

        self.sys_bp3 = Image.open('icons/terminal.png')
        self.bp03 = ImageTk.PhotoImage(self.sys_bp3)
        self.bl03 = Label(image=self.bp03)

        self.sys_bp33 = Image.open('icons/terminal3.png')
        self.bp033 = ImageTk.PhotoImage(self.sys_bp33)
        self.bl033 = Label(image=self.bp033)

        self.sys_bp4 = Image.open('icons/gparted.png')
        self.bp04 = ImageTk.PhotoImage(sys_bp4)
        self.bl04 = Label(image=self.bp04)

        self.sys_bp5 = Image.open('icons/indicator-cpufreq.png')
        self.bp05 = ImageTk.PhotoImage(self.sys_bp5)
        self.bl05 = Label(image=self.bp05)

        self.sys_bp6 = Image.open('icons/folder.png')
        self.bp06 = ImageTk.PhotoImage(self.sys_bp6)
        self.bl06 = Label(image=self.bp06)

        self.sys_bp7 = Image.open('icons/links.png')
        self.bp07 = ImageTk.PhotoImage(self.sys_bp7)
        self.bl07 = Label(image=self.bp07)
        
        self.ico_1 = Image.open('icons/gui_icon.png')
        self.ico_m = ImageTk.PhotoImage(self.ico_1)
        self.ico_win = Label(image=self.ico_m)
        
        self.ico_2 = Image.open('icons/weblink_icon.png')
        self.ico_m2 = ImageTk.PhotoImage(self.ico_2)
        self.ico_win2 = Label(image=self.ico_m2)
        
        self.tab_tpinfm = Image.open('icons/info_m.png')
        self.tpinfm = ImageTk.PhotoImage(self.tab_tpinfm)
        self.tlinfm = Label(image=self.tpinfm)
        
        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)



        #Button Set/Frame1
        self.rahmen2 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,padx=60,pady=10)
        self.rahmen2.pack(padx=40, pady=20, fill='both')
        self.rahmen2['background'] = '#333333'

        sys_btn6 = Button(self.rahmen2, image=self.bp01, text="Raspi-Config CLI", command=pi_configbutton,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn6.grid(row=0,column=0)

        sys_btn1 = Button(self.rahmen2, image=self.bp01, text="Raspi-Config GUI", command=pi_configbutton2,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn1.grid(row=0,column=1)

        sys_btn2 = Button(self.rahmen2, image=self.ico_m, text="Config.txt", command=contxt_button,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn2.grid(row=0,column=2)

        sys_btnvs = Button(self.rahmen2, image=self.bp03, text="rm vscode.list ", command=rm_vsc,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btnvs.grid(row=0,column=3)

        sys_btn3 = Button(self.rahmen2, image=self.bp04, text="Gparted", command=gparted_exec,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn3.grid(row=1,column=0)

        sys_btn4 = Button(self.rahmen2, image=self.bp05, text="NeoFetch", command=neofetch_button,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn4.grid(row=1,column=1)

        sys_btn5 = Button(self.rahmen2, image=self.bp06, text="FM God Mode", command=onc_ben, highlightthickness=0,
                          borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn5.grid(row=1,column=2)
        sys_btn5_ttp = CreateToolTip(sys_btn5, \
                                           "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)")

        sys_btn6 = Button(self.rahmen2, image=self.bp07, text="Upgrade Linux Kernel", command=button_lk,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn6.grid(row=1,column=3)

        sys_btn7 = Button(self.rahmen2, image=self.bp03, text="DeskpiPro Control", command=button_dpfc,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn7.grid(row=2,column=0)

        sys_btn8 = Button(self.rahmen2, image=self.bp03, text="Boot Log", command=button_boot,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn8.grid(row=2,column=1)

        sys_btn9 = Button(self.rahmen2, image=self.bp033, text="Xfce Autostarts", command=button_auto,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn9.grid(row=2,column=2)

        sys_btn9 = Button(self.rahmen2, image=self.bp033, text="Xfce Settings", command=button_xsett,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn9.grid(row=2,column=3)

        sys_btn10 = Button(self.rahmen2, image=self.ico_m, text="Network Settings", command=net_set,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn10.grid(row=3,column=0)

        sys_btn11 = Button(self.rahmen2, image=self.ico_m, text="Taskmanager", command=lx_task,
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",10,"bold"))
        sys_btn11.grid(row=3,column=1)
        
    
        #System_Info/Frame2
        
        #Parameters for System
        pid = os.getpid()
        ps = psutil.Process(pid)
        my_system = platform.uname()
        cpufreq = psutil.cpu_freq()
        svmem = psutil.virtual_memory()
        swap = psutil.swap_memory()
        hostname = socket.gethostname()   
        IPAddr = extract_ip() 
        cpu = CPUTemperature()
        Pi_Model = open("/proc/device-tree/model", "r")
        
       
        self.rahmen21 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=20)
        self.rahmen21.pack(padx=40, pady=20, fill='both')
        self.rahmen21['background'] = '#333333'

        self.rahmen22 = Frame(self.rahmen21,borderwidth=0, highlightthickness=0, relief=GROOVE,pady=10,padx=20)
        self.rahmen22.grid(row=1,column=2)
        self.rahmen22['background'] = '#333333'

        self.my_img = ImageTk.PhotoImage(Image.open("icons/deb_logo.png"))
        self.my_label = Label(image=self.my_img)

        self.sysinf0 = Label(self.rahmen22,justify="left",image=self.my_img, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="#d4244d",pady=20,padx=20,anchor=W)
        self.sysinf0.pack()

        self.rahmen23 = Frame(self.rahmen21,borderwidth=0, highlightthickness=0, relief=GROOVE)
        self.rahmen23.grid(row=1,column=0)
        self.rahmen23['background'] = '#333333'
        
        self.rahmen24 = Frame(self.rahmen21,borderwidth=0, highlightthickness=0, relief=GROOVE)
        self.rahmen24.grid(row=0,column=2)
        self.rahmen24['background'] = '#333333'






        self.sysinf0 = Label(self.rahmen24, text="System Info",font=("Helvetica",16,"bold"),justify="center", highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="#d4244d", width=30,anchor=W).pack()

        self.sysinf0 = Label(self.rahmen23, text=f"System: {my_system.system}",font=("Helvetica",10,"bold"),justify="left", highlightthickness=0,
                        borderwidth=0, background='#333333', foreground="white", width=30,anchor=W).pack()
 
        self.sysinfd = Label(self.rahmen23, text=f"Distro: {distro}",justify="left", highlightthickness=0,
                        borderwidth=0, background='#333333', foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf1 = Label(self.rahmen23, text=f"Node Name: {my_system.node}",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()
       
        self.sysinf9 = Label(self.rahmen23, text=Pi_Model.read(),justify="left", background='#333333',
                    foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()


        self.sysinf2 = Label(self.rahmen23, text=f"Kernel: {my_system.release}",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf3 = Label(self.rahmen23, text=f"Machine: {my_system.machine}",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf8 = Label(self.rahmen23, text="", background='#333333',
                    foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W)
        self.sysinf8.pack()

        self.sysinf6 = Label(self.rahmen23, text=f"CPU Max Freq: {cpufreq.max:.2f}Mhz",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf7 = Label(self.rahmen23, text=f"CPU Min Freq: {cpufreq.min:.2f}Mhz",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf10 = Label(self.rahmen23, text="",justify="left", background='#333333',
                    foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W)
        self.sysinf10.pack()
        
        self.sysinf3 = Label(self.rahmen23, text=f"RAM Total: {get_size(svmem.total)}",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()

        self.sysinf3 = Label(self.rahmen23, text=f"SWAP Total: {get_size(swap.total)}",justify="left", background='#333333',
                        foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()
     
        self.sysinf9 = Label(self.rahmen23, text=f"IP Address: {IPAddr}",justify="left", background='#333333',
                    foreground="white", width=30,font=("Helvetica",10,"bold"),anchor=W).pack()




        self.info_sys_btn = Button(self, image=self.tpinfm,highlightthickness=0,
                        borderwidth=0,command=info_system_tab)
        self.info_sys_btn.place(x=700,y=620)
        
        def refresh():
        
            #Parameters for System
            pid = os.getpid()
            ps = psutil.Process(pid)            
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            cpu = CPUTemperature()

            self.sysinf8.configure(text=f"Current CPU Freq: {cpufreq.current:.2f}Mhz")
            self.sysinf10.configure(text=f"CPU Temp: {cpu.temperature} °C")
            self.after(1000, refresh)
            
        refresh()
        
        
#Installer Tab      
class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()
        
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

        def web_OVC():
            popen("xdg-open https://www.gnome-look.org/p/1158321/")

        def arc_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")

        def breeze_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install breeze-cursor-theme; exec bash\"'")

        def papi_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install papirus-icon-theme; exec bash\"'")

        def gparted_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install gparted; exec bash\"'")

        def snapcraft():
            popen("xdg-open https://snapcraft.io/store")

        def flatflat():
            popen("xdg-open https://flathub.org/")

        def inst_bleach():
            popen("xterm -e 'bash -c \"sudo apt-get install bleachbit ; exec bash\"'")

        def inst_ima():
            popen("xterm -e 'bash -c \"sudo apt install rpi-imager; exec bash\"'")

        def inst_neo():
            popen("xterm -e 'bash -c \"sudo apt-get install neofetch; exec bash\"'")

        def pi_apps():
            popen("xterm -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'")


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
            pop_goodstuff=Toplevel(self)
            pop_goodstuff['background'] = '#333333'
            
            shop_btn01 = Button(pop_goodstuff, width=120, image=self.ip03, text="Whatsapp\n(Snap)", anchor="w", command=w_app, highlightthickness=0,borderwidth=0, background='#d4244d',foreground="white", compound=LEFT).grid(column=0, row=1)

            shop_lbl011 = Label(pop_goodstuff,width=60, text="... is... you know Whatsapp", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=1)

            shop_btn2 = Button(pop_goodstuff, width=120, image=self.ip03, text="Compiz", anchor="w", command=compiz_button,
                            highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=2)

            shop_lbl21 = Label(pop_goodstuff,width=60, text="When I was young it was cool You know it as wobbly windows", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=2)
            
            shop_btn3 = Button(pop_goodstuff, width=120, image=self.ip03, text="Gparted", anchor="w", command=gparted_inst,
                            highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=3)

            shop_btn31 = Label(pop_goodstuff,width=60, text="A Partition Manager", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=3)

            shop_btn4 = Button(pop_goodstuff, width=120, image=self.ip03, text="NeoFetch", anchor="w", command=inst_neo, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=4)

            shop_btn41 = Label(pop_goodstuff,width=60, text="Shows system specs you already know but ... uhhm...", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=4)

            shop_btn5 = Button(pop_goodstuff, width=120, image=self.ip03, text="PiKiss", anchor="w", command=kiss_button, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=5)

            shop_btn51 = Label(pop_goodstuff,width=60, text="Bow down!", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=5)

            shop_btn6 = Button(pop_goodstuff, width=120, image=self.ip03, text="Bleach Bit", anchor="w", command=inst_bleach,
                            highlightthickness=0, borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=6)
            
            shop_btn61 = Label(pop_goodstuff,width=60, text="Cleans the System", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=6)

            shop_btn7 = Button(pop_goodstuff, width=120, image=self.ip03, text="Pi Imager", anchor="w", command=inst_ima, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=7)
            
            shop_btn71 = Label(pop_goodstuff,width=60, text="Pi-Imager on RaspiOS is like the Replicants from Stargate... o,o", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=7)
            
            shop_btn8 = Button(pop_goodstuff, width=120, image=self.ip03, text="Synaptic", anchor="w", command=inst_syn, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=8)
            
            shop_btn81 = Label(pop_goodstuff,width=60, text="THE Pakegemanager", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=8)

            shop_btn9 = Button(pop_goodstuff, width=120, image=self.ip03, text="Gnome-Pie", anchor="w", command=gnome_pie, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=9)

            shop_btn91 = Label(pop_goodstuff,width=60, compound=LEFT, text="When you tell peolpe i3 is god but you need a hidden menu cuz\nyou dont cope with it", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white").grid(column=1, row=9)

            shop_btn10 = Button(pop_goodstuff, width=120, image=self.ip03, text="Pi-Apps", anchor="w", command=pi_apps, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=10)
            
            shop_btn101 = Label(pop_goodstuff,width=60, text="DOWNLOAD IT!!!!!11", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=10)

            shop_btn18 = Button(pop_goodstuff, width=120, image=self.ip03, text="Plank", anchor="w", command=p_lank, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=11)

            shop_btn118 = Label(pop_goodstuff,width=60, text="It's a Dock!", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=11)     

            shop_btn20 = Button(pop_goodstuff, width=120, image=self.ip03, text="Tilix", anchor="w", command=inst_tilix, highlightthickness=0,
                            borderwidth=0, background='#d4244d', foreground="white", compound=LEFT).grid(column=0, row=12)

            shop_btn120 = Label(pop_goodstuff,width=60, text="Multi-Tiling-Super-Terminal-Emulator", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT).grid(column=1, row=12)

        #PDL
        def shop():
            os.system("python3 ~/PiGro-Aid-/PDL.py")

        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.tab_shop = Image.open('icons/shop.png')
        self.ipshop = ImageTk.PhotoImage(self.tab_shop)
        self.ilshop = Label(image=self.ipshop)

        self.tab_finst = Image.open('icons/fast_install.png')
        self.ipfinst = ImageTk.PhotoImage(self.tab_finst)
        self.ilfinst = Label(image=self.ipfinst)
        
        self.tab_tpinfm = Image.open('icons/info_m.png')
        self.tpinfm = ImageTk.PhotoImage(self.tab_tpinfm)
        self.tlinfm = Label(image=self.tpinfm)

        self.rahmen_shop = Frame(self,borderwidth=0, highlightthickness=1)
        self.rahmen_shop.pack(padx=40, pady=40)
        self.rahmen_shop['background'] = '#333333'


        self.shop_click = Button(self.rahmen_shop,image=self.ipshop, command=shop, highlightthickness=1, borderwidth=5, background='green', foreground="white", compound=LEFT,width=500)
        self.shop_click.pack()

        self.rahmen3x = Frame(self, relief=GROOVE,borderwidth=1, highlightthickness=1,pady=10,padx=10)
        self.rahmen3x['background'] = 'green'
        self.rahmen3x.pack()

        self.sysinf0 = Label(self.rahmen3x,image=self.ipfinst, compound=LEFT, anchor='n',font=("Helvetica",16), highlightthickness=0, borderwidth=0,background='green', foreground="white",pady=20)
        self.sysinf0.pack()


        self.rahmen3 = Frame(self.rahmen3x, relief=GROOVE,borderwidth=0, highlightthickness=1, padx=42, pady=20)
        self.rahmen3.pack()
        self.rahmen3['background'] = '#333333'


        #apt-get_entry
        inst1_p1=""" xterm -e 'bash -c \"sudo apt-get install """
        inst1_p2="""; exec bash\"' """


        def inst_btn1():
            entry_text = self.eingabefeld1.get()
            popen(inst1_p1 + entry_text + inst1_p2)

        def uninst_btn1():
                popen("sudo synaptic")
                
        def inst_syn():
                popen("xterm -e 'bash -c \"sudo apt-get install synaptic; exec bash\"'")

        self.i4 = Image.open('icons/apt-get.png')
        self.p4 = ImageTk.PhotoImage(self.i4)
        self.l4 = Label(image=self.p4)

        self.welcome_label1 = Label(self.rahmen3)
        self.eingabefeld1 = Entry(self.rahmen3, bd=5, width=31, borderwidth=1)
        self.eingabefeld1.insert(0,"Enter Package Name")
        self.welcom_button1 = Button(self.rahmen3, text="install", command=inst_btn1, highlightthickness=0, borderwidth=0,
                                background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
        self.welcom_button1_ttp = CreateToolTip(self.welcom_button1, \
                                        'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.')



        self.my_label = Label(self.rahmen3, image=self.p4, fg="white")
        self.my_label['background'] = '#333333'
        self.my_label.grid(column=0, row=0, )
        self.eingabefeld1.grid(column=2, row=0)
        self.welcom_button1.grid(column=1, row=0)



        #pi-apps_entry
        inst3_p1=""" xterm -e 'bash -c \"~/pi-apps/manage install """
        inst3_p2="""; exec bash\"' """

        def inst_pi_apps():
            entry_text = self.eingabefeld3.get()
            popen(inst3_p1 + entry_text + inst3_p2)


        uninst3_p1=""" xterm -e 'bash -c \"~/pi-apps/manage uninstall """
        uninst3_p2="""; exec bash\"' """

        def uninst_pi_apps():
            entry_text = self.eingabefeld3.get()
            popen(uninst3_p1 + entry_text + uninst3_p2)

        def pi_apps_list():
            popen("xterm -e 'bash -c \"ls ~/pi-apps/apps/ ; exec bash\"'")

        self.ia6 = Image.open('icons/pi-app.png')
        self.pa6 = ImageTk.PhotoImage(self.ia6)
        self.la6 = Label(image=self.pa6)

        self.apps_inst_btn = Label(self.rahmen3, image=self.pa6, text="piapps install", fg="white")
        self.apps_inst_btn ['background'] = '#333333'

        self.welcome_label2 = Label(self.rahmen3)
        self.eingabefeld3 = Entry(self.rahmen3, bd=5, width=31, borderwidth=1)
        self.welcom_button3 = Button(self.rahmen3, text="install", command=inst_pi_apps, highlightthickness=0, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))



        self.apps_inst_btn.grid(column=0, row=3)
        self.eingabefeld3.grid(column=2, row=3)
        self.welcom_button3.grid(column=1, row=3)


        #snap_entry
        inst2_p1=""" xterm -e 'bash -c \"sudo snap install """
        inst2_p2="""; exec bash\"' """

        def inst_btn2():
            entry_text = self.eingabefeld2.get()
            popen(inst2_p1 + entry_text + inst2_p2)


        self.i6 = Image.open('icons/snap.png')
        self.p6 = ImageTk.PhotoImage(self.i6)
        self.l6 = Label(image=self.p6)

        self.my_label2 = Label(self.rahmen3, image=self.p6, text="Snap install", fg="white")
        self.my_label2['background'] = '#333333'

        self.welcome_label2 = Label(self.rahmen3)
        self.eingabefeld2 = Entry(self.rahmen3, bd=5, width=31, borderwidth=1)
        self.welcom_button2 = Button(self.rahmen3, text="install", command=inst_btn2, highlightthickness=0, borderwidth=0,
                                background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
        self.welcom_button2_ttp = CreateToolTip(self.welcom_button2, \
                                        '*to use snap install, you must\napt-get install snapd xD lol')

        self.my_label2.grid(column=0, row=1)
        self.eingabefeld2.grid(column=2, row=1)
        self.welcom_button2.grid(column=1, row=1)


        self.tab_ip3 = Image.open('icons/download_ico.png')
        self.ip03 = ImageTk.PhotoImage(self.tab_ip3)
        self.il03 = Label(image=self.ip03)




        #flat_entry
        inst4_p1=""" xterm -e 'bash -c \"sudo flatpak install flathub """
        inst4_p2="""; exec bash\"' """

        def inst_btn4():
            entry_text = self.eingabefeld4.get()
            popen(inst4_p1 + entry_text + inst4_p2)


        self.i66 = Image.open('icons/flathub.png')
        self.p66 = ImageTk.PhotoImage(self.i66)
        self.l66 = Label(image=self.p66)

        self.my_label4 = Label(self.rahmen3, image=self.p66, text="Snap install", fg="white")
        self.my_label4['background'] = '#333333'

        self.welcome_label4 = Label(self.rahmen3)
        self.eingabefeld4 = Entry(self.rahmen3, bd=5, width=31, borderwidth=1)
        self.welcom_button44 = Button(self.rahmen3, text="install", command=inst_btn4, highlightthickness=0, borderwidth=0,
                                background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
        self.welcom_button44_ttp = CreateToolTip(self.welcom_button44, \
                                        '*past without--->>>flatpak install flathub<<< org.mozilla.firefox')

        self.my_label4.grid(column=0, row=7)
        self.eingabefeld4.grid(column=2, row=7)
        self.welcom_button44.grid(column=1, row=7)

        self.frame311 = Frame(self, relief=GROOVE,borderwidth=0, highlightthickness=1,pady=5,padx=36,bg="green")
        self.frame311.pack(pady=10)

        self.snapstore_btn = Button(self.frame311, text="snapcraft.io", command=snapcraft, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

        self.welcom_button33 = Button(self.frame311, text="list all pi-apps", command=pi_apps_list, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

        self.uninst_button = Button(self.frame311, text="Synaptic", command=uninst_btn1, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))
        self.uninst_button_ttp = CreateToolTip(self.uninst_button, \
                                        'If nothing happens you must install Synaptic')

        self.goodstuff_btn = Button(self.frame311, text="Must Haves", command=goodstuff, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))

        self.flat_btn = Button(self.frame311, text="Flathub", command=flatflat, highlightthickness=1, borderwidth=0,background='#333333', foreground="white",font=(("Helvetica,bold"),"12"))


        self.snapstore_btn.grid(column=0, row=6)
        self.welcom_button33.grid(column=1, row=6)
        self.uninst_button.grid(column=2, row=6)
        self.goodstuff_btn.grid(column=4, row=6)
        self.flat_btn.grid(column=3, row=6)


        self.info_inst_btn = Button(self, image=self.tpinfm,highlightthickness=0,
                        borderwidth=0,command=info_installer_tab)
        self.info_inst_btn.place(x=700,y=620)


#Look
class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def button_xf4s():
            popen("xfwm4-settings")

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

        def pi_appear():
            popen("env SUDO_ASKPASS=/usr/lib/pipanel/pwdpip.sh pipanel")
            
        def opbox_button():
            popen("sudo obconf")    

        def lxap_button():
            popen("lxappearance")

        def xfceappear_button():
            popen("xfce4-appearance-settings")

        def tasksel_button():
            popen("xterm -e 'bash -c \"sudo tasksel; exec bash\"'")

        def xfcelook_f():
            popen("xdg-open https://www.xfce-look.org/browse/cat/")    

        def ch_desk():
            popen("xterm -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'")

        def button_xfwm():
            popen("xterm -e 'bash -c \"sudo update-alternatives --config x-window-manager; exec bash\"'")

        def theme_f():
            popen("sudo xdg-open /usr/share/themes/")
            
        def icon_f():
            popen("sudo xdg-open /usr/share/icons/")

        def xfcefix():
            popen("xterm -e 'bash -c \"sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'")

        def xfcefix2():
            popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'")
            
        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")
        
        def arc_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install arc-theme; exec bash\"'")

        def breeze_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install breeze-cursor-theme; exec bash\"'")

        def papi_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install papirus-icon-theme; exec bash\"'")

        def web_OVC():
            popen("xdg-open https://www.xfce-look.org/browse/")

        #Images/Icons
        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.tab_tpinfm = Image.open('icons/info_m.png')
        self.tpinfm = ImageTk.PhotoImage(self.tab_tpinfm)
        self.tlinfm = Label(image=self.tpinfm)

        self.sys_bp6 = Image.open('icons/folder.png')
        self.bp06 = ImageTk.PhotoImage(self.sys_bp6)
        self.bl06 = Label(image=self.bp06)

        self.ico_1 = Image.open('icons/gui_icon.png')
        self.ico_m = ImageTk.PhotoImage(self.ico_1)
        self.ico_win = Label(image=self.ico_m)

        self.sys_bp3 = Image.open('icons/terminal.png')
        self.bp03 = ImageTk.PhotoImage(self.sys_bp3)
        self.bl03 = Label(image=self.bp03)

        self.ico_2 = Image.open('icons/weblink_icon.png')
        self.ico_m2 = ImageTk.PhotoImage(self.ico_2)
        self.ico_win2 = Label(image=self.ico_m2)

        self.tab_ip1 = Image.open('icons/download_ico.png')
        self.ip01 = ImageTk.PhotoImage(self.tab_ip1)
        self.il01 = Label(image=self.ip01)

        self.tab_loktt = Image.open('icons/tuxterm.png')
        self.ttp01 = ImageTk.PhotoImage(self.tab_loktt)
        self.ttl01 = Label(image=self.ttp01)

        self.tab_ip2 = Image.open('icons/fix1i.png')
        self.ip02 = ImageTk.PhotoImage(self.tab_ip2)
        self.il02 = Label(image=self.ip02)


        #Frame/Button Set
        self.rahmen4 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10, padx=10,width=300)
        self.rahmen4.pack(pady=40,padx=40 , fill='both' )#
        self.rahmen4['background'] = '#333333'

        self.guitweaks = Label(self.rahmen4, text="GUI Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d", anchor="w")
        self.guitweaks.grid(column=0, row=0)

        self.in_btn1 = Button(self.rahmen4,image=self.ttp01, text="Tasksel",font=("Helvetica",10,"bold"), command=tasksel_button, highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
        self.in_btn1.grid(column=1, row=0, padx=5)

        self.in_btn2 = Button(self.rahmen4,image=self.ttp01, text="Change Desktop", command=ch_desk,font=("Helvetica",10,"bold"), highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
        self.in_btn2.grid(column=1, row=1, padx=5)

        self.in_btn3 = Button(self.rahmen4,image=self.ttp01, text="Change Win-Manager", command=button_xfwm,font=("Helvetica",10,"bold"), highlightthickness=0, borderwidth=0,
                        background='#333333', foreground="white", compound=LEFT, anchor='w',width=220)
        self.in_btn3.grid(column=1, row=2, padx=5)

        self.in_btn7 = Button(self.rahmen4,image=self.bp06, text="Theme Folder",font=("Helvetica",10,"bold"),
                        command=theme_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=200)
        self.in_btn7.grid(column=2, row=0, padx=5,pady=5)

        self.in_btn7 = Button(self.rahmen4,image=self.bp06, text="Icon Folder",font=("Helvetica",10,"bold"),
                        command=icon_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=200)
        self.in_btn7.grid(column=2, row=1, padx=5)

        self.xfcelook_ttp = CreateToolTip(self.in_btn7, \
                                        '*download the themes extract em and throw it into Theme/Icon Folder')
        
        self.in_btn7 = Button(self.rahmen4,image=self.ico_m2, text="Get Themes",font=("Helvetica",10,"bold"),
                        command=web_OVC, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=200)
        self.in_btn7.grid(column=2, row=2, padx=5)
        
        



        #xfce_tweaks
        self.rahmen41 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=15)
        self.rahmen41.pack(padx=40, pady=20, fill='both')
        self.rahmen41['background'] = '#333333'

        self.xfce = Label(self.rahmen41, text="Xfce Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d",width=10)
        self.xfce.grid(column=0, row=0)

        self.in_btn3 = Button(self.rahmen41,image=self.ico_m,justify="left", text="Xfwm4 Settings",
                        command=button_xf4s, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT, anchor='w',width=160,font=("Helvetica",10,"bold"))
        self.in_btn3.grid(column=1, row=0, padx=5)

        self.in_btn5 = Button(self.rahmen41,image=self.bp03,justify="left", text="WiFi Fix", compound=LEFT,
                        command=xfcefix2, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.in_btn5.grid(column=3, row=0)

        self.in_btn5 = Button(self.rahmen41,image=self.bp03,justify="left", text="Bluetooth Fix", compound=LEFT,
                        command=xfcefix, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", anchor='w',width=160,font=("Helvetica",10,"bold"))
        self.in_btn5.grid(column=2, row=0)

        self.in_btn5 = Button(self.rahmen41,image=self.ico_m,justify="left", text="Xfce4 Appearance", compound=LEFT,
                        command=xfceappear_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white", anchor='w',width=160,font=("Helvetica",10,"bold"))
        self.in_btn5.grid(column=1, row=1)

        self.in_btn7 = Button(self.rahmen41,image=self.ico_m2,justify="left", text="Xfce_look", compound=LEFT,
                        command=xfcelook_f, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.in_btn7.grid(column=2, row=1)

        self.in_btn8 = Button(self.rahmen41,image=self.ico_m2,justify="left", text="Make-Me-Xfce", compound=LEFT,
                        command=xfce_make, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.in_btn8.grid(column=3, row=1)



        #gui_tweaks
        self.rahmen42 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10,padx=15)
        self.rahmen42.pack(padx=40, pady=20, fill='both')
        self.rahmen42['background'] = '#333333'

        self.lxde = Label(self.rahmen42, text="Pixel Tweaks",font=("Helvetica",14,"bold"), background='#333333', foreground="#d4244d")
        self.lxde.grid(column=0, row=0)

        self.lx_btn0 = Button(self.rahmen42,image=self.ico_m,justify="left", text="LXAppearace", compound=LEFT,
                        command=lxap_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.lx_btn0.grid(column=1, row=0)

        self.lxde = Button(self.rahmen42,image=self.ico_m,justify="left", text="OpenBox Conf", compound=LEFT,
                        command=opbox_button, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.lxde.grid(column=2, row=0)

        self.lxde = Button(self.rahmen42,image=self.ico_m,justify="left", text="Pi Appeariance", compound=LEFT,
                        command=pi_appear, highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=160, anchor='w',font=("Helvetica",10,"bold"))
        self.lxde.grid(column=3, row=0)

        self.info_look_btn = Button(self, image=self.tpinfm,highlightthickness=0,
                        borderwidth=0,command=info_look_tab)
        self.info_look_btn.place(x=700,y=620)


#Tuning_Tab
class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def z_inst():
            popen("xterm -e 'bash -c \"sudo apt-get install zram-tools; exec bash\"'")
            
        #Current OV settings   
        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def generate_lines_that_equal(string, fp):
            for line in fp:
                if line == string:
                    yield line
                    

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

        #BG + Icons
        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.tu_tp1 = Image.open('icons/PiGroOV2.png')
        self.tu01 = ImageTk.PhotoImage(self.tu_tp1)
        self.tul01 = Label(image=self.tu01)

        self.tu_tp2 = Image.open('icons/PiGroOV.png')
        self.tu02 = ImageTk.PhotoImage(self.tu_tp2)
        self.tul02 = Label(image=self.tu02)

        self.tu_tp3 = Image.open('icons/PiGroOV3.png')
        self.tu03 = ImageTk.PhotoImage(self.tu_tp3)
        self.tul03 = Label(image=self.tu03)

        self.tu_tp4 = Image.open('icons/PiGroOV4.png')
        self.tu04 = ImageTk.PhotoImage(self.tu_tp4)
        self.tul04 = Label(image=self.tu04)

        self.tab_tpinfm = Image.open('icons/info_m.png')
        self.tpinfm = ImageTk.PhotoImage(self.tab_tpinfm)
        self.tlinfm = Label(image=self.tpinfm)
        
        self.tab_ip3 = Image.open('icons/download_ico.png')
        self.ip03 = ImageTk.PhotoImage(self.tab_ip3)
        self.il03 = Label(image=self.ip03)


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
            pop_2000=Toplevel(self)
            pop_2000.config(bg='#333333')
            app_width = 500
            app_height = 150
            screen_width = pop_2000.winfo_screenwidth()
            screen_height = pop_2000.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2000.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            pop_2000.resizable(0, 0)
            
            frame_pop_2000 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
            frame_pop_2000.pack()
            frame_pop_2000['background'] = '#333333'

            frame_pop_2000_1 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
            frame_pop_2000_1.pack()
            frame_pop_2000_1['background'] = '#333333'
            
            pop_lbl_2000=Label(frame_pop_2000,anchor="w", text="Done! The new settings take effect after a reboot",font=("Helvetica",12), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
            pop_lbl_2000.pack(pady=20)
            
            pop_btn_2000=Button(frame_pop_2000_1,text="Continue", anchor="w", command=pop_dest2,
                                highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
            pop_btn_2000.pack(padx=5,pady=20,side=LEFT)
            pop_btn_shut=Button(frame_pop_2000_1,text="Reboot", anchor="w", command=reboot_n,
                                highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
            pop_btn_shut.pack(padx=5,pady=20)


        #overclocking_2147    
        def ov_2147():
            popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/ov_2.sh && exit; exec bash\"'")
            popen("mpg123 ~/PiGro-Aid-/scripts/HOLYPiT.mp3")
            
            global pop_2147
            pop_2147=Toplevel(self)
            pop_2147.config(bg='#333333')
            app_width = 500
            app_height = 150
            screen_width = pop_2147.winfo_screenwidth()
            screen_height = pop_2147.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2147.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            pop_2147.resizable(0, 0)

            frame_pop_2147 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
            frame_pop_2147.pack()
            frame_pop_2147['background'] = '#333333'

            frame_pop_2147_1 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
            frame_pop_2147_1.pack(pady=10)
            frame_pop_2147_1['background'] = '#333333'
        
            pop_lbl_2147=Label(frame_pop_2147,anchor="w", text="Done! The new settings take effect after a reboot",font=("Helvetica",12), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
            pop_lbl_2147.pack(pady=20)
            pop_btn_2147=Button(frame_pop_2147_1,text="Continue", anchor="w", command=pop_dest1,
                                highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
            pop_btn_2147.pack(padx=5,pady=20,side=LEFT)
            pop_btn_shut=Button(frame_pop_2147_1,text="Reboot", anchor="w", command=reboot_n,
                                highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
            pop_btn_shut.pack(padx=5,pady=20)
            

        #overclocking_default/reset      
        def set_default():
            popen("xterm -e 'bash -c \"sudo chmod +x ~/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
            popen("xterm -e 'bash -c \"sudo ~/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'")
            

            global pop_default
            pop_default=Toplevel(self)
            pop_default.config(bg='#333333')
            app_width = 500
            app_height = 150
            screen_width = pop_default.winfo_screenwidth()
            screen_height = pop_default.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_default.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            pop_default.resizable(0, 0)

            frame_pop_de = Frame(pop_default, borderwidth=0, relief=GROOVE)
            frame_pop_de.pack()
            frame_pop_de['background'] = '#333333'

            frame_pop_de1 = Frame(pop_default, borderwidth=0, relief=GROOVE)
            frame_pop_de1.pack(pady=10)
            frame_pop_de1['background'] = '#333333'

            pop_lbl_default=Label(frame_pop_de,anchor="w", text="Settings Restored",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
            pop_lbl_default.pack(pady=20)
            pop_btn_default=Button(frame_pop_de1,text="Continue", anchor="w", command=pop_dest,
                                highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
            pop_btn_default.pack(padx=5,pady=20,side=LEFT)
            pop_btn_shut=Button(frame_pop_de1,text="Reboot", anchor="w", command=reboot_n,
                                highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
            pop_btn_shut.pack(padx=5,pady=20)
            

        #overclocking_2200    
        def ov_2200():
            popen("xterm -e 'bash -c \"~/PiGro-Aid-/scripts/ov_3.sh && exit; exec bash\"'")
            popen("mpg123 ~/PiGro-Aid-/scripts/over9000.mp3")
            global pop_2200
            pop_2200=Toplevel(self)
            pop_2200.config(bg='#333333')
            app_width = 500
            app_height = 150
            screen_width = pop_2200.winfo_screenwidth()
            screen_height = pop_2200.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2200.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
            pop_2200.resizable(0, 0)
            
            frame_pop_2200 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
            frame_pop_2200.pack()
            frame_pop_2200['background'] = '#333333'

            frame_pop_2200_1 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
            frame_pop_2200_1.pack(pady=10)
            frame_pop_2200_1['background'] = '#333333'
        
            pop_lbl_2200=Label(frame_pop_2200,anchor="w", text="Done! The new settings take effect after a reboot",font=("Helvetica",16), highlightthickness=0, borderwidth=2,background='#333333', foreground="white",compound=LEFT)
            pop_lbl_2200.pack(pady=20)
            pop_btn_2200=Button(frame_pop_2200_1,text="Continue", anchor="w", command=pop_dest3,
                                highlightthickness=0, borderwidth=0, background='#2246c4', foreground="white", compound=LEFT)
            pop_btn_2200.pack(padx=5,pady=20,side=LEFT)
            pop_btn_shut=Button(frame_pop_2200_1,text="Reboot", anchor="w", command=reboot_n,
                                highlightthickness=0, borderwidth=0, background='#f03838', foreground="white", compound=LEFT)
            pop_btn_shut.pack(padx=5,pady=20)
            


        self.rahmen6 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE, pady=20,padx=50)
        self.rahmen6.pack(padx=20, pady=20, fill='both')
        self.rahmen6['background'] = '#333333'
        
        #Header_Frame
        self.ov_header = Frame(self.rahmen6,borderwidth=0, highlightthickness=0, relief=GROOVE, pady=20,padx=50)
        self.ov_header.pack()
        self.ov_header['background'] = '#333333'
        
        self.tu_lb0 = Label(self.ov_header,justify="left", text="Pi4 Overclocking", highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="white",font=("Helvetica",18),pady=5).grid(column=0, row=0)
        
        global tu_current
        tu_current = Label(self.ov_header, text="Current Settings: Base Clock", highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="green",bg="black",font=("Helvetica",12,"bold"),padx=10)
        tu_current.grid(column=1, row=0,columnspan=2)

        #Butten_Frame
        self.ov_buttons = Frame(self.rahmen6,borderwidth=0, highlightthickness=0, relief=GROOVE, pady=20)
        self.ov_buttons.pack()
        self.ov_buttons['background'] = '#333333'
        
        self.tu_lb3 = Label(self.ov_buttons, text="\nReset Overclocking", highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="#d4244d",font=("Helvetica",14),justify="left").grid(column=1, row=1)        

        self.tu_btn3 = Button(self.ov_buttons,justify="left", image=self.tu03,text="Base Clock       \n1.5 / 1.8 Ghz       ", anchor="w", command=set_default,
                        highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=1, row=2)

        self.tu_lb1 = Label(self.ov_buttons,justify="left", text="\nCrank It Up", highlightthickness=0, borderwidth=2, background='#333333',
                    foreground="#d4244d",font=("Helvetica",14)).grid(column=0, row=3)

        self.tu_btn1 = Button(self.ov_buttons,justify="left", image=self.tu01, text="Arm_Freq = 2000\nGpu_Freq = 750\nOver_Voltage = 6", anchor="w", command=ov_2000,
                        highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold"))
        self.tu_btn1.grid(column=0, row=4)

        self.tu_lb2 = Label(self.ov_buttons,justify="left", text="\nYou Sir... Need A Fan! ", highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="#d4244d",font=("Helvetica",14)).grid(column=1, row=3,padx=10)

        self.tu_btn2 = Button(self.ov_buttons,justify="left", image=self.tu02, text="Arm_Freq = 2147\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2147,
                        highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=1, row=4)

        self.tu_lb4 = Label(self.ov_buttons,justify="left", text="\nTake It To The Max!", highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="#d4244d",font=("Helvetica",14)).grid(column=2, row=3)

        self.tu_btn4 = Button(self.ov_buttons,justify="left", image=self.tu04,text="Arm_Freq = 2200\nGpu_Freq = 750\nOver_Voltage = 8", anchor="w", command=ov_2200,
                        highlightthickness=2, borderwidth=0, background='#333333', foreground="white", compound=LEFT,font=("Helvetica",10,"bold")).grid(column=2, row=4)

        self.tu_info = Label(self.ov_buttons, text="Settings tested with\nPi4 + Ice Tower Cooler and Pi400.\nI take no responsibility if\nyour Pi is damaged.", font=("Helvetica", 8), highlightthickness=0, borderwidth=2,
                    background='#333333', foreground="yellow").grid(column=1, row=8,pady=20)
        



        #Misc_Frame
        self.rahmen622 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE, padx=100, pady=10)#
        self.rahmen622.pack(padx=40, pady=20, fill='both')
        self.rahmen622['background'] = '#333333'
        
        self.rahmen61 = Frame(self.rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=30, pady=10)#
        self.rahmen61.pack(side=LEFT)
        self.rahmen61['background'] = '#333333'

        self.rahmen62 = Frame(self.rahmen622,borderwidth=0, highlightthickness=0, relief=GROOVE, padx=10, pady=10)#
        self.rahmen62.pack(padx=10, side=LEFT)
        self.rahmen62['background'] = '#333333'


        def OV1_label():
            tu_current.config(text="Current Settings: Crank It Up",fg="yellow",bg="black")

        def OV2_label():
            tu_current.config(text="Current Settings: You Sir... Need A Fan!",fg="red",bg="black")
            
        def OV3_label():
            tu_current.config(text="Current Settings: Take It To The Max!",fg="pink",bg="black")

            

        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking1", fp):
                print (line)
                if line :
                    OV1_label()
                    
                    
                    
        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking2", fp):
                print (line)
                if line :
                    OV2_label()


                    
        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking3", fp):
                print (line)
                if line :
                    OV3_label()

        def z_ram():
            global z_ram_pop
            z_ram_pop=Toplevel(self)
            z_ram_pop['background'] = '#333333'
            
            def top_inst():
                os.system("xterm -e 'bash -c \"~/PiGro-Aid-/essentials/bpytop/install.sh; exec bash\"'")
            def top_uninst():
                os.system("xterm -e 'bash -c \"~/PiGro-Aid-/essentials/bpytop/uninstall.sh; exec bash\"'")

            logo = Label(z_ram_pop, image=self.ip03, text="ZRAM",font=("Helvetica",16), anchor="w",
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
            
            bt_inst = Button(z_ram_pop, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=z_inst).grid(column=0, row=1)
            
            bt_info = Label(z_ram_pop, text="\nzram is a Linux kernel feature and userspace tools for creating compressible RAM-based block devices.\nIt has been included as a module of the mainline Linux since kernel version 3.14. \nStarting with kernel version 3.15, zram supports multiple compression streams and the ability to change \nthe compression algorithms without a system restart.",justify="left", anchor="w",
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0)




        def btswitch_64():
            global six4_mode_pop
            six4_mode_pop=Toplevel(self)
            six4_mode_pop['background'] = '#333333'
            

            
            def top_inst():
                os.system("xterm -e 'bash -c \"sudo apt-get install -y raspbian-nspawn-64; exec bash\"'")
            logo = Label(six4_mode_pop, image=self.ip03, text="64-Bit\nMode",font=("Helvetica",16), anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=0, row=0)
            
            bt_inst = Button(six4_mode_pop, text="Install",font=("Helvetica",11,"bold"),justify="left", anchor="w",
                            highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=LEFT,command=z_inst).grid(column=0, row=1)
            
            bt_info = Label(six4_mode_pop, text="\nAdds 64 bit support.\nRun >ds64-shell< in terminal.\nBut I recommend using the RPi OS 64 bit.\nYou can find the link under LINK TAB",justify="left", anchor="w",
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP).grid(column=1, row=0)


        self.tu_zbtn = Button(self.rahmen61, text="ZRAM",font=("Helvetica",16), anchor="w", command=z_ram,highlightthickness=0, borderwidth=0, background='#333333', compound=LEFT,foreground="#d4244d").grid(column=0, row=1)

        self.tu_bbtn=Button(self.rahmen62, text="64 Bit Mode",font=("Helvetica",16), anchor="w", command=btswitch_64,highlightthickness=0, borderwidth=0, background='#333333', foreground="#d4244d", compound=LEFT).grid(column=0, row=1)

        self.info_tuning_btn = Button(self, image=self.tpinfm,highlightthickness=0,
                        borderwidth=0,command=info_tuning_tab)
        self.info_tuning_btn.place(x=665,y=40)


#Links
class Frame7(ttk.Frame):
    def __init__(self, container):
        super().__init__()

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
            
        def ubi_bubi():
            popen("xdg-open https://ubuntu.com/download/raspberry-pi")
            
        def popo_bubi():
            popen("xdg-open https://pop.system76.com/")
            
        def six4_berry():
            popen("xdg-open https://downloads.raspberrypi.org/raspios_arm64/images/")

        def pi_doc():
            popen("xdg-open https://www.raspberrypi.com/documentation/")
            
            
           

        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.tab8_dist1 = Image.open('icons/TwisterOSLogo-Large-New3.png')
        self.di01 = ImageTk.PhotoImage(self.tab8_dist1)
        self.dl01 = Label(image=self.di01)

        self.tab8_dist2 = Image.open('icons/Puppy_Linux_Logo.png')
        self.di02 = ImageTk.PhotoImage(self.tab8_dist2)
        self.dl02 = Label(image=self.di02)

        self.tab8_dist3 = Image.open('icons/dietpi.png')
        self.di03 = ImageTk.PhotoImage(self.tab8_dist3)
        self.dl03 = Label(image=self.di03)

        self.tab8_dist4 = Image.open('icons/MX-icon.png')
        self.di04 = ImageTk.PhotoImage(self.tab8_dist4)
        self.dl04 = Label(image=self.di04)

        self.tab8_dist5 = Image.open('icons/fydeos.png')
        self.di05 = ImageTk.PhotoImage(self.tab8_dist5)
        self.dl05 = Label(image=self.di05)

        self.tab8_dist6 = Image.open('icons/android.png')
        self.di06 = ImageTk.PhotoImage(self.tab8_dist6)
        self.dl06 = Label(image=self.di06)

        self.tab8_dist7 = Image.open('icons/logo_berryserver.png')
        self.di07 = ImageTk.PhotoImage(self.tab8_dist7)
        self.dl07 = Label(image=self.di07)

        self.tab8_dist8 = Image.open('icons/NCP.png')
        self.di08 = ImageTk.PhotoImage(self.tab8_dist8)
        self.dl08 = Label(image=self.di08)

        self.pop_os_ico = ImageTk.PhotoImage(Image.open("icons/popo_os_icon.png"))
        self.pop_os_icol = Label(image=self.pop_os_ico)

        self.ubu_os_ico = ImageTk.PhotoImage(Image.open("icons/Logo-ubuntu_.png"))
        self.ubu_os_icol = Label(image=self.ubu_os_ico)

        self.pi64_os_ico = ImageTk.PhotoImage(Image.open("icons/Raspberry_Pi_Logo.png"))
        self.pi64_os_icol = Label(image=self.pi64_os_ico)

        self.rahmen = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,padx=10,pady=20)
        self.rahmen.grid(row=0,rowspan=11, column=0,pady=20,padx=40)
        self.rahmen['background'] = '#333333'

        sys_btn2 = Label(self.rahmen,text="Distros",
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white",font=("Helvetica",16,"bold"))
        sys_btn2.pack()

        self.dist_btn1 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di01,anchor="w", text="Twister OS ", command=down_twist,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn2 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di02,anchor="w", text="Puppy Linux", command=down_puppy,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn3 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di03,anchor="w", text="DietPi     ", command=down_diet,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn4 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di04,anchor="w", text="MX Linux   ", command=down_mx,
                        highlightthickness=0, borderwidth=0, background='#333333',   foreground="white",width=150).pack()

        self.dist_btn5 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di05,anchor="w", text="FydeOS     ", command=down_fy,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn6 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di06,anchor="w", text="Android    ", command=down_kk,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn7 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di07,anchor="w", text="Berryserver", command=down_bb,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn8 = Button(self.rahmen,compound=LEFT,justify="left", image=self.di08,anchor="w", text="NextCloudPi", command=down_NCP,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn9 = Button(self.rahmen,compound=LEFT,justify="left", image=self.ubu_os_ico,anchor="w", text="Ubuntu", command=ubi_bubi,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn10 = Button(self.rahmen,compound=LEFT,justify="left", image=self.pop_os_ico,anchor="w", text="Pop_OS", command=popo_bubi,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()

        self.dist_btn11 = Button(self.rahmen,compound=LEFT,justify="left", image=self.pi64_os_ico,anchor="w", text="RPi OS 64 Bit", command=six4_berry,
                        highlightthickness=0, borderwidth=0, background='#333333', foreground="white",width=150).pack()
        


        self.rahmen3 = Frame(self,borderwidth=0, highlightthickness=2, relief=GROOVE,pady=10)
        self.rahmen3.grid(row=0, column=1,pady=20)
        self.rahmen3['background'] = '#333333'

        sys_btn2 = Label(self.rahmen3,  text=" Other ",
                          highlightthickness=0, borderwidth=0, background='#333333', foreground="white", compound=TOP,font=("Helvetica",14,"bold"))
        sys_btn2.pack()
        
        choice_link1=Button(sys_btn2, anchor="w", width=50,text="Mankiere.com (Commandline Database)", command=link_mankier,
                 highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()
        
        choice_link2=Button(sys_btn2,anchor="w", width=50,text="Guake (Drop Down Terminal)",  command=link_guake,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2,anchor="w", width=50,text="OnBoard (Onscreen Keyboard)",  command=link_onBoard,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2, anchor="w",width=50,text="Draculatheme.com", command=link_drac,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2, anchor="w",width=50,text="Starship (Cross-Shell-Promt)", command=link_star,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link1=Button(sys_btn2,width=50,text="LernLinux.tv", anchor="w", command=lern_l,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2,width=50,text="Rocket Beans(ger.)", anchor="w", command=rb_tv,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2,width=50,text="52Pi", anchor="w", command=fitwo_p,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()

        choice_link2=Button(sys_btn2,width=50,text="LCD Wiki", anchor="w", command=l4_e,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()
        
        choice_link2=Button(sys_btn2,width=50,text="Offical Raspberry Pi Documentation", anchor="w", command=pi_doc,
                         highlightthickness=0, borderwidth=0, background='#333333', foreground="white").pack()



#Poll
class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.bg = PhotoImage(file="icons/pigro_bg.png")
        self.bg_label = Label(self,image=self.bg)
        self.bg_label.place(x=-1,y=-1, relwidth=1,relheight=1)

        self.pig_x = Image.open('icons/poke_pig.jpg')
        self.pg0x = ImageTk.PhotoImage(self.pig_x)
        self.pl0x = Label(image=self.pg0x)


        def pick_at_you():
            global pop_pig
            pop_pig=Toplevel(self)
            pop_pig['background'] = 'white'
            
            poke_pig = Label(pop_pig,image=self.pg0x,background='#333333').pack()

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


        self.pig_1 = Image.open('icons/pigpi_btn.png')
        self.pg01 = ImageTk.PhotoImage(self.pig_1)
        self.pl01 = Label(image=self.pg01)

        self.pig_logo = Button(self,image=self.pg01,background='#333333', command=pick_at_you).pack(pady=40)

        self.rahmen102 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2)
        self.rahmen102.pack(padx=40, pady=20, fill='both')
        self.rahmen102['background'] = '#333333'


        self.poke_pig_21 = Label(self.rahmen102,justify="left",text="I never thought that so many people would use Pigro.\nAs open source lives from community,I want you to have a say in that too.\nIf you click on poll, you can vote on what else I should add to Pigro.\nSo ... let's fatten up the hog! xD\nIf you want to support me, click on the RedBubble button below.\nHere you can get Pi / Linux design from me.\n\nBest regards\n\nTimo\n\nQuestions or suggestions?:",font=("Helvetica",12),background='#333333', fg="white",padx=5,pady=3).pack()


        self.mail = Entry(self.rahmen102, bd=5, width=31, borderwidth=1)
        self.mail.insert(END,"pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)


        self.rahmen101 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2)
        self.rahmen101.pack(padx=40, pady=20, fill='both')
        self.rahmen101['background'] = '#333333'





        self.pig_btn_1 = Button(self.rahmen101,text="User Poll", highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="#2FFC05", command=poll,font=(("Helvetica,bold"),"12","bold")).grid(column=0,row=0,pady=20, padx=20)

        self.pig_btn_2 = Button(self.rahmen101,text="Wallpapers", highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="#EBFC05", command=wpaps,font=(("Helvetica,bold"),"12","bold")).grid(column=1,row=0,pady=20)

        self.pig_btn_3 = Button(self.rahmen101,text="PiGro Manuel", highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="#053AFC",command=wiki,font=(("Helvetica,bold"),"12","bold")).grid(column=2,row=0,pady=20, padx=20)

        self.pig_btn_4 = Button(self.rahmen101,text="Redbubble.com", highlightthickness=0,
                            borderwidth=0, background='#333333', foreground="#FC05A0",command=red_bub,font=(("Helvetica,bold"),"12","bold")).grid(column=3,row=0,pady=20, padx=20)

#TOOLTIPZ
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




#End Of The Line xD xD xD... If you're reading this, you've read the code that I've put into over 1000 hours of work.
if __name__ == '__main__':
    app = MainApplication()
    app.mainloop()