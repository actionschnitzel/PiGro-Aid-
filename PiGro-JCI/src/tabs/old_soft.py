class PiAppsSearchPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)

        def error_message_0():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

        def error_message_1():
            e_mass = Error_Mass(self)
            e_mass.grab_set()

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
            piapps_search_frame.pack(
                anchor="n", pady=20, padx=10, fill="both", expand=True
            )
            piapps_info_throber_frame.pack(fill="x", pady=20, padx=10)

        def piapps_install():
            fullstring = piapps_entry.get()
            substring = " "
            if substring in fullstring:
                replace_space = fullstring.replace(" ", "\\ ")
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
                replace_space = fullstring.replace(" ", "\\ ")
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
                        width=10,
                        command=piapps_uninstall,
                        style="Red.TButton",
                    )
                else:
                    piapps_pkg_inst.config(
                        text="Install",
                        width=10,
                        command=piapps_install,
                        style="Green.TButton",
                    )

                piapps_search_frame.pack_forget()
                piapps_get_icon()
                piapps_get_screenshot()
                piapps_get_description()

        def install_piapps_apt():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/install | bash; exec bash\"'"
            )
            rs_pigro = RestartPigroMass(self)
            rs_pigro.grab_set()

        if piapps_path == False:
            pi_apps_main_container.pack_forget()

            pi_apps_not_installad_container = Frame(self, pady=200)
            pi_apps_not_installad_container.pack(fill="both", expand=True)

            piapps_big_icon = Label(
                pi_apps_not_installad_container,
                image=self.pi_apps_big_icon,
                font=font_10_b,
                justify="left",
            )
            piapps_big_icon.pack(anchor="center", pady=20)

            piapps_app_inst = ttk.Button(
                pi_apps_not_installad_container,
                text="Install Pi-Apps",
                width=20,
                command=install_piapps_apt,
            )
            piapps_app_inst.pack()

        pi_apps_main_container = Frame(self)
        pi_apps_main_container.pack(fill="both", expand=True)

        piapps_search_frame = ttk.LabelFrame(
            pi_apps_main_container, text="Search", padding=20
        )
        piapps_search_frame.pack(
            anchor="n", pady=20, padx=10, fill="both", expand=True, side=TOP
        )

        piapps_search_field = Frame(
            piapps_search_frame,
            borderwidth=0,
            highlightthickness=0,
        )
        piapps_search_field.pack(fill="x", pady=5)

        piapps_search_btn = Label(
            piapps_search_field,
            image=self.search_btn,
        )

        piapps_entry = ttk.Entry(piapps_search_field, font=("Sans", 15))
        piapps_entry.pack(fill="x", expand=True, side="left")
        listbox_ttp = CreateToolTip(
            piapps_entry,
            " - Typ to finde a package\n\n - Single click on a listbox item to show more infos",
        )

        piapps_list_box = Listbox(
            piapps_search_frame,
            borderwidth=0,
            highlightthickness=0,
            selectmode=tk.SINGLE,
        )

        piapps_list_box_scrollbar = ttk.Scrollbar(piapps_search_frame)
        piapps_list_box_scrollbar.pack(side=RIGHT, fill=Y)
        piapps_list_box.config(yscrollcommand=piapps_list_box_scrollbar.set)
        piapps_list_box_scrollbar.config(command=piapps_list_box.yview)

        piapps_list_box.pack(fill=BOTH, expand=True)

        update_piapps(piapps_cache_content)

        piapps_list_box.bind("<ButtonRelease-1>", piapps_list_fillout)

        piapps_entry.bind("<KeyRelease>", piapps_search_check)

        piapps_info_throber_frame = Frame(pi_apps_main_container)
        piapps_info_throber_frame.pack(fill="x", pady=20, padx=10)

        # piapps OneClicks
        piapps_one_click_frame = ttk.LabelFrame(
            piapps_info_throber_frame, text="One Click Install", padding=20
        )
        piapps_one_click_frame.pack(fill="x")

        piapps_one_click_frame.grid_columnconfigure(0, weight=1)
        piapps_one_click_frame.grid_columnconfigure(1, weight=1)
        piapps_one_click_frame.grid_columnconfigure(2, weight=1)
        piapps_one_click_frame.grid_columnconfigure(3, weight=1)

        piapps_one_click_dict = PiAppsOneClicks.piapps_one_click_dict

        piapps_one_click_dict1 = []
        conf_row = 0
        conf_column = 0

        def piapps_one_click(package):
            fullstring = package
            substring = " "
            if substring in fullstring:
                replace_space = fullstring.replace(" ", "\\ ")
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

            piapps_one_click_button_x = ttk.Button(
                piapps_one_click_frame,
                image=self.piapps_butt,
                compound="left",
                text=software_name,
                width=15,
                command=lambda package=package_name: piapps_one_click(package),
            )

            self.piapps_one_click_ttp = CreateToolTip(
                piapps_one_click_button_x, package_info
            )

            piapps_one_click_button_x.grid(
                row=conf_row, column=conf_column, padx=5, pady=5, sticky="nsew"
            )
            piapps_one_click_dict1.append(piapps_one_click_button_x)
            conf_column += 1

            if conf_column == 4:
                conf_row += 1
                conf_column = 0

        piapps_info_frame = ttk.Frame(pi_apps_main_container, padding=20)

        piapps_exit = ttk.Button(
            piapps_info_frame,
            text="Back",
            command=hide_piapps_frame,
        )
        piapps_exit.grid(row=0, column=0, sticky="e")

        piapps_application_labelframe = ttk.LabelFrame(
            piapps_info_frame, text="Application", padding=20
        )
        piapps_application_labelframe.grid(row=1, column=0, sticky="ew")

        piapps_pkg_header_frame = Frame(
            piapps_application_labelframe,
            borderwidth=0,
            highlightthickness=0,
        )
        piapps_pkg_header_frame.pack(fill="x")
        piapps_pkg_header_frame.columnconfigure(1, weight=2)

        piapps_pkg_icon = Label(
            piapps_pkg_header_frame,
            image=self.pi_appsinstall_icon,
            font=font_10_b,
            justify="left",
        )
        piapps_pkg_icon.grid(row=0, rowspan=2, column=0)

        piapps_pkg_name = Label(
            piapps_pkg_header_frame,
            text="",
            font=font_20,
            justify="left",
            anchor="w",
            padx=20,
        )
        piapps_pkg_name.grid(row=0, column=1, sticky="ew")

        piapps_pkg_status = Label(
            piapps_pkg_header_frame,
            text="",
            font=font_10,
            justify="left",
            anchor="w",
            padx=20,
        )
        piapps_pkg_status.grid(row=1, column=1, sticky="ew")

        piapps_pkg_inst = ttk.Button(
            piapps_pkg_header_frame,
            text="Install",
            width=10,
            command=piapps_install,
        )
        piapps_pkg_inst.grid(row=0, column=2, sticky="e")

        def open_pi_apps():
            os.system(f"{home}/pi-apps/gui")

        def open_pi_apps_settings():
            popen(f"{home}/pi-apps/settings")

        piapps_configs_frame = Frame(piapps_pkg_header_frame)
        piapps_configs_frame.grid(row=2, column=1, pady=0)

        piapps_app_open = Button(
            piapps_configs_frame,
            justify="left",
            imag=self.pi_appsopen_icon,
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
            font=font_10_b,
            borderwidth=0,
            highlightthickness=0,
            command=open_pi_apps_settings,
        )
        piapps_setting_open.grid(row=0, column=1, pady=0, padx=5)

        piapps_detail_frame = ttk.LabelFrame(
            piapps_info_frame, text="Details", padding=20
        )
        piapps_detail_frame.grid(row=2, column=0, sticky="nsew")

        piapps_detail_frame.columnconfigure(0, weight=1)
        piapps_detail_frame.rowconfigure(0, weight=1)

        piapps_canvas = Canvas(piapps_detail_frame, borderwidth=0, highlightthickness=0)
        piapps_canvas.grid(row=0, column=0, sticky="nsew")

        piapps_canvas_scrollbar = ttk.Scrollbar(
            piapps_detail_frame, orient="vertical", command=piapps_canvas.yview
        )
        piapps_canvas_scrollbar.grid(row=0, column=1, sticky="ns")

        piapps_canvas.configure(yscrollcommand=piapps_canvas_scrollbar.set)

        piapps_canvas_frame = Frame(piapps_canvas)
        piapps_canvas.create_window((0, 0), window=piapps_canvas_frame, anchor="nw")

        piapps_canvas_frame.bind(
            "<Configure>",
            lambda e: piapps_canvas.configure(scrollregion=piapps_canvas.bbox("all")),
        )

        piapps_panel = Label(piapps_canvas_frame)
        piapps_panel.grid(row=0, column=0, columnspan=2, pady=20)

        piapps_description_text = Text(
            piapps_canvas_frame,
            borderwidth=0,
            highlightthickness=0,
            font=("Sans", 9),
            wrap=WORD,
            padx=20,
        )
        piapps_description_text.grid(row=1, column=0, sticky="nesw", padx=(20, 0))

        piapps_canvas_frame.columnconfigure(0, weight=1)
        piapps_canvas_frame.rowconfigure(1, weight=1)

        piapps_info_frame.columnconfigure(0, weight=1)
        piapps_info_frame.rowconfigure(2, weight=1)


