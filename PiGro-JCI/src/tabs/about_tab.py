from os import popen
from tkinter import *
from tkinter import ttk
import tkinter as tk
import webbrowser
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *


class AboutTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew")

        def callback(event):
            webbrowser.open_new(event.widget.cget("text"))

        def ch_log():
            popen(
                "xdg-open https://github.com/actionschnitzel/PiGro-Aid-/wiki/Change-Log"
            )

        def update_checker():
            up_chk = Update_Pop(self)
            up_chk.grab_set()

        def paypal_link():
            popen("xdg-open https://www.paypal.com/paypalme/actionschnitzel")

        self.auto_start = PhotoImage(file=f"{application_path}/images/icons/logo1.png")

        self.paypal_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PayPal_donation.png"
        )

        self.rahmen102 = ttk.Frame(
            self,padding=10
        )
        self.rahmen102.pack(fill=BOTH, padx=50, pady=20)

        self.actn_shn = ttk.Label(
            self.rahmen102,
            image=self.auto_start,
        ).pack(pady=20)

        self.poke_pig_21 = ttk.Label(
            self.rahmen102,
            text=f"PiGro - Just Click It!\nVersion: {current_version}",
            font=font_16,
            padding=5
        ).pack()

        self.change_log = ttk.Button(
            self.rahmen102,
            text="Changelog",
            command=ch_log,
            style="Custom.TButton", 
            width=20
        )
        self.change_log.pack()

        self.check_for_update = ttk.Button(
            self.rahmen102,
            text="Check for Update",
            style="Custom.TButton",
            command=update_checker,
            width=20
        )
        self.check_for_update.pack(pady=10)

        self.gihub_link = ttk.Label(
            self.rahmen102,
            text=r"https://github.com/actionschnitzel/PiGro-Aid-",
            cursor="hand2",
        )
        self.gihub_link.pack(pady=5)
        self.gihub_link.bind("<Button-1>", callback)

        self.poke_pig_21 = ttk.Label(
            self.rahmen102,
            text="\n\n\nDeveloped and maintained by:\n\nTimo Westphal\n(Actionschnitzel)\n\nContact:",
            padding=5
        ).pack()

        self.mail = ttk.Entry(self.rahmen102, width=20)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.paypal = ttk.Button(
            self.rahmen102,
            text="Paypal",
            image=self.paypal_icon,
            command=paypal_link,
        )
        self.paypal.pack()

        self.poke_pig_21 = ttk.Label(
            self.rahmen102,
            text="\n\n\nThis program comes with ABSOLUTELY NO WARRANTY!\nIt is licensed under the GNU General Public License v3.0\nIcons have been partially adopted and modified from the\nPapirus Icon Theme licensed under the\nGNU General Public License v3.0",
            padding=5
        ).pack()

        self.papirus_link = tk.Label(
            self.rahmen102,
            text=r"https://github.com/PapirusDevelopmentTeam/papirus-icon-theme",
            cursor="hand2",
        )
        self.papirus_link.pack()
        self.papirus_link.bind("<Button-1>", callback)
