import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image
from resorcess import *
from apt_manage import *
import subprocess
from flatpak_alias_list import *
from tabs.pop_ups import *
from tabs.system_tab_check import *
import json
from tabs.system_tab_check import check_papirus


class LookTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")


        self.folder_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/folder_s_light.png"
        )
        self.icon_folder_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/start_here_s_light.png"
        )
        self.cursor_folder_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/cursor_s_light.png"
        )
        self.theme_folder_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/theme_s_light.png"
        )
        self.refresh_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/fresh_s_light.png"
        )

        self.pixel_set = ttk.LabelFrame(
            self,
            text="Theme Your Desktop",
            padding=10
        )
        self.pixel_set.pack(pady=20, padx=40, fill="x", anchor="n")
        self.pixel_set.columnconfigure(0, weight=1)
        self.pixel_set.rowconfigure(0, weight=1)

        def done_message_0():
            d_mass = Done_(self)
            d_mass.grab_set()

        def why_message_0():
            y_mass = Look_Disabled(self)
            y_mass.grab_set()

        def update_theme_combobox():
            try:
                themes = [
                    d
                    for d in os.listdir("/usr/share/themes")
                    if os.path.isdir(os.path.join("/usr/share/themes", d))
                ]
                themes.sort()
                theme_combobox["values"] = themes
                theme_combobox.set("Select Theme")
            except Exception as e:
                theme_combobox.set("Error: " + str(e))

            try:
                icons = [
                    d
                    for d in os.listdir("/usr/share/icons")
                    if os.path.isdir(os.path.join("/usr/share/icons", d))
                    and "cursors" not in os.listdir(os.path.join("/usr/share/icons", d))
                ]
                icons.sort()
                icon_combobox["values"] = icons
                icon_combobox.set("Select Icons")
            except Exception as e:
                icon_combobox.set("Error: " + str(e))

            try:
                icons = [
                    d
                    for d in os.listdir("/usr/share/icons")
                    if os.path.isdir(os.path.join("/usr/share/icons", d))
                ]

                # Separate cursor themes from regular icon themes
                icons.sort()
                cursor_themes = [
                    icon
                    for icon in icons
                    if "cursors" in os.listdir(os.path.join("/usr/share/icons", icon))
                ]

                cursor_combobox["values"] = cursor_themes
                cursor_combobox.set("Select Cursor")
            except Exception as e:
                cursor_combobox.set("Error: " + str(e))

        def update_lxde_theme_config(selected_theme):
            config_file_path = os.path.expanduser(
                "~/.config/lxsession/LXDE-pi/desktop.conf"
            )

            with open(config_file_path, "r") as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if "sNet/ThemeName=" in line:
                    lines[i] = f"sNet/ThemeName={selected_theme}\n"
                    found = True
                    break

            if not found:
                lines.append(f"sNet/ThemeName={selected_theme}\n")

            with open(config_file_path, "w") as file:
                file.writelines(lines)

        def update_lxde_icons_config(selected_icon):
            config_file_path = os.path.expanduser(
                "~/.config/lxsession/LXDE-pi/desktop.conf"
            )

            with open(config_file_path, "r") as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if "sNet/IconThemeName" in line:
                    lines[i] = f"sNet/IconThemeName={selected_icon}\n"
                    found = True
                    break

            if not found:
                lines.append(f"sNet/IconThemeName={selected_icon}\n")

            with open(config_file_path, "w") as file:
                file.writelines(lines)

        def update_lxde_cursor_config(selected_cursor):
            config_file_path = os.path.expanduser(
                "~/.config/lxsession/LXDE-pi/desktop.conf"
            )

            with open(config_file_path, "r") as file:
                lines = file.readlines()

            found = False
            for i, line in enumerate(lines):
                if "sGtk/CursorThemeName" in line:
                    lines[i] = f"sGtk/CursorThemeName={selected_cursor}\n"
                    found = True
                    break

            if not found:
                lines.append(f"sGtk/CursorThemeName={selected_cursor}\n")

            with open(config_file_path, "w") as file:
                file.writelines(lines)

        def set_theme():
            selected_theme = theme_combobox.get()

            if selected_theme != "Press Refresh":
                if get_desktop_environment() == "xfce":
                    subprocess.run(
                        [
                            "xfconf-query",
                            "-c",
                            "xsettings",
                            "-p",
                            "/Net/ThemeName",
                            "-s",
                            selected_theme,
                        ]
                    )
                    subprocess.run(
                        [
                            "xfconf-query",
                            "-c",
                            "xfwm4",
                            "-p",
                            "/general/theme",
                            "-s",
                            selected_theme,
                        ]
                    )
                if get_desktop_environment() == "mate":
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.mate.interface",
                            "gtk-theme",
                            selected_theme,
                        ]
                    )
                if get_desktop_environment() == "lxde":
                    update_lxde_theme_config(selected_theme)

                else:
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.interface",
                            "gtk-theme",
                            selected_theme,
                        ]
                    )
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.wm.preferences",
                            "theme",
                            selected_theme,
                        ]
                    )
                done_message_0()

        def set_icon():
            selected_icon = icon_combobox.get()

            if selected_icon != "Press Refresh":
                if get_desktop_environment() == "xfce":
                    subprocess.run(
                        [
                            "xfconf-query",
                            "-c",
                            "xsettings",
                            "-p",
                            "/Net/IconThemeName",
                            "-s",
                            selected_icon,
                        ]
                    )
                if get_desktop_environment() == "lxde":
                    update_lxde_icons_config(selected_icon)
                else:
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.interface",
                            "icon-theme",
                            selected_icon,
                        ]
                    )
            done_message_0()

        def set_cursor():
            selected_cursor = cursor_combobox.get()

            if selected_cursor != "Press Refresh":
                if get_desktop_environment() == "xfce":
                    subprocess.run(
                        [
                            "xfconf-query",
                            "-c",
                            "xsettings",
                            "-p",
                            "/Gtk/CursorThemeName",
                            "-s",
                            selected_cursor,
                        ]
                    )
                if get_desktop_environment() == "lxde":
                    update_lxde_cursor_config(selected_cursor)
                else:
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.interface",
                            "cursor-theme",
                            selected_cursor,
                        ]
                    )
            done_message_0()

        def open_theme_folder():
            if check_pcmanfm() == True:
                popen("sudo pcmanfm /usr/share/themes")
            else:
                popen(
                    f"{permit} env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xdg-open /usr/share/themes"
                )

        def open_icon_folder():
            if check_pcmanfm() == True:
                popen("sudo pcmanfm /usr/share/icons")
            else:
                popen(
                    f"{permit} env DISPLAY=$DISPLAY XAUTHORITY=$XAUTHORITY xdg-open /usr/share/icons"
                )

        def open_lxappearance():
            popen("lxappearance")

        theme_combobox = ttk.Combobox(self.pixel_set, state="readonly")
        theme_combobox.grid(
            row=1, column=0, columnspan=2, padx=10, pady=5, sticky="ewsn"
        )
        theme_combobox.set("Press Refresh")

        icon_combobox = ttk.Combobox(self.pixel_set, state="readonly")
        icon_combobox.grid(
            row=2, column=0, columnspan=2, padx=10, pady=5, sticky="ewsn"
        )
        icon_combobox.set("Press Refresh")

        cursor_combobox = ttk.Combobox(self.pixel_set, state="readonly")
        cursor_combobox.grid(
            row=3, column=0, columnspan=2, padx=10, pady=5, sticky="ewsn"
        )
        cursor_combobox.set("Press Refresh")

        theme_button = ttk.Button(
            self.pixel_set,
            text="Set Theme",
            compound="left",
            image=self.theme_folder_icon,
            command=set_theme,
            width=20

        )
        theme_button.grid(row=1, column=3, padx=10, pady=5, sticky="ew")

        icon_button = ttk.Button(
            self.pixel_set,
            text="Set Icon",
            compound="left",
            image=self.icon_folder_icon,
            command=set_icon,
            width=20

        )
        icon_button.grid(row=2, column=3, padx=10, pady=5, sticky="ew")

        cursor_button = ttk.Button(
            self.pixel_set,
            text="Set Cursor",
            compound="left",
            image=self.cursor_folder_icon,
            command=set_cursor,
            width=20

        )
        cursor_button.grid(row=3, column=3, padx=10, pady=5, sticky="ew")

        theme_refresh_button = ttk.Button(
            self.pixel_set,
            text="Refresh",
            compound="left",
            image=self.refresh_icon,
            command=update_theme_combobox,
            width=20,
            style="Custom.TButton"
        )
        theme_refresh_button.grid(
            row=4, column=0, columnspan=3, padx=10, pady=5, sticky="ew"
        )

        theme_legacy_button = ttk.Button(
            self.pixel_set,
            text="Legacy Theme Bullseye",
            command=open_lxappearance,
            style="Custom.TButton",
            state=DISABLED,
            width=20
        )
        theme_legacy_button.grid(row=4, column=3, padx=10, pady=5, sticky="ewns")

        theme_folder_button = ttk.Button(
            self.pixel_set,
            text="Theme Folder",
            image=self.folder_icon,
            compound="left",
            command=open_theme_folder,
            width=20
        )
        theme_folder_button.grid(row=1, column=4, padx=10, pady=5, sticky="ew")

        icon_folder_button = ttk.Button(
            self.pixel_set,
            text="Icon Folder",
            compound="left",
            image=self.folder_icon,
            command=open_icon_folder,
            width=20
        )
        icon_folder_button.grid(row=2, column=4, padx=10, pady=5, sticky="ew")

        cursor_folder_button = ttk.Button(
            self.pixel_set,
            text="Cursor Folder",
            compound="left",
            image=self.folder_icon,
            command=open_icon_folder,
            width=20
        )
        cursor_folder_button.grid(row=3, column=4, padx=10, pady=5, sticky="ew")

        wp_folder_button = ttk.Button(
            self.pixel_set,
            text="Set Wallpaper Folder",
            compound="left",
            image=self.folder_icon,
            command=self.select_wallpaper_directory,
            width=20
        )
        wp_folder_button.grid(row=4, column=4, padx=10, pady=5, sticky="ew")

        info_button = tk.Button(
            self.pixel_set,
            text="Why is everthing DISABLED?",
            #borderwidth=0,
            #highlightthickness=0,
            #background=ext_btn,
            #foreground=ext_btn_font,
            command=why_message_0,
        )

        def install_papirus():
            # Add the functionality to be executed when the "Install Papirus + Folders" button is clicked
            print("Installing Papirus + Folders...")
            popen(
                "x-terminal-emulator -e 'bash -c \"wget -qO- https://git.io/papirus-icon-theme-install | sh && wget -qO- https://git.io/papirus-folders-install | sh; exec bash\"'"
            )
            self.install_button.config(state=DISABLED)

        def set_icon_theme():
            selected_theme = self.papirus_theme_combobox.get()
            selected_ver = self.papirus_version_combobox.get()
            if selected_theme != "Select a Color":
                print(f"Setting icon theme to: {selected_theme}")
                os.system(
                    f"{permit} papirus-folders -C {selected_theme} --theme {selected_ver}"
                )
                if get_desktop_environment() == "xfce":
                    subprocess.run(
                        [
                            "xfconf-query",
                            "-c",
                            "xsettings",
                            "-p",
                            "/Net/IconThemeName",
                            "-s",
                            selected_ver,
                        ]
                    )
                elif get_desktop_environment() == "lxde-pi" or "lxde":
                    update_lxde_icons_config(selected_ver)
                else:
                    subprocess.run(
                        [
                            "gsettings",
                            "set",
                            "org.gnome.desktop.interface",
                            "icon-theme",
                            selected_ver,
                        ]
                    )
            else:
                print("Please select a valid icon theme.")
            done_message_0()

        self.papirus_icons_frame = ttk.LabelFrame(
            self,
            text="Papirus Icons",
            padding=10
        )
        self.papirus_icons_frame.pack(pady=20, padx=40, fill="x", anchor="n")

        self.install_button = ttk.Button(
            self.papirus_icons_frame,
            text="Install Papirus + Folders",
            command=install_papirus,
            style="Custom.TButton"
        )
        self.install_button.grid(
            row=1, column=0, columnspan=5, padx=10, pady=10, sticky="we"
        )

        self.icon_themes = [
            "adwaita",
            "black",
            "blue",
            "bluegrey",
            "breeze",
            "brown",
            "carmine",
            "cyan",
            "darkcyan",
            "deeporange",
            "green",
            "grey",
            "indigo",
            "magenta",
            "nordic",
            "orange",
            "palebrown",
            "paleorange",
            "pink",
            "red",
            "teal",
            "violet",
            "white",
            "yaru",
            "yellow",
        ]
        self.papirus_theme_combobox = ttk.Combobox(
            self.papirus_icons_frame, values=self.icon_themes, state="readonly"
        )
        self.papirus_theme_combobox.grid(
            row=2, column=0, columnspan=2, padx=10, pady=10, sticky="wns"
        )
        self.papirus_theme_combobox.set("Select a Color")
        self.icon_papirus_version = [
            "ePapirus",
            "Papirus",
            "Papirus-Dark",
            "Papirus-Light",
        ]
        self.papirus_version_combobox = ttk.Combobox(
            self.papirus_icons_frame, values=self.icon_papirus_version, state="readonly"
        )
        self.papirus_version_combobox.grid(
            row=2, column=2, columnspan=2, padx=10, pady=10, sticky="wns"
        )
        self.papirus_version_combobox.set("Select a Version")

        self.set_button = ttk.Button(
            self.papirus_icons_frame,
            text="Set",
            command=set_icon_theme,
            style="Custom.TButton"
        )
        self.set_button.grid(row=2, column=4, padx=10, pady=10)

        def xfce_theme_():
            pass

        update_theme_combobox()

        if get_desktop_environment() not in [
            "xfce",
            "GNOME",
            "mate",
            "lxde",
            "lxde-pi-wayfire",
        ]:
            theme_button.config(state=tk.DISABLED)
            icon_button.config(state=tk.DISABLED)
            cursor_button.config(state=tk.DISABLED)
            theme_refresh_button.config(state=tk.DISABLED)
            theme_combobox.config(state=tk.DISABLED)
            icon_combobox.config(state=tk.DISABLED)
            cursor_combobox.config(state=tk.DISABLED)
            self.papirus_theme_combobox.config(state=tk.DISABLED)
            self.papirus_version_combobox.config(state=tk.DISABLED)
            self.set_button.config(state=tk.DISABLED)
            self.install_button.config(state=tk.DISABLED)
            info_button.grid(row=5, column=4, padx=10, pady=5, sticky="ew")

        if (
            get_desktop_environment() == "lxde-pi"
            or get_desktop_environment() == "lxde"
        ):
            theme_legacy_button.config(state=tk.NORMAL)
            self.papirus_theme_combobox.config(state=tk.NORMAL)
            self.papirus_version_combobox.config(state=tk.NORMAL)
            self.set_button.config(state=tk.NORMAL)
            self.install_button.config(state=tk.NORMAL)

        if get_desktop_environment() == "xfce":
            theme_legacy_button.config(
                text="XFCE Theme", state=tk.NORMAL, command=xfce_theme_
            )
            self.papirus_theme_combobox.config(state=tk.NORMAL)
            self.papirus_version_combobox.config(state=tk.NORMAL)
            self.set_button.config(state=tk.NORMAL)
            self.install_button.config(state=tk.NORMAL)
        if check_papirus() is True:
            self.install_button.config(state=DISABLED)

        self.wp_gallery = ttk.LabelFrame(
            self,
            text="Wallpaper Gallery",
            padding=10

        )
        self.wp_gallery.pack(pady=20, padx=40, fill="both", expand=True, anchor="n")

        # Create a Canvas widget to hold the content of wp_frame
        self.canvas = Canvas(self.wp_gallery, borderwidth=0, highlightthickness=0)
        self.canvas.pack(side="left", fill="both", expand=True)

        # Add a Scrollbar and link it to the Canvas for scrolling
        self.scrollbar = ttk.Scrollbar(self.wp_gallery, command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.canvas.config( yscrollcommand=self.scrollbar.set)

        # Create wp_frame as a child of the Canvas
        self.wp_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.wp_frame, anchor="nw")

        # Bind the Canvas to configure the scroll region when the frame size changes
        self.wp_frame.bind("<Configure>", self.configure_canvas)

        self.thumbnails_frame = None  # Initialize thumbnails_frame here
        self.thumbnails = []

        self.home_dir = os.path.expanduser("~")
        self.config_dir = os.path.join(self.home_dir, ".pigro")
        os.makedirs(self.config_dir, exist_ok=True)

        self.wallpaper_dir = None
        self.load_wallpaper_list()

    def set_wallpapers(self, image_path):
        try:
            if get_desktop_environment() == "lxde-pi-wayfire":
                os.popen(f"pcmanfm --set-wallpaper {image_path}")
            elif get_desktop_environment() == "lxde":
                os.popen(f"pcmanfm --set-wallpaper {image_path}")
            elif get_desktop_environment() == "xfce":
                os.popen(
                    f"xfconf-query -c xfce4-desktop -p insert_property_here -s {image_path}"
                )
            elif get_desktop_environment() == "mate":
                subprocess.run(
                    [
                        "gsettings",
                        "set",
                        "org.mate.background",
                        "picture-filename",
                        f"{image_path}",
                    ]
                )
            elif get_desktop_environment() == "gnome":
                subprocess.run(
                    [
                        "gsettings",
                        "set",
                        "org.gnome.desktop.background",
                        "picture-uri-dark",
                        f"file://{image_path}",
                    ]
                )
                subprocess.run(
                    [
                        "gsettings",
                        "set",
                        "org.gnome.desktop.background",
                        "picture-uri",
                        f"file://{image_path}",
                    ]
                )
            print(f"Wallpaper set to: {image_path}")
        except Exception as e:
            print(f"Error setting wallpaper: {e}")

    def change_wallpaper(self, image_path):
        self.set_wallpapers(image_path)

    def select_wallpaper_directory(self):
        self.wallpaper_dir = filedialog.askdirectory(
            title="Select Wallpaper Directory", initialdir=self.home_dir
        )

        if self.wallpaper_dir:
            self.refresh_thumbnails()
            self.save_wallpaper_list()

    def save_wallpaper_list(self):
        if self.wallpaper_dir:
            data = {
                "wallpaper_dir": self.wallpaper_dir,
                "wallpapers": [img[0] for img in self.thumbnails],
            }
            config_path = os.path.join(self.config_dir, "config.json")
            with open(config_path, "w", encoding="utf-8") as config_file:
                json.dump(data, config_file)

    def load_wallpaper_list(self):
        config_path = os.path.join(self.config_dir, "config.json")
        if os.path.isfile(config_path):
            with open(config_path, "r", encoding="utf-8") as config_file:
                data = json.load(config_file)
                self.wallpaper_dir = data["wallpaper_dir"]
                self.refresh_thumbnails()

    def refresh_thumbnails(self):
        if self.thumbnails_frame is not None:
            for widget in self.thumbnails_frame.winfo_children():
                widget.destroy()

        if not self.wallpaper_dir:
            return

        image_files = [
            f
            for f in os.listdir(self.wallpaper_dir)
            if f.lower().endswith((".jpg", ".jpeg", ".png", ".gif"))
        ]

        self.thumbnails_frame = ttk.Frame(self.wp_frame)
        self.thumbnails_frame.pack()

        self.row, self.col = 0, 0
        self.thumbnails = []

        for image_file in image_files:
            image_path = os.path.join(self.wallpaper_dir, image_file)
            image = Image.open(image_path)
            image.thumbnail((220, 220))
            thumbnail = ImageTk.PhotoImage(image)
            self.thumbnails.append((image_path, thumbnail))

        for image_path, thumbnail in self.thumbnails:
            button = Button(
                self.thumbnails_frame,
                image=thumbnail,
                command=lambda path=image_path: self.change_wallpaper(path),
                borderwidth=0,
                highlightthickness=0,
            )
            button.grid(row=self.row, column=self.col, padx=5, pady=5)

            self.col += 1
            if self.col == 4:
                self.col = 0
                self.row += 1

    def add_content(self):
        for i in range(50):
            label = Label(self.wp_frame, text=f"Item {i}")
            label.pack()

    def configure_canvas(self, event):
        self.canvas.config(scrollregion=self.canvas.bbox("all"))