class FlatpakSearchPanel(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
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
            flatpak_search_frame.pack(
                anchor="w", pady=20, padx=10, fill=BOTH, expand=True
            )
            flatpak_info_throber_frame.pack(fill="x", pady=20, padx=10)

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
                flatpak_panel.config(self.no_img)

            except subprocess.CalledProcessError as err:
                print("Command returned non-zero exit status:", err)
                if "returned non-zero exit status 4" in str(err):
                    try:
                        app_id += ".desktop"
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

                    except subprocess.CalledProcessError as err:
                        print("Command returned non-zero exit status again:", err)
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
                        width=10,
                        command=flatpak_uninstall,
                    )
                else:
                    flatpak_pkg_inst.config(
                        text="Install",
                        width=10,
                        command=flatpak_install,
                    )

        flatpak_inst_main_frame = Frame(self)
        flatpak_inst_main_frame.pack(fill="both", expand=True)

        def install_flatpak_apt():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"sudo apt install flatpak && flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo | bash; exec bash\"'"
            )
            rs_pigro = RestartPigroMass(self)
            rs_pigro.grab_set()

        if flatpak_path == False:
            flatpak_inst_main_frame.pack_forget()

            flat_not_installad_container = Frame(self, pady=200)
            flat_not_installad_container.pack(fill=BOTH, expand=True)

            flat_big_icon = Label(
                flat_not_installad_container,
                image=self.flatpak_big_icon,
                font=font_10_b,
                justify="left",
            )
            flat_big_icon.pack(anchor="center", pady=20)

            flat_app_inst = ttk.Button(
                flat_not_installad_container,
                text="Install Flatpak",
                width=20,
                command=install_flatpak_apt,
                style="Custom.TButton",
            )
            flat_app_inst.pack()

        flatpak_search_frame = ttk.LabelFrame(
            flatpak_inst_main_frame,
            text="Search",
            padding=20,
        )
        flatpak_search_frame.pack(
            anchor="w", pady=20, padx=10, fill="both", expand=True
        )

        flatpak_search_field = Frame(
            flatpak_search_frame,
            borderwidth=0,
            highlightthickness=0,
        )
        flatpak_search_field.pack(fill="x", pady=5)

        flatpak_search_btn = Label(
            flatpak_search_field,
            image=self.search_btn,
        )

        flatpak_entry = ttk.Entry(
            flatpak_search_field,
            font=("Sans", 15),
        )
        flatpak_entry.pack(fill="x", expand=True, side="left")
        listbox_ttp = CreateToolTip(
            flatpak_entry,
            " - Typ to finde a package\n\n - Single click on a listbox item to show more infos",
        )

        flatpak_list_box = Listbox(
            flatpak_search_frame,
            borderwidth=0,
            highlightthickness=0,
            selectmode=tk.SINGLE,
        )

        flatpak_list_scrollbar = ttk.Scrollbar(flatpak_search_frame)
        flatpak_list_scrollbar.pack(side=RIGHT, fill=Y)
        flatpak_list_box.config(yscrollcommand=flatpak_list_scrollbar.set)
        flatpak_list_scrollbar.config(command=flatpak_list_box.yview)

        flatpak_list_box.pack(fill=BOTH, expand=True)

        update_flatpak(Flat_remote_dict.keys())

        flatpak_list_box.bind("<ButtonRelease-1>", flatpak_list_fillout)

        flatpak_entry.bind("<KeyRelease>", flatpak_search_check)

        flatpak_info_throber_frame = Frame(
            flatpak_inst_main_frame,
        )
        flatpak_info_throber_frame.pack(fill="x", pady=20, padx=10)

        flatpak_info_frame = Frame(flatpak_inst_main_frame)

        flatpak_exit = Button(
            flatpak_info_frame,
            text="Back",
            image=self.exit_btn,
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

        flatpak_pkg_info_frame = ttk.LabelFrame(
            flatpak_info_frame,
            padding=20,
        )
        flatpak_pkg_info_frame.pack(anchor="n", fill="x")

        flatpak_pkg_info_container = Frame(
            flatpak_pkg_info_frame,
            borderwidth=0,
            highlightthickness=0,
        )
        flatpak_pkg_info_container.pack(fill="x")
        flatpak_pkg_info_container.columnconfigure(1, weight=2)

        flatpak_pkg_icon = Label(
            flatpak_pkg_info_container,
            image=self.debinstall_icon,
            font=font_10_b,
            justify="left",
            padx=10,
        )
        flatpak_pkg_icon.grid(row=0, rowspan=2, column=0)

        flatpak_pkg_name = Label(
            flatpak_pkg_info_container,
            text="",
            font=font_20,
            justify="left",
            anchor="w",
            padx=20,
        )
        flatpak_pkg_name.grid(row=0, column=1, sticky="ew")

        flatpak_pkg_status = Label(
            flatpak_pkg_info_container,
            text="",
            font=font_8,
            justify="left",
            anchor="w",
            padx=20,
        )
        flatpak_pkg_status.grid(row=1, column=1, sticky="ew")

        flatpak_pkg_inst = Button(
            flatpak_pkg_info_container,
            text="Install",
            width=10,
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

        flatpak_canvas_container = Frame(flatpak_info_frame, width=869)
        flatpak_canvas_container.pack(side=LEFT, fill="both", expand=True)

        flatpak_canvas = tk.Canvas(flatpak_canvas_container, highlightthickness=0)
        flatpak_canvas.pack(fill=BOTH, expand=True, side=RIGHT)
        flatpak_canvas.pack_propagate(False)
        flatpak_canvas_frame = tk.Frame(flatpak_canvas, padx=120)
        flatpak_canvas.create_window(
            (0, 0), window=flatpak_canvas_frame, anchor="n", tags="frame"
        )

        flatpak_panel = Label(flatpak_canvas_frame, text="Apartment Panel")
        flatpak_panel.pack(anchor="n", pady=20)

        flatpak_description_text = Text(
            flatpak_canvas_frame,
            borderwidth=0,
            highlightthickness=0,
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
        flatpak_one_click_frame = ttk.LabelFrame(
            flatpak_info_throber_frame, text="One Click Install", padding=20
        )
        flatpak_one_click_frame.pack(fill="x")
        flatpak_one_click_frame.grid_columnconfigure(0, weight=1)
        flatpak_one_click_frame.grid_columnconfigure(1, weight=1)
        flatpak_one_click_frame.grid_columnconfigure(2, weight=1)
        flatpak_one_click_frame.grid_columnconfigure(3, weight=1)

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

            flatpak_one_click_button_x = ttk.Button(
                flatpak_one_click_frame,
                image=self.flatpak_butt,
                compound="left",
                text=software_name,
                width=15,
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

            if conf_column == 4:
                conf_row += 1
                conf_column = 0
