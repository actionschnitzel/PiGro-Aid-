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

        if "dark" in theme or "noir" in theme:
            self.folder_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/folder_s.png"
            )
            self.backup_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/backup_s.png"
            )
            self.deb_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/deb_s.png"
            )
            self.recover_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/recover_s.png"
            )
        else:
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

        self.backup_main_frame = LabelFrame(
            self,
            text="Debian Package Backup",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=20,
        )

        self.backup_main_frame.pack(pady=20, padx=20, fill=BOTH)
        self.backup_main_frame["background"] = frame_color

        self.backup_discription = Label(
            self.backup_main_frame,
            text="This option creates a file named packages.list. It containes a list of all debian packages installed on this system.\n\n",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            anchor=W,
            pady=5,
        ).pack()

        self.backup_frame1 = Frame(
            self.backup_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.backup_frame1.pack(pady=5, padx=20)
        self.backup_frame1["background"] = frame_color

        self.step_1 = Label(
            self.backup_frame1,
            text="Step 1: Click on 'Select Directory' to select a place where the file should be deployed.\nFor example a usb dongle.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path = Button(
            self.backup_frame1,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Select Directory",
            image=self.folder_icon,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=get_dir,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.backup_frame2 = Frame(
            self.backup_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.backup_frame2.pack(pady=5, padx=20)
        self.backup_frame2["background"] = frame_color

        self.step2 = Label(
            self.backup_frame2,
            text="Step 2: Click on 'Backup' to start the prosses. After 1 sec it should be done.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path2 = Button(
            self.backup_frame2,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Backup",
            image=self.backup_icon,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=do_backup,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.recover_main_frame = LabelFrame(
            self,
            text="Debian Package Recovery",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=20,
        )

        self.recover_main_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)
        self.recover_main_frame["background"] = frame_color

        self.recover_discription = Label(
            self.recover_main_frame,
            text="The recovery requires the tool 'dselect'. Please note that you should never use recovery cross distro or architecture.\nPackages from PPAs will be not installed if the PPA is not integrated.\n\n",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            anchor=W,
            pady=5,
        ).pack()

        self.recover_frame1 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame1.pack(pady=5, padx=20)
        self.recover_frame1["background"] = frame_color

        self.step3 = Label(
            self.recover_frame1,
            text="Step 3: Click on 'Install dselect' ( or sudo apt install dselect ).",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_path1 = Button(
            self.recover_frame1,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Install dselect",
            image=self.deb_icon,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=install_dselect,
        )
        self.select_path1.pack(padx=5, pady=15, side=tk.LEFT)

        if check_dselect() == True:
            self.select_path1.config(state=DISABLED, text="dselect is installed")

        self.recover_frame2 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame2.pack(pady=5, padx=20)
        self.recover_frame2["background"] = frame_color

        self.step_4 = Label(
            self.recover_frame2,
            text="Step 4: Click on 'Select Backup' and choose the packages.list file",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.select_file = Button(
            self.recover_frame2,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Select Backup",
            image=self.folder_icon,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=get_list,
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.recover_frame3 = Frame(
            self.recover_main_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            padx=20,
            pady=5,
        )
        self.recover_frame3.pack(pady=5, padx=20)
        self.recover_frame3["background"] = frame_color

        self.step5 = Label(
            self.recover_frame3,
            text="Step 5: Click on 'Recovery' to start the prosses.",
            justify="left",
            background=frame_color,
            foreground=main_font,
            font=(font_10),
            width=75,
            anchor="w",
        ).pack(padx=5, pady=15, side=tk.LEFT)

        self.do_ds = Button(
            self.recover_frame3,
            justify="left",
            anchor="w",
            width=200,
            compound="left",
            text="Recovery",
            image=self.recover_icon,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=do_recover,
        ).pack(padx=5, pady=15, side=tk.LEFT)
