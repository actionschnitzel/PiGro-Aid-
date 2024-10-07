import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *
from tabs.system_tab_check import check_dselect


class DebRecoverTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")


        self.folder_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/folder_s_light.png"
        )
        self.backup_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/backup_s_light.png"
        )
        self.deb_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/deb_s_light.png"
        )
        self.recover_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/recover_s_light.png"
        )

        def get_dir():
            self.filename = filedialog.askdirectory(
                initialdir="~", title="Select A Directory"
            )
            print(self.filename)

        def do_backup():
            popen(f"dpkg --get-selections > {self.filename}/packages.list")
            popen(f"xdg-open {self.filename}")

        def install_dselect():
            command = f"x-terminal-emulator -e 'bash -c \"{permit} apt install dselect -y; exec bash\"'"

            subprocess.Popen(command, shell=True)

            self.select_path1.config(state=DISABLED)

        def get_list():
            self.p_list = filedialog.askopenfilename(
                initialdir="~",
                title="Select packages.list",
                filetypes=(("list files", "*.list"),),
            )
            print(self.p_list)

        def do_recover():
            dselect_r = f"""sudo dselect update
sudo dpkg --set-selections < {self.p_list}
sudo apt-get dselect-upgrade
printf 'Done!'"""

            popen(f"x-terminal-emulator -e 'bash -c \"{dselect_r}; exec bash\"'")

        self.backup_frame = ttk.LabelFrame(
            self,
            text="Debian Package Backup",
            padding=20
        )

        self.backup_frame.pack(pady=20, padx=20, fill=BOTH)

        self.backup_frame.columnconfigure(0, weight=1)
        self.backup_frame.rowconfigure(0, weight=1)


        self.backup_discription = ttk.Label(
            self.backup_frame,
            text="This option creates a file named packages.list. It containes a list of all debian packages installed on this system.\n\n",
            justify="left",
            anchor=W,
        ).grid(row=0,column=0,columnspan=2,sticky="ew")

        self.step_1 = ttk.Label(
            self.backup_frame,
            text="Step 1: Click on 'Select Directory' to select a place where the file should be deployed. For example a usb dongle.",
            justify="left",
            anchor="w",
        ).grid(row=1,column=0,sticky="ew")#pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path = ttk.Button(
            self.backup_frame,
            text="Select Directory",
            compound="left",
            width=20,
            image=self.folder_icon,
            command=get_dir,
        ).grid(row=1,column=1,sticky="ew",padx=5,pady=20)#.pack(padx=5, pady=15, side=tk.LEFT)



        self.step2 = ttk.Label(
            self.backup_frame,
            text="Step 2: Click on 'Backup' to start the prosses. After 1 sec it should be done.",
            justify="left",
            anchor="w",
        ).grid(row=2,column=0,sticky="ew")#.pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path2 = ttk.Button(
            self.backup_frame,
            compound="left",
            width=20,
            text="Backup",
            image=self.backup_icon,
            command=do_backup,
        ).grid(row=2,column=1,sticky="ew",padx=5)#.pack(padx=5, pady=15, side=tk.LEFT)

        self.recover_frame = ttk.LabelFrame(
            self,
            text="Debian Package Recovery",
            padding=20
        )
        self.recover_frame.pack(pady=20, padx=20, fill=BOTH)

        self.recover_frame.columnconfigure(0, weight=1)
        self.recover_frame.rowconfigure(0, weight=1)

        self.recover_discription = ttk.Label(
            self.recover_frame,
            text="The recovery requires the tool 'dselect'. Please note that you should never use recovery cross distro or architecture.\nPackages from PPAs will be not installed if the PPA is not integrated.\n\n",
            justify="left",
            anchor="w",
        ).grid(row=0,column=0,columnspan=2,sticky="ew")

        self.step3 = ttk.Label(
            self.recover_frame,
            text="Step 3: Click on 'Install dselect' ( or sudo apt install dselect ).",
            justify="left",
            anchor="w",
        ).grid(row=1,column=0,sticky="ew",padx=5,pady=20)

        self.select_path1 = ttk.Button(
            self.recover_frame,
            compound="left",
            width=20,
            text="Install dselect",
            image=self.deb_icon,
            command=install_dselect,
        )
        self.select_path1.grid(row=1,column=1,sticky="ew",padx=5,pady=20)

        if check_dselect() == True:
            self.select_path1.config(state=DISABLED, text="dselect is installed")

        self.step_4 = ttk.Label(
            self.recover_frame,
            text="Step 4: Click on 'Select Backup' and choose the packages.list file",
            justify="left",
            anchor="w",
        ).grid(row=2,column=0,sticky="ew",padx=5)

        self.select_file = ttk.Button(
            self.recover_frame,
            width=20,
            compound="left",
            text="Select Backup",
            image=self.folder_icon,
            command=get_list,
        ).grid(row=2,column=1,sticky="ew",padx=5)

        self.step5 = ttk.Label(
            self.recover_frame,
            text="Step 5: Click on 'Recovery' to start the prosses.",
            justify="left",
            anchor="w",
        ).grid(row=3,column=0,sticky="ew",padx=5,pady=20)

        self.do_ds = ttk.Button(
            self.recover_frame,
            width=20,
            compound="left",
            text="Recovery",
            image=self.recover_icon,
            command=do_recover,
        ).grid(row=3,column=1,sticky="ew",padx=5,pady=20)
