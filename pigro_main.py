import os
import os.path
import tkinter as tk
from tkinter.dialog import DIALOG_ICON
from turtle import width
import tkinter.font as tkFont
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
from datetime import datetime
import distro
import socket
from gpiozero import CPUTemperature
from pathlib import Path
from cgitb import enable
from pynotifier import Notification


# Define Home
global home
home = str(Path.home())
print(f"{home} is your home directory!")

# Get Desktop Environment
global get_de
get_de = os.environ.get("XDG_CURRENT_DESKTOP")
print("You are using: " + get_de)


# def reboot_n():
#    popen("sudo reboot")


# Main Winddow / Notebook Config
class MainApplication(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("PiGro - Vincitore_Fedele")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self["background"] = "#333333"
        self.resizable(0, 0)
        app_width = 1000
        app_height = 700
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.wait_visibility(self)
        self.wm_attributes("-alpha", 0.95)

        self.notebook = ttk.Notebook(self)

        self.Frame1 = Frame1(self.notebook)
        self.Frame2 = Frame2(self.notebook)
        self.Frame3 = Frame3(self.notebook)
        self.Frame4 = Frame4(self.notebook)
        self.Frame5 = Frame5(self.notebook)
        self.Frame6 = Frame6(self.notebook)
        self.Frame7 = Frame7(self.notebook)
        # self.Frame9 = Frame9(self.notebook)
        self.Frame8 = Frame8(self.notebook)

        # Notebook Decoration TOP_BOTTOM
        tabi = Image.open("images/backgrounds/side_bar.png")
        tabp = ImageTk.PhotoImage(tabi)
        tabl = Label(self.notebook, image=tabp)
        tabl.image = tabp
        tabl["background"] = "#333333"
        tabl.place(x=-2, y=0)

        tab2i = Image.open("images/backgrounds/side_bar2.png")
        tab2p = ImageTk.PhotoImage(tab2i)
        tab2l = Label(self.notebook, image=tab2p)
        tab2l.image = tab2p
        tab2l["background"] = "#333333"
        tab2l.place(x=-2, y=630)

        self.welcome_icon = PhotoImage(file=r"images/icons/Logotab.png")
        self.system_icon = PhotoImage(file=r"images/icons/system.png")
        self.update_icon = PhotoImage(file=r"images/icons/updatetab.png")
        self.install_icon = PhotoImage(file=r"images/icons/installer_ico.png")
        self.look_icon = PhotoImage(file=r"images/icons/look.png")
        self.tuning_icon = PhotoImage(file=r"images/icons/tuning.png")
        self.look_icon = PhotoImage(file=r"images/icons/look.png")
        self.tuning_icon = PhotoImage(file=r"images/icons/tuning.png")
        self.dm_icon = PhotoImage(file=r"images/icons/dm.png")
        self.pig_icon = PhotoImage(file=r"images/icons/pigpi.png")
        self.play_icon = PhotoImage(file=r"images/icons/play_ground.png")
        self.cam_icon = PhotoImage(file=r"images/icons/PyPiCam_Go.png")
        self.config_icon = PhotoImage(file=r"images/icons/config_txt.png")

        # Tabs
        self.notebook.add(
            self.Frame1, compound=LEFT, text="Welcome", image=self.welcome_icon
        )
        self.notebook.add(
            self.Frame3, compound=LEFT, text="System", image=self.system_icon
        )
        self.notebook.add(
            self.Frame2, compound=LEFT, text="Update", image=self.update_icon
        )
        self.notebook.add(
            self.Frame4, compound=LEFT, text="Software", image=self.install_icon
        )
        self.notebook.add(self.Frame5, compound=LEFT, text="Look", image=self.look_icon)
        self.notebook.add(
            self.Frame6, compound=LEFT, text="Tuning", image=self.tuning_icon
        )
        self.notebook.add(self.Frame7, compound=LEFT, text="Links", image=self.dm_icon)

        #        self.notebook.add(
        #            self.Frame9, compound=LEFT, text="Pi Camera", image=self.cam_icon
        #        )

        self.notebook.add(
            self.Frame8, compound=LEFT, text="PiG-Grow", image=self.pig_icon
        )

        self.notebook.pack()

        # Notebook Themeing
        self.noteStyler = ttk.Style(self)
        self.noteStyler.configure(
            "TNotebook",
            borderwidth=0,
            background="#333333",
            tabposition="w",
            highlightthickness=0,
        )
        self.noteStyler.configure(
            "TNotebook.Tab",
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 16),
            width=13,
            highlightthickness=0,
        )
        self.noteStyler.configure("TFrame", background="#333333")
        self.noteStyler.map(
            "TNotebook.Tab",
            background=[("selected", "#333333")],
            foreground=[("selected", "#d4244d")],
        )


