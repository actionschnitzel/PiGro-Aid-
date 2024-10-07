import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
from resorcess import *
from apt_manage import *
from flatpak_alias_list import *
from tabs.pop_ups import *
from tabs.system_tab_check import check_preload_state
from tabs.system_tab_check import check_zram


class TuningTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.grid(row=0, column=0, sticky="nsew",padx=20)

        # Current OV settings

        def tuning_legende():
            tu_le = Tuning_Legende(self)
            tu_le.grab_set()

        def int_error_mass():
            int_e_mass = Int_Error_Mass(self)
            int_e_mass.grab_set()

        # BG + Icons
        self.rm_ov_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV_rm.png"
        )
        self.ov1_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV1.png"
        )
        self.ov2_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV2.png"
        )
        self.ov3_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV3.png"
        )
        self.ov4_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV4.png"
        )
        self.ov5_icon = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/PiGroOV5.png"
        )
        self.ip03 = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/download_ico.png"
        )
        self.tu_legend_ico = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/io.otsaloma.nfoview.png"
        )
        self.zram_icon = PhotoImage(
            file=f"{application_path}/images/icons/papirus/48x48/device_mem.png"
        )
        self.toggle_on = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/toggle_on.png"
        )
        self.toggle_off = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/toggle_off.png"
        )
        self.toggle_off_enter = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/toggle_button_enter.png"
        )
        self.toggle_on_enter = PhotoImage(
            file=f"{application_path}/images/icons/pigro_icons/toggle_button_enter2.png"
        )
        # OV Notifications

        def done_msg():
            d_msg = Done_Reboot(self)
            d_msg.grab_set()

        # overclocking_default/reset

        def set_default():
            os.system(f"{permit} {application_path}/scripts/rm_ov.sh && exit")
            done_msg()
            tu_btn1.config(state=NORMAL)
            tu_btn2.config(state=NORMAL)
            tu_btn3.config(state=NORMAL)
            tu_btn4.config(state=NORMAL)

            arm_f_display.config(text="not configured")
            gpu_f_display.config(text="not configured")
            gpu_m_display.config(text="not configured")
            over_v_display.config(text="not configured")
            force_t_display.config(text="not configured")

        # overclocking_2000

        def ov_2000():
            os.system(
                f"""{permit} sh -c 'echo "#Pigro_Overclocking1\narm_freq=2000\ngpu_freq=750\nover_voltage=6\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        # overclocking_2147

        def ov_2147():
            os.system(
                f"""{permit} sh -c 'echo "#Pigro_Overclocking2\narm_freq=2147\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        # overclocking_2200

        def ov_2200():
            os.system(
                f"""{permit} sh -c 'echo "#Pigro_Overclocking3\narm_freq=2200\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )

            done_msg()

            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        # overclocking_2300
        def ov_2300():
            os.system(
                f"""{permit} sh -c 'echo "#Pigro_Overclocking4\narm_freq=2300\ngpu_freq=750\nover_voltage=14\ndisable_splash=1\nforce_turbo=1" >> {config_path}'"""
            )

            done_msg()
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        # OV_Button_Frame
        self.ov_buttons = ttk.LabelFrame(
            self,
            text="Pi4 Tuning Presets",
            padding=20
        )
        self.ov_buttons.pack(side=LEFT, pady=20, padx=20, fill=BOTH,expand=TRUE)
        self.ov_buttons.columnconfigure(0, weight=1)

        # Tuning_Button_Frame

        self.tu_reset = ttk.Button(
            self.ov_buttons,
            image=self.rm_ov_icon,
            text="Default Settings",
            command=set_default,
            compound=LEFT,

        )
        self.tu_reset.grid(column=0, row=2, pady=10,sticky="ew")


        global tu_btn1
        tu_btn1 = ttk.Button(
            self.ov_buttons,
            image=self.ov1_icon,
            text="Crank It Up",
            command=ov_2000,
            compound=LEFT,

        )
        tu_btn1.grid(column=0, row=4, pady=10,sticky="ew")

        global tu_btn2
        tu_btn2 = ttk.Button(
            self.ov_buttons,
            image=self.ov2_icon,
            text="You Sir... Need A Fan!",
            command=ov_2147,
            compound=LEFT,

        )
        tu_btn2.grid(column=0, row=6, pady=10,sticky="ew")

        global tu_btn3
        tu_btn3 = ttk.Button(
            self.ov_buttons,
            image=self.ov3_icon,
            text="Take It To The Max!",
            command=ov_2200,

            compound=LEFT,
        )
        tu_btn3.grid(column=0, row=8, pady=10,sticky="ew")

        global tu_btn4
        tu_btn4 = ttk.Button(
            self.ov_buttons,
            image=self.ov4_icon,
            text="Honey,\nthe fuse blew again!",
            command=ov_2300,
            compound=LEFT,
        )
        tu_btn4.grid(column=0, row=9, pady=10,sticky="ew")

        self.tu_legende = ttk.Button(
            self.ov_buttons,
            text="Preset Info",
            command=tuning_legende,
            image=self.tu_legend_ico,
            compound=LEFT,

        ).grid(column=0, row=10, pady=10,sticky="ew")



        def set_arm_freq():
            if arm_freq_spinbox.get().isdigit():
                print("Setting arm_freq to:", arm_freq_spinbox.get())
                os.system(
                    f"""{permit} sh -c 'echo "arm_freq={arm_freq_spinbox.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
            else:
                int_error_mass()

        def reset_arm_freq():
            print("Resetting arm_freq to:", arm_freq_spinbox.get())
            os.system(f"{permit} sed -i '/arm_freq/d' {config_path}")

        def set_gpu_freq():
            if gpu_freq_spinbox.get().isdigit():
                print("Setting gpu_freq to:", gpu_freq_spinbox.get())
                os.system(
                    f"""{permit} sh -c 'echo "gpu_freq={gpu_freq_spinbox.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
            else:
                int_error_mass()

        def reset_gpu_freq():
            print("Resetting gpu_freq to:", gpu_freq_spinbox.get())
            os.system(f"{permit} sed -i '/gpu_freq/d' {config_path}")

        def set_gpu_mem():
            if gpu_mem_spinbox.get().isdigit():
                print("Setting gpu_mem to:", gpu_mem_spinbox.get())
                os.system(
                    f"""{permit} sh -c 'echo "gpu_mem={gpu_mem_spinbox.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
            else:
                int_error_mass()

        def reset_gpu_mem():
            print("Resetting gpu_mem to:", gpu_mem_spinbox.get())
            os.system(f"{permit} sed -i '/gpu_mem/d' {config_path}")

        def set_over_voltage():
            if over_voltage_spinbox.get().isdigit():
                print("Setting over_voltage to:", over_voltage_spinbox.get())
                os.system(
                    f"""{permit} sh -c 'echo "over_voltage={over_voltage_spinbox.get()}" >> {config_path}'"""
                )
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
            else:
                int_error_mass()

        def reset_over_voltage():
            print("Resetting over_voltage to:", over_voltage_spinbox.get())
            os.system(f"{permit} sed -i '/over_voltage/d' {config_path}")

        def set_over_voltage_delta():
            if over_voltage_delta_spinbox.get().isdigit():
                print("Setting over_voltage to:", over_voltage_delta_spinbox.get())
                os.system(
                    f"""{permit} sh -c 'echo "over_voltage_delta={over_voltage_delta_spinbox.get()}" >> {config_path}'"""
                )
            else:
                int_error_mass()

        def reset_over_voltage_delta():
            print("Resetting over_voltage to:", over_voltage_delta_spinbox.get())
            os.system(f"{permit} sed -i '/over_voltage_delta/d' {config_path}")

        def set_force_turbo():
            os.system(f"""{permit} sh -c 'echo "force_turbo=1" >> {config_path}'""")
            tu_btn1.config(state=DISABLED)
            tu_btn2.config(state=DISABLED)
            tu_btn3.config(state=DISABLED)
            tu_btn4.config(state=DISABLED)

        def reset_force_turbo():
            os.system(f"{permit} sed -i '/force_turbo/d' {config_path}")
            force_t_display.config(text="State: Default")

        def lines_that_contain(string, fp):
            return [line for line in fp if string in line]

        def reboot_n():
            popen(f"{permit} reboot")

        # Overclocking State Main Frame
        self.ov_state_display_frame = ttk.Frame(
            self,

        )
        self.ov_state_display_frame.pack(padx=20, pady=20, fill=BOTH, expand=True
        )
        self.ov_state_display_frame.columnconfigure(0, weight=1)


        # Custom Settings
        self.custom_settings = ttk.LabelFrame(
            self.ov_state_display_frame,
            text="Custom Settings",
            padding=20
        )
        self.custom_settings.grid(column=0, row=0,sticky="ew")



        # Expert Frame
        x_mode_frame = ttk.Frame(self.custom_settings)
        x_mode_frame.pack(fill=BOTH, expand=True)

        arm_freq_label = ttk.Label(
            x_mode_frame,
            text="arm_freq ",
            justify="right",
            anchor="w",

        )
        arm_freq_label.grid(row=0, column=0, sticky="ew", padx=5)

        arm_freq_spinbox = ttk.Entry(x_mode_frame)
        arm_freq_spinbox.grid(row=0, column=1, sticky="ew", pady=5, padx=5)

        arm_freq_set_button = tk.Button(
            x_mode_frame,
            text="Set",
            command=set_arm_freq,
            image=self.toggle_off,
            highlightthickness=0,
            borderwidth=0,
            activebackground="#f7f7f7",
        )
        arm_freq_set_button.grid(row=0, column=2, sticky="ew", padx=5)

        global arm_f_display
        arm_f_display = ttk.Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            width=25,
        )
        arm_f_display.grid(column=4, row=0, padx=5)

        gpu_freq_label = tk.Label(
            x_mode_frame,
            text="gpu_freq ",
            justify="right",
            compound="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        gpu_freq_label.grid(row=1, column=0, sticky="ew", padx=5)

        gpu_freq_spinbox = ttk.Entry(
            x_mode_frame,
        )
        gpu_freq_spinbox.grid(row=1, column=1, sticky="ew", pady=5, padx=5)

        gpu_freq_set_button = tk.Button(
            x_mode_frame,
            text="Set",
            command=set_gpu_freq,
            foreground=ext_btn_font,
            background=maincolor,
            highlightthickness=0,
            activebackground=maincolor,
            borderwidth=0,
        )
        gpu_freq_set_button.grid(row=1, column=2, pady=5, sticky="ew", padx=5)

        global gpu_f_display
        gpu_f_display = Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_10,
            width=25,
        )
        gpu_f_display.grid(column=4, row=1, padx=5)

        gpu_mem_label = tk.Label(
            x_mode_frame,
            text="gpu_mem ",
            justify="right",
            compound="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        gpu_mem_label.grid(row=2, column=0, sticky="ew", padx=5)

        gpu_mem_spinbox = ttk.Entry(
            x_mode_frame,
        )
        gpu_mem_spinbox.grid(row=2, column=1, sticky="ew", pady=5, padx=5)

        gpu_mem_set_button = tk.Button(
            x_mode_frame,
            text="Set",
            command=set_gpu_mem,
            foreground=ext_btn_font,
            background=maincolor,
            highlightthickness=0,
            activebackground=maincolor,
            borderwidth=0,
        )
        gpu_mem_set_button.grid(row=2, column=2, pady=5, sticky="ew", padx=5)

        global gpu_m_display
        gpu_m_display = Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_10,
            width=25,
        )
        gpu_m_display.grid(column=4, row=2, padx=5)

        over_voltage_label = tk.Label(
            x_mode_frame,
            text="over_voltage ",
            justify="right",
            compound="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        over_voltage_label.grid(row=3, column=0, sticky="ew", padx=5)

        over_voltage_spinbox = ttk.Entry(
            x_mode_frame,
        )
        over_voltage_spinbox.grid(row=3, column=1, sticky="ew", pady=5, padx=5)

        over_voltage_set_button = tk.Button(
            x_mode_frame,
            text="Set",
            command=set_over_voltage,
            foreground=ext_btn_font,
            background=maincolor,
            highlightthickness=0,
            activebackground=maincolor,
            borderwidth=0,
        )
        over_voltage_set_button.grid(row=3, column=2, pady=5, sticky="ew", padx=5)

        global over_v_display
        over_v_display = Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_10,
            width=25,
        )
        over_v_display.grid(column=4, row=3, padx=5)

        over_voltage_delta_delta_label = tk.Label(
            x_mode_frame,
            text="over_voltage_delta ",
            justify="right",
            compound="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        over_voltage_delta_delta_label.grid(row=4, column=0, sticky="ew", padx=5)

        over_voltage_delta_spinbox = ttk.Entry(x_mode_frame)
        over_voltage_delta_spinbox.grid(row=4, column=1, sticky="ew", pady=5, padx=5)

        over_voltage_delta_set_button = tk.Button(
            x_mode_frame,
            text="",
            command=set_over_voltage_delta,
            foreground=ext_btn_font,
            background=maincolor,
            highlightthickness=0,
            activebackground=maincolor,
            borderwidth=0,
        )
        over_voltage_delta_set_button.grid(row=4, column=2, pady=5, sticky="ew", padx=5)

        global over_v_d_display
        over_v_d_display = Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_10,
            width=25,
        )
        over_v_d_display.grid(column=4, row=4, padx=5)

        force_turbo_label = tk.Label(
            x_mode_frame,
            text="force_turbo ",
            justify="right",
            compound="left",
            anchor="w",
            background=frame_color,
            foreground=main_font,
        )
        force_turbo_label.grid(row=5, column=0, sticky="ew", padx=5)

        force_turbo_set_button = tk.Button(
            x_mode_frame,
            text="Set",
            command=set_force_turbo,
            foreground=ext_btn_font,
            background=maincolor,
            highlightthickness=0,
            activebackground=maincolor,
            borderwidth=0,
        )
        force_turbo_set_button.grid(row=5, column=2, padx=5, pady=5, sticky="ew")

        force_turbo_label = tk.Label(
            x_mode_frame,
            text="",
            width=25,
            background=frame_color,
            foreground=main_font,
        )
        force_turbo_label.grid(row=5, column=1, sticky="ew", padx=5)

        global force_t_display
        force_t_display = Label(
            x_mode_frame,
            anchor="w",
            justify=LEFT,
            text="State: Default",
            highlightthickness=0,
            borderwidth=2,
            background=frame_color,
            foreground=main_font,
            font=font_10,
            width=25,
        )
        force_t_display.grid(row=5, column=4, sticky="ew", padx=5)

        reboot_button = ttk.Button(
            x_mode_frame,
            text="Reboot System",
            command=reboot_n,
            style="Custom.TButton"

        )
        reboot_button.grid(row=6, column=0, columnspan=3, sticky="ew", pady=5, padx=5)

        def install_zram():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"cd && wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/apps/More%20RAM/install | bash; exec bash\"'"
            )
            check_z_ram_button_state()
            done_msg()

        def uninstall_zram():
            os.system(
                f"x-terminal-emulator -e 'bash -c \"cd && wget -qO- https://raw.githubusercontent.com/Botspot/pi-apps/master/apps/More%20RAM/uninstall | bash; exec bash\"'"
            )

            check_z_ram_button_state()
            done_msg()

        self.swap_frame = ttk.LabelFrame(
            self.ov_state_display_frame,
            text="Use Zram [More Ram]",
            padding=20
        )
        self.swap_frame.grid(column=0, row=1, pady=10,sticky="ew")

        zram_text = """Setup of ZRAM (compressed RAM) to enhance memory usage and performance. It disables existing swap services, loads the ZRAM kernel module, and creates a systemd service for ZRAM to run on startup.[Taken From Pi-Apps(BotSpot)]"""
        
        self.z_info = Label(
            self.swap_frame,
            text=zram_text,
            justify="left",
            anchor="w",
            wraplength=600,
        ).pack(padx=10, fill="x", expand=True)

        # Create a Button next to the Combobox
        self.zram_button = ttk.Button(
            self.swap_frame,
            style="Custom.TButton"

        )
        self.zram_button.pack(padx=10, pady=10, anchor="w", fill="x")

        def check_z_ram_button_state():
            if check_zram() is True:
                self.zram_button.config(text="Uninstall", command=uninstall_zram)
            else:
                self.zram_button.config(text="Install", command=install_zram)

        check_z_ram_button_state()

        def check_preload_button_state():
            if check_preload_state() == True:
                self.preload_button.config(
                    text="Uninstall Preload", command=uninstall_preload
                )
            if check_preload_state() == False:
                self.preload_button.config(
                    text="Install Preload", command=install_preload
                )

        def install_preload():
            command = f"x-terminal-emulator -e 'bash -c \"{permit} apt install preload; exec bash\"'"

            os.system(command)

        def uninstall_preload():
            command = f"x-terminal-emulator -e 'bash -c \"{permit} apt purge preload; exec bash\"'"

            os.system(command)

        preload_text = """Preload is a Linux tool designed to improve system responsiveness by predicting and preloading
frequently used dynamic libraries into memory, reducing application startup times.
It analyzes the user's behavior and optimizesresource utilization to enhance overall system performance."""

        self.preload_frame = ttk.LabelFrame(
            self.ov_state_display_frame,
            text="Preload",
            padding=20
        )
        self.preload_frame.grid(column=0, row=2,sticky="nesw")

        self.tu_info = ttk.Label(
            self.preload_frame,
            text=preload_text,
            justify="left",
            anchor="w",
        ).pack(padx=10, fill="x", expand=True)

        # Create a Button next to the Combobox
        self.preload_button = ttk.Button(
            self.preload_frame,
            style="Custom.TButton"
        )
        self.preload_button.pack(padx=10, pady=10, anchor="w",fill="x")

        def ov_display():
            with open("/proc/device-tree/model", "r") as model_file:
                # Read and print the model information
                global pi_model
                pi_model = model_file.read().strip()

            if "Raspberry Pi 5" in pi_model:
                self.tu_reset.config(state=DISABLED)
                tu_btn1.config(state=DISABLED)
                tu_btn2.config(state=DISABLED)
                tu_btn3.config(state=DISABLED)
                tu_btn4.config(state=DISABLED)
            else:
                with open(f"{config_path}") as f:
                    for line in f:
                        if not "#Pigro_Overclocking" in line:
                            tu_btn1.config(state=NORMAL)
                            tu_btn2.config(state=NORMAL)
                            tu_btn3.config(state=NORMAL)
                            tu_btn4.config(state=NORMAL)
                            break
            # Overclock Display Functions
            with open(f"{config_path}") as f:
                for line in f:
                    if "arm_freq=" in line:
                        # print(line)

                        arm_freq_set_button.config(
                            text="Reset",
                            image=self.toggle_on,
                            command=reset_arm_freq,
                        )
                        arm_freq_set_button.bind(
                            "<Enter>",
                            func=lambda e: arm_freq_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )

                        arm_f_display.config(text=f"State: {line[9:-1]} MHz")
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)
                        break

                else:
                    arm_freq_set_button.config(
                        text="Set",
                        image=self.toggle_off,
                        command=set_arm_freq,
                    )
                    arm_f_display.config(text="State: Default")
                    arm_freq_set_button.bind(
                        "<Enter>",
                        func=lambda e: arm_freq_set_button.config(
                            image=self.toggle_off_enter
                        ),
                    )

            with open(f"{config_path}") as f:
                for line in f:
                    if "gpu_freq=" in line:
                        gpu_freq_set_button.config(
                            text="Reset",
                            background=maincolor,
                            image=self.toggle_on,
                            command=reset_gpu_freq,
                        )
                        gpu_freq_set_button.bind(
                            "<Enter>",
                            func=lambda e: gpu_freq_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )
                        gpu_f_display.config(
                            text=f"State: {line[9:-1]} MHz",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)
                        break
                else:
                    gpu_freq_set_button.config(
                        text="Set",
                        background=maincolor,
                        image=self.toggle_off,
                        command=set_gpu_freq,
                    )
                    gpu_freq_set_button.bind(
                        "<Enter>",
                        func=lambda e: gpu_freq_set_button.config(
                            image=self.toggle_off_enter
                        ),
                    )
                    gpu_f_display.config(text="State: Default")

            with open(f"{config_path}") as f:
                for line in f:
                    if "gpu_mem=" in line:
                        gpu_mem_set_button.config(
                            text="Reset",
                            background=maincolor,
                            image=self.toggle_on,
                            command=reset_gpu_mem,
                        )
                        gpu_mem_set_button.bind(
                            "<Enter>",
                            func=lambda e: gpu_mem_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )
                        if "gpu_mem" in line:
                            gpu_m_display.config(
                                text=f"State: {line[8:-1]} MB",
                            )
                        break
                else:
                    gpu_mem_set_button.config(
                        text="Set",
                        background=maincolor,
                        image=self.toggle_off,
                        command=set_gpu_mem,
                    )
                    gpu_mem_set_button.bind(
                        "<Enter>",
                        func=lambda e: gpu_mem_set_button.config(
                            image=self.toggle_off_enter
                        ),
                    )
                    gpu_m_display.config(text="State: Default")

            with open(f"{config_path}") as f:
                for line in f:
                    if "over_voltage=" in line:
                        over_voltage_set_button.config(
                            text="Reset",
                            background=maincolor,
                            image=self.toggle_on,
                            command=reset_over_voltage,
                        )
                        over_voltage_set_button.bind(
                            "<Enter>",
                            func=lambda e: over_voltage_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )
                        over_v_display.config(
                            text=f"State: {line[13:-1]}",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)
                        break
                else:
                    over_voltage_set_button.config(
                        text="Set",
                        background=maincolor,
                        image=self.toggle_off,
                        command=set_over_voltage,
                    )
                    over_voltage_set_button.bind(
                        "<Enter>",
                        func=lambda e: over_voltage_set_button.config(
                            image=self.toggle_off_enter
                        ),
                    )
                    over_v_display.config(text="State: Default")

            with open(f"{config_path}") as f:
                for line in f:
                    if "over_voltage_delta=" in line:
                        over_voltage_delta_set_button.config(
                            text="Reset",
                            background=maincolor,
                            image=self.toggle_on,
                            command=reset_over_voltage_delta,
                        )
                        over_voltage_delta_set_button.bind(
                            "<Enter>",
                            func=lambda e: over_voltage_delta_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )
                        over_v_d_display.config(
                            text=f"State: {line[19:-1]}",
                        )
                        break
                else:
                    if "Raspberry Pi 4" in pi_model:
                        over_voltage_delta_set_button.config(state="disabled")
                        over_v_d_display.config(text="Pi 5 Only")
                    else:
                        over_v_d_display.config(text="State: Default")
                        over_voltage_delta_set_button.bind(
                            "<Enter>",
                            func=lambda e: over_voltage_delta_set_button.config(
                                image=self.toggle_off_enter
                            ),
                        )
                        over_voltage_delta_set_button.config(
                            text="Set",
                            background=maincolor,
                            image=self.toggle_off,
                            command=set_over_voltage_delta,
                        )
            with open(f"{config_path}") as f:
                for line in f:
                    if "force_turbo=" in line:
                        force_turbo_set_button.config(
                            text="Reset",
                            background=maincolor,
                            image=self.toggle_on,
                            command=reset_force_turbo,
                        )
                        force_turbo_set_button.bind(
                            "<Enter>",
                            func=lambda e: force_turbo_set_button.config(
                                image=self.toggle_on_enter
                            ),
                        )
                        force_turbo_label.config(text="ENABLED")
                        force_t_display.config(
                            text=f"State: {line[12:-1]}",
                        )
                        tu_btn1.config(state=DISABLED)
                        tu_btn2.config(state=DISABLED)
                        tu_btn3.config(state=DISABLED)
                        tu_btn4.config(state=DISABLED)
                        break
                else:
                    force_turbo_set_button.config(
                        text="Set",
                        background=maincolor,
                        image=self.toggle_off,
                        command=set_force_turbo,
                    )
                    force_turbo_set_button.bind(
                        "<Enter>",
                        func=lambda e: force_turbo_set_button.config(
                            image=self.toggle_off_enter
                        ),
                    )
                    force_turbo_label.config(text="DISABLED")
            check_preload_button_state()

        def refresh_OV_stats():
            ov_display()
            self.after(1000, refresh_OV_stats)

        refresh_OV_stats()
