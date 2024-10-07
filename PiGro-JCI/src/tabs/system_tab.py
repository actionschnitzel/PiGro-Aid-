#!/usr/bin/python3

import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *
from tabs.system_tab_check import *
from tabs.text_dict_lib import SystemTabDict
from tool_tipps import CreateToolTip


class SystemTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")
        """System Tab Icons"""
        self.raspi_config_cli_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.raspi_config_gui_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.rename_user_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-raspbian.png"
        )
        self.edit_config_txt_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/mousepad.png"
        )
        self.gparted_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/gparted.png"
        )
        self.mouse_keyboard_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/gnome-settings-keybinding.png"
        )
        self.deskpipro_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/deskpi.png"
        )
        self.network_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/blueman-server.png"
        )
        self.sd_card_copier_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/media-flash-sd-mmc.png"
        )
        self.printer_settings_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/boomaga.png"
        )
        self.desktop_settings_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/com.github.bluesabre.darkbar.png"
        )
        self.screen_settings_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/grandr.png"
        )
        self.neofetch_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/neofetch.png"
        )
        self.fm_godmode_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/folder-yellow.png"
        )
        self.kernel_2_latest_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-madlinux.png"
        )
        self.boot_log_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/bash.png"
        )
        self.xfce_autostarts_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.xfce_settings_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/desktop-environment-xfce.png"
        )
        self.taskmanager_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/appimagekit-gqrx.png"
        )
        self.bash_history_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/bash.png"
        )
        self.cron_job_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/mousepad.png"
        )
        self.alacard_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/classicmenu-indicator-light.png"
        )
        self.source_settings_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/applications-interfacedesign.png"
        )

        self.update_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/aptdaemon-upgrade.png"
        )
        self.bookshelf_icon = PhotoImage(
            file=f"{application_path}/images/icons/PiXflat/bookshelf.png"
        )
        self.raspi_pipanel = PhotoImage(
            file=f"{application_path}/images/icons/PiXflat/preferences-desktop-theme.png"
        )
        self.gnome_ext_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/org.gnome.Extensions.png"
        )
        self.gnome_tweaks_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/gnome-tweak-tool.png"
        )

        def pi_settings(text):
            """commands for auto generated buttons"""
            if text == "Raspi Bookshelf":
                popen("rp-bookshelf")
            if text == "Raspi-Config GUI":
                popen("env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui")
            if text == "Raspi-Config CLI":
                popen(
                    f"x-terminal-emulator -e 'bash -c \"sudo raspi-config; exec bash\"'"
                )

            if text == "Edit Config.txt":
                popen(f"{permit} mousepad {config_path}")
                print("[Info] With great power comes great responsibility")

            if text == "Raspi Diagnostics":
                popen("agnostics")

            if text == "Raspi Recommended\nSoftware":
                popen(
                    "env SUDO_ASKPASS=/usr/lib/rp-prefapps/pwdrpp.sh sudo -AE rp-prefapps"
                )
            if text == "Gparted":
                popen(f"{permit}  gparted")
            if text == "Raspi Mouse & Keyboard":
                popen("lxinput")
            if text == "DeskpiPro Control":
                popen("x-terminal-emulator -e 'bash -c \"deskpi-config; exec bash\"'")
            if text == "Raspi SD Card Copier":
                popen(
                    "env SUDO_ASKPASS=/usr/lib/piclone/pwdpic.sh sudo -AE dbus-launch piclone"
                )
            if text == "Raspi Printer Settings":
                popen("system-config-printer")
            if text == "Raspi Desktop Settings":
                popen("pcmanfm --desktop-pref")
            if text == "Raspi Screen Settings":
                popen("lxrandr")
            if text == "NeoFetch":
                popen("x-terminal-emulator -e 'bash -c \"neofetch; exec bash\"'")
            if text == "FM God Mode":
                if get_desktop_environment() == "gnome":
                    popen(
                        f"{permit} env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xdg-open /"
                    )

                if get_desktop_environment() == "lxde-pi" or "lxde-pi-wayfire":
                    popen(f"sudo pcmanfm /")

                print("[Info] With great power comes great responsibility")

            if text == "dmesg":
                if os.environ.get("DESKTOP_SESSION") == "gnome" or "ubuntu":
                    popen("x-terminal-emulator -e 'bash -c \"sudo dmesg; exec bash\"'")

                elif (
                    os.environ.get("DESKTOP_SESSION") == "LXDE-pi" or "LXDE-pi-wayfire"
                ):
                    popen("x-terminal-emulator -e 'bash -c \"dmesg; exec bash\"'")
            if text == "dmesg --follow":
                if os.environ.get("DESKTOP_SESSION") == "ubuntu:gnome" or "ubuntu":
                    popen(
                        "x-terminal-emulator -e 'bash -c \"sudo dmesg --follow; exec bash\"'"
                    )

                elif (
                    os.environ.get("DESKTOP_SESSION") == "LXDE-pi" or "LXDE-pi-wayfire"
                ):
                    popen(
                        "x-terminal-emulator -e 'bash -c \"dmesg --follow; exec bash\"'"
                    )

            if text == "Xfce Settings":
                popen("xfce4-settings-manager")

            if text == "Taskmanager":
                popen("lxtask")

            if text == "Bash History":
                popen(f"xdg-open {home}/.bash_history")

            if text == "Cron Job":
                popen(f"{permit}  mousepad /etc/crontab")

            if text == "Menu Settings\nAlacart":
                popen("alacarte")

            if text == "Update-Alternatives":
                add_auto = Update_Alternatives(self)
                add_auto.grab_set()

            if text == "Gnome Tweaks":
                popen("gnome-tweaks")

            if text == "Gnome Extensions":
                popen("xdg-open https://extensions.gnome.org/")

            if text == "Gnome Software\nUpdates":
                popen("update-manager")

            if text == "Gnome Update\nSettings":
                popen("software-properties-gtk")

            if text == "Gnome Settings":
                popen("gnome-control-center")

            if text == "Reconfigure Keyboard":
                popen(
                    "x-terminal-emulator -e 'bash -c \"sudo dpkg-reconfigure keyboard-configuration; exec bash\"'"
                )

            if text == "Reconfigure Locales":
                popen(
                    "x-terminal-emulator -e 'bash -c \"sudo dpkg-reconfigure locales; exec bash\"'"
                )
            if text == "Raspi Appearance\nSettings":
                popen("pipanel")

        self.pi_set = LabelFrame(
            self,
            text="Raspberry Pi Settings",
            font=font_16,
            #foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
            pady=10,
            padx=10,
        )
        self.pi_set.pack(pady=20, padx=40, fill="both")
        #self.pi_set["background"] = frame_color

        pi_settings_btn_list = [
            "Bash History",
            "Cron Job",
            "DeskpiPro Control",
            "dmesg --follow",
            "dmesg",
            "Edit Config.txt",
            "FM God Mode",
            "Gnome Extensions",
            "Gnome Settings",
            "Gnome Software\nUpdates",
            "Gnome Tweaks",
            "Gnome Update\nSettings",
            "Gparted",
            "Menu Settings\nAlacart",
            "NeoFetch",
            "Raspi Appearance\nSettings",
            "Raspi Bookshelf",
            "Raspi-Config CLI",
            "Raspi-Config GUI",
            "Raspi Diagnostics",
            "Raspi Mouse & Keyboard",
            "Raspi Printer Settings",
            "Raspi Screen Settings",
            "Raspi SD Card Copier",
            "Raspi Recommended\nSoftware",
            "Reconfigure Keyboard",
            "Reconfigure Locales",
            "Update-Alternatives",
            "Xfce Settings",
        ]
        pi_settings_btn_list1 = []
        conf_row = 0
        conf_column = 0
        for pi_settings_btn in pi_settings_btn_list:
            self.pi_button_x = Button(
                self.pi_set,
                width=140,
                height=110,
                text=pi_settings_btn,
                command=lambda text=pi_settings_btn: pi_settings(text),
                highlightthickness=0,
                borderwidth=0,
                #background=frame_color,
                foreground=main_font,
                compound=TOP,
                activebackground=ext_btn,
            )
            self.pi_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="nesw"
            )
            pi_settings_btn_list1.append(self.pi_button_x)
            conf_column = conf_column + 1
            if conf_column == 5:
                conf_row = conf_row + 1
                conf_column = 0

            if pi_settings_btn == "Raspi Bookshelf":
                self.pi_button_x.config(image=self.bookshelf_icon)

                if check_bookshelf() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Recommended\nSoftware":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
                if check_agnostics() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Diagnostics":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
                if check_rp_prefapps() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi-Config CLI":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
                if check_raspi_config() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Appearance\nSettings":
                self.pi_button_x.config(image=self.raspi_pipanel)
                if check_pipanel() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi-Config GUI":
                self.pi_button_x.config(image=self.raspi_config_cli_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Edit Config.txt":
                self.pi_button_x.config(image=self.edit_config_txt_icon)

            if pi_settings_btn == "Raspi Mouse & Keyboard":
                self.pi_button_x.config(image=self.mouse_keyboard_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "DeskpiPro Control":
                self.pi_button_x.config(image=self.deskpipro_icon)
                if check_deskpi_config() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi SD Card Copier":
                self.pi_button_x.config(image=self.sd_card_copier_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Printer Settings":
                self.pi_button_x.config(image=self.printer_settings_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Desktop Settings":
                self.pi_button_x.config(image=self.desktop_settings_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "Raspi Screen Settings":
                self.pi_button_x.config(image=self.screen_settings_icon)
                if check_rc_gui() == False:
                    self.pi_button_x.configure(state=DISABLED)
            if pi_settings_btn == "NeoFetch":
                self.pi_button_x.config(image=self.neofetch_icon)
                if os.path.isfile("/bin/neofetch"):
                    print("[Info] Neofetch is installed")
                    self.pi_button_x.configure(state=NORMAL)
                else:
                    print("[Info] Neofetch is not installed")
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Gparted":
                self.pi_button_x.config(image=self.gparted_icon)
                if os.path.isfile("/usr/sbin/gparted"):
                    print("[Info] Gparted is installed")
                    self.pi_button_x.configure(state=NORMAL)
                else:
                    print("[Info] Gparted is not installed")
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "FM God Mode":
                self.pi_button_x.config(image=self.fm_godmode_icon)

            if pi_settings_btn == "dmesg --follow":
                self.pi_button_x.config(image=self.boot_log_icon)
            if pi_settings_btn == "dmesg":
                self.pi_button_x.config(image=self.boot_log_icon)

            if pi_settings_btn == "Reconfigure Keyboard":
                self.pi_button_x.config(image=self.boot_log_icon)
            if pi_settings_btn == "Reconfigure Locales":
                self.pi_button_x.config(image=self.boot_log_icon)

            if pi_settings_btn == "Xfce Settings":
                self.pi_button_x.config(image=self.xfce_settings_icon)
                self.pi_button_x.configure(state=DISABLED)
                if get_desktop_environment() == "xfce":
                    self.pi_button_x.configure(state=NORMAL)

            if pi_settings_btn == "Bash History":
                self.pi_button_x.config(image=self.bash_history_icon)

            if pi_settings_btn == "Cron Job":
                self.pi_button_x.config(image=self.cron_job_icon)

            if pi_settings_btn == "Menu Settings\nAlacart":
                self.pi_button_x.config(image=self.alacard_icon)
                if check_alacarte() == False:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Update-Alternatives":
                self.pi_button_x.config(image=self.bash_history_icon)

            if pi_settings_btn == "Gnome Tweaks":
                self.pi_button_x.config(image=self.gnome_tweaks_icon)
                if check_gnome_tweaks() == False:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Gnome Extensions":
                self.pi_button_x.config(image=self.gnome_ext_icon)
                if get_desktop_environment() == "gnome":
                    self.pi_button_x.configure(state=NORMAL)
                else:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Gnome Software\nUpdates":
                self.pi_button_x.config(image=self.update_icon)
                if check_update_manager() == False:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Gnome Update\nSettings":
                self.pi_button_x.config(image=self.update_icon)
                if check_software_properties_gtk() == False:
                    self.pi_button_x.configure(state=DISABLED)

            if pi_settings_btn == "Gnome Settings":
                self.pi_button_x.config(image=self.source_settings_icon)
                if check_gnome_control_center() == False:
                    self.pi_button_x.configure(state=DISABLED)
