#!/usr/bin/python3

import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image
import requests
from itertools import count, cycle
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *


class Update_Alternatives(tk.Toplevel):
    """child window for editing update-alternatives"""

    def __init__(self, parent):
        super().__init__(parent)
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 400
        app_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.title("Update-Alternatives")
        self["background"] = maincolor

        def choose_up():
            popen(
                f"x-terminal-emulator -e 'bash -c \"sudo update-alternatives --config {self.choosen.get()}; exec bash\"'"
            )

        self.up_al_frame = Frame(self, background=maincolor)
        self.up_al_frame.pack(padx=20, pady=20)

        n1 = tk.StringVar()
        self.choosen = ttk.Combobox(
            self.up_al_frame, width=30, textvariable=n1, state="readonly"
        )
        self.choosen.set("Select an item")
        self.choosen["values"] = (
            "editor",
            "start-here.svg",
            "x-cursor-theme",
            "x-session-manager",
            "x-terminal-emulator",
            "x-window-manager",
            "x-www-browser",
        )

        self.choosen.grid(column=0, row=0, pady=50, sticky=NS)

        self.choosen_btn3 = Button(
            self.up_al_frame,
            text="Config",
            highlightthickness=0,
            borderwidth=0,
            background=ext_btn,
            foreground=ext_btn_font,
            font=font_10,
            command=choose_up,
        )
        self.choosen_btn3.grid(column=1, row=0)