# Welcome Tab
class Frame1(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def changelog():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Changelog")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/changelog.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)
            # scrollbar.config(command=mylist.yview)

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        self.bg = PhotoImage(file=f"{home}/PiGro-Aid-/images/backgrounds/pigronew.png")
        self.welcome_canvas = Canvas(self, width=900, height=700, highlightthickness=0)
        self.welcome_canvas.pack(fill="both", expand=True)
        self.welcome_canvas.create_image(0, 0, image=self.bg, anchor="nw")

        self.web_link = tk.Label(
            self,
            text=r"https://www.actionschnitzel.de/PiGro/",
            fg="blue",
            cursor="hand2",
        )
        self.web_link.place(x=480, y=645)
        self.web_link.bind("<Button-1>", callback)

        self.web_link["background"] = "#333333"

        self.gihub_link = tk.Label(
            self,
            text=r"https://github.com/actionschnitzel/PiGro-Aid-",
            fg="blue",
            cursor="hand2",
        )
        self.gihub_link.place(x=480, y=670)
        self.gihub_link.bind("<Button-1>", callback)

        self.gihub_link["background"] = "#333333"

        self.changelog_btn = Button(
            self,
            text="Changelog",
            font=(("Helvetica,bold"), "14", "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#fbc463",
            foreground="grey",
            command=changelog,
        ).place(x=105, y=445)


# Update Tab
class Frame2(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def info_update_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Update Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/update_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)
            # scrollbar.config(command=mylist.yview)

        def update_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 120x25 -e "{home}/PiGro-Aid-/scripts/update.sh && read -p PRESS_ENTER && exit; exec bash"'
                % self.wid
            )

        def upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 120x25 -e "{home}/PiGro-Aid-/scripts/upgrade.sh && read -p PRESS_ENTER && exit; exec bash"'
                % self.wid
            )

        def full_upgrade_btn():
            os.popen(
                f'xterm -into %d -bg Grey1 -geometry 120x25 -e "{home}/PiGro-Aid-/scripts/full_upgrade.sh && read -p PRESS_ENTER && exit; exec bash"'
                % self.wid
            )

        def autoremove_btn():
            os.popen(
                'xterm -into %d -bg Grey1 -geometry 120x25 -e "sudo apt autoremove -y && sudo apt clean && sudo apt-get purge -y && read -p PRESS_ENTER && exit ; exec bash"'
                % self.wid
            )

        def add_unsi_btn():
            os.popen(
                f"xterm -into %d -bg Grey1 -geometry 120x25 -e {home}/PiGro-Aid-/scripts/addunsignedrepo.sh &"
                % self.wid
            )

        def button_gpk():
            popen("sudo pi-gpk-update-viewer")

        def save_list():
            os.system("sudo chmod 777 -R /etc/apt/sources.list")
            text_file = open("/etc/apt/sources.list", "w")
            text_file.write(s_list.get(1.0, END))
            m_text = "\
        \n\
        \n\
        Sources List has been saved\n\
        \n\
        \n\
        "
            messagebox.showinfo(message=m_text, title="Infos")

        def reboot_n():
            popen("sudo reboot")

        self.update_info_btn = PhotoImage(file=r"images/icons/info_m.png")

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.source_list_frame = Frame(self, relief=GROOVE, borderwidth=0)
        self.source_list_frame.pack(padx=45, pady=40, anchor=W)
        self.source_list_frame["background"] = "#333333"

        self.termf = Frame(
            self, height=270, width=700, padx=10, highlightthickness=2, borderwidth=0
        )
        self.wid = self.termf.winfo_id()
        self.termf["background"] = "#333333"

        s_list = Text(
            self.source_list_frame, width=1550, height=10, highlightthickness=1
        )
        text_file = open("/etc/apt/sources.list", "r")
        stuff = text_file.read()
        s_list.insert(END, stuff)
        text_file.close()
        s_list.pack(anchor="w")

        self.update_btn_frame = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=2, padx=5, pady=5
        )
        self.update_btn_frame.pack(padx=45, anchor="w")
        self.update_btn_frame["background"] = "#333333"

        self.update_button = Button(
            self.update_btn_frame,
            text="Update",
            width=15,
            anchor="w",
            command=update_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.update_button.grid(column=0, row=0)

        self.update_button = Button(
            self.update_btn_frame,
            text="Upgrade",
            width=15,
            anchor="w",
            command=upgrade_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.update_button.grid(column=0, row=1)

        self.fupgrade_button = Button(
            self.update_btn_frame,
            text="Full Upgrade",
            width=15,
            anchor="w",
            command=full_upgrade_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.fupgrade_button.grid(column=0, row=2)

        self.gpk_button = Button(
            self.update_btn_frame,
            text="GPK UpdateViewer",
            width=15,
            anchor="w",
            command=button_gpk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.gpk_button.grid(column=0, row=3)

        self.auth_button = Button(
            self.update_btn_frame,
            text="Allow Sources",
            width=20,
            anchor="w",
            command=add_unsi_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.auth_button.grid(column=1, row=0)

        self.rm_button = Button(
            self.update_btn_frame,
            text="Remove Config Files",
            width=20,
            anchor="w",
            command=autoremove_btn,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 12, "bold"),
        )
        self.rm_button.grid(column=1, row=1)

        self.sv_button = Button(
            self.update_btn_frame,
            text="Save Source List",
            width=20,
            anchor="w",
            command=save_list,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#d4244d",
            font=("Helvetica", 12, "bold"),
        )
        self.sv_button.grid(column=1, row=2)

        self.reboot_button = Button(
            self.update_btn_frame,
            text="Reboot",
            width=20,
            anchor="w",
            command=reboot_n,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#d4244d",
            font=("Helvetica", 12, "bold"),
        )
        self.reboot_button.grid(column=1, row=3)

        self.termf.pack(padx=45, pady=20, anchor=W)

        self.info_up_btn = Button(
            self,
            image=self.update_info_btn,
            highlightthickness=0,
            borderwidth=0,
            command=info_update_tab,
        )
        self.info_up_btn.place(x=650, y=320)


# System tab
class Frame3(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def button_boot():
            popen("xterm -e 'bash -c \"dmesg; exec bash\"'")

        def rm_vscode():
            popen(
                "xterm -e 'bash -c \"sudo rm /etc/apt/sources.list.d/vscode.list & echo DONE!; exec bash\"'"
            )

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
            popen("sudo xdg-open $HOME")
            print("With great power comes great responsibility")
            Notification(
                title="Sudo File Manager\n",
                description="With great power comes great responsibility\n\n                          - Oncle Ben",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

        def button_lk():
            global pop_kernel
            pop_kernel = Toplevel(self)
            pop_kernel.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_kernel.winfo_screenwidth()
            screen_height = pop_kernel.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_kernel.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_kernel.resizable(0, 0)

            def pop_kernel_dest():
                pop_kernel.destroy()

            def do_it():
                popen("xterm -e 'bash -c \"sudo BRANCH=next rpi-update; exec bash\"'")
                print("Kernel Upgrade GO!")
                pop_kernel.destroy()

            frame_pop_kernel = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel.pack()
            frame_pop_kernel["background"] = "#333333"

            frame_pop_kernel_1 = Frame(pop_kernel, borderwidth=0, relief=GROOVE)
            frame_pop_kernel_1.pack()
            frame_pop_kernel_1["background"] = "#333333"

            pop_lbl_2000 = Label(
                frame_pop_kernel,
                anchor="w",
                text="Do you really want to Upgrade the Kernel?",
                font=("Helvetica", 12),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_2000.pack(pady=20)

            pop_btn_2000 = Button(
                frame_pop_kernel_1,
                text="No",
                anchor="w",
                command=pop_kernel_dest,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_2000.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_kernel_1,
                text="Do It!",
                anchor="w",
                command=do_it,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        def button_dpfc():
            popen("xterm -e 'bash -c \"deskpi-config; exec bash\"'")

        def button_auto():
            popen("xfce4-session-settings")

        def button_xsett():
            popen("xfce4-settings-manager")

        def info_system_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("System Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/system_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

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
                st.connect(("10.255.255.255", 1))
                IP = st.getsockname()[0]
            except Exception:
                IP = "127.0.0.1"
            finally:
                st.close()
            return IP

        # Icon Set
        self.bp01 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp02 = PhotoImage(file=r"images/icons/raspberry-pi-logo.png")
        self.bp03 = PhotoImage(file=r"images/icons/terminal.png")
        self.bp033 = PhotoImage(file=r"images/icons/terminal3.png")
        self.bp04 = PhotoImage(file=r"images/icons/gparted.png")
        self.bp05 = PhotoImage(file=r"images/icons/indicator-cpufreq.png")
        self.bp06 = PhotoImage(file=r"images/icons/folder.png")
        self.bp07 = PhotoImage(file=r"images/icons/links.png")
        self.ico_m = PhotoImage(file=r"images/icons/gui_icon.png")
        self.ico_m2 = PhotoImage(file=r"images/icons/weblink_icon.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        # Button Set/Frame1
        self.rahmen2 = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, padx=60, pady=10
        )
        self.rahmen2.pack(padx=40, pady=20, fill="both")
        self.rahmen2["background"] = "#333333"

        sys_btn6 = Button(
            self.rahmen2,
            image=self.bp01,
            text="Raspi-Config CLI",
            command=pi_configbutton,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn6.grid(row=0, column=0)

        sys_btn1 = Button(
            self.rahmen2,
            image=self.bp01,
            text="Raspi-Config GUI",
            command=pi_configbutton2,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn1.grid(row=0, column=1)

        sys_btn2 = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Config.txt",
            command=contxt_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn2.grid(row=0, column=2)

        sys_btnvs = Button(
            self.rahmen2,
            image=self.bp03,
            text="rm vscode.list ",
            command=rm_vscode,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btnvs.grid(row=0, column=3)

        sys_btn3 = Button(
            self.rahmen2,
            image=self.bp04,
            text="Gparted",
            command=gparted_exec,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn3.grid(row=1, column=0)

        if os.path.isfile("/usr/sbin/gparted"):
            print("Gparted exist")
            sys_btn3.configure(state=NORMAL)
        else:
            print("Gparted does not exist")
            sys_btn3.configure(state=DISABLED)

        sys_btn4 = Button(
            self.rahmen2,
            image=self.bp05,
            text="NeoFetch",
            command=neofetch_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn4.grid(row=1, column=1)

        if os.path.isfile("/bin/neofetch"):
            print("Neofetch exist")
            sys_btn4.configure(state=NORMAL)
        else:
            print("Neofetch does not exist")
            sys_btn4.configure(state=DISABLED)

        sys_btn5 = Button(
            self.rahmen2,
            image=self.bp06,
            text="FM God Mode",
            command=onc_ben,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn5.grid(row=1, column=2)
        sys_btn5_ttp = CreateToolTip(
            sys_btn5,
            "This puts the filemanager on SUDO. You could break the system. Warned you!! ;-)",
        )

        sys_btn6 = Button(
            self.rahmen2,
            image=self.bp07,
            text="Upgrade Linux Kernel",
            command=button_lk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn6.grid(row=1, column=3)

        sys_btn7 = Button(
            self.rahmen2,
            image=self.bp03,
            text="DeskpiPro Control",
            command=button_dpfc,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn7.grid(row=2, column=0)

        sys_btn8 = Button(
            self.rahmen2,
            image=self.bp03,
            text="Boot Log",
            command=button_boot,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn8.grid(row=2, column=1)

        sys_btn9 = Button(
            self.rahmen2,
            image=self.bp033,
            text="Xfce Autostarts",
            command=button_auto,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn9.grid(row=2, column=2)
        sys_btn9.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_btn9.configure(state=NORMAL)

        sys_btn91 = Button(
            self.rahmen2,
            image=self.bp033,
            text="Xfce Settings",
            command=button_xsett,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn91.grid(row=2, column=3)
        sys_btn91.configure(state=DISABLED)
        if get_de == "XFCE":
            sys_btn91.configure(state=NORMAL)

        sys_btn10 = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Network Settings",
            command=net_set,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn10.grid(row=3, column=0)

        sys_btn11 = Button(
            self.rahmen2,
            image=self.ico_m,
            text="Taskmanager",
            command=lx_task,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 10, "bold"),
        )
        sys_btn11.grid(row=3, column=1)

        # System_Info/Frame2

        # Parameters for System
        global distro
        distro = distro.id()

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

        self.sys_info_main_frame = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10, padx=20
        )
        self.sys_info_main_frame.pack(padx=40, pady=20, fill="both")
        self.sys_info_main_frame["background"] = "#333333"

        self.sys_frame_left = Frame(
            self.sys_info_main_frame, borderwidth=0, highlightthickness=0, relief=GROOVE
        )
        self.sys_frame_left.pack(side=LEFT)  # grid(row=1, column=0)
        self.sys_frame_left["background"] = "#333333"

        self.sys_frame_right = Frame(
            self.sys_info_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=10,
            padx=20,
        )
        self.sys_frame_right.pack(pady=20)  # grid(row=1, column=1)
        self.sys_frame_right["background"] = "#333333"

        self.my_img = ImageTk.PhotoImage(Image.open("images/icons/deb_logo.png"))
        self.my_label = Label(image=self.my_img)

        self.sysinf0 = Label(
            self.sys_frame_right,
            image=self.my_img,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#d4244d",
            pady=20,
            padx=20,
            anchor=E,
        )
        self.sysinf0.pack()

        self.sysinf0 = Label(
            self.sys_frame_left,
            text=f"System: {my_system.system}",
            font=("Helvetica", 10, "bold"),
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=40,
            anchor=W,
        ).pack()

        self.sysinfd = Label(
            self.sys_frame_left,
            text=f"Distro: {distro}",
            justify="left",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf1 = Label(
            self.sys_frame_left,
            text=f"Device Name: {my_system.node}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=f"Board: {Pi_Model.read()}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf2 = Label(
            self.sys_frame_left,
            text=f"Kernel: {my_system.release}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"Architecture: {my_system.machine}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf8 = Label(
            self.sys_frame_left,
            text="",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        )
        self.sysinf8.pack()

        self.sysinf6 = Label(
            self.sys_frame_left,
            text=f"CPU Max Freq: {cpufreq.max:.2f}Mhz",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf7 = Label(
            self.sys_frame_left,
            text=f"CPU Min Freq: {cpufreq.min:.2f}Mhz",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf10 = Label(
            self.sys_frame_left,
            text="",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        )
        self.sysinf10.pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"RAM Total: {get_size(svmem.total)}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf3 = Label(
            self.sys_frame_left,
            text=f"SWAP Total: {get_size(swap.total)}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.sysinf9 = Label(
            self.sys_frame_left,
            text=f"IP Address: {IPAddr}",
            justify="left",
            background="#333333",
            foreground="white",
            width=40,
            font=("Helvetica", 10, "bold"),
            anchor=W,
        ).pack()

        self.info_sys_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_system_tab,
        )
        self.info_sys_btn.place(x=700, y=620)

        def refresh():

            # Parameters for System
            pid = os.getpid()
            ps = psutil.Process(pid)
            cpufreq = psutil.cpu_freq()
            svmem = psutil.virtual_memory()
            swap = psutil.swap_memory()
            cpu = CPUTemperature()
            # print(cpu)

            self.sysinf8.configure(text=f"Current CPU Freq: {cpufreq.current:.2f}Mhz")
            self.sysinf10.configure(text=f"CPU Temp: {cpu.temperature:.1f} °C")
            self.after(1000, refresh)

        refresh()


# [Overclocking_Legend] button in Frame6
class Tuning_Legende(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = "#333333"
        self.title("Overclocking Legend")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 500
        app_height = 600
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.tu_1 = PhotoImage(file=r"images/icons/PiGroOV_rm.png")
        self.tu_2 = PhotoImage(file=r"images/icons/PiGroOV1.png")
        self.tu_3 = PhotoImage(file=r"images/icons/PiGroOV2.png")
        self.tu_4 = PhotoImage(file=r"images/icons/PiGroOV3.png")
        self.tu_5 = PhotoImage(file=r"images/icons/PiGroOV4.png")

        # Main Frame
        self.tu_main_frame = Frame(self, bg="#333333")
        self.tu_main_frame.pack(pady=20)
        # xd
        # Reset
        self.rm_lbl = Label(
            self.tu_main_frame,
            text="Reset Settings",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.rm_lbl.grid(row=0, column=0)

        self.rm_ov = Label(self.tu_main_frame, image=self.tu_1, bg="#333333")
        self.rm_ov.grid(row=1, column=0)

        self.rm_text = Label(
            self.tu_main_frame,
            text="Removes all\noverclocking parameters\n\n",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.rm_text.grid(row=1, column=1)

        # OV_1
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Crank It Up!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=2, column=0)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_2, bg="#333333", fg="white")
        self.ov_1.grid(row=3, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2000\ngpu_freq = 750\nover_voltage = 6\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=3, column=1)

        # OV_2
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Sir, You Need A Fan!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=4, column=0)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_3, bg="#333333", fg="white")
        self.ov_1.grid(row=5, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2147\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=5, column=1)

        # OV_3
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Take It To The Max!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=6, column=0)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_4, bg="#333333", fg="white")
        self.ov_1.grid(row=7, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2200\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=7, column=1)

        # OV_4
        self.ov1_lbl = Label(
            self.tu_main_frame,
            text="Honey,the fuse blew again!",
            bg="#333333",
            fg="#d4244d",
            font=("Helvetica", 14),
            justify=LEFT,
        )
        self.ov1_lbl.grid(row=8, column=0)

        self.ov_1 = Label(self.tu_main_frame, image=self.tu_5, bg="#333333", fg="white")
        self.ov_1.grid(row=9, column=0)

        self.ov_1_text = Label(
            self.tu_main_frame,
            text="arm_freq = 2300\ngpu_freq = 700\nover_voltage = 14\nforce_turbo = 1",
            justify=LEFT,
            bg="#333333",
            fg="white",
        )
        self.ov_1_text.grid(row=9, column=1)


# Software Tab
class Frame4(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def info_installer_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Installer Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/installer_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def open_must_haves():
            os.system(f"python3 {home}/PiGro-Aid-/Shop/Shop.py")

        def snapcraft():
            popen("xdg-open https://snapcraft.io/store")

        def flatflat():
            popen("xdg-open https://flathub.org/")

        # images/icons/BG
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.ipshop = PhotoImage(file=r"images/icons/shop.png")
        self.ipfinst = PhotoImage(file=r"images/icons/fast_install.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")

        # Shop
        self.rahmen_shop = Frame(self, borderwidth=0, highlightthickness=1)
        self.rahmen_shop.pack(padx=40, pady=40)
        self.rahmen_shop["background"] = "#333333"

        self.shop_click = Button(
            self.rahmen_shop,
            image=self.ipshop,
            command=open_must_haves,
            highlightthickness=1,
            borderwidth=5,
            background="green",
            foreground="white",
            compound=LEFT,
            width=500,
        )
        self.shop_click.pack()
        self.shop_click_ttp = CreateToolTip(
            self.shop_click,
            "The shop is currently deactivated due to renovations. All installers can be found under Must Haves",
        )
        # Fast_Installer Main_Frame
        self.fast_main_frame = Frame(
            self, relief=GROOVE, borderwidth=1, highlightthickness=1, pady=10, padx=10
        )
        self.fast_main_frame["background"] = "green"
        self.fast_main_frame.pack()

        # Definition Fast Installer Label
        self.sysinf0 = Label(
            self.fast_main_frame,
            image=self.ipfinst,
            compound=LEFT,
            anchor="n",
            font=("Helvetica", 16),
            highlightthickness=0,
            borderwidth=0,
            background="green",
            foreground="white",
            pady=20,
        )
        self.sysinf0.pack()

        # Sec Fast Frame
        self.fast_sec_frame = Frame(
            self.fast_main_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=1,
            padx=42,
            pady=20,
        )
        self.fast_sec_frame.pack()
        self.fast_sec_frame["background"] = "#333333"

        # apt-get_entry
        self.apt_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.apt_frame.pack()
        self.apt_frame["background"] = "#333333"

        fo = open("scripts/apt_cache.list", "r")
        content = fo.readlines()
        for i, s in enumerate(content):
            content[i] = s.strip()
        # print(content)

        def check_input(event):
            value = event.widget.get()

            if value == "":
                self.combo_box["values"] = content
            else:
                data = []
                for item in content:
                    if value.lower() in item.lower():
                        data.append(item)

                self.combo_box["values"] = data

        def inst_btn1():
            entry_text = self.combo_box.get()
            popen(
                f"xterm -e 'bash -c \"sudo apt-get install {self.combo_box.get()}; exec bash\"'"
            )

        def uninst_btn1():
            popen("sudo synaptic")

        def inst_syn():
            popen("xterm -e 'bash -c \"sudo apt-get install synaptic; exec bash\"'")

        self.p4 = PhotoImage(file=r"images/icons/apt-get.png")

        self.eingabefeld1 = Entry(self.apt_frame, bd=5, width=31, borderwidth=1)

        self.combo_box = ttk.Combobox(self.apt_frame)
        self.combo_box["values"] = content
        self.combo_box.bind("<KeyRelease>", check_input)
        self.combo_box.config(width=30)

        self.apt_inst_btn = Button(
            self.apt_frame,
            text="install",
            command=inst_btn1,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.apt_inst_btn_ttp = CreateToolTip(
            self.apt_inst_btn,
            'Just enter the "apt-get-list-name" of the program: E.g. compiz, chomium-browser, gparted, etc.',
        )

        self.apt_ico = Label(self.apt_frame, image=self.p4, fg="white")
        self.apt_ico["background"] = "#333333"
        self.apt_ico.grid(
            column=0,
            row=0,
        )
        self.combo_box.grid(column=2, row=0)
        self.apt_inst_btn.grid(column=1, row=0)

        # APT- remove
        self.un_apt_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.un_apt_frame.pack()
        self.un_apt_frame["background"] = "#333333"

        ua_fo = open("scripts/packages.list", "r")
        un_content = ua_fo.readlines()
        for i, s in enumerate(un_content):
            un_content[i] = s.strip()

        def check_input(event):
            value = event.widget.get()

            if value == "":
                self.un_combo_box["values"] = un_content
            else:
                data = []
                for item in un_content:
                    if value.lower() in item.lower():
                        data.append(item)

                self.un_combo_box["values"] = data

        def un_inst_btn1():
            entry_text = self.un_combo_box.get()
            popen(
                f"xterm -e 'bash -c \"sudo apt-get remove {self.un_combo_box.get()}; exec bash\"'"
            )

        self.apt_un_ico = PhotoImage(file=r"images/icons/apt-get.png")

        self.apt_un_entry = Entry(self.un_apt_frame, bd=5, width=31, borderwidth=1)

        self.un_combo_box = ttk.Combobox(self.un_apt_frame)
        self.un_combo_box["values"] = un_content
        self.un_combo_box.bind("<KeyRelease>", check_input)
        self.un_combo_box.config(width=30)

        self.un_apt_inst_btn = Button(
            self.un_apt_frame,
            text="remove",
            command=un_inst_btn1,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="red",
            font=(("Helvetica,bold"), "8"),
        )

        self.apt_ico = Label(self.un_apt_frame, fg="white", width=10)
        self.apt_ico["background"] = "#333333"
        self.apt_ico.grid(
            column=0,
            row=0,
        )
        self.un_combo_box.grid(column=2, row=0)
        self.un_apt_inst_btn.grid(column=1, row=0)

        # pi-apps_entry

        self.pi_apps = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.pi_apps.pack()
        self.pi_apps["background"] = "#333333"

        def inst_pi_apps():
            entry_text = self.eingabefeld3.get()
            popen(
                f"xterm -e 'bash -c \"{home}/pi-apps/manage install {self.eingabefeld3.get()}; exec bash\"'"
            )

        def pi_apps_list():
            popen(f"xterm -e 'bash -c \"ls {home}/pi-apps/apps/ ; exec bash\"'")

        self.pa6 = PhotoImage(file=r"images/icons/pi-app.png")

        self.pi_apps_ico = Label(
            self.pi_apps, image=self.pa6, text="piapps install", fg="white"
        )
        self.pi_apps_ico["background"] = "#333333"

        self.eingabefeld3 = Entry(self.pi_apps, bd=5, width=31, borderwidth=1)
        self.pi_apps_inst_btn = Button(
            self.pi_apps,
            text="install",
            command=inst_pi_apps,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )

        self.pi_apps_ico.grid(column=0, row=3)
        self.eingabefeld3.grid(column=2, row=3)
        self.pi_apps_inst_btn.grid(column=1, row=3)

        # snap_entry
        self.snap_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.snap_frame.pack()
        self.snap_frame["background"] = "#333333"

        def inst_btn2():
            entry_text = self.eingabefeld2.get()
            popen(
                f"xterm -e 'bash -c \"sudo snap install {self.eingabefeld2.get()}; exec bash\"'"
            )

        self.p6 = PhotoImage(file=r"images/icons/snap.png")

        self.snap_ico = Label(
            self.snap_frame, image=self.p6, text="Snap install", fg="white"
        )
        self.snap_ico["background"] = "#333333"

        self.eingabefeld2 = Entry(self.snap_frame, bd=5, width=31, borderwidth=1)
        self.snap_inst_btn = Button(
            self.snap_frame,
            text="install",
            command=inst_btn2,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.snap_inst_btn_ttp = CreateToolTip(
            self.snap_inst_btn,
            "*to use snap install, you must\napt-get install snapd xD lol",
        )

        self.snap_ico.grid(column=0, row=1)
        self.eingabefeld2.grid(column=2, row=1)
        self.snap_inst_btn.grid(column=1, row=1)

        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")

        # flat_entry

        self.flat_frame = Frame(
            self.fast_sec_frame,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
        )
        self.flat_frame.pack()
        self.flat_frame["background"] = "#333333"

        def inst_btn4():
            entry_text = self.eingabefeld4.get()
            popen(
                f" xterm -e 'bash -c \"sudo flatpak install flathub {self.eingabefeld4.get()}; exec bash\"'"
            )

        self.p66 = PhotoImage(file=r"images/icons/flathub.png")

        self.flatp_ico = Label(
            self.flat_frame, image=self.p66, text="Flat install", fg="white"
        )
        self.flatp_ico["background"] = "#333333"

        self.eingabefeld4 = Entry(self.flat_frame, bd=5, width=31, borderwidth=1)
        self.flatp_inst_btn = Button(
            self.flat_frame,
            text="install",
            command=inst_btn4,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "12"),
        )
        self.flatp_inst_btn_ttp = CreateToolTip(
            self.flatp_inst_btn,
            "*past without--->>>flatpak install flathub<<< org.mozilla.firefox",
        )

        self.flatp_ico.grid(column=0, row=7)
        self.eingabefeld4.grid(column=2, row=7)
        self.flatp_inst_btn.grid(column=1, row=7)

        self.frame311 = Frame(
            self,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=1,
            pady=5,
            padx=50,
            bg="green",
        )
        self.frame311.pack(pady=10)

        self.snapstore_btn = Button(
            self.frame311,
            text="snapcraft.io",
            command=snapcraft,
            highlightthickness=1,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        self.pi_apps_inst_btn3 = Button(
            self.frame311,
            text="list all pi-apps",
            command=pi_apps_list,
            highlightthickness=1,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        self.uninst_button = Button(
            self.frame311,
            text="Synaptic",
            command=uninst_btn1,
            highlightthickness=1,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )
        self.uninst_button_ttp = CreateToolTip(
            self.uninst_button, "If nothing happens you must install Synaptic"
        )

        self.flat_btn = Button(
            self.frame311,
            text="Flathub",
            command=flatflat,
            highlightthickness=1,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=(("Helvetica,bold"), "9"),
        )

        self.snapstore_btn.grid(column=0, row=6)
        self.pi_apps_inst_btn3.grid(column=1, row=6)
        self.uninst_button.grid(column=2, row=6)
        self.flat_btn.grid(column=3, row=6)

        self.info_inst_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_installer_tab,
        )
        self.info_inst_btn.place(x=700, y=620)


# Look
class Frame5(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def button_xf4s():
            popen("xfwm4-settings")

        def info_look_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Looks Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/looks_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)
            # scrollbar.config(command=mylist.yview)

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
            popen(
                "xterm -e 'bash -c \"sudo update-alternatives --config x-session-manager; exec bash\"'"
            )

        def button_xfwm():
            popen(
                "xterm -e 'bash -c \"sudo update-alternatives --config x-window-manager; exec bash\"'"
            )

        def theme_f():
            popen("sudo xdg-open /usr/share/themes/")

        def icon_f():
            popen("sudo xdg-open /usr/share/images/icons/")

        def xfcefix():
            popen(
                "xterm -e 'bash -c \"sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware; exec bash\"'"
            )

        def xfcefix2():
            popen(
                f"xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/xfce4fix.sh; exec bash\"'"
            )

        def xfce_make():
            popen("xdg-open https://github.com/actionschnitzel/Make-Me-Xfce")

        def web_OVC():
            popen("xdg-open https://www.xfce-look.org/browse/")

        # Images/Icons
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.bp06 = PhotoImage(file=r"images/icons/folder.png")
        self.ico_m = PhotoImage(file=r"images/icons/gui_icon.png")
        self.bp03 = PhotoImage(file=r"images/icons/terminal.png")
        self.ico_m2 = PhotoImage(file=r"images/icons/weblink_icon.png")
        self.ip01 = PhotoImage(file=r"images/icons/download_ico.png")
        self.ttp01 = PhotoImage(file=r"images/icons/tuxterm.png")
        self.ip02 = PhotoImage(file=r"images/icons/fix1i.png")

        # Frame/Button Set
        self.rahmen4 = Frame(
            self,
            borderwidth=0,
            highlightthickness=2,
            relief=GROOVE,
            pady=10,
            padx=10,
            width=300,
        )
        self.rahmen4.pack(pady=40, padx=40, fill="both")  #
        self.rahmen4["background"] = "#333333"

        self.guitweaks = Label(
            self.rahmen4,
            text="GUI Tweaks",
            font=("Helvetica", 14, "bold"),
            background="#333333",
            foreground="#d4244d",
            anchor="w",
        )
        self.guitweaks.grid(column=0, row=0)

        self.in_btn1 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Tasksel",
            font=("Helvetica", 10, "bold"),
            command=tasksel_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn1.grid(column=1, row=0, padx=5)

        self.in_btn2 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Change Desktop",
            command=ch_desk,
            font=("Helvetica", 10, "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn2.grid(column=1, row=1, padx=5)

        self.in_btn3 = Button(
            self.rahmen4,
            image=self.ttp01,
            text="Change Win-Manager",
            command=button_xfwm,
            font=("Helvetica", 10, "bold"),
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=220,
        )
        self.in_btn3.grid(column=1, row=2, padx=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.bp06,
            text="Theme Folder",
            font=("Helvetica", 10, "bold"),
            command=theme_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=200,
        )
        self.in_btn7.grid(column=2, row=0, padx=5, pady=5)

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.bp06,
            text="Icon Folder",
            font=("Helvetica", 10, "bold"),
            command=icon_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=200,
        )
        self.in_btn7.grid(column=2, row=1, padx=5)

        self.xfcelook_ttp = CreateToolTip(
            self.in_btn7,
            "*download the themes extract em and throw it into Theme/Icon Folder",
        )

        self.in_btn7 = Button(
            self.rahmen4,
            image=self.ico_m2,
            text="Get Themes",
            font=("Helvetica", 10, "bold"),
            command=web_OVC,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=200,
        )
        self.in_btn7.grid(column=2, row=2, padx=5)

        # xfce_tweaks
        self.rahmen41 = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10, padx=15
        )
        self.rahmen41.pack(padx=40, pady=20, fill="both")
        self.rahmen41["background"] = "#333333"

        self.xfce = Label(
            self.rahmen41,
            text="Xfce Tweaks",
            font=("Helvetica", 14, "bold"),
            background="#333333",
            foreground="#d4244d",
            width=10,
        )
        self.xfce.grid(column=0, row=0)

        self.in_btn3 = Button(
            self.rahmen41,
            image=self.ico_m,
            justify="left",
            text="Xfwm4 Settings",
            command=button_xf4s,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn3.grid(column=1, row=0, padx=5)
        self.in_btn3.configure(state=DISABLED)

        self.in_btn5 = Button(
            self.rahmen41,
            image=self.bp03,
            justify="left",
            text="WiFi Fix",
            compound=LEFT,
            command=xfcefix2,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn5.grid(column=3, row=0)
        self.in_btn5.configure(state=DISABLED)

        self.in_btn51 = Button(
            self.rahmen41,
            image=self.bp03,
            justify="left",
            text="Bluetooth Fix",
            compound=LEFT,
            command=xfcefix,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn51.grid(column=2, row=0)
        self.in_btn51.configure(state=DISABLED)

        self.in_btn52 = Button(
            self.rahmen41,
            image=self.ico_m,
            justify="left",
            text="Xfce4 Appearance",
            compound=LEFT,
            command=xfceappear_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            anchor="w",
            width=160,
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn52.grid(column=1, row=1)
        self.in_btn52.configure(state=DISABLED)

        self.in_btn7 = Button(
            self.rahmen41,
            image=self.ico_m2,
            justify="left",
            text="Xfce_look",
            compound=LEFT,
            command=xfcelook_f,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn7.grid(column=2, row=1)
        self.in_btn7.configure(state=DISABLED)

        self.in_btn8 = Button(
            self.rahmen41,
            image=self.ico_m2,
            justify="left",
            text="Make-Me-Xfce",
            compound=LEFT,
            command=xfce_make,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.in_btn8.grid(column=3, row=1)

        if get_de == "XFCE":
            self.in_btn3.configure(state=NORMAL)
            self.in_btn5.configure(state=NORMAL)
            self.in_btn51.configure(state=NORMAL)
            self.in_btn52.configure(state=NORMAL)
            self.in_btn7.configure(state=NORMAL)

        # gui_tweaks
        self.rahmen42 = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10, padx=15
        )
        self.rahmen42.pack(padx=40, pady=20, fill="both")
        self.rahmen42["background"] = "#333333"

        self.lxde = Label(
            self.rahmen42,
            text="Pixel Tweaks",
            font=("Helvetica", 14, "bold"),
            background="#333333",
            foreground="#d4244d",
        )
        self.lxde.grid(column=0, row=0)

        self.lx_btn0 = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="LXAppearace",
            compound=LEFT,
            command=lxap_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lx_btn0.grid(column=1, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="OpenBox Conf",
            compound=LEFT,
            command=opbox_button,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lxde.grid(column=2, row=0)

        self.lxde = Button(
            self.rahmen42,
            image=self.ico_m,
            justify="left",
            text="Pi Appeariance",
            compound=LEFT,
            command=pi_appear,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=160,
            anchor="w",
            font=("Helvetica", 10, "bold"),
        )
        self.lxde.grid(column=3, row=0)

        self.info_look_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_look_tab,
        )
        self.info_look_btn.place(x=700, y=620)


# ZRAM
class z_ram_pop(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # self["background"] = "#333333"
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 280
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")

        def z_ram_install():
            popen(
                popen(
                    "xterm -e 'bash -c \"sudo apt-get install zram-tools; exec bash\"'"
                )
            )
            # subprocess.call(['notify-send','PiGro - Just Click It!','z_ram has been installed'])

        def z_ram_uninstall():
            popen("xterm -e 'bash -c \"sudo apt-get remove zram-tools; exec bash\"'")
            subprocess.call(
                [
                    "notify-send",
                    "PiGro - Just Click It!",
                    "z_ram has been uninstalled",
                ]
            )

        GLabel_804 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.ip03
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "ZRAM"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "Zram is a Linux kernel module that allows\nyou to set up compressed filesystems in RAM.\nzram-tools uses this module to set up compressed \nswap space.\nThis is useful on systems with low memory or servers\nrunning a large amount of services with data that's\neasily swappable but that you may wish to swap back\nfast without sacrificing disk bandwidth.\n"
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = z_ram_install

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = z_ram_uninstall


# 64 Bit Mode
class six4_bit_pop(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        # self["background"] = "#333333"
        self.title("")
        self.icon = tk.PhotoImage(file="images/icons/pigro_spalsh.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 280
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")

        def sixfour_bit_install():
            popen(
                popen(
                    "xterm -e 'bash -c \"sudo apt-get install -y raspbian-nspawn-64; exec bash\"'"
                )
            )
            # subprocess.call(['notify-send','PiGro - Just Click It!','sixfour_bit has been installed'])

        def sixfour_bit_uninstall():
            popen(
                "xterm -e 'bash -c \"sudo apt-get remove raspbian-nspawn-64; exec bash\"'"
            )
            subprocess.call(
                [
                    "notify-send",
                    "PiGro - Just Click It!",
                    "sixfour_bit has been uninstalled",
                ]
            )

        GLabel_804 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_804["font"] = ft
        GLabel_804["fg"] = "#333333"
        GLabel_804["justify"] = "center"
        GLabel_804["text"] = "Icon"
        GLabel_804["image"] = self.ip03
        GLabel_804.place(x=20, y=40, width=100, height=100)

        GLabel_0 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=14)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "left"
        GLabel_0["text"] = "64 Bit Mode"
        GLabel_0.place(x=160, y=30, width=391, height=33)

        GLabel_29 = tk.Label(self)
        ft = tkFont.Font(family="Helvetica", size=10)
        GLabel_29["font"] = ft
        GLabel_29["fg"] = "#333333"
        GLabel_29["justify"] = "left"
        GLabel_29[
            "text"
        ] = "This project is a bootable, microSD card 64-bit kernel,\n32-bit Raspbian Buster Desktop host OS + 64-bit\nDebian Buster guest OS image for the\nRaspberry Pi 4 model B,\nand Pi 3 model B/B+ single board computers (SBC).\nIt is intended for users who would like to retain\ntheir familiar Raspbian tools, desktop and\nrepos, but who also need to run one or\nmore 64-bit only software components on their Pi."
        GLabel_29.place(x=140, y=70, width=390, height=194)

        GButton_883 = tk.Button(self)
        GButton_883["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_883["font"] = ft
        GButton_883["fg"] = "#000000"
        GButton_883["justify"] = "center"
        GButton_883["text"] = "Install"
        GButton_883.place(x=30, y=190, width=70, height=25)
        GButton_883["command"] = sixfour_bit_install

        GButton_585 = tk.Button(self)
        GButton_585["bg"] = "#efefef"
        ft = tkFont.Font(family="Helvetica", size=10)
        GButton_585["font"] = ft
        GButton_585["fg"] = "#000000"
        GButton_585["justify"] = "center"
        GButton_585["text"] = "Uninstall"
        GButton_585.place(x=30, y=230, width=70, height=25)
        GButton_585["command"] = sixfour_bit_uninstall


# Tuning
class Frame6(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        # Current OV settings
        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def generate_lines_that_equal(string, fp):
            for line in fp:
                if line == string:
                    yield line

        def info_tuning_tab():
            global pop_changelog
            pop_changelog = Toplevel()
            pop_changelog.geometry("700x800")
            pop_changelog.title("Tuning Info")
            scrollbar = Scrollbar(pop_changelog)
            scrollbar.pack(side=RIGHT, fill=Y)
            s_list = Text(pop_changelog, yscrollcommand=scrollbar.set)
            text_file = open("docs/tuning_info.txt")
            stuff = text_file.read()
            s_list.insert(END, stuff)
            text_file.close()
            s_list.config(state=DISABLED)
            s_list.pack(anchor="w", fill=BOTH, expand=True)

        def tuning_legende():
            tu_le = Tuning_Legende(self)
            tu_le.grab_set()

        def btswitch_64():
            six_4 = six4_bit_pop(self)
            six_4.grab_set()

        def z_ram():
            z_ram = z_ram_pop(self)
            z_ram.grab_set()

        # BG + Icons

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.rm_ov_icon = PhotoImage(file=r"images/icons/PiGroOV_rm.png")
        self.ov1_icon = PhotoImage(file=r"images/icons/PiGroOV1.png")
        self.ov2_icon = PhotoImage(file=r"images/icons/PiGroOV2.png")
        self.ov3_icon = PhotoImage(file=r"images/icons/PiGroOV3.png")
        self.ov4_icon = PhotoImage(file=r"images/icons/PiGroOV4.png")
        self.tpinfm = PhotoImage(file=r"images/icons/info_m.png")
        self.ip03 = PhotoImage(file=r"images/icons/download_ico.png")
        self.tu_legend_ico = PhotoImage(file=r"images/icons/legende.png")

        # OV Notifications
        def pop_dest():
            pop_default.destroy()

        def pop_dest1():
            pop_2147.destroy()

        def pop_dest2():
            pop_2000.destroy()

        def pop_dest3():
            pop_2200.destroy()

        def pop_dest4():
            pop_2300.destroy()

        def reboot_n():
            popen("sudo reboot")

        # overclocking_2000
        def ov_2000():
            popen(
                f"xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/ov_1.sh && exit; exec bash\"'"
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2000\ngpu_fequ = 750\nover_voltage = 6\nforce_turbo = 1",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            global pop_2000
            pop_2000 = Toplevel(self)
            pop_2000.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_2000.winfo_screenwidth()
            screen_height = pop_2000.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2000.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_2000.resizable(0, 0)

            frame_pop_2000 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
            frame_pop_2000.pack()
            frame_pop_2000["background"] = "#333333"

            frame_pop_2000_1 = Frame(pop_2000, borderwidth=0, relief=GROOVE)
            frame_pop_2000_1.pack()
            frame_pop_2000_1["background"] = "#333333"

            pop_lbl_2000 = Label(
                frame_pop_2000,
                anchor="w",
                text="Done! The new settings take effect after a reboot",
                font=("Helvetica", 12),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_2000.pack(pady=20)

            pop_btn_2000 = Button(
                frame_pop_2000_1,
                text="Continue",
                anchor="w",
                command=pop_dest2,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_2000.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_2000_1,
                text="Reboot",
                anchor="w",
                command=reboot_n,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        # overclocking_2147
        def ov_2147():
            popen(
                f"xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/ov_2.sh && exit; exec bash\"'"
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2147\ngpu_fequ = 750\nover_voltage = 8\nforce_turbo = 1",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            popen(f"mpg123 {home}/PiGro-Aid-/scripts/HOLYPiT.mp3")

            global pop_2147
            pop_2147 = Toplevel(self)
            pop_2147.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_2147.winfo_screenwidth()
            screen_height = pop_2147.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2147.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_2147.resizable(0, 0)

            frame_pop_2147 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
            frame_pop_2147.pack()
            frame_pop_2147["background"] = "#333333"

            frame_pop_2147_1 = Frame(pop_2147, borderwidth=0, relief=GROOVE)
            frame_pop_2147_1.pack(pady=10)
            frame_pop_2147_1["background"] = "#333333"

            pop_lbl_2147 = Label(
                frame_pop_2147,
                anchor="w",
                text="Done! The new settings take effect after a reboot",
                font=("Helvetica", 12),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_2147.pack(pady=20)
            pop_btn_2147 = Button(
                frame_pop_2147_1,
                text="Continue",
                anchor="w",
                command=pop_dest1,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_2147.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_2147_1,
                text="Reboot",
                anchor="w",
                command=reboot_n,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        # overclocking_default/reset
        def set_default():
            popen(
                f"xterm -e 'bash -c \"sudo chmod +x {home}/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'"
            )
            popen(
                f"xterm -e 'bash -c \"sudo {home}/PiGro-Aid-/scripts/rm_ov.sh && exit; exec bash\"'"
            )
            self.tu_btn1.config(state=NORMAL)
            self.tu_btn2.config(state=NORMAL)
            self.tu_btn3.config(state=NORMAL)
            self.tu_btn4.config(state=NORMAL)

            Notification(
                title="PiGro Overclocking\n",
                description="All Settings Restored\n\n",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            global pop_default
            pop_default = Toplevel(self)
            pop_default.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_default.winfo_screenwidth()
            screen_height = pop_default.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_default.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_default.resizable(0, 0)

            frame_pop_de = Frame(pop_default, borderwidth=0, relief=GROOVE)
            frame_pop_de.pack()
            frame_pop_de["background"] = "#333333"

            frame_pop_de1 = Frame(pop_default, borderwidth=0, relief=GROOVE)
            frame_pop_de1.pack(pady=10)
            frame_pop_de1["background"] = "#333333"

            pop_lbl_default = Label(
                frame_pop_de,
                anchor="w",
                text="Settings Restored",
                font=("Helvetica", 16),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_default.pack(pady=20)
            pop_btn_default = Button(
                frame_pop_de1,
                text="Continue",
                anchor="w",
                command=pop_dest,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_default.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_de1,
                text="Reboot",
                anchor="w",
                command=reboot_n,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        # overclocking_2200
        def ov_2200():
            popen(
                f"xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/ov_3.sh && exit; exec bash\"'"
            )
            popen(f"mpg123 {home}/PiGro-Aid-/scripts/over9000.mp3")

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2200\ngpu_fequ = 750\nover_voltage = 8\force_turbo = 1",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

            global pop_2200
            pop_2200 = Toplevel(self)
            pop_2200.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_2200.winfo_screenwidth()
            screen_height = pop_2200.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2200.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_2200.resizable(0, 0)

            frame_pop_2200 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
            frame_pop_2200.pack()
            frame_pop_2200["background"] = "#333333"

            frame_pop_2200_1 = Frame(pop_2200, borderwidth=0, relief=GROOVE)
            frame_pop_2200_1.pack(pady=10)
            frame_pop_2200_1["background"] = "#333333"

            pop_lbl_2200 = Label(
                frame_pop_2200,
                anchor="w",
                text="Done! The new settings take effect after a reboot",
                font=("Helvetica", 16),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_2200.pack(pady=20)
            pop_btn_2200 = Button(
                frame_pop_2200_1,
                text="Continue",
                anchor="w",
                command=pop_dest3,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_2200.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_2200_1,
                text="Reboot",
                anchor="w",
                command=reboot_n,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        # overclocking_2300
        def ov_2300():
            popen(
                f"xterm -e 'bash -c \"{home}/PiGro-Aid-/scripts/ov_4.sh && exit; exec bash\"'"
            )
            popen(f"mpg123 {home}/PiGro-Aid-/scripts/over9000.mp3")

            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

            Notification(
                title="PiGro Overclocking\n",
                description="arm_freq = 2300\ngpu_fequ = 700\nover_voltage = 14\nforce_turbo = 1",
                icon_path=f"{home}/PiGro-Aid-/images/icons/Logotab.png",
                duration=5,
                urgency="normal",
            ).send()

            global pop_2300
            pop_2300 = Toplevel(self)
            pop_2300.config(bg="#333333")
            app_width = 500
            app_height = 150
            screen_width = pop_2300.winfo_screenwidth()
            screen_height = pop_2300.winfo_screenheight()
            x = (screen_width / 2) - (app_width / 2)
            y = (screen_height / 2) - (app_height / 2)
            pop_2300.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
            pop_2300.resizable(0, 0)

            frame_pop_2300 = Frame(pop_2300, borderwidth=0, relief=GROOVE)
            frame_pop_2300.pack()
            frame_pop_2300["background"] = "#333333"

            frame_pop_2300_1 = Frame(pop_2300, borderwidth=0, relief=GROOVE)
            frame_pop_2300_1.pack(pady=10)
            frame_pop_2300_1["background"] = "#333333"

            pop_lbl_2300 = Label(
                frame_pop_2300,
                anchor="w",
                text="Done! The new settings take effect after a reboot",
                font=("Helvetica", 16),
                highlightthickness=0,
                borderwidth=2,
                background="#333333",
                foreground="white",
                compound=LEFT,
            )
            pop_lbl_2300.pack(pady=20)
            pop_btn_2300 = Button(
                frame_pop_2300_1,
                text="Continue",
                anchor="w",
                command=pop_dest4,
                highlightthickness=0,
                borderwidth=0,
                background="#2246c4",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_2300.pack(padx=5, pady=20, side=LEFT)
            pop_btn_shut = Button(
                frame_pop_2300_1,
                text="Reboot",
                anchor="w",
                command=reboot_n,
                highlightthickness=0,
                borderwidth=0,
                background="#f03838",
                foreground="white",
                compound=LEFT,
            )
            pop_btn_shut.pack(padx=5, pady=20)

        self.ov_main_frame = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, pady=20, padx=50
        )
        self.ov_main_frame.pack(padx=20, pady=20, fill="both")
        self.ov_main_frame["background"] = "#333333"

        # OV_Display_Frame
        self.ov_display_frame = Frame(
            self.ov_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=50,
            padx=50,
        )
        self.ov_display_frame.grid(row=0, column=1, padx=70)
        self.ov_display_frame["background"] = "#333333"

        global tu_current
        tu_current = Label(
            self.ov_display_frame,
            text="PiGro Settings: Not Configured\n",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="green",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
        )
        tu_current.grid(column=1, row=0, columnspan=2)

        global tu_current2
        tu_current2 = Label(
            self.ov_display_frame,
            text="arm_freq not configured",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="white",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
        )
        tu_current2.grid(column=1, row=2, columnspan=2)

        global tu_current3
        tu_current3 = Label(
            self.ov_display_frame,
            text="gpu_freq not configured",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="white",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
        )
        tu_current3.grid(column=1, row=3, columnspan=2)

        global tu_current4
        tu_current4 = Label(
            self.ov_display_frame,
            text="over_voltage not configured",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="white",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
        )
        tu_current4.grid(column=1, row=4, columnspan=2)

        global tu_current5
        tu_current5 = Label(
            self.ov_display_frame,
            text="force_turbo not configured",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="white",
            bg="#333333",
            font=("Helvetica", 12, "bold"),
        )
        tu_current5.grid(column=1, row=5, columnspan=2)

        self.tu_info = Label(
            self.ov_display_frame,
            text="Settings tested with\nRaspberry Pi 4B 8 GB\n+ Ice Tower Cooler and Pi400.\nI take no responsibility if\nyour Pi is damaged.\nPlease click on the Info Button\nto learn more",
            font=("Helvetica", 8),
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="yellow",
        ).grid(column=1, row=6, pady=20)

        self.tu_legende = Button(
            self.ov_display_frame,
            text="Legende",
            font=("Helvetica", 8),
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="yellow",
            command=tuning_legende,
            image=self.tu_legend_ico,
        ).grid(column=1, row=7)

        # Tuning_Button_Frame
        self.ov_buttons = Frame(
            self.ov_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
        )
        self.ov_buttons.grid(row=0, column=0)
        self.ov_buttons["background"] = "#333333"

        self.tuning_options = Label(
            self.ov_buttons,
            text="Overclocking Options",
            highlightthickness=0,
            borderwidth=2,
            background="#333333",
            foreground="#d4244d",
            font=("Helvetica", 16),
            justify="left",
        ).grid(column=0, row=1, pady=10)

        self.tu_reset = Button(
            self.ov_buttons,
            justify="left",
            image=self.rm_ov_icon,
            text="Reset Overclocking",
            anchor="w",
            command=set_default,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        ).grid(column=0, row=2, pady=10)

        self.tu_btn1 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov1_icon,
            text="Crank It Up",
            anchor="w",
            command=ov_2000,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        self.tu_btn1.grid(column=0, row=4, pady=10)

        self.tu_btn2 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov2_icon,
            text="You Sir... Need A Fan!",
            anchor="w",
            command=ov_2147,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        self.tu_btn2.grid(column=0, row=6, pady=10)

        self.tu_btn3 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov3_icon,
            text="Take It To The Max!",
            anchor="w",
            command=ov_2200,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        self.tu_btn3.grid(column=0, row=8, pady=10)

        self.tu_btn4 = Button(
            self.ov_buttons,
            justify="left",
            image=self.ov4_icon,
            text="Honey,\nthe fuse blew again!",
            anchor="w",
            command=ov_2300,
            highlightthickness=2,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=LEFT,
            font=("Helvetica", 10, "bold"),
            width=200,
        )
        self.tu_btn4.grid(column=0, row=9, pady=10)

        # Overclock Display Functions
        def OV1_label():
            tu_current.config(
                text="Current Settings: Crank It Up\n", fg="yellow", bg="#333333"
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

        def OV2_label():
            tu_current.config(
                text="Current Settings: You Sir... Need A Fan!\n",
                fg="red",
                bg="#333333",
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

        def OV3_label():
            tu_current.config(
                text="Current Settings: Take It To The Max!\n", fg="pink", bg="#333333"
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

        def OV4_label():
            tu_current.config(
                text="Honey,\nthe fuse blew again!\n", fg="purple", bg="#333333"
            )
            self.tu_btn1.config(state=DISABLED)
            self.tu_btn2.config(state=DISABLED)
            self.tu_btn3.config(state=DISABLED)
            self.tu_btn4.config(state=DISABLED)

        def a_f_label():
            tu_current2.config(text=line1, fg="white", bg="#333333")

        def g_f_label():
            tu_current3.config(text=line2, fg="white", bg="#333333")

        def o_v_label():
            tu_current4.config(text=line3, fg="white", bg="#333333")

        def f_t_label():
            tu_current5.config(text=line3, fg="white", bg="#333333")

        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking1", fp):
                print(line)
                if line:
                    OV1_label()

        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking2", fp):
                print(line)
                if line:
                    OV2_label()

        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking3", fp):
                print(line)
                if line:
                    OV3_label()

        with open("/boot/config.txt", "r") as fp:
            for line in lines_that_contain("#Pigro_Overclocking4", fp):
                print(line)
                if line:
                    OV4_label()

        with open("/boot/config.txt", "r") as fp:
            for line1 in lines_that_contain("arm_freq=", fp):
                print(line1)
                if line1:
                    a_f_label()

        with open("/boot/config.txt", "r") as fp:
            for line2 in lines_that_contain("gpu_freq=", fp):
                print(line2)
                if line2:
                    g_f_label()

        with open("/boot/config.txt", "r") as fp:
            for line3 in lines_that_contain("force_turbo=", fp):
                print(line3)
                if line3:
                    f_t_label()

        with open("/boot/config.txt", "r") as fp:
            for line3 in lines_that_contain("over_voltage=", fp):
                print(line3)
                if line3:
                    o_v_label()

        # Misc_Frame
        self.misc_main_frame = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, padx=20
        )
        self.misc_main_frame.pack(padx=20, pady=10, fill="both", expand=True)
        self.misc_main_frame["background"] = "#333333"

        self.misc_zram_frame = Frame(
            self.misc_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.misc_zram_frame.pack(side=LEFT)
        self.misc_zram_frame["background"] = "#333333"

        self.misc_64mode_frame = Frame(
            self.misc_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
        )
        self.misc_64mode_frame.pack(side=LEFT, padx=50)
        self.misc_64mode_frame["background"] = "#333333"

        self.tu_zbtn = Button(
            self.misc_zram_frame,
            text="ZRAM",
            font=("Helvetica", 16),
            anchor="w",
            command=z_ram,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            compound=LEFT,
            foreground="#d4244d",
        ).grid(column=0, row=1)

        self.tu_bbtn = Button(
            self.misc_64mode_frame,
            text="64 Bit Mode",
            font=("Helvetica", 16),
            anchor="w",
            command=btswitch_64,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#d4244d",
            compound=LEFT,
        ).grid(column=0, row=1)

        self.info_tuning_btn = Button(
            self,
            image=self.tpinfm,
            highlightthickness=0,
            borderwidth=0,
            command=info_tuning_tab,
        )
        self.info_tuning_btn.place(x=700, y=500)


# Links
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
            popen(
                "xdg-open https://mxlinux.org/blog/fluxbox-raspberrypi-respin-ragout-beta/"
            )

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

        def ubi_bubi():
            popen("xdg-open https://ubuntu.com/download/raspberry-pi")

        def popo_bubi():
            popen("xdg-open https://pop.system76.com/")

        def six4_berry():
            popen("xdg-open https://downloads.raspberrypi.org/raspios_arm64/images/")

        def pi_doc():
            popen("xdg-open https://www.raspberrypi.com/documentation/")

        def pi_tuto():
            popen("xdg-open https://tutorials-raspberrypi.com/")

        def vis_tk():
            popen("xdg-open https://visualtk.com/")

        # äö
        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.di01 = PhotoImage(file=r"images/icons/TwisterOSLogo-Large-New3.png")
        self.di02 = PhotoImage(file=r"images/icons/Puppy_Linux_Logo.png")
        self.di03 = PhotoImage(file=r"images/icons/dietpi.png")
        self.di04 = PhotoImage(file=r"images/icons/MX-icon.png")
        self.di05 = PhotoImage(file=r"images/icons/fydeos.png")
        self.di06 = PhotoImage(file=r"images/icons/android.png")
        self.di06 = PhotoImage(file=r"images/icons/android.png")
        self.di07 = PhotoImage(file=r"images/icons/logo_berryserver.png")
        self.di08 = PhotoImage(file=r"images/icons/NCP.png")
        self.pop_os_ico = PhotoImage(file=r"images/icons/popo_os_icon.png")
        self.ubu_os_ico = PhotoImage(file=r"images/icons/Logo-ubuntu_.png")
        self.pi64_os_ico = PhotoImage(file=r"images/icons/Raspberry_Pi_Logo.png")

        self.rahmen = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, padx=10, pady=20
        )
        self.rahmen.grid(row=0, rowspan=11, column=0, pady=20, padx=40)
        self.rahmen["background"] = "#333333"

        sys_btn2 = Label(
            self.rahmen,
            text="Distros",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            font=("Helvetica", 16, "bold"),
        )
        sys_btn2.pack()

        self.dist_btn1 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di01,
            anchor="w",
            text="Twister OS ",
            command=down_twist,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn2 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di02,
            anchor="w",
            text="Puppy Linux",
            command=down_puppy,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn3 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di03,
            anchor="w",
            text="DietPi     ",
            command=down_diet,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn4 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di04,
            anchor="w",
            text="MX Linux   ",
            command=down_mx,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn5 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di05,
            anchor="w",
            text="FydeOS     ",
            command=down_fy,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn6 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di06,
            anchor="w",
            text="Android    ",
            command=down_kk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn7 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di07,
            anchor="w",
            text="Berryserver",
            command=down_bb,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn8 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.di08,
            anchor="w",
            text="NextCloudPi",
            command=down_NCP,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn9 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.ubu_os_ico,
            anchor="w",
            text="Ubuntu",
            command=ubi_bubi,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn10 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.pop_os_ico,
            anchor="w",
            text="Pop_OS",
            command=popo_bubi,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.dist_btn11 = Button(
            self.rahmen,
            compound=LEFT,
            justify="left",
            image=self.pi64_os_ico,
            anchor="w",
            text="RPi OS 64 Bit",
            command=six4_berry,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            width=150,
        ).pack()

        self.fast_sec_frame = Frame(
            self, borderwidth=0, highlightthickness=2, relief=GROOVE, pady=10
        )
        self.fast_sec_frame.grid(row=0, column=1, pady=20)
        self.fast_sec_frame["background"] = "#333333"

        sys_btn2 = Label(
            self.fast_sec_frame,
            text=" Other ",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
            compound=TOP,
            font=("Helvetica", 14, "bold"),
        )
        sys_btn2.pack()

        self.choice_link1 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Mankier.com (Commandline Database)",
            command=link_mankier,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Guake (Drop Down Terminal)",
            command=link_guake,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="OnBoard (Onscreen Keyboard)",
            command=link_onBoard,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Draculatheme.com",
            command=link_drac,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            anchor="w",
            width=50,
            text="Starship (Cross-Shell-Promt)",
            command=link_star,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link1 = Button(
            sys_btn2,
            width=50,
            text="LernLinux.tv",
            anchor="w",
            command=lern_l,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Rocket Beans(ger.)",
            anchor="w",
            command=rb_tv,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="52Pi",
            anchor="w",
            command=fitwo_p,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="LCD Wiki",
            anchor="w",
            command=l4_e,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Offical Raspberry Pi Documentation",
            anchor="w",
            command=pi_doc,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="Raspberry Pi Tutorials",
            anchor="w",
            command=pi_tuto,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()

        self.choice_link2 = Button(
            sys_btn2,
            width=50,
            text="VisualTk.com",
            anchor="w",
            command=vis_tk,
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="white",
        ).pack()


# Poll
class Frame8(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg2.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        def poll():
            popen("xdg-open http://www.actionschnitzel.de/Pig-Grow-Poll/")

        def wpaps():
            popen("xdg-open http://www.actionschnitzel.de/Wallpapers/")

        def wiki():
            popen("xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki")

        def red_bub():
            popen(
                "xdg-open https://www.redbubble.com/de/people/Actionschnitzel/shop?asc=u"
            )

        self.rahmen102 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=2, pady=10, padx=10
        )
        self.rahmen102.place(x=60, y=300)
        self.rahmen102["background"] = "#333333"

        self.poke_pig_21 = Label(
            self.rahmen102,
            justify="left",
            text="I never thought that so many people would use Pigro.\nAs open source lives from community,I want you to have a say in that too.\nIf you click on poll, you can vote on what else I should add to Pigro.\nSo ... let's fatten up the hog! xD\nIf you want to support me, click on the RedBubble button below.\nHere you can get Pi / Linux design from me.\n\nBest regards\n\nTimo\n\nQuestions or suggestions?:",
            font=("Helvetica", 12),
            background="#333333",
            fg="white",
            padx=5,
            pady=3,
        ).pack()

        self.mail = Entry(self.rahmen102, bd=5, width=31, borderwidth=1)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.rahmen101 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2)
        self.rahmen101.place(x=60, y=600)
        self.rahmen101["background"] = "#333333"

        self.pig_btn_1 = Button(
            self.rahmen101,
            text="User Poll",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#2FFC05",
            command=poll,
            font=(("Helvetica,bold"), "12", "bold"),
        ).grid(column=0, row=0, pady=20, padx=20)

        self.pig_btn_2 = Button(
            self.rahmen101,
            text="Wallpapers",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#EBFC05",
            command=wpaps,
            font=(("Helvetica,bold"), "12", "bold"),
        ).grid(column=1, row=0, pady=20)

        self.pig_btn_3 = Button(
            self.rahmen101,
            text="PiGro Manuel",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#053AFC",
            command=wiki,
            font=(("Helvetica,bold"), "12", "bold"),
        ).grid(column=2, row=0, pady=20, padx=20)

        self.pig_btn_4 = Button(
            self.rahmen101,
            text="Redbubble.com",
            highlightthickness=0,
            borderwidth=0,
            background="#333333",
            foreground="#FC05A0",
            command=red_bub,
            font=(("Helvetica,bold"), "12", "bold"),
        ).grid(column=3, row=0, pady=20, padx=20)


# Cam
class Frame9(ttk.Frame):
    def __init__(self, container):
        super().__init__()

        self.bg = PhotoImage(file="images/backgrounds/pigro_bg.png")
        self.bg_label = Label(self, image=self.bg)
        self.bg_label.place(x=-1, y=-1, relwidth=1, relheight=1)

        self.rahmen101 = Frame(self, borderwidth=0, relief=GROOVE, highlightthickness=2)
        self.rahmen101.pack(pady=200)
        self.rahmen101["background"] = "#333333"

        self.welcome_icon = PhotoImage(file=r"~/PiGro-Aid-/images/icons/Pi-Camera.png")
        self.head_frame = Frame(self.rahmen101)
        self.head_frame.pack()
        self.header_label = Label(
            self.head_frame, image=self.welcome_icon, bg="#333333"
        )
        self.header_label.pack()

        # Clicker_Frame
        self.btn_frame = Frame(self.rahmen101, bg="#333333")
        self.btn_frame.pack()
        self.label = Label(
            self.btn_frame,
            text=f"Files will be saved in:\n{home}\n\nGive it a Name:",
            bg="#333333",
            fg="white",
        )
        self.label.pack()

        self.entry = Entry(self.btn_frame, bd=5, width=31, borderwidth=1)
        self.entry.pack()
        self.photo_btn = Button(
            self.btn_frame,
            text="Take A Photo",
            command=self.photo1,
            bg="#333333",
            fg="white",
            highlightthickness=0,
        )
        self.photo_btn.pack()

        self.video_btn = Button(
            self.btn_frame,
            text="Take A Video",
            command=self.video1,
            bg="#333333",
            fg="white",
            highlightthickness=0,
        )
        self.video_btn.pack()

    def photo1(self):
        photo = str(self.entry.get())
        popen(f"libcamera-jpeg -o {home}/{photo}.jpg")

    def video1(self):
        video = str(self.entry.get())
        popen(f"libcamera-vid -t 10000 -o {home}/{video}.h264")


# TOOLTIPZ
class CreateToolTip(object):
    """
    create a tooltip for a given widget
    """

    def __init__(self, widget, text="widget info"):
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
        label = tk.Label(
            self.tw,
            text=self.text,
            justify="left",
            background="#ffffff",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


# End Of The Line
if __name__ == "__main__":
    app = MainApplication()
    app.mainloop()
