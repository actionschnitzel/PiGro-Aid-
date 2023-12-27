import os
from os import popen
import os.path
from tkinter import *
from tkinter import ttk
import tkinter as tk
import platform
import psutil
from time import strftime
import socket
from PIL import ImageTk, Image
from resorcess import *
from apt_manage import *
from snap_manage import *
from flatpak_manage import count_flatpaks
from flatpak_alias_list import *
from tabs.pop_ups import *
from tool_tipps import CreateToolTip


class DashTab(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)

        current_month = strftime("%B")

        def pigro_sound():
            popen(
                f"mpg123 {application_path}/scripts/PiGro-just_click_it.mp3 >/dev/null 2>&1"
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

        self.distro_ubuntu_logo_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/ubuntu_logo_dash.png")
        )

        self.distro_pi_logo_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/rpi_logo_dash.png")
        )

        self.distro_debian_logo_img = ImageTk.PhotoImage(
            Image.open(f"{application_path}/images/icons/debian_logo_dash.png")
        )

        self.dash_pigro_logo_frame = Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.dash_pigro_logo_frame.pack()
        self.dash_pigro_logo_frame["background"] = maincolor

        # Sys Info Labels
        self.logo_btn = Button(
            self.dash_pigro_logo_frame,
            borderwidth=0,
            bg=frame_color,
            highlightthickness=0,
            command=pigro_sound,
            activebackground=frame_color,
        )
        self.logo_btn.pack(pady=20)
        self.logo_btn_ttp = CreateToolTip(
            self.logo_btn,
            "\n\nEverything is a button if you are brave enough!\n\n",
        )

        # Changes Header
        if current_month == "October":
            self.logo_btn.config(image=self.pigroh_img)
        elif current_month == "December":
            self.logo_btn.config(image=self.pigrox_img)
        elif current_month == "February":
            self.logo_btn.config(image=self.pigro_feb_img)
        else:
            self.logo_btn.config(image=self.pigro_img)

        # Open the /proc/device-tree/model file for reading
        try:
            with open("/proc/device-tree/model", "r") as model_file:
                # Read and print the model information
                global pi_model
                pi_model = model_file.read().strip()
                print(f"[Info] Raspberry Pi Model: {pi_model}")

        except FileNotFoundError:
            print(
                "The /proc/device-tree/model file does not exist. Are you running this on a Raspberry Pi?"
            )
            pi_model = "DEV MODE"
        except Exception as e:
            print("An error occurred:", str(e))

        # Create a frame to hold the progress bars
        self.usage_frame = tk.Frame(
            self,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=20,
            padx=10,
            width=885,
            height=100,
        )

        self.usage_frame.pack(pady=20)
        self.usage_frame.pack_propagate(0)
        self.usage_frame["background"] = frame_color

        # Create a frame to hold the progress bars
        self.useage_container = tk.Frame(
            self.usage_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.useage_container.pack()
        self.useage_container["background"] = frame_color

        # Create a label and progress bar for CPU usage
        cpu_label = Label(
            self.useage_container,
            text="CPU",
            font=font_12,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=label_frame_color,
            width=20,
        )
        cpu_label.grid(row=1, column=0)

        self.cpu_percent = Label(
            self.useage_container,
            text="0%",
            font=font_20,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
        )
        self.cpu_percent.grid(row=0, column=0)

        # Create a label and progress bar for CPU usage
        cpu_temp_label = Label(
            self.useage_container,
            text="CPU Temp",
            font=font_12,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=label_frame_color,
            width=20,
        )
        cpu_temp_label.grid(row=1, column=1)

        self.cpu_temp_percent = Label(
            self.useage_container,
            text="0%",
            font=font_20,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
        )
        self.cpu_temp_percent.grid(row=0, column=1)

        # Create a label and progress bar for RAM usage
        ram_label = Label(
            self.useage_container,
            text="RAM",
            font=font_12,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=label_frame_color,
            width=20,
        )
        ram_label.grid(row=1, column=2)

        self.ram_percent = Label(
            self.useage_container,
            text="0%",
            font=font_20,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
        )
        self.ram_percent.grid(row=0, column=2)

        # Create a label and progress bar for HDD usage
        hdd_label = Label(
            self.useage_container,
            text="HDD",
            font=font_12,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=label_frame_color,
            width=20,
        )
        hdd_label.grid(row=1, column=3)

        self.hdd_percent = Label(
            self.useage_container,
            text="0%",
            font=font_20,
            highlightthickness=0,
            borderwidth=0,
            background=frame_color,
            foreground=main_font,
        )
        self.hdd_percent.grid(row=0, column=3)

        self.os_info_frame = LabelFrame(
            self,
            text=pi_model,
            font=font_20,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
            pady=20,
            padx=20,
            width=885,
            height=600,
        )

        self.os_info_frame.pack(pady=20)
        self.os_info_frame.pack_propagate(0)
        self.os_info_frame["background"] = frame_color

        self.info_frame_column_1 = Frame(
            self.os_info_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.info_frame_column_1.pack(side=LEFT, fill="both", expand=True)
        self.info_frame_column_1["background"] = frame_color

        self.os_label_frame = LabelFrame(
            self.info_frame_column_1,
            text="Operating System",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.os_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.os_label_frame["background"] = frame_color

        self.os_info_list = [
            "Distro:",
            "Architecture:",
            "Kernel:",
            "Shell:",
            "Desktop:",
            "Window Manager:",
            "Session:",
            "Resolution:",
            "User:",
        ]

        self.os_labels = []

        for os_info in self.os_info_list:
            label = tk.Label(self.os_label_frame, text=os_info)
            label.pack(anchor="w", padx=10)
            self.os_labels.append(label)

        self.rp_label_frame = LabelFrame(
            self.info_frame_column_1,
            text="Raspberry Pi",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.rp_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.rp_label_frame["background"] = frame_color

        self.rp_info_list = [
            "Board:",
            "Arm Model:",
            "Cpu Freq Max.:",
            "Cpu Freq Current:",
            "Cpu Freq Min.:",
        ]

        self.rp_labels = []

        for rp_info in self.rp_info_list:
            label = tk.Label(self.rp_label_frame, text=rp_info)
            label.pack(anchor="w", padx=10)
            self.rp_labels.append(label)

        self.info_frame_column_2 = Frame(
            self.os_info_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.info_frame_column_2.pack(side=LEFT, fill="both", expand=True)
        self.info_frame_column_2["background"] = frame_color

        self.mem_label_frame = LabelFrame(
            self.info_frame_column_2,
            text="Memory",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.mem_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.mem_label_frame["background"] = frame_color

        self.mem_list = [
            "Ram Total:",
            "Ram Available:",
            "Ram Used:",
            "Swap Total:",
            "Swap Free:",
            "Swap Used:",
        ]

        self.mem_labels = []

        for mem_info in self.mem_list:
            label = tk.Label(self.mem_label_frame, text=mem_info)
            label.pack(anchor="w", padx=10)
            self.mem_labels.append(label)

        self.net_label_frame = LabelFrame(
            self.info_frame_column_2,
            text="Network",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.net_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.net_label_frame["background"] = frame_color

        self.net_list = ["Hostname:", "IP:", "Web:", "Down:", "Up:"]

        self.net_labels = []

        for net_info in self.net_list:
            label = tk.Label(self.net_label_frame, text=net_info)
            label.pack(anchor="w", padx=10)
            self.net_labels.append(label)

        self.info_frame_column_0 = Frame(
            self.os_info_frame,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor=label_frame_color,
            relief=GROOVE,
        )

        self.info_frame_column_0.pack(side=LEFT, fill="both", expand=True)
        self.info_frame_column_0["background"] = frame_color

        self.disk_label_frame = LabelFrame(
            self.info_frame_column_0,
            text="Disk",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.disk_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.disk_label_frame["background"] = frame_color

        self.disk_list = [
            "Total Size:",
            "Used:",
            "Free:",
        ]

        self.disk_labels = []

        for disk_info in self.disk_list:
            label = tk.Label(self.disk_label_frame, text=disk_info)
            label.pack(anchor="w", padx=10)
            self.disk_labels.append(label)

        self.pakage_count_label_frame = LabelFrame(
            self.info_frame_column_0,
            text="Packages Installed",
            font=font_16,
            foreground=label_frame_color,
            borderwidth=0,
            highlightthickness=0,
            highlightcolor="white",
            relief=GROOVE,
        )
        self.pakage_count_label_frame.pack(anchor="n", fill=BOTH, expand=True)
        self.pakage_count_label_frame["background"] = frame_color

        self.pakage_count_list = ["Debian:", "Flatpak:", "Snap:"]

        self.pakage_count_labels = []

        for pakage_count_info in self.pakage_count_list:
            label = tk.Label(self.pakage_count_label_frame, text=pakage_count_info)
            label.pack(anchor="w", padx=10)
            self.pakage_count_labels.append(label)

        self.distro_logo_label = Label(
            self.info_frame_column_0,
            borderwidth=0,
            bg=frame_color,
            highlightthickness=0,
            image=self.distro_ubuntu_logo_img,
        )
        self.distro_logo_label.pack(fill=BOTH, expand=True)

        if "Ubuntu" in nice_name:
            self.distro_logo_label.config(image=self.distro_ubuntu_logo_img)
        elif get_desktop_environment() == "lxde-pi-wayfire" or "lxde-pi" or "lxde":
            self.distro_logo_label.config(image=self.distro_pi_logo_img)
        else:
            self.distro_logo_label.config(image=self.distro_debian_logo_img)

        self.update_labels()

    def update_labels(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        my_system = platform.uname()
        cpufreq = psutil.cpu_freq()
        obj_Disk = psutil.disk_usage("/")
        cpufreq = psutil.cpu_freq()
        swap = psutil.swap_memory()
        get_shell = os.environ["SHELL"]
        get_xdg_session = os.environ["XDG_SESSION_TYPE"]
        try:
            cpu_temp = psutil.sensors_temperatures()
            cpu_temp = round(cpu_temp["cpu_thermal"][0][1])
        except:
            cpu_temp = "N/A"

        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        hdd_usage = psutil.disk_usage("/").percent

        svmem = psutil.virtual_memory()

        self.cpu_percent["text"] = f"{cpu_usage}%"
        self.cpu_temp_percent["text"] = f"{cpu_temp}°C"
        self.ram_percent["text"] = f"{ram_usage}%"
        self.hdd_percent["text"] = f"{hdd_usage}%"

        self.hostname = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.hostname)

        try:
            self.local_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.local_ip.connect(("8.8.8.8", 80))
            lan_ip = self.local_ip.getsockname()[0]
            net_io_counters = psutil.net_io_counters()
            down_rate = round(net_io_counters.bytes_recv / 1024 / 1024, 2)
            up_rate = round(net_io_counters.bytes_sent / 1024 / 1024, 2)
            web_state = "Connected"
        except (socket.error, socket.gaierror) as e:
            # Handle the exception or log an error message
            print(f"[Info] Failed to determine local IP address: {e}")
            web_state = "Disconnected"
            lan_ip = None
            down_rate = "-"
            up_rate = "-"

        def get_size(bytes, suffix="B"):
            """
            Scale bytes to its proper format
            e.g:
                1253656 => '1.20MB'
                1253656678 => '1.17GB'
            """
            factor = 1024
            for unit in ["", "K", "M", "G", "T", "P"]:
                if bytes < factor:
                    return f"{bytes:.2f}{unit}{suffix}"
                bytes /= factor

        def get_cpu_model_name():
            command = "lscpu | grep -E 'Model name|Modellname' | awk -F ': ' '{gsub(/^[ \t]+|[ \t]+$/, \"\", $2); print $2}'"

            try:
                output = subprocess.check_output(
                    command, shell=True, universal_newlines=True
                )
                return output.strip()
            except subprocess.CalledProcessError:
                return "N/A"

        def get_window_manager_name():
            try:
                result = subprocess.run(
                    ["wmctrl", "-m"], capture_output=True, text=True, check=True
                )

                output_lines = result.stdout.strip().split("\n")
                for line in output_lines:
                    if line.startswith("Name: "):
                        window_manager_name = line.split("Name: ")[1]
                        return window_manager_name
            except subprocess.CalledProcessError as e:
                print(f"Error running wmctrl: {e}")

            return None

        # Simulate updating the labels with new information (replace with actual data retrieval)
        update_os_info_data = [
            f"{nice_name[13:-2]}",
            f"{os_arch_output}",
            f"{my_system.release}",
            f"{get_shell}",
            f"{get_desktop_environment()}",
            f"{get_window_manager_name()}",
            f"{get_xdg_session}",
            f"{screen_width}x{screen_height}",
            f"{user}",
        ]

        for label, new_os_info in zip(self.os_labels, update_os_info_data):
            label.config(
                text=self.os_info_list[self.os_labels.index(label)] + " " + new_os_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )

        update_rp_info_data = [
            f"{pi_model}",
            f"{get_cpu_model_name()}",
            f"{cpufreq.max:.0f} Mhz",
            f"{cpufreq.current:.0f} Mhz",
            f"{cpufreq.min:.0f} Mhz",
        ]

        for label, new_info in zip(self.rp_labels, update_rp_info_data):
            label.config(
                text=self.rp_info_list[self.rp_labels.index(label)] + " " + new_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )

        update_mem_info_data = [
            f"{get_size(svmem.total)}",
            f"{get_size(svmem.available)}",
            f"{get_size(svmem.used)}",
            f"{get_size(swap.total)}",
            f"{get_size(swap.free)}",
            f"{get_size(swap.used)}",
        ]

        for label, new_mem_info in zip(self.mem_labels, update_mem_info_data):
            label.config(
                text=self.mem_list[self.mem_labels.index(label)] + " " + new_mem_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )

        update_disk_info_data = [
            f"{obj_Disk.total / (2**30):.2f} GB",
            f"{obj_Disk.used / (2**30):.2f} GB",
            f"{obj_Disk.free / (2**30):.2f} GB",
        ]

        for label, new_disk_info in zip(self.disk_labels, update_disk_info_data):
            label.config(
                text=self.disk_list[self.disk_labels.index(label)]
                + " "
                + new_disk_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )

        update_net_info_data = [
            f"{self.hostname}",
            f"{lan_ip}",
            f"{web_state}",
            f"{down_rate} MB/s",
            f"{up_rate} MB/s",
        ]

        for label, new_net_info in zip(self.net_labels, update_net_info_data):
            label.config(
                text=self.net_list[self.net_labels.index(label)] + " " + new_net_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )
        self.local_ip.getsockname()[0]

        update_pakage_count_info_data = [
            f"{deb_counted[:-1]}",
            f"{count_flatpaks()}",
            f"{snap_package_count}",
        ]

        for label, new_pakage_count_info in zip(
            self.pakage_count_labels, update_pakage_count_info_data
        ):
            label.config(
                text=self.pakage_count_list[self.pakage_count_labels.index(label)]
                + " "
                + new_pakage_count_info,
                borderwidth=0,
                background=frame_color,
                foreground=main_font,
            )

        self.after(3000, self.update_labels)