class Tuning_Legende(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Overclocking")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 450
        app_height = 900
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        self.tu_1 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV_rm.png"
        )
        self.tu_2 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV1.png"
        )
        self.tu_3 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV2.png"
        )
        self.tu_4 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV3.png"
        )
        self.tu_5 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV4.png"
        )

        self.tu_main_frame = Frame(self, bg=maincolor)
        self.tu_main_frame.pack(pady=20, padx=20)

        self.rm_lbl = LabelFrame(
            self.tu_main_frame,
            text="Default Settings",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        self.rm_lbl.pack(fill="both", expand=True)

        self.rm_ov = Label(self.rm_lbl, image=self.tu_1, bg=maincolor)
        self.rm_ov.grid(
            row=1,
            column=0,
            padx=10,
        )

        self.rm_text = Label(
            self.rm_lbl,
            text="Removes all\noverclocking parameters\n\n",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.rm_text.grid(
            row=1,
            column=1,
            padx=20,
        )

        self.ov1_frame = LabelFrame(
            self.tu_main_frame,
            text="Crank It Up!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        self.ov1_frame.pack(fill="both", expand=True)

        self.ov_1 = Label(
            self.ov1_frame, image=self.tu_2, bg=maincolor, foreground=main_font
        )
        self.ov_1.grid(
            row=3,
            column=0,
            padx=10,
        )

        self.ov_1_text = Label(
            self.ov1_frame,
            text="arm_freq = 2000\ngpu_freq = 750\nover_voltage = 6\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_1_text.grid(
            row=3,
            column=1,
            padx=20,
        )

        self.ov2_frame = LabelFrame(
            self.tu_main_frame,
            text="You Sir, Need A Fan!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        self.ov2_frame.pack(fill="both", expand=True)

        self.ov2_lbl = Label(
            self.ov2_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        self.ov2_lbl.grid(row=4, column=1)

        self.ov_2 = Label(
            self.ov2_frame, image=self.tu_3, bg=maincolor, foreground=main_font
        )
        self.ov_2.grid(
            row=5,
            column=0,
            padx=10,
        )

        self.ov_2_text = Label(
            self.ov2_frame,
            text="arm_freq = 2147\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_2_text.grid(row=5, column=1)

        self.ov3_frame = LabelFrame(
            self.tu_main_frame,
            text="Take It To The Max!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        self.ov3_frame.pack(fill="both", expand=True)

        self.ov3_lbl = Label(
            self.ov3_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        self.ov3_lbl.grid(row=6, column=1)

        self.ov_3 = Label(
            self.ov3_frame, image=self.tu_4, bg=maincolor, foreground=main_font
        )
        self.ov_3.grid(
            row=7,
            column=0,
            padx=10,
        )

        self.ov_3_text = Label(
            self.ov3_frame,
            text="arm_freq = 2200\ngpu_freq = 750\nover_voltage = 8\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        self.ov_3_text.grid(row=7, column=1)

        ov4_frame = LabelFrame(
            self.tu_main_frame,
            text="Honey,the fuse blew again!",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        ov4_frame.pack(fill="both", expand=True)

        ov4_lbl_w = Label(
            ov4_frame,
            text="Works for rev. 1.4 & Pi400",
            bg=maincolor,
            foreground=info_color,
            font=font_9,
            justify=LEFT,
        )
        ov4_lbl_w.grid(row=0, column=1)

        ov_4_i = Label(ov4_frame, image=self.tu_5, bg=maincolor, foreground=main_font)
        ov_4_i.grid(
            row=1,
            column=0,
            padx=10,
        )

        ov_4_text = Label(
            ov4_frame,
            text="arm_freq = 2300\ngpu_freq = 750\nover_voltage = 14\nforce_turbo = 1",
            justify=LEFT,
            bg=maincolor,
            foreground=main_font,
        )
        ov_4_text.grid(row=1, column=1)

        info_frame = Frame(
            self.tu_main_frame,
            bg=maincolor,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        info_frame.pack(fill="both", expand=True)

        pigro_t_info = Label(
            info_frame,
            anchor="w",
            text="To unlock lock the Presets click on Default Settings\n\nSettings tested with:\n- Raspberry Pi 5 4GB Rev.1.0 + Official Activ Cooler\n- Pi400\n- Rev.1.0 Raspberry Pi 4B 8 GB Rev.1.4 + Ice Tower Cooler\n- Raspberry Pi 4B 4 GB Rev.1.1 + Ice Tower Cooler\nPlease note that overclocking the Pi 5 is a bit of gambling.\nNot all Pi 5s can be overclocked.\nInstead of over_voltage use over_voltage_delta.",
            highlightthickness=0,
            justify=LEFT,
            borderwidth=2,
            background=frame_color,
            foreground=info_color,
            font=font_8_b,
        )
        pigro_t_info.grid(column=0, row=0)


class Done_Restart_P(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 150
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        done_label = tk.Label(self)
        ft = tkFont.Font(family="Sans", size=12)
        done_label["font"] = ft
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Restart of PiGro is require\nfor changes to take effect"
        done_label.pack(pady=20)

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"
        cont_btn["font"] = font_10
        cont_btn["fg"] = ext_btn_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Got It!"
        cont_btn.pack()
        cont_btn["command"] = self.destroy


class Done_(tk.Toplevel):
    """custom messagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done!")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 120
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"
        cont_btn["font"] = font_10
        cont_btn["fg"] = ext_btn_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Ok"
        cont_btn.pack(fill="x", expand=True, pady=20, padx=20)
        cont_btn["command"] = self.destroy


class Done_Reboot(tk.Toplevel):
    """a custom massagebox"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Done! Reboot?")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 292
        app_height = 180
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        cont_btn = tk.Button(self)
        cont_btn["bg"] = "#efefef"
        ft = tkFont.Font(family="Sans", size=10)
        cont_btn["font"] = ft
        cont_btn["fg"] = ext_btn_font
        cont_btn["bg"] = ext_btn
        cont_btn["justify"] = "center"
        cont_btn["highlightthickness"] = 0
        cont_btn["borderwidth"] = 0
        cont_btn["text"] = "Continue"
        cont_btn.place(x=50, y=130, width=70, height=25)
        cont_btn["command"] = self.destroy

        rebt_btn = tk.Button(self)
        rebt_btn["bg"] = "#efefef"
        rebt_btn["font"] = font_10
        rebt_btn["fg"] = ext_btn_font
        rebt_btn["bg"] = ext_btn
        rebt_btn["justify"] = "center"
        rebt_btn["highlightthickness"] = 0
        rebt_btn["borderwidth"] = 0
        rebt_btn["text"] = "Reboot"
        rebt_btn.place(x=160, y=130, width=70, height=25)
        rebt_btn["command"] = self.rebt_btn_command

        done_label = tk.Label(self)
        done_label["font"] = font_14
        done_label["fg"] = main_font
        done_label["bg"] = maincolor
        done_label["justify"] = "center"
        done_label["text"] = "Done !"
        done_label.place(x=110, y=40, width=70, height=25)

    def rebt_btn_command(self):
        popen(f"pkexec reboot")


class Update_Pop(tk.Toplevel):
    """NOT IMPLEMENTED YET!"""

    def __init__(self, parent):
        super().__init__(parent)
        self.title("PiGro Update Check")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 552
        app_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.config(bg=maincolor)

        def get_info_version():
            url = "https://github.com/actionschnitzel/PiGro-Aid-/releases/latest"
            r = requests.get(url)

            global github_release
            github_release = r.url.split("/")[-1]
            github_release = str(github_release)

            self.version_label.config(
                text=f"Latest Version: {github_release}\nYour Version: {current_version}"
            )

            def compare_versions(version1, version2):
                parts1 = [int(part) for part in version1.split(".")]
                parts2 = [int(part) for part in version2.split(".")]

                for p1, p2 in zip(parts1, parts2):
                    if p1 > p2:
                        return 1
                    elif p1 < p2:
                        return -1

                if len(parts1) > len(parts2):
                    return 1
                elif len(parts1) < len(parts2):
                    return -1
                else:
                    return 0

            result = compare_versions(current_version, github_release)

            if result >= 0:
                print("[Info] PiGro is up to date.")
                self.nothin_2_do_label.pack(pady=10)
            else:
                print("[Info] An Update is available")
                self.pigro_update_button.pack(pady=10)

        def pigro_github_update():
            popen(
                "xdg-open https://github.com/actionschnitzel/PiGro-Aid-/releases/latest"
            )

        self.auto_start = PhotoImage(file=f"{application_path}/images/icons/logo1.png")

        self.actn_shn = Label(
            self,
            image=self.auto_start,
            background=maincolor,
        ).pack(pady=20)

        self.version_label = Label(
            self, font=font_14, bg=maincolor, fg=main_font, text=" "
        )
        self.version_label.pack(pady=20)

        self.pigro_update_button = tk.Button(self)
        self.pigro_update_button["bg"] = ext_btn
        self.pigro_update_button["highlightthickness"] = 0
        self.pigro_update_button["borderwidth"] = 0
        self.pigro_update_button["font"] = font_10
        self.pigro_update_button["fg"] = ext_btn_font
        self.pigro_update_button["justify"] = "center"
        self.pigro_update_button["text"] = "Download Latest"
        self.pigro_update_button["command"] = pigro_github_update

        self.nothin_2_do_label = Label(self)
        self.nothin_2_do_label["bg"] = maincolor
        self.nothin_2_do_label["highlightthickness"] = 0
        self.nothin_2_do_label["borderwidth"] = 0
        self.nothin_2_do_label["font"] = font_12
        self.nothin_2_do_label["fg"] = main_font
        self.nothin_2_do_label["justify"] = "center"
        self.nothin_2_do_label["text"] = "Nothing to do."

        PATH = f"/home/{user}/pi-apps/data/status/PiGro"
        if os.path.isfile(PATH) is True:
            pigro_via_pi_apps = open(f"/home/{user}/pi-apps/data/status/PiGro", "r")
            install_status = pigro_via_pi_apps.read()
            pigro_via_pi_apps.close()
            if install_status.strip() == "installed":
                self.pigro_update_button.forget()

        get_info_version()


class Error_Mass(tk.Toplevel):
    """opens a popup when entry field is empty"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Info")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 420
        app_height = 220
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def cu_error():
            Error_Mass.destroy(self)

        self.e_m = PhotoImage(file=f"{application_path}/images/backgrounds/yuno.png")

        error_frame = Frame(self, bg=maincolor)
        error_frame.pack(pady=20, padx=20)

        error_img = Label(error_frame, image=self.e_m, bg=maincolor)
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(
            error_frame,
            text="Y U MAKE ERROR?",
            foreground=main_font,
            font=font_16,
            bg=maincolor,
        )
        error_y.grid(row=0, column=1)

        error_y2 = Label(
            error_frame,
            text="You did not enter a value!",
            foreground=main_font,
            bg=maincolor,
        )
        error_y2.grid(row=1, column=1, sticky="n")

        error_btn = Button(
            error_frame,
            text="...got It!",
            foreground=ext_btn_font,
            borderwidth=0,
            highlightthickness=0,
            bg="#f04a50",
            command=cu_error,
        )
        error_btn.grid(row=3, column=0, columnspan=3, sticky="ew", pady=10)


class Int_Error_Mass(tk.Toplevel):
    """opens a popup when entry field is empty"""

    def __init__(self, parent):
        super().__init__(parent)
        #self["background"] = maincolor
        self.title("Info")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 420
        app_height = 220
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def cu_error():
            Error_Mass.destroy(self)

        self.e_m = PhotoImage(file=f"{application_path}/images/backgrounds/hint.png")

        error_frame = Frame(self) #bg=maincolor)
        error_frame.pack(pady=20, padx=20)

        error_img = Label(error_frame, image=self.e_m)#, bg=maincolor)
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(
            error_frame,
            text="I'll give you a hint:\nHere should be an INT",
            #foreground=main_font,
            font=font_16,
            #bg=maincolor,
        )
        error_y.grid(row=0, column=1)
        global error_y2
        error_y2 = Label(
            error_frame,
            text="The value entered must be a number",
            #foreground=main_font,
            #bg=maincolor,
        )
        error_y2.grid(row=1, column=1, sticky="n")

        error_btn = Button(
            error_frame,
            text="...got It!",
            #foreground=ext_btn_font,
            borderwidth=0,
            highlightthickness=0,
            #bg="#f04a50",
            command=cu_error,
        )
        error_btn.grid(row=3, column=0, columnspan=3, sticky="ew", pady=10)


class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info["duration"]
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)


class Look_Disabled(tk.Toplevel):
    """child window that shows tuning options in detail"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Info")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 700
        app_height = 400
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")
        self.e_m = PhotoImage(file=f"{application_path}/images/backgrounds/yuno.png")

        self.tu_main_frame = Frame(self, bg=maincolor)
        self.tu_main_frame.pack(pady=20, padx=20)

        self.rm_lbl = LabelFrame(
            self.tu_main_frame,
            text="Y U DISABLED?",
            bg=maincolor,
            foreground=label_frame_color,
            font=font_14,
            borderwidth=0,
            padx=20,
            pady=10,
        )
        self.rm_lbl.pack(fill="both", expand=True)

        self.rm_ov = Label(self.rm_lbl, image=self.e_m, bg=maincolor)
        self.rm_ov.grid(
            row=0,
            column=0,
            padx=10,
        )

        self.rm_ovs = Label(
            self.rm_lbl,
            text="The new Look & Feel tab is tailored to the capabilities of the desktop environment you are using. In Raspberry Pi OS Bookworm, compromises were made. This window is only displayed when you are using the Wayfire variant of the Pixel desktop. Color adjustments can only be made using the tools provided by PiOS, which can be found in the System tab. Currently, only the Pixel theme can be reliably used on Pixel. Changing the desktop environment theme or icon theme may lead to display issues with the Wayfire window manager.\n\nIf you are not satisfied with the performance under Wayland you can switch to X11:\n\nsudo raspi-config > 6 Advanced Options > A6 Wayland > W1 X11",
            wraplength=400,
            bg=maincolor,
            justify="left",
            fg=main_font,
        )
        self.rm_ovs.grid(
            row=0,
            column=1,
            padx=10,
        )


class RestartPigroMass(tk.Toplevel):
    """opens a popup when entry field is empty"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.title("Info")
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        app_width = 420
        app_height = 220
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (app_width / 2)
        y = (screen_height / 2) - (app_height / 2)
        self.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        def cu_error():
            Error_Mass.destroy(self)

        self.e_m = PhotoImage(file=f"{application_path}/images/icons/logo1.png")

        error_frame = Frame(self, bg=maincolor)
        error_frame.pack(pady=20, padx=20)

        error_img = Label(error_frame, image=self.e_m, bg=maincolor)
        error_img.grid(row=0, column=0, rowspan=2)

        error_y = Label(
            error_frame,
            text="Please restart PiGro",
            foreground=main_font,
            font=font_16,
            bg=maincolor,
        )
        error_y.grid(row=0, column=1)
        global error_y2
        error_y2 = Label(
            error_frame,
            text="After that, the changes come into effect",
            foreground=main_font,
            bg=maincolor,
        )
        error_y2.grid(row=1, column=1, sticky="n")

        error_btn = Button(
            error_frame,
            text="...got It!",
            foreground=ext_btn_font,
            borderwidth=0,
            highlightthickness=0,
            bg="#f04a50",
            command=cu_error,
        )
        error_btn.grid(row=3, column=0, columnspan=3, sticky="ew", pady=10)
