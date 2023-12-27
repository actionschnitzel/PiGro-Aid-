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

        self.rahmen102 = Frame(
            self, borderwidth=0, relief=GROOVE, highlightthickness=0, pady=10, padx=10
        )
        self.rahmen102.pack(fill=BOTH, padx=50, pady=20)
        self.rahmen102["background"] = maincolor

        self.actn_shn = Label(
            self.rahmen102,
            image=self.auto_start,
            background=maincolor,
        ).pack(pady=20)

        self.poke_pig_21 = Label(
            self.rahmen102,
            text=f"PiGro - Just Click It!\nVersion: {current_version}",
            font=font_16,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.change_log = Button(
            self.rahmen102,
            text="Changelog",
            font=(font_10),
            borderwidth=0,
            highlightthickness=0,
            width=20,
            background=ext_btn,
            foreground=ext_btn_font,
            command=ch_log,
        )
        self.change_log.pack()

        self.check_for_update = Button(
            self.rahmen102,
            text="Check for Update",
            font=(font_10),
            borderwidth=0,
            highlightthickness=0,
            width=20,
            background=ext_btn,
            foreground=ext_btn_font,
            command=update_checker,
        )
        self.check_for_update.pack(pady=10)

        self.gihub_link = tk.Label(
            self.rahmen102,
            text=r"https://github.com/actionschnitzel/PiGro-Aid-",
            fg="blue",
            background=maincolor,
            cursor="hand2",
        )
        self.gihub_link.pack(pady=5)
        self.gihub_link.bind("<Button-1>", callback)

        self.poke_pig_21 = Label(
            self.rahmen102,
            text="\n\n\nDeveloped and maintained by:\n\nTimo Westphal\n(Actionschnitzel)\n\nContact:",
            font=font_12,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.mail = Entry(self.rahmen102, bd=6, width=20, borderwidth=0)
        self.mail.insert(END, "pigroxtrmo@gmail.com")
        self.mail.pack(pady=5)

        self.paypal = Button(
            self.rahmen102,
            text="Paypal",
            font=(font_10),
            image=self.paypal_icon,
            highlightthickness=0,
            borderwidth=0,
            background=maincolor,
            foreground=ext_btn_font,
            command=paypal_link,
            activebackground=maincolor,
        )
        self.paypal.pack()

        self.poke_pig_21 = Label(
            self.rahmen102,
            text="\n\n\nThis program comes with ABSOLUTELY NO WARRANTY!\nIt is licensed under the GNU General Public License v3.0\nIcons have been partially adopted and modified from the\nPapirus Icon Theme licensed under the\nGNU General Public License v3.0",
            font=font_9_b,
            background=maincolor,
            foreground=main_font,
            padx=5,
            pady=3,
        ).pack()

        self.papirus_link = tk.Label(
            self.rahmen102,
            text=r"https://github.com/PapirusDevelopmentTeam/papirus-icon-theme",
            fg="blue",
            background=maincolor,
            cursor="hand2",
        )
        self.papirus_link.pack()
        self.papirus_link.bind("<Button-1>", callback)
