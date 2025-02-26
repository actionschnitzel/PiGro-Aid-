#!/usr/bin/python3

import os
import os.path
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from resorcess import *
from apt_manage import *
from snap_manage import *
from flatpak_alias_list import *
from flatpak_manage import *
from tool_tipps import CreateToolTip
from tool_tipps import TipsText
from tabs.pop_ups import *
from tabs.text_dict_lib import Update_Tab_Buttons
from resorcess import pi_identify
from icon_lib import UpdateTabIcons


class UpdateTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.update_tab_icons = UpdateTabIcons()

        def up_action(text):
            """Passes commands du auto generated buttons"""
            frame_width = self.termf.winfo_width()

            frame_height = self.termf.winfo_height()
            print(
                "The width & height of the label is:",
                frame_width,
                frame_height,
                "pixels",
            )
            if text == "Update":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt update -y |lolcat && sleep 5 && exit ; exec bash"'
                    % wid
                )
            if text == "Update & Upgrade":
                if pi_identify() == "pi_os":
                    os.popen(
                        f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt update -y |lolcat && {permit} apt upgrade -y |lolcat && sleep 5 && exit ; exec bash"'
                        % wid
                    )
                else:
                    command = (
                        f"xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "
                        "\"pkexec env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY bash -c 'apt update -y && apt upgrade -y' | lolcat && "
                        'sleep 5 && exit; exec bash"' % wid
                    )
                    os.popen(command)
            if text == "Fix Missing":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt install --fix-missing |lolcat && sleep 5 && exit; exec bash"'
                    % wid
                )
            if text == "Fix Broken":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt --fix-broken install |lolcat && sleep 5 && exit; exec bash"'
                    % wid
                )
            if text == "Dist Upgrade":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt dist-upgrade -y |lolcat && sleep 5 && exit; exec bash"'
                    % wid
                )
            if text == "Autoremove":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} apt autoremove -y |lolcat && sleep 5 && exit ; exec bash"'
                    % wid
                )
            if text == "Install Local .DEB":
                self.filename = filedialog.askopenfilename(
                    initialdir="~",
                    title="Select A File",
                    filetypes=((".deb files", "*.deb"),),
                )
                os.popen(f"gdebi-gtk {self.filename}")

            if text == "dpkg --configure -a":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} dpkg --configure -a |lolcat && sleep 5 && exit; exec bash"'
                    % wid
                )
            if text == "Allow Sources":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{application_path}/scripts/addunsignedrepo.sh && exit; exec bash"'
                    % wid
                )
            if text == "Show Upgradable":
                if pi_identify() == "pi_os":
                    subprocess.run(
                        f"xterm -into {wid} -bg Grey11 -geometry {frame_height}x{frame_width} -e \"{permit} apt list --upgradable |lolcat && read -p 'Press Enter to exit.' && exit ; exec bash\"",
                        shell=True,
                    )
                else:
                    os.popen(
                        f"xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "
                        "\"pkexec apt list --upgradable |lolcat && read -p 'Press Enter to exit.' && exit; exec bash\""
                        % wid
                    )

        self.update_btn_frame = ttk.Frame(
            self,
        )
        self.update_btn_frame.pack(padx=20, pady=20, anchor="n", fill="x", side="left")

        self.termf = ttk.LabelFrame(self, text="Progress")

        self.term_logo_label = Label(
            self.termf,
            image=self.update_tab_icons.term_logo,
        )
        self.term_logo_label.pack(fill=BOTH, expand=True)

        self.termf.pack(fill=BOTH, expand=True, pady=20, padx=20)

        global wid
        wid = self.termf.winfo_id()

        self.btn_frame = ttk.LabelFrame(
            self.update_btn_frame,
            text="APT Options",
        )
        self.btn_frame.pack(anchor="n")

        up_button_dict = Update_Tab_Buttons.up_button_dict

        up_button_list1 = []
        conf_row = 0
        conf_column = 0

        for up_button, description in up_button_dict.items():
            self.up_button_x = ttk.Button(
                self.btn_frame,
                compound="left",
                text=up_button,
                command=lambda text=up_button: up_action(text),
                width=20,
            )

            self.up_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            up_button_list1.append(self.up_button_x)
            conf_column += 1

            if conf_column == 1:
                conf_row += 1
                conf_column = 0

            if up_button == "Update":
                self.up_button_x.config(image=self.update_tab_icons.up_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Show Upgradable":
                self.up_button_x.config(image=self.update_tab_icons.up_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Fix Missing":
                self.up_button_x.config(image=self.update_tab_icons.up_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Fix Broken":
                self.up_button_x.config(image=self.update_tab_icons.up_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Update & Upgrade":
                self.up_button_x.config(image=self.update_tab_icons.gup_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Autoremove":
                self.up_button_x.config(image=self.update_tab_icons.arm_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Install Local .DEB":
                self.up_button_x.config(image=self.update_tab_icons.inst_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "dpkg --configure -a":
                self.up_button_x.config(image=self.update_tab_icons.confa_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)
            elif up_button == "Allow Sources":
                self.up_button_x.config(image=self.update_tab_icons.gup_icon)
                self.up_button_x_ttp = CreateToolTip(self.up_button_x, description)

        def nala_action(text):
            """Passes commands for auto-generated buttons"""
            frame_width = self.termf.winfo_width()
            frame_height = self.termf.winfo_height()
            print(
                "The width & height of the label is:",
                frame_width,
                frame_height,
                "pixels",
            )

            if text == "Fetch":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} nala fetch && sleep 5 && exit ; exec bash"'
                    % wid
                )
            elif text == "Update":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} nala update && sleep 5 && exit ; exec bash"'
                    % wid
                )
            elif text == "Update & Upgrade":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} nala upgrade && sleep 5 && exit ; exec bash"'
                    % wid
                )

        self.nala_frame = ttk.LabelFrame(
            self.update_btn_frame,
            text="Nala Options",
        )
        self.nala_frame.pack(anchor="n", fill="x")

        self.nala_frame.columnconfigure(0, weight=1)
        self.nala_frame.rowconfigure(0, weight=1)

        nala_button_dict = {
            "Update": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if nala_path else DISABLED,
                "tooltip": TipsText.ttip_nala_update,
            },
            "Update & Upgrade": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if nala_path else DISABLED,
                "tooltip": TipsText.ttip_nala_update,
            },
            "Fetch": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if nala_path else DISABLED,
                "tooltip": "Which brings us to our next standout feature, nala fetch.This command works similar to how most people use netselect and netselect-apt.nala fetch will check if your distro is either Debian or Ubuntu.Nala will then go get all the mirrors from the respective master list.Once done we test the latency and score each mirror.Nala will choose the fastest 3 mirrors (configurable) and write them to a file.",
            },
        }

        nala_button_list1 = []
        conf_row = 0
        conf_column = 0

        for nala_button, config in nala_button_dict.items():
            self.nala_button_x = ttk.Button(
                self.nala_frame,
                compound="left",
                text=nala_button,
                command=lambda btn=nala_button: nala_action(btn),
                state=config.get("state", NORMAL),
                width=20,
            )

            self.nala_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            nala_button_list1.append(self.nala_button_x)
            conf_column += 1

            if conf_column == 1:
                conf_row += 1
                conf_column = 0

            self.nala_button_x.config(image=config["image"], state=config["state"])
            self.nala_button_x_ttp = CreateToolTip(
                self.nala_button_x, config["tooltip"]
            )

        def flatpak_action(text):
            """Passes commands for auto-generated buttons"""
            frame_width = self.termf.winfo_width()
            frame_height = self.termf.winfo_height()
            print(
                "The width & height of the label is:",
                frame_width,
                frame_height,
                "pixels",
            )

            if text == "Update":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "flatpak update -y && sleep 5 && exit ; exec bash"'
                    % wid
                )
            elif text == "Tidy Up Unused":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "flatpak uninstall --unused -y && sleep 5 && exit; exec bash"'
                    % wid
                )

        self.flatpak_frame = ttk.LabelFrame(
            self.update_btn_frame,
            text="Flatpak Options",
        )
        self.flatpak_frame.pack(anchor="n", fill="x")

        self.flatpak_frame.columnconfigure(0, weight=1)
        self.flatpak_frame.rowconfigure(0, weight=1)

        flatpak_button_dict = {
            "Update": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if flatpak_path else DISABLED,
                "tooltip": TipsText.ttip_flatpak_update,
            },
            "Tidy Up Unused": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if flatpak_path else DISABLED,
                "tooltip": TipsText.ttip_flatpak_unused,
            },
        }

        flatpak_button_list1 = []
        conf_row = 0
        conf_column = 0

        for flatpak_button, config in flatpak_button_dict.items():
            self.flatpak_button_x = ttk.Button(
                self.flatpak_frame,
                compound="left",
                text=flatpak_button,
                command=lambda btn=flatpak_button: flatpak_action(btn),
                state=config.get("state", NORMAL),
                width=20,
            )
            self.flatpak_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            flatpak_button_list1.append(self.flatpak_button_x)
            conf_column += 1

            if conf_column == 1:
                conf_row += 1
                conf_column = 0

            self.flatpak_button_x.config(image=config["image"], state=config["state"])
            self.flatpak_button_x_ttp = CreateToolTip(
                self.flatpak_button_x, config["tooltip"]
            )

        def snap_action(text):
            """Passes commands for auto-generated buttons"""
            frame_width = self.termf.winfo_width()
            frame_height = self.termf.winfo_height()
            print(
                "The width & height of the label is:",
                frame_width,
                frame_height,
                "pixels",
            )

            if text == "Update":
                os.popen(
                    f'xterm -into %d -bg Grey11 -geometry {frame_height}x{frame_width} -e "{permit} snap refresh && sleep 5 && exit ; exec bash"'
                    % wid
                )

        self.snap_frame = ttk.LabelFrame(
            self.update_btn_frame,
            text="Snap Options",
        )
        self.snap_frame.pack(anchor="n", fill="x", expand=True)

        self.snap_frame.columnconfigure(0, weight=1)
        self.snap_frame.rowconfigure(0, weight=1)

        snap_button_dict = {
            "Update": {
                "image": self.update_tab_icons.up_icon,
                "state": NORMAL if is_snap_installed() else DISABLED,
            },
        }

        snap_button_list1 = []
        conf_row = 0
        conf_column = 0

        for snap_button, config in snap_button_dict.items():
            self.snap_button_x = ttk.Button(
                self.snap_frame,
                compound="left",
                text=snap_button,
                command=lambda btn=snap_button: snap_action(btn),
                state=config.get("state", NORMAL),
                width=20,
            )
            self.snap_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            snap_button_list1.append(self.snap_button_x)
            conf_column += 1

            if conf_column == 1:
                conf_row += 1
                conf_column = 0

            self.snap_button_x.config(image=config["image"], state=config["state"])
