from tkinter import Tk, PhotoImage

# from resorcess import application_path
from int_theme import get_theme
from PIL import Image, ImageTk
import os


script_dir = os.path.dirname(os.path.abspath(__file__))
application_path = os.path.dirname(script_dir)


class NavIcons:
    def __init__(self):
        if "dark" in get_theme() or "noir" in get_theme():
            # self.tk.call("set_theme", "dark")
            self.status_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/dash_dark_24x24.png"
            )

            self.system_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sys_dark_24x24.png"
            )
            self.update_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/update_dark_24x24.png"
            )
            self.install_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/software_dark_24x24.png"
            )
            self.look_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/look_dark_24x24.png"
            )
            self.tuning_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tuning_dark_24x24.png"
            )
            self.links_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/links_dark_24x24.png"
            )
            self.support_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/about_dark_24x24.png"
            )
            self.cam_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/gtkam-camera.png"
            )
            self.ubuntu_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-ubuntu.png"
            )
            self.auto_start = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/auto_dark_24x24.png"
            )
            self.kill_proc = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tasks_dark_24x24.png"
            )
            self.git_more = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_dark_24x24.png"
            )

            self.deb_pack = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/backup_dark_24x24.png"
            )
            self.source_lists = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sources_dark_16x16.png"
            )

            self.deb_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/debian_dark_24x24.png"
            )

            self.piapps_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/piapps_dark_24x24.png"
            )
            self.snap_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/snap_dark_24x24.png"
            )

            self.flatpak_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/flatpak_dark_24x24.png"
            )

            self.oneclick_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_dark_24x24.png"
            )
            self.q_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/apt_queue_dark_24x24.png"
            )
            self.exit_btn = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
            )
            self.search_btn = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/glass_icon.png"
            )
            self.one_click_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/1click_dark_24x24.png"
            )

        else:
            self.status_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/dash_light_24x24.png"
            )
            self.system_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sys_light_24x24.png"
            )
            self.update_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/update_light_24x24.png"
            )
            self.install_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/software_light_24x24.png"
            )
            self.look_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/look_light_24x24.png"
            )
            self.tuning_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tuning_light_24x24.png"
            )
            self.links_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/links_light_24x24.png"
            )
            self.support_icon = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/about_light_24x24.png"
            )
            self.cam_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/gtkam-camera.png"
            )
            self.ubuntu_icon = PhotoImage(
                file=f"{application_path}/images/icons/papirus/48x48/distributor-logo-ubuntu.png"
            )
            self.auto_start = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/auto_light_24x24.png"
            )
            self.kill_proc = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/tasks_light_24x24.png"
            )
            self.git_more = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_light_24x24.png"
            )

            self.deb_pack = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/backup_light_24x24.png"
            )
            self.source_lists = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/sources_light_16x16.png"
            )

            self.deb_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/debian_light_24x24.png"
            )

            self.piapps_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/piapps_light_24x24.png"
            )

            self.flatpak_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/flatpak_light_24x24.png"
            )

            self.oneclick_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/g2h_light_24x24.png"
            )
            self.q_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/apt_queue_light_24x24.png"
            )
            self.exit_btn = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
            )
            self.search_btn = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/glass_icon.png"
            )
            self.snap_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/snap_light_24x24.png"
            )
            self.one_click_nav = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/1click_light_24x24.png"
            )


class UpdateTabIcons:

    def __init__(self):
        if "dark" in get_theme() or "noir" in get_theme():
            self.folder_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/folder_s.png"
            )
            self.up_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_up_s.png"
            )
            self.gup_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_upg_s.png"
            )
            self.recover_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/recover_s.png"
            )
            self.fup_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_fupg_s.png"
            )
            self.allow_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/allow_s.png"
            )
            self.arm_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/del_s.png"
            )
            self.confa_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/confa_s.png"
            )
            self.re_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/re_s.png"
            )
            self.inst_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/debinst_s.png"
            )
            self.term_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/terminal_s.png"
            )
            self.term_logo = PhotoImage(
                file=f"{application_path}/images/icons/papirus/goterminal.png"
            )
        else:
            self.folder_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/folder_s_light.png"
            )
            self.up_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_up_s_light.png"
            )
            self.gup_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_upg_s_light.png"
            )
            self.recover_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/recover_s_light.png"
            )
            self.fup_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/pack_fupg_s_light.png"
            )
            self.allow_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/allow_s_light.png"
            )
            self.arm_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/del_s_light.png"
            )
            self.confa_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/confa_s_light.png"
            )
            self.re_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/re_s_light.png"
            )
            self.inst_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/debinst_s_light.png"
            )
            self.term_icon = PhotoImage(
                file=f"{application_path}/images/icons/pigro_icons/terminal_s_light.png"
            )
            self.term_logo = PhotoImage(
                file=f"{application_path}/images/icons/papirus/goterminal_light.png"
            )


class PigroIcons:
    def __init__(self):
        self.pigro_256 = PhotoImage(
            file=f"/usr/share/icons/hicolor/256x256/apps/pigro-logo.png"
        )
        self.pigro_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/pigro_icons/pigrologo.png")
        )
        self.pigroh_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/pigro_icons/pigrologoh.png")
        )
        self.pigrox_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/pigro_icons/pigrologox.png")
        )
        self.pigro_feb_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/pigro_icons/pigrologo_feb.png")
        )


class ColorIcons:
    def __init__(self):
        self.debinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/64x64/debian-logo.png"
        )
        self.no_img = PhotoImage(file=f"{application_path}/images/apps/no_image.png")

        self.exit_btn = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
        )
        self.flatpak_big_icon = PhotoImage(
            file=f"{application_path}/images/icons/flatpak-glogo.png"
        )
        self.flatpak_appsinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/flathub64x64.png"
        )
        self.boot_log_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack.png"
        )
        self.install_ok_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack_ok.png"
        )
        self.install_error_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack_error.png"
        )
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
