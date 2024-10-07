from os import popen
from tkinter import *
from tkinter import ttk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *


class LinksTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        self.link = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/web_light.png"
        )

        def link_tab(text):
            if text == "Mankier.com (Commandline Database)":
                popen("xdg-open https://mankier.com")
            if text == "Guake (Drop Down Terminal)":
                popen("xdg-open https://github.com/Guake/guake")
            if text == "Draculatheme.com":
                popen("xdg-open https://draculatheme.com/")
            if text == "Starship (Cross-Shell-Promt)":
                popen("xdg-open https://starship.rs/")
            if text == "Linuxcommandlibrary.com":
                popen("xdg-open https://linuxcommandlibrary.com/")
            if text == "LCD Wiki":
                popen("xdg-open https://www.lcdwiki.com")
            if text == "Offical Raspberry Pi Documentation":
                popen("xdg-open https://www.raspberrypi.com/documentation/")
            if text == "Raspberry Pi Tutorials":
                popen("xdg-open https://tutorials-raspberrypi.com/")
            if text == "WaveShare Wiki":
                popen("xdg-open  https://www.waveshare.com/wiki/Main_Page")
            if text == "My ZSH Prompt":
                popen("xdg-open  https://github.com/actionschnitzel/my_zsh_prompt")
            if text == "Xfce-Look.org":
                popen("xdg-open  https://www.xfce-look.org/s/XFCE/browse/")
            if text == "Brave Browser Nighly arm64":
                popen("xdg-open  https://github.com/brave/brave-browser/releases")
            if text == "Ubuntuusers.de":
                popen("xdg-open https://wiki.ubuntuusers.de/")
            if text == "Explainingcomputers":
                popen("xdg-open https://www.explainingcomputers.com/")
            if text == "Chat GPT":
                popen("xdg-open https://chat.openai.com/")
            if text == "OMG Ubuntu":
                popen("xdg-open https://www.omgubuntu.co.uk/")
            if text == "Lutris":
                popen("xdg-open https://lutris.net/games")
            if text == "JeffGeerling.com":
                popen("xdg-open https://www.jeffgeerling.com/")
            if text == "MX Linux Raspi Spin":
                popen("xdg-open https://mxlinux.org/download-links/")
            if text == "Ubuntu For Raspberry Pi":
                popen("xdg-open  https://ubuntu.com/download/raspberry-pi")
            if text == "Markdown To PDF":
                popen("xdg-open  https://md2pdf.netlify.app/")
            if text == "Explainshell.com":
                popen("xdg-open https://explainshell.com/")
            if text == "Linux + Open Source News PodCast":
                popen("xdg-open https://podcast.thelinuxexp.com/@tlenewspodcast")
            if text == "OMG Linux":
                popen("xdg-open https://www.omglinux.com/")

        self.link_left = ttk.Frame(
            self,
            padding=20
        )
        self.link_left.pack(padx=40,fill=BOTH)

        # Konfiguriere jede Spalte so, dass sie expandiert
        self.link_left.grid_columnconfigure(0, weight=1)
        self.link_left.grid_columnconfigure(1, weight=1)

        # Keine Gewichtung für die Zeilen, sodass sie nicht expandieren
        self.link_left.grid_rowconfigure(0, weight=0)
        self.link_left.grid_rowconfigure(1, weight=0)



        sources_d = [
            "Chat GPT",
            "Draculatheme.com",
            "Explainshell.com",
            "Guake (Drop Down Terminal)",
            "JeffGeerling.com",
            "LCD Wiki",
            "Linux + Open Source News PodCast",
            "Linuxcommandlibrary.com",
            "Mankier.com (Commandline Database)",
            "Markdown To PDF",
            "MX Linux Raspi Spin",
            "My ZSH Prompt",
            "Offical Raspberry Pi Documentation",
            "OMG Linux",
            "OMG Ubuntu",
            "Raspberry Pi Tutorials",
            "Starship (Cross-Shell-Promt)",
            "Ubuntu For Raspberry Pi",
            "WaveShare Wiki",
            "Xfce-Look.org",
        ]

        sources_d1 = []

        conf_row = 0
        conf_column = 0

        for file in sources_d:
            self.choice_link1 = ttk.Button(
                self.link_left,
                #width=400,
                compound="left",
                text=file,
                image=self.link,
                command=lambda text=file: link_tab(text),
            ).grid(row=conf_row, column=conf_column, padx=5, pady=5, sticky="ew")
            sources_d1.append(self.choice_link1)

            conf_column = conf_column + 1
            if conf_column == 2:
                conf_row = conf_row + 1
                conf_column = 0
