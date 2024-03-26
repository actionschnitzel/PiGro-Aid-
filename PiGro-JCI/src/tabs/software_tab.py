import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
import tkinter.font as tkFont
from threading import Thread
from PIL import ImageTk, Image
from urllib.request import urlopen
import urllib.error
import requests
import xml.etree.ElementTree as ET
import apt
from bs4 import BeautifulSoup
from resorcess import *
from apt_manage import *
import subprocess
from piapps_manage import *
from flatpak_manage import flatpak_path
from flatpak_manage import Flat_remote_dict
from flatpak_manage import refresh_flatpak_installs
from flatpak_alias_list import *
from tabs.pop_ups import *
import re
import webbrowser
from subprocess import Popen, PIPE
from threading import Thread
from tool_tipps import CreateToolTip
from tabs.text_dict_lib import OneClicks, PiAppsOneClicks, FlatpakOneClicks


def resize(img):
    basewidth = 500
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    return img.resize((basewidth, hsize))


def resize2(img):
    basewidth = 96
    wpercent = basewidth / float(img.size[0])
    hsize = int((float(img.size[1]) * float(wpercent)))
    return img.resize((basewidth, hsize))


def get_app_summary(appstream_id):
    command = f"appstreamcli dump {appstream_id} | grep -m 1 -oP '<summary>\K[^<]*'"
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        print(f"Error executing the command: {e.stderr}")
        return ""


def extract_default_screenshot_url(application_id):
    output = subprocess.check_output(
        ["appstreamcli", "dump", application_id], text=True
    )

    start_index = output.find("<screenshots>")
    end_index = output.find("</screenshots>") + len("</screenshots>")

    xml_part = output[start_index:end_index]

    root = ET.fromstring(xml_part)

    for screenshot in root.findall(
        ".//screenshot[@type='default']/image[@type='source']"
    ):
        return screenshot.text

    return None


def build_screenshot_url():
    app_id = Flat_remote_dict[flatpak_entry.get()]

    screenshot_url = extract_default_screenshot_url(app_id)
    if screenshot_url:
        print("Standard-Screenshot-URL für {}:".format(app_id))
        print(screenshot_url)

    else:
        print("Kein Standard-Screenshot gefunden für {}.".format(app_id))


class SoftwareTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.inst_notebook = ttk.Notebook(self)
        self.inst_notebook.pack(fill=BOTH, expand=True)

        self.deban_navbar_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/deb_s.png"
        )
        self.debinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/64x64/debian-logo.png"
        )
        self.pi_appsinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/pi-apps64x64.png"
        )
        self.pi_appsopen_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/piapps_logo_24x24.png"
        )
        self.pi_appssett_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/piapps_settings_24x24.png"
        )
        self.flatpak_appsinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/flathub64x64.png"
        )
        self.no_img = PhotoImage(file=f"{application_path}/images/apps/no_image.png")

        self.ok_installed = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/ok_16x16.png"
        )

        self.not_ok_installed = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/not_ok_16x16.png"
        )

        self.pi_apps_big_icon = PhotoImage(
            file=f"{application_path}/images/icons/pi-apps-glogo.png"
        )

        self.flatpak_big_icon = PhotoImage(
            file=f"{application_path}/images/icons/flatpak-glogo.png"
        )

        self.deb_pack_l = PhotoImage(
            file=f"{application_path}/images/icons/deb_pack_l.png"
        )
        self.piapps_pack_l = PhotoImage(
            file=f"{application_path}/images/icons/piapps_pack_l.png"
        )
        self.flat_pack_l = PhotoImage(
            file=f"{application_path}/images/icons/flat_pack_l.png"
        )
        self.deb_butt = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/debian_dark_24x24.png"
        )

        self.piapps_butt = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/piapps_dark_24x24.png"
        )
        self.snap_butt = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/snap_dark_24x24.png"
        )

        self.flatpak_butt = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/flatpak_dark_24x24.png"
        )

        if "dark" in theme or "noir" in theme:
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

        apt_frame = ttk.Frame(self.inst_notebook)
        piapps_frame = ttk.Frame(self.inst_notebook)
        flat_frame = ttk.Frame(self.inst_notebook)

        apt_frame.pack(fill="both", expand=True)
        piapps_frame.pack(fill="both", expand=True)
        flat_frame.pack(fill="both", expand=True)

        # add frames to notebook
        self.inst_notebook.add(apt_frame, compound=LEFT, text="APT", image=self.deb_nav)

        self.inst_notebook.add(
            piapps_frame, compound=LEFT, text="Pi Apps", image=self.piapps_nav
        )
        self.inst_notebook.add(
            flat_frame, compound=LEFT, text="Flatpak", image=self.flatpak_nav
        )

        piapps_frame.columnconfigure(0, weight=1)
        piapps_frame.rowconfigure(0, weight=1)

        flat_frame.columnconfigure(0, weight=1)
        flat_frame.rowconfigure(0, weight=1)

        apt_search_panel = AptSearchPanel(apt_frame)
        apt_search_panel.pack(fill=tk.BOTH, expand=True)

        piapps_search_panel = PiAppsSearchPanel(piapps_frame)
        piapps_search_panel.pack(fill=tk.BOTH, expand=True)

        flatpack_search_panel = FlatpakSearchPanel(flat_frame)
        flatpack_search_panel.pack(fill=tk.BOTH, expand=True)


class AptSearchPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        def error_message_0():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_message_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        self["background"] = maincolor
        if "dark" in theme or "noir" in theme:
            self.deb_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/debian_dark_24x24.png"
            )
        else:
            self.deb_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/debian_light_24x24.png"
            )
        self.debinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/64x64/debian-logo.png"
        )
        self.no_img = PhotoImage(file=f"{application_path}/images/apps/no_image.png")
        self.deb_pack_l = PhotoImage(
            file=f"{application_path}/images/icons/deb_pack_l.png"
        )

        self.deb_nav = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/debian_light_24x24.png"
        )
        self.search_btn = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/glass_icon.png"
        )
        self.exit_btn = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
        )

        def apt_install():
            hide_apt_frame()
            pigro_skript_task = "Installing ..."
            pigro_skript_task_app = f"{apt_entry.get()}"
            pigro_skript = [f"{permit}", "apt", "install", "-y", f"{apt_entry.get()}"]
            custom_installer = Custom_Installer(master)
            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

        def apt_uninstall():
            hide_apt_frame()
            pigro_skript_task = "Removing From System"
            pigro_skript_task_app = f"{apt_entry.get()}"
            pigro_skript = [f"{permit}", "apt", "remove", "-y", f"{apt_entry.get()}"]

            custom_installer = Custom_Installer(master)
            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

            apt_search_container.pack(anchor="w", side=LEFT, pady=20, padx=10)

        def update_apt_list(apt_data):
            apt_data = sorted(apt_data)
            apt_list_box.delete(0, END)
            for item in apt_data:
                apt_list_box.insert(END, item)

        def apt_list_fillout(e):
            apt_entry.delete(0, END)
            apt_entry.insert(0, apt_list_box.get(apt_list_box.curselection()))
            apt_show_infos()

        def apt_entry_delete():
            apt_entry.delete(0, END)

        def apt_search_check(e):
            typed = apt_entry.get()
            if typed == "":
                apt_data = get_apt_cache()
            else:
                apt_data = []
                for item in get_apt_cache():
                    if typed.lower() in item.lower():
                        apt_data.append(item)
            update_apt_list(apt_data)

        def get_debian_icon():
            if apt_entry.get() in apt_flatpak_matches:
                try:
                    url_output = f"https://dl.flathub.org/repo/appstream/x86_64/icons/128x128/{apt_flatpak_matches[apt_entry.get()]}.png"
                    with urlopen(url_output) as url_output:
                        self.deban_navbar_icon = Image.open(url_output)
                    self.deban_navbar_icon = resize2(self.deban_navbar_icon)

                    self.deban_navbar_icon = ImageTk.PhotoImage(self.deban_navbar_icon)
                    apt_pkg_icon.config(image=self.deban_navbar_icon)
                except urllib.error.HTTPError as e:
                    print(f"{e}")
                    apt_pkg_icon.config(image=self.debinstall_icon)
            else:
                apt_pkg_icon.config(image=self.debinstall_icon)

        def apt_screenshot():
            try:
                apt_app = str(apt_entry.get())
                url = f"https://screenshots.debian.net/package/{apt_app}#gallery-1"
                response = requests.get(url)
                soup = BeautifulSoup(response.text, "html.parser")
                links = [
                    link.get("href")
                    for link in soup.find_all("a")
                    if link.get("href").endswith(".png")
                ]

                url_output = f"https://screenshots.debian.net{str(links[1])}"
                with urlopen(url_output) as url_output:
                    self.app_img = Image.open(url_output)
                self.app_img = resize(self.app_img)

                self.app_img = ImageTk.PhotoImage(self.app_img)
                apt_panel.config(image=self.app_img)
            except IndexError as e:
                print(f"{e}")
                if apt_entry.get() in apt_flatpak_matches:
                    try:
                        app_id = Flat_remote_dict[flatpak_entry.get()]

                        screenshot_url = extract_default_screenshot_url(app_id)
                        if screenshot_url:
                            print("Screenshot-URL {}:".format(app_id))
                            print(screenshot_url)

                        else:
                            print("No Screenshot Found {}.".format(app_id))

                        with urlopen(screenshot_url) as url_output:
                            self.img = Image.open(url_output)
                        self.img = resize(self.img)
                        self.img = ImageTk.PhotoImage(self.img)
                        apt_panel.config(image=self.img)

                    except requests.exceptions.RequestException as e:
                        print("Error fetching URL:", e)
                        # return None
                        apt_panel.config(self.no_img)

        def put_apt_description():
            pkg_infos = os.popen(f"apt show -a {apt_entry.get()}")
            read_pkg_infos = pkg_infos.read()

            insert_description = read_pkg_infos
            description_text.delete("1.0", "end")
            description_text.insert(END, insert_description)

        def hide_apt_search_container():
            apt_search_container.pack_forget()

        def apt_show_infos():
            if apt_entry.get() == "":
                error_message_0()
            elif apt_entry.get() not in get_apt_cache():
                error_message_1()
            else:
                apt_info_throber_frame.pack_forget()
                apt_info_container.pack(fill=BOTH, expand=True)
                apt_pkg_name.config(text=f"{apt_entry.get()}")
                pkg_infos_desc = os.popen(
                    f"apt show -a {apt_entry.get()} | grep -E 'Description:'"
                )
                read_pkg_infos_desc = pkg_infos_desc.read()

                apt_pkg_status.config(
                    text=f"{read_pkg_infos_desc.split(':')[1]}",
                    justify="left",
                    anchor="w",
                )

                if apt_entry.get() in get_installed_apt_pkgs():
                    apt_pkg_inst.config(
                        text="Uninstall",
                        justify="left",
                        width=10,
                        background="#f04a50",
                        foreground=ext_btn_font,
                        font=font_10_b,
                        borderwidth=0,
                        highlightthickness=0,
                        command=apt_uninstall,
                    )
                else:
                    apt_pkg_inst.config(
                        text="Install",
                        justify="left",
                        width=10,
                        background="#6abd43",
                        foreground=ext_btn_font,
                        font=font_10,
                        borderwidth=0,
                        highlightthickness=0,
                        command=apt_install,
                    )

                apt_panel.config(image=self.no_img)

                hide_apt_search_container()
                get_debian_icon()
                apt_screenshot()
                put_apt_description()

        def hide_apt_frame():
            apt_info_container.pack_forget()
            apt_search_container.pack(anchor="w", side=LEFT, pady=20, padx=10)
            apt_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        apt_main_container = Frame(self, background=maincolor)
        apt_main_container.pack(fill="both", expand=True)

        apt_search_container = LabelFrame(
            apt_main_container,
            text="Search",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
            padx=20,
            background=frame_color,
        )
        apt_search_container.pack(anchor="w", side=LEFT, pady=20, padx=10)

        apt_search_field = Frame(
            apt_search_container,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
        )
        apt_search_field.pack(fill="x", pady=5)

        apt_search_btn = Label(
            apt_search_field,
            image=self.search_btn,
            text="Select",
            bg=ext_btn,
            fg=main_font,
            borderwidth=0,
            highlightthickness=0,
            # command=apt_show_infos,
        )
        apt_search_btn.pack(side="left", fill="both")

        apt_entry = Entry(
            apt_search_field, font=("Sans", 15), borderwidth=0, highlightthickness=0
        )
        listbox_ttp = CreateToolTip(
            apt_entry,
            " - Typ to finde a package\n\n - Single click on a listbox item to show more infos",
        )
        apt_entry.pack(fill="x", expand=True, side="left")

        apt_list_box = Listbox(
            apt_search_container,
            height=59,
            width=40,
            borderwidth=1,
            highlightthickness=0,
            selectmode=tk.SINGLE,
        )
        apt_list_box_scrollbar = ttk.Scrollbar(apt_search_container)
        apt_list_box_scrollbar.pack(side=RIGHT, fill=Y)
        apt_list_box.config(yscrollcommand=apt_list_box_scrollbar.set)
        apt_list_box_scrollbar.config(command=apt_list_box.yview)
        apt_list_box.pack(fill=BOTH)

        update_apt_list(get_apt_cache())

        apt_list_box.bind("<ButtonRelease-1>", apt_list_fillout)

        apt_entry.bind("<KeyRelease>", apt_search_check)

        apt_info_throber_frame = Frame(apt_main_container, background=maincolor)
        apt_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        # APT OneClicks
        self.repo_sec_frame = LabelFrame(
            apt_info_throber_frame,
            text="One Click Install",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            padx=20,
            pady=20,
        )
        self.repo_sec_frame["background"] = frame_color
        self.repo_sec_frame.pack(fill="x")

        apt_one_click_dict = OneClicks.apt_one_click_dict

        apt_one_click_dict1 = []
        conf_row = 0
        conf_column = 0

        def apt_one_click(package):
            pigro_skript_task = "Installing ..."
            pigro_skript_task_app = f"{package}"
            pigro_skript = [f"{permit}", "apt", "install", "-y", f"{package}"]

            custom_installer = Custom_Installer(master)

            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

        for software_name, software_info in apt_one_click_dict.items():
            package_name = software_info["Package"]
            package_info = software_info["Description"]

            apt_one_click_button_x = Button(
                self.repo_sec_frame,
                image=self.deb_butt,
                justify="left",
                anchor="w",
                compound="left",
                text=software_name,
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=ext_btn_font,
                command=lambda package=package_name: apt_one_click(package),
            )

            self.apt_one_click_ttp = CreateToolTip(apt_one_click_button_x, package_info)

            apt_one_click_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            apt_one_click_dict1.append(apt_one_click_button_x)
            conf_column += 1

            if conf_column == 2:
                conf_row += 1
                conf_column = 0

        for col in range(2):
            self.repo_sec_frame.grid_columnconfigure(col, weight=1, uniform="columns")

        apt_info_container = Frame(apt_main_container, background=maincolor)

        apt_exit = Button(
            apt_info_container,
            text="Back",
            image=self.exit_btn,
            background=nav2_color,
            foreground="white",
            borderwidth=0,
            highlightthickness=0,
            compound=LEFT,
            font=font_10_b,
            command=hide_apt_frame,
            anchor="w",
            padx=10,
        )
        apt_exit.pack(fill="x")

        apt_pkg_header_1 = Frame(
            apt_info_container,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
            padx=20,
            background=nav_color,
        )
        apt_pkg_header_1.pack(anchor="n", fill="x")

        apt_pkg_header_1_1 = Frame(
            apt_pkg_header_1, borderwidth=0, highlightthickness=0, background=nav_color
        )
        apt_pkg_header_1_1.pack(fill="x")
        apt_pkg_header_1_1.columnconfigure(1, weight=2)

        apt_pkg_icon = Label(
            apt_pkg_header_1_1,
            image=self.debinstall_icon,
            font=font_10_b,
            justify="left",
            background=nav_color,
            foreground=main_font,
            padx=10,
        )
        apt_pkg_icon.grid(row=0, rowspan=2, column=0)

        apt_pkg_name = Label(
            apt_pkg_header_1_1,
            text="",
            font=font_20,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        apt_pkg_name.grid(row=0, column=1, sticky="ew")

        apt_pkg_status = Label(
            apt_pkg_header_1_1,
            text="",
            font=font_8,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        apt_pkg_status.grid(row=1, column=1, sticky="ew")

        apt_pkg_inst = Button(
            apt_pkg_header_1_1,
            text="Install",
            justify="left",
            width=10,
            background="#6abd43",
            foreground=ext_btn_font,
            font=font_10,
            borderwidth=0,
            highlightthickness=0,
            command=apt_install,
        )
        apt_pkg_inst.grid(row=0, column=2, sticky="e")

        def on_configure(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
            update_canvas()

        def on_mousewheel(event):
            canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def update_canvas():
            canvas_width = canvas.winfo_width()
            frame_width = canvas_frame.winfo_reqwidth()
            x_offset = max((canvas_width - frame_width) // 2, 0)
            canvas.coords("frame", x_offset, 0)

        canvas_container = Frame(apt_info_container, background=maincolor, width=869)
        canvas_container.pack(side=LEFT, fill="both", expand=True)

        canvas = Canvas(canvas_container, bg=maincolor, highlightthickness=0)
        canvas.pack(fill="both", expand=True, side=RIGHT)
        canvas.pack_propagate(False)

        canvas_frame = tk.Frame(canvas, bg=maincolor, padx=120)
        canvas.create_window((0, 0), window=canvas_frame, anchor="n", tags="frame")

        apt_panel = Label(canvas_frame, text="Apartment Panel", bg=frame_color)
        apt_panel.pack(anchor="n", pady=20)

        description_text = Text(
            canvas_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
            font=("Sans", 9),
            height=100,
            width=80,
            wrap=WORD,
            padx=20,
        )
        description_text.pack(side=LEFT, fill=BOTH, expand=True, padx=20)

        scrollbar = ttk.Scrollbar(
            apt_info_container, orient=VERTICAL, command=canvas.yview
        )
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.config(yscrollcommand=scrollbar.set)

        canvas_frame.bind("<Configure>", on_configure)
        canvas_frame.bind_all("<MouseWheel>", on_mousewheel)


class PiAppsSearchPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        def error_message_0():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_message_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        self["background"] = maincolor
        self.no_img = PhotoImage(file=f"{application_path}/images/apps/no_image.png")

        if "dark" in theme or "noir" in theme:
            self.piapps_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/piapps_dark_24x24.png"
            )
        else:
            self.piapps_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/piapps_light_24x24.png"
            )
        self.pi_appsinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/pi-apps64x64.png"
        )
        self.search_btn = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/glass_icon.png"
        )
        self.exit_btn = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
        )
        self.pi_appsopen_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/piapps_logo_24x24.png"
        )
        self.pi_appssett_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/piapps_settings_24x24.png"
        )

        self.pi_apps_big_icon = PhotoImage(
            file=f"{application_path}/images/icons/pi-apps-glogo.png"
        )

        def hide_piapps_frame():
            piapps_info_frame.pack_forget()
            piapps_search_frame.pack(anchor="w", side=LEFT, pady=20, padx=10)
            piapps_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        def piapps_install():
            fullstring = piapps_entry.get()
            substring = " "
            if substring in fullstring:
                replace_space = fullstring.replace(" ", "\ ")
                popen(
                    f"x-terminal-emulator -e 'bash -c \"cd && ~/pi-apps/manage install {replace_space}; exec bash\"'"
                )
                print(f"[Info] {piapps_entry.get()} is installeble")

            else:
                popen(
                    f"x-terminal-emulator -e 'bash -c \"cd && ~/pi-apps/manage install {piapps_entry.get()}; exec bash\"'"
                )
            hide_piapps_frame()

        def piapps_uninstall():
            fullstring = piapps_entry.get()
            substring = " "
            if substring in fullstring:
                replace_space = fullstring.replace(" ", "\ ")
                popen(
                    f"x-terminal-emulator -e 'bash -c \"cd && ~/pi-apps/manage uninstall {replace_space}; exec bash\"'"
                )

            else:
                popen(
                    f"x-terminal-emulator -e 'bash -c \"cd && ~/pi-apps/manage uninstall {piapps_entry.get()}; exec bash\"'"
                )
            hide_piapps_frame()

        def update_piapps(piapps_data):
            piapps_list_box.delete(0, END)
            for item in piapps_data:
                piapps_list_box.insert(END, item)

        def piapps_list_fillout(e):
            piapps_entry.delete(0, END)
            piapps_entry.insert(0, piapps_list_box.get(piapps_list_box.curselection()))
            piapps_show_infos()

        def piapps_search_check(e):
            typed = piapps_entry.get()
            if typed == "":
                piapps_data = piapps_cache_content
            else:
                piapps_data = []
                for item in piapps_cache_content:
                    if typed.lower() in item.lower():
                        piapps_data.append(item)

            update_piapps(piapps_data)

        def piapps_get_screenshot():
            app_string = f"{piapps_entry.get()}"
            app_string_web = app_string.replace(" ", "%20")
            try:
                url_output = f"https://github.com/actionschnitzel/PiGro-Aid-/blob/data/screenshots/pi-apps/{app_string_web}.png?raw=true"
                with urlopen(url_output) as url_output:
                    self.img = Image.open(url_output)
                self.img = resize(self.img)

                self.img = ImageTk.PhotoImage(self.img)
                piapps_panel.config(image=self.img)
            except urllib.error.HTTPError as e:
                print(f"{e}")
                if piapps_entry.get() in piapps_flatpak_matches:
                    url = f"https://flathub.org/apps/{piapps_flatpak_matches[piapps_entry.get()]}"

                    try:
                        desired_content = f"https://dl.flathub.org/repo/screenshots/{piapps_flatpak_matches[piapps_entry.get()]}-stable/752x423/"

                        web_content = requests.get(url).text

                        match = re.search(rf'({desired_content}[^"\s]+)', web_content)

                        if match:
                            extracted_url = match.group(1)
                            og_image_content = extracted_url
                            with urlopen(og_image_content) as url_output:
                                self.img = Image.open(url_output)
                            self.img = resize(self.img)
                            self.img = ImageTk.PhotoImage(self.img)
                            piapps_panel.config(image=self.img)

                        else:
                            print("No og:image meta property found.")
                            piapps_panel.config(image=self.no_img)
                    except requests.exceptions.RequestException as e:
                        print("Error fetching URL:", e)
                        return None

        def piapps_get_icon():
            app_string = f"{piapps_entry.get()}"
            app_string_web = app_string.replace(" ", "%20")

            self.piapps_select_icon = PhotoImage(
                file=f"~/pi-apps/apps/{piapps_entry.get()}/icon-64.png"
            )
            piapps_pkg_icon.config(image=self.piapps_select_icon)

            app_string = f"{piapps_entry.get()}"
            app_string_web = app_string.replace(" ", "%20")

        def piapps_get_description():
            if piapps_entry.get() in piapps_flatpak_matches:
                appstream_id = piapps_flatpak_matches[piapps_entry.get()]
                piapps_summary = get_app_summary(appstream_id)
                piapps_pkg_status.config(text=piapps_summary)
            else:
                piapps_pkg_status.config(text=" ")

            piapps_pkg_infos = open(
                f"{home}/pi-apps/apps/{piapps_entry.get()}/description",
                "r",
            )
            read_piapps_pkg_infos = piapps_pkg_infos.read()

            insert_piapps_description = read_piapps_pkg_infos
            piapps_description_text.delete("1.0", "end")
            piapps_description_text.insert(END, insert_piapps_description)

        def piapps_show_infos():
            piapps_panel.config(image=self.no_img)
            if piapps_entry.get() == "":
                error_message_0()
            elif piapps_entry.get() not in piapps_cache_content:
                error_message_1()
            else:
                piapps_info_throber_frame.pack_forget()
                piapps_info_frame.pack(fill=BOTH, expand=True)
                piapps_pkg_name.config(text=f"{piapps_entry.get()}")
                if piapps_entry.get() in refresh_piapps_installs():
                    piapps_pkg_inst.config(
                        text="Uninstall",
                        justify="left",
                        width=10,
                        background="#f04a50",
                        foreground=ext_btn_font,
                        font=font_10_b,
                        borderwidth=0,
                        highlightthickness=0,
                        command=piapps_uninstall,
                    )
                else:
                    piapps_pkg_inst.config(
                        text="Install",
                        justify="left",
                        width=10,
                        background="#6abd43",
                        foreground=ext_btn_font,
                        font=font_10,
                        borderwidth=0,
                        highlightthickness=0,
                        command=piapps_install,
                    )

                piapps_search_frame.pack_forget()
                piapps_get_icon()
                piapps_get_screenshot()
                piapps_get_description()

        pi_apps_main_container = Frame(self, background=maincolor)
        pi_apps_main_container.pack(fill="both", expand=True)

        def install_piapps_apt():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'"
            )
            rs_pigro = RestartPigroMass(self)
            rs_pigro.grab_set()

        if piapps_path == False:
            pi_apps_main_container.pack_forget()

            pi_apps_not_installad_container = Frame(
                self, background=maincolor, pady=200
            )
            pi_apps_not_installad_container.pack(fill="both", expand=True)

            piapps_big_icon = Label(
                pi_apps_not_installad_container,
                image=self.pi_apps_big_icon,
                font=font_10_b,
                justify="left",
                background=maincolor,
                foreground=main_font,
            )
            piapps_big_icon.pack(anchor="center", pady=20)

            piapps_app_inst = Button(
                pi_apps_not_installad_container,
                text="Install Pi-Apps",
                justify="left",
                width=20,
                background=ext_btn,
                foreground=ext_btn_font,
                font=font_10_b,
                borderwidth=0,
                highlightthickness=0,
                command=install_piapps_apt,
            )
            piapps_app_inst.pack()

        piapps_search_frame = LabelFrame(
            pi_apps_main_container,
            text="Search",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
            padx=20,
            background=frame_color,
        )
        piapps_search_frame.pack(anchor="w", side=LEFT, pady=20, padx=10)

        piapps_search_field = Frame(
            piapps_search_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
        )
        piapps_search_field.pack(fill="x", pady=5)

        piapps_search_btn = Label(
            piapps_search_field,
            image=self.search_btn,
            text="Select",
            bg=ext_btn,
            fg=main_font,
            borderwidth=0,
            highlightthickness=0,
            # command=piapps_show_infos,
        )
        piapps_search_btn.pack(side="left", fill=BOTH)

        piapps_entry = Entry(
            piapps_search_field,
            font=("Sans", 15),
            borderwidth=0,
            highlightthickness=0,
        )
        piapps_entry.pack(fill="x", expand=True, side="left")
        listbox_ttp = CreateToolTip(
            piapps_entry,
            " - Typ to finde a package\n\n - Single click on a listbox item to show more infos",
        )

        piapps_list_box = Listbox(
            piapps_search_frame,
            height=50,
            width=40,
            borderwidth=1,
            highlightthickness=0,
            selectmode=tk.SINGLE,
        )

        piapps_list_box_scrollbar = ttk.Scrollbar(piapps_search_frame)
        piapps_list_box_scrollbar.pack(side=RIGHT, fill=Y)
        piapps_list_box.config(yscrollcommand=piapps_list_box_scrollbar.set)
        piapps_list_box_scrollbar.config(command=piapps_list_box.yview)

        piapps_list_box.pack(fill=BOTH)

        update_piapps(piapps_cache_content)

        piapps_list_box.bind("<ButtonRelease-1>", piapps_list_fillout)

        piapps_entry.bind("<KeyRelease>", piapps_search_check)

        piapps_info_throber_frame = Frame(pi_apps_main_container, background=maincolor)
        piapps_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        piapps_info_frame = Frame(pi_apps_main_container, background=maincolor)

        piapps_exit = Button(
            piapps_info_frame,
            text="Back",
            image=self.exit_btn,
            background=nav2_color,
            foreground="white",
            borderwidth=0,
            highlightthickness=0,
            compound=LEFT,
            font=font_10_b,
            command=hide_piapps_frame,
            anchor="w",
            padx=10,
        )
        piapps_exit.pack(fill="x")

        piapps_pkg_info_frame = LabelFrame(
            piapps_info_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            background=nav_color,
            pady=20,
            padx=20,
        )
        piapps_pkg_info_frame.pack(anchor="n", fill="x")

        piapps_pkg_info_container = Frame(
            piapps_pkg_info_frame,
            borderwidth=0,
            highlightthickness=0,
            background=nav_color,
        )
        piapps_pkg_info_container.pack(fill="x")
        piapps_pkg_info_container.columnconfigure(1, weight=2)

        piapps_pkg_icon = Label(
            piapps_pkg_info_container,
            image=self.pi_appsinstall_icon,
            font=font_10_b,
            justify="left",
            background=nav_color,
            foreground=main_font,
        )
        piapps_pkg_icon.grid(row=0, rowspan=2, column=0)

        piapps_pkg_name = Label(
            piapps_pkg_info_container,
            text="",
            font=font_20,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        piapps_pkg_name.grid(row=0, column=1, sticky="ew")

        piapps_pkg_status = Label(
            piapps_pkg_info_container,
            text="",
            font=font_10,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        piapps_pkg_status.grid(row=1, column=1, sticky="ew")

        piapps_pkg_inst = Button(
            piapps_pkg_info_container,
            text="Install",
            justify="left",
            width=10,
            background="#6abd43",
            foreground=ext_btn_font,
            font=font_10,
            borderwidth=0,
            highlightthickness=0,
            command=piapps_install,
        )
        piapps_pkg_inst.grid(row=0, column=2, sticky="e")

        def open_pi_apps():
            os.system(f"{home}/pi-apps/gui")

        def open_pi_apps_settings():
            popen(f"{home}/pi-apps/settings")

        piapps_configs_frame = Frame(piapps_pkg_info_container, background=nav_color)
        piapps_configs_frame.grid(row=2, column=1, pady=0)

        piapps_app_open = Button(
            piapps_configs_frame,
            justify="left",
            imag=self.pi_appsopen_icon,
            background=nav_color,
            foreground=ext_btn_font,
            font=font_10_b,
            borderwidth=0,
            highlightthickness=0,
            command=open_pi_apps,
        )
        piapps_app_open.grid(row=0, column=0, pady=0, padx=5)

        piapps_setting_open = Button(
            piapps_configs_frame,
            image=self.pi_appssett_icon,
            justify="left",
            background=nav_color,
            foreground=ext_btn_font,
            font=font_10_b,
            borderwidth=0,
            highlightthickness=0,
            command=open_pi_apps_settings,
        )
        piapps_setting_open.grid(row=0, column=1, pady=0, padx=5)

        def on_configure_piapps_canvas(event):
            piapps_canvas.configure(scrollregion=piapps_canvas.bbox("all"))
            update_piapps_canvas()

        def on_mousewheel_piapps_canvas(event):
            piapps_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

        def update_piapps_canvas():
            piapps_canvas_width = piapps_canvas.winfo_width()
            frame_width = piapps_canvas_frame.winfo_reqwidth()
            x_offset = max((piapps_canvas_width - frame_width) // 2, 0)
            piapps_canvas.coords("frame", x_offset, 0)

        piapps_canvas_container = Frame(
            piapps_info_frame, background=maincolor, width=869
        )
        piapps_canvas_container.pack(side=LEFT, fill="both", expand=True)

        piapps_canvas = tk.Canvas(
            piapps_canvas_container, bg=frame_color, highlightthickness=0
        )
        piapps_canvas.pack(fill=BOTH, expand=True, side=RIGHT)
        piapps_canvas.pack_propagate(False)

        piapps_canvas_frame = tk.Frame(piapps_canvas, bg=maincolor, padx=120)
        piapps_canvas.create_window(
            (0, 0), window=piapps_canvas_frame, anchor="n", tags="frame"
        )

        piapps_panel = Label(
            piapps_canvas_frame, text="Apartment Panel", bg=frame_color
        )
        piapps_panel.pack(anchor="n", pady=20)

        piapps_description_text = Text(
            piapps_canvas_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
            font=("Sans", 9),
            height=100,
            width=80,
            wrap=WORD,
            padx=20,
        )
        piapps_description_text.pack(side=LEFT, fill=BOTH, expand=True, padx=20)

        piapps_scrollbar = ttk.Scrollbar(
            piapps_info_frame, orient=VERTICAL, command=piapps_canvas.yview
        )
        piapps_scrollbar.pack(side=RIGHT, fill=Y)
        piapps_canvas.config(yscrollcommand=piapps_scrollbar.set)

        piapps_canvas_frame.bind("<Configure>", on_configure_piapps_canvas)
        piapps_canvas_frame.bind_all("<MouseWheel>", on_mousewheel_piapps_canvas)

        # piapps OneClicks
        piapps_one_click_frame = LabelFrame(
            piapps_info_throber_frame,
            text="One Click Install",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            padx=20,
            pady=20,
        )
        piapps_one_click_frame["background"] = frame_color
        piapps_one_click_frame.pack(fill="x")

        piapps_one_click_dict = PiAppsOneClicks.piapps_one_click_dict

        piapps_one_click_dict1 = []
        conf_row = 0
        conf_column = 0

        def piapps_one_click(package):
            fullstring = package
            substring = " "
            if substring in fullstring:
                replace_space = fullstring.replace(" ", "\ ")
                popen(
                    f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage install {replace_space}; exec bash\"'"
                )
                refresh_piapps_installs().append(package)
                print(f"[Info] {package} is installeble")

            else:
                popen(
                    f"x-terminal-emulator -e 'bash -c \"~/pi-apps/manage install {package}; exec bash\"'"
                )
                refresh_piapps_installs().append(package)
                for item in refresh_piapps_installs():
                    if item == package:
                        print(f"[Info] {package} is installed")

        for software_name, software_info in piapps_one_click_dict.items():
            package_name = software_info["Package"]
            package_info = software_info["Description"]

            piapps_one_click_button_x = Button(
                piapps_one_click_frame,
                image=self.piapps_butt,
                justify="left",
                anchor="w",
                compound="left",
                text=software_name,
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=ext_btn_font,
                command=lambda package=package_name: piapps_one_click(package),
            )

            self.piapps_one_click_ttp = CreateToolTip(
                piapps_one_click_button_x, package_info
            )

            piapps_one_click_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            piapps_one_click_dict1.append(piapps_one_click_button_x)
            conf_column += 1

            if conf_column == 2:
                conf_row += 1
                conf_column = 0

        for col in range(2):
            piapps_one_click_frame.grid_columnconfigure(
                col, weight=1, uniform="columns"
            )


class FlatpakSearchPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self["background"] = maincolor
        self.no_img = PhotoImage(file=f"{application_path}/images/apps/no_image.png")

        if "dark" in theme or "noir" in theme:
            self.flatpak_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/flatpak_dark_24x24.png"
            )
        else:
            self.flatpak_butt = PhotoImage(
                file=f"{application_path}/images/icons/nav_bar/flatpak_light_24x24.png"
            )
        self.flatpak_big_icon = PhotoImage(
            file=f"{application_path}/images/icons/flatpak-glogo.png"
        )

        self.debinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/64x64/debian-logo.png"
        )
        self.search_btn = PhotoImage(
            file=f"{application_path}/images/icons/nav_bar/glass_icon.png"
        )
        self.exit_btn = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/exit_btn.png"
        )
        self.flatpak_appsinstall_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/flathub64x64.png"
        )

        def error_message_0():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_message_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def hide_flatpak_frame():
            flatpak_info_frame.pack_forget()
            flatpak_search_frame.pack(anchor="w", side=LEFT, pady=20, padx=10)
            flatpak_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        def flatpak_install():
            hide_flatpak_frame()

            pigro_skript_task = "Installing ..."
            pigro_skript_task_app = f"{flatpak_entry.get()}"
            pigro_skript = [
                f"flatpak",
                "install",
                "-y",
                "flathub",
                f"{Flat_remote_dict[flatpak_entry.get()]}",
            ]

            custom_installer = Custom_Installer(master)

            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

            update_flatpak(Flat_remote_dict.keys())

        def flatpak_uninstall():
            hide_flatpak_frame()

            pigro_skript_task = "Removing From System"
            pigro_skript_task_app = f"{flatpak_entry.get()}"
            pigro_skript = [
                f"flatpak",
                "uninstall",
                "-y",
                f"{Flat_remote_dict[flatpak_entry.get()]}",
            ]

            custom_installer = Custom_Installer(master)

            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

            update_flatpak(Flat_remote_dict.keys())

        def update_flatpak(flatpak_data):
            flatpak_data = sorted(flatpak_data)
            flatpak_list_box.delete(0, END)
            for item in flatpak_data:
                flatpak_list_box.insert(END, item)

        def flatpak_list_fillout(e):
            flatpak_entry.delete(0, END)
            flatpak_entry.insert(
                0, flatpak_list_box.get(flatpak_list_box.curselection())
            )
            flatpak_show_infos()

        def flatpak_search_check(e):
            typed = flatpak_entry.get()
            if typed == "":
                flatpak_data = Flat_remote_dict.keys()
            else:
                flatpak_data = []
                for item in Flat_remote_dict.keys():
                    if typed.lower() in item.lower():
                        flatpak_data.append(item)
            update_flatpak(flatpak_data)

        def get_flatpak_icon():
            try:
                url_output = f"https://dl.flathub.org/repo/appstream/x86_64/icons/128x128/{Flat_remote_dict[flatpak_entry.get()]}.png"
                with urlopen(url_output) as url_output:
                    self.flat_icon = Image.open(url_output)
                self.flat_icon = resize2(self.flat_icon)

                self.flat_icon = ImageTk.PhotoImage(self.flat_icon)
                flatpak_pkg_icon.config(image=self.flat_icon)
            except urllib.error.HTTPError as e:
                flatpak_pkg_icon.config(image=self.flatpak_appsinstall_icon)

        def get_flatpak_screenshot():
            try:
                app_id = Flat_remote_dict[flatpak_entry.get()]

                screenshot_url = extract_default_screenshot_url(app_id)
                if screenshot_url:
                    print("Screenshot-URL {}:".format(app_id))
                    print(screenshot_url)

                else:
                    print("No Screenshot Found {}.".format(app_id))

                with urlopen(screenshot_url) as url_output:
                    self.img = Image.open(url_output)
                self.img = resize(self.img)
                self.img = ImageTk.PhotoImage(self.img)
                flatpak_panel.config(image=self.img)

            except requests.exceptions.RequestException as e:
                print("Error fetching URL:", e)
                # return None
                flatpak_panel.config(self.no_img)

        def get_flatpak_description():
            url = f"https://flathub.org/apps/{Flat_remote_dict[flatpak_entry.get()]}"

            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")
            prose_element = soup.find(
                "div", {"class": "prose dark:prose-invert xl:max-w-[75%]"}
            )
            flatpak_description_text.delete("1.0", "end")
            flatpak_description_text.insert(tk.END, prose_element.text)

        def flatpak_show_infos():
            if flatpak_entry.get() == "":
                error_message_0()
            elif flatpak_entry.get() not in Flat_remote_dict.keys():
                error_message_1()
            else:
                flatpak_search_frame.pack_forget()
                flatpak_info_throber_frame.pack_forget()
                flatpak_info_frame.pack(fill=BOTH, expand=True)
                get_flatpak_icon()
                get_flatpak_screenshot()
                get_flatpak_description()

                flatpak_pkg_name.config(text=f"{flatpak_entry.get()}")
                if flatpak_entry.get() in refresh_flatpak_installs().keys():
                    flatpak_pkg_inst.config(
                        text="Uninstall",
                        justify="left",
                        width=10,
                        background="#f04a50",
                        foreground=ext_btn_font,
                        font=font_10_b,
                        borderwidth=0,
                        highlightthickness=0,
                        command=flatpak_uninstall,
                    )
                else:
                    flatpak_pkg_inst.config(
                        text="Install",
                        justify="left",
                        width=10,
                        background="#6abd43",
                        foreground=ext_btn_font,
                        font=font_10,
                        borderwidth=0,
                        highlightthickness=0,
                        command=flatpak_install,
                    )

        flatpak_inst_main_frame = Frame(self, background=maincolor)
        flatpak_inst_main_frame.pack(fill="both", expand=True)

        def install_flatpak_apt():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"sudo apt install flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo | bash; exec bash\"'"
            )
            rs_pigro = RestartPigroMass(self)
            rs_pigro.grab_set()

        if flatpak_path == False:
            flatpak_inst_main_frame.pack_forget()

            flat_not_installad_container = Frame(self, background=maincolor, pady=200)
            flat_not_installad_container.pack(fill=BOTH, expand=True)

            flat_big_icon = Label(
                flat_not_installad_container,
                image=self.flatpak_big_icon,
                font=font_10_b,
                justify="left",
                background=maincolor,
                foreground=main_font,
            )
            flat_big_icon.pack(anchor="center", pady=20)

            flat_app_inst = Button(
                flat_not_installad_container,
                text="Install Flatpak",
                justify="left",
                width=20,
                background=ext_btn,
                foreground=ext_btn_font,
                font=font_10_b,
                borderwidth=0,
                highlightthickness=0,
                command=install_flatpak_apt,
            )
            flat_app_inst.pack()

        flatpak_search_frame = LabelFrame(
            flatpak_inst_main_frame,
            text="Search",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
            padx=20,
            background=frame_color,
        )
        flatpak_search_frame.pack(anchor="w", side=LEFT, pady=20, padx=10)

        flatpak_search_field = Frame(
            flatpak_search_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
        )
        flatpak_search_field.pack(fill="x", pady=5)

        flatpak_search_btn = Label(
            flatpak_search_field,
            image=self.search_btn,
            text="Select",
            bg=ext_btn,
            fg=main_font,
            borderwidth=0,
            highlightthickness=0,
            # command=flatpak_show_infos,
        )
        flatpak_search_btn.pack(side="left", fill=BOTH)

        flatpak_entry = Entry(
            flatpak_search_field,
            font=("Sans", 15),
            borderwidth=0,
            highlightthickness=0,
        )
        flatpak_entry.pack(fill="x", expand=True, side="left")
        listbox_ttp = CreateToolTip(
            flatpak_entry,
            " - Typ to finde a package\n\n - Single click on a listbox item to show more infos",
        )

        flatpak_list_box = Listbox(
            flatpak_search_frame,
            height=50,
            width=40,
            borderwidth=1,
            highlightthickness=0,
            selectmode=tk.SINGLE,
        )

        flatpak_list_scrollbar = ttk.Scrollbar(flatpak_search_frame)
        flatpak_list_scrollbar.pack(side=RIGHT, fill=Y)
        flatpak_list_box.config(yscrollcommand=flatpak_list_scrollbar.set)
        flatpak_list_scrollbar.config(command=flatpak_list_box.yview)

        flatpak_list_box.pack(fill=BOTH)

        update_flatpak(Flat_remote_dict.keys())

        flatpak_list_box.bind("<ButtonRelease-1>", flatpak_list_fillout)

        flatpak_entry.bind("<KeyRelease>", flatpak_search_check)

        flatpak_info_throber_frame = Frame(
            flatpak_inst_main_frame, background=maincolor
        )
        flatpak_info_throber_frame.pack(fill=BOTH, expand=True, pady=20, padx=10)

        flatpak_info_frame = Frame(flatpak_inst_main_frame, background=maincolor)

        flatpak_exit = Button(
            flatpak_info_frame,
            text="Back",
            image=self.exit_btn,
            background=nav2_color,
            foreground="white",
            borderwidth=0,
            highlightthickness=0,
            compound=LEFT,
            font=font_10_b,
            command=hide_flatpak_frame,
            anchor="w",
            padx=10,
        )
        flatpak_exit.pack(fill="x")

        flatpak_pkg_info_frame = LabelFrame(
            flatpak_info_frame,
            borderwidth=0,
            highlightthickness=0,
            relief=GROOVE,
            pady=20,
            padx=20,
            background=nav_color,
        )
        flatpak_pkg_info_frame.pack(anchor="n", fill="x")

        flatpak_pkg_info_container = Frame(
            flatpak_pkg_info_frame,
            borderwidth=0,
            highlightthickness=0,
            background=nav_color,
        )
        flatpak_pkg_info_container.pack(fill="x")
        flatpak_pkg_info_container.columnconfigure(1, weight=2)

        flatpak_pkg_icon = Label(
            flatpak_pkg_info_container,
            image=self.debinstall_icon,
            font=font_10_b,
            justify="left",
            background=nav_color,
            foreground=main_font,
            padx=10,
        )
        flatpak_pkg_icon.grid(row=0, rowspan=2, column=0)

        flatpak_pkg_name = Label(
            flatpak_pkg_info_container,
            text="",
            font=font_20,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        flatpak_pkg_name.grid(row=0, column=1, sticky="ew")

        flatpak_pkg_status = Label(
            flatpak_pkg_info_container,
            text="",
            font=font_8,
            justify="left",
            background=nav_color,
            foreground=main_font,
            anchor="w",
            padx=20,
        )
        flatpak_pkg_status.grid(row=1, column=1, sticky="ew")

        flatpak_pkg_inst = Button(
            flatpak_pkg_info_container,
            text="Install",
            justify="left",
            width=10,
            background="#6abd43",
            foreground=ext_btn_font,
            font=font_10,
            borderwidth=0,
            highlightthickness=0,
            command=flatpak_install,
        )
        flatpak_pkg_inst.grid(row=0, column=2, sticky="e")

        def on_configure_flatpak_canvas(event):
            flatpak_canvas.configure(scrollregion=flatpak_canvas.bbox("all"))
            update_flatpak_canvas()

        def on_mousewheel_flatpak_canvas(event):
            flatpak_canvas.yview_scroll(int(0 * (event.delta / 120)), "units")

        def update_flatpak_canvas():
            flatpak_canvas_width = flatpak_canvas.winfo_width()
            frame_width = flatpak_canvas_frame.winfo_reqwidth()
            x_offset = max((flatpak_canvas_width - frame_width) // 2, 0)
            flatpak_canvas.coords("frame", x_offset, 0)

        flatpak_canvas_container = Frame(
            flatpak_info_frame, background=maincolor, width=869
        )
        flatpak_canvas_container.pack(side=LEFT, fill="both", expand=True)

        flatpak_canvas = tk.Canvas(
            flatpak_canvas_container, bg=frame_color, highlightthickness=0
        )
        flatpak_canvas.pack(fill=BOTH, expand=True, side=RIGHT)
        flatpak_canvas.pack_propagate(False)
        flatpak_canvas_frame = tk.Frame(flatpak_canvas, bg=maincolor, padx=120)
        flatpak_canvas.create_window(
            (0, 0), window=flatpak_canvas_frame, anchor="n", tags="frame"
        )

        flatpak_panel = Label(
            flatpak_canvas_frame, text="Apartment Panel", bg=frame_color
        )
        flatpak_panel.pack(anchor="n", pady=20)

        flatpak_description_text = Text(
            flatpak_canvas_frame,
            borderwidth=0,
            highlightthickness=0,
            background=frame_color,
            foreground=main_font,
            font=("Sans", 9),
            height=100,
            width=80,
            wrap=WORD,
        )
        flatpak_description_text.pack(side=LEFT, fill=BOTH, expand=True, padx=20)

        flatpak_scrollbar = ttk.Scrollbar(
            flatpak_info_frame, orient=VERTICAL, command=flatpak_canvas.yview
        )
        flatpak_scrollbar.pack(side=RIGHT, fill=Y)
        flatpak_canvas.config(yscrollcommand=flatpak_scrollbar.set)

        flatpak_canvas_frame.bind("<Configure>", on_configure_flatpak_canvas)
        flatpak_canvas_frame.bind_all("<MouseWheel>", on_mousewheel_flatpak_canvas)

        # flatpak OneClicks
        flatpak_one_click_frame = LabelFrame(
            flatpak_info_throber_frame,
            text="One Click Install",
            font=font_16,
            foreground=label_frame_color,
            relief=GROOVE,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            padx=20,
            pady=20,
        )
        flatpak_one_click_frame["background"] = frame_color
        flatpak_one_click_frame.pack(fill="x")

        flatpak_one_click_dict = FlatpakOneClicks.flatpak_one_click_dict

        flatpak_one_click_dict1 = []
        conf_row = 0
        conf_column = 0

        def flatpak_one_click(package):
            print(f"Installiere Paket: {package}")
            pigro_skript_task = "Installing ..."
            pigro_skript_task_app = f"{package}"
            pigro_skript = [f"flatpak", "install", "-y", f"{package}"]

            custom_installer = Custom_Installer(master)

            custom_installer.do_task(
                pigro_skript_task, pigro_skript_task_app, pigro_skript
            )

        for software_name, software_info in flatpak_one_click_dict.items():
            package_name = software_info["Package"]
            package_info = software_info["Description"]

            flatpak_one_click_button_x = Button(
                flatpak_one_click_frame,
                image=self.flatpak_butt,
                justify="left",
                anchor="w",
                compound="left",
                text=software_name,
                highlightthickness=0,
                borderwidth=0,
                background=ext_btn,
                foreground=ext_btn_font,
                command=lambda package=package_name: flatpak_one_click(package),
            )

            self.flatpak_one_click_ttp = CreateToolTip(
                flatpak_one_click_button_x, package_info
            )

            flatpak_one_click_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew"
            )
            flatpak_one_click_dict1.append(flatpak_one_click_button_x)
            conf_column += 1

            if conf_column == 2:
                conf_row += 1
                conf_column = 0

        for col in range(2):  # Assuming 2 columns, adjust as needed
            flatpak_one_click_frame.grid_columnconfigure(
                col, weight=1, uniform="columns"
            )


class Custom_Installer(tk.Toplevel):
    """child window that makes the the install process graphicle"""

    def __init__(self, parent):
        super().__init__(parent)
        self["background"] = maincolor
        self.icon = tk.PhotoImage(file=f"{application_path}/images/icons/logo.png")
        self.tk.call("wm", "iconphoto", self._w, self.icon)
        self.resizable(0, 0)
        cust_app_width = 700
        cust_app_height = 200
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width / 2) - (cust_app_width / 2)
        y = (screen_height / 2) - (cust_app_height / 2)
        self.geometry(f"{cust_app_width}x{cust_app_height}+{int(x)}+{int(y)}")
        self.title("Software Manager")
        self.configure(bg=maincolor)

        self.installer_main_frame = Frame(self, background=maincolor)
        self.installer_main_frame.pack(padx=20, pady=20, fill="both", expand=True)
        self.installer_main_frame.columnconfigure(1, weight=1)
        self.installer_main_frame.rowconfigure(0, weight=0)

        self.boot_log_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack.png"
        )
        self.install_ok_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack_ok.png"
        )
        self.install_error_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/unpack_error.png"
        )

        self.icon_label = tk.Label(
            self.installer_main_frame, image=self.boot_log_icon, bg=maincolor
        )

        self.icon_label.grid(row=0, rowspan=3, column=0, sticky="w", padx=10, pady=10)
        self.done_label = tk.Label(
            self.installer_main_frame,
            text="",
            font=("Helvetica", 16),
            bg=maincolor,
            fg=label_frame_color,
            justify="left",
            anchor="w",
        )
        self.done_label.grid(row=0, column=1, sticky="nw")
        self.done_label2 = tk.Label(
            self.installer_main_frame,
            text="",
            font=("Helvetica", 16),
            bg=maincolor,
            fg=main_font,
            justify="left",
            anchor="w",
        )
        self.done_label2.grid(row=1, column=1, sticky="nw")
        self.text = tk.Text(
            self.installer_main_frame,
            bg=maincolor,
            fg=main_font,
            height=1,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=main_font,
        )

        self.text.grid(row=2, column=1, columnspan=3, sticky="ew")

        self.install_button = tk.Button(
            self.installer_main_frame,
            text="Close",
            command=self.close_btn_command,
            borderwidth=0,
            highlightthickness=0,
            background=ext_btn,
            foreground=ext_btn_font,
            state=DISABLED,
        )
        self.install_button.grid(row=3, column=2, sticky="e", pady=10)
        self.grab_set()
        self.thread = None

    def do_task(self, task_label, task_app_label, task_script):
        self.done_label.config(text=task_label)
        self.done_label2.config(text=task_app_label)
        process = Popen(task_script, stdout=PIPE, stderr=PIPE, text=True)

        self.thread = Thread(target=self.run_update_output, args=(process, task_label))
        self.thread.start()

    def run_update_output(self, process, task_label):
        self.update_output(process, task_label)

    def update_output(self, process, task_label):
        while process.poll() is None:
            line = process.stdout.readline().strip()
            if line:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, line)
                self.text.see(tk.END)

        self.text.delete(1.0, tk.END)
        exit_code = process.returncode
        if exit_code == 0:
            self.done_label.config(text=f"{task_label} Done!")
            self.icon_label.config(image=self.install_ok_icon)
        else:
            self.done_label.config(text=f"Error! (Exit-Code: {exit_code})")
            self.icon_label.config(image=self.install_error_icon)
        self.install_button.config(state=NORMAL)

    def close_btn_command(self):
        Custom_Installer.destroy(self)

    def on_thread_finished(self):
        print("Thread beendet")
