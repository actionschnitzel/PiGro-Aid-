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

        self.dash_pigro_logo_frame = ttk.Frame(
            self,
        )

        self.dash_pigro_logo_frame.pack(fill=BOTH)

        # Sys Info Labels
        self.logo_btn = Button(
            self.dash_pigro_logo_frame,
            borderwidth=0,
            highlightthickness=0,
            command=pigro_sound,
            activebackground="#ffffff",
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
        self.usage_frame = ttk.LabelFrame(
            self,
            text="System Usage",
        )
        self.usage_frame.pack(fill=BOTH, pady=20, padx=60)

        # Create a frame to hold the progress bars
        self.useage_container = ttk.Frame(
            self.usage_frame,
        )

        self.useage_container.pack(fill=BOTH, expand=True)

        # Create a label and progress bar for CPU usage
        cpu_label = tk.Label(
            self.useage_container,
            text="CPU",
            font=font_12,
        )
        cpu_label.grid(row=1, column=0, sticky="nsew")

        self.cpu_percent = tk.Label(
            self.useage_container,
            text="0%",
            font=font_20,
        )
        self.cpu_percent.grid(row=0, column=0, sticky="nsew")

        # Create a label and progress bar for CPU usage
        cpu_temp_label = tk.Label(
            self.useage_container,
            text="CPU Temp",
            font=font_12,
        )
        cpu_temp_label.grid(row=1, column=1, sticky="nsew")

        self.cpu_temp_percent = tk.Label(
            self.useage_container,
            text="0%",
            font=font_20,
        )
        self.cpu_temp_percent.grid(row=0, column=1, sticky="nsew")

        # Create a label and progress bar for RAM usage
        ram_label = tk.Label(
            self.useage_container,
            text="RAM",
            font=font_12,
        )
        ram_label.grid(row=1, column=2, sticky="nsew")

        self.ram_percent = Label(
            self.useage_container,
            text="0%",
            font=font_20,
        )
        self.ram_percent.grid(row=0, column=2, sticky="nsew")

        # Create a label and progress bar for HDD usage
        hdd_label = tk.Label(
            self.useage_container,
            text="HDD",
            font=font_12,
        )
        hdd_label.grid(row=1, column=3, sticky="nsew")

        self.hdd_percent = tk.Label(
            self.useage_container,
            text="0%",
            font=font_20,
        )
        self.hdd_percent.grid(row=0, column=3, sticky="nsew")

        # Konfiguriere jede Spalte so, dass sie expandiert
        self.useage_container.grid_columnconfigure(0, weight=1)
        self.useage_container.grid_columnconfigure(1, weight=1)
        self.useage_container.grid_columnconfigure(2, weight=1)
        self.useage_container.grid_columnconfigure(3, weight=1)

        self.useage_container.grid_rowconfigure(0, weight=0)
        self.useage_container.grid_rowconfigure(1, weight=0)

        self.os_info_frame = ttk.LabelFrame(
            self,
            text=pi_model,
            padding=20,
        )

        self.os_info_frame.pack(pady=20, fill="x", padx=60)

        self.info_frame_container = Frame(
            self.os_info_frame,
        )

        self.info_frame_container.pack(fill="x", expand=TRUE, anchor="n")

        self.info_frame_container.grid_columnconfigure(0, weight=1)
        self.info_frame_container.grid_columnconfigure(1, weight=1)
        self.info_frame_container.grid_columnconfigure(2, weight=1)
        self.info_frame_container.grid_columnconfigure(3, weight=1)

        self.info_frame_container.grid_rowconfigure(0, weight=0)
        self.info_frame_container.grid_rowconfigure(1, weight=0)

        # CPU Info Frame & Labels
        self.cpu_info_frame = ttk.LabelFrame(self.info_frame_container, text="Cpu Info")
        self.cpu_info_frame.grid(column=0, row=0, sticky="nesw")

        self.cpu_model_label = tk.Label(self.cpu_info_frame, text="Model:")
        self.cpu_model_label.pack(anchor="w", padx=10)

        self.cpu_max_label = tk.Label(self.cpu_info_frame, text="Max:")
        self.cpu_max_label.pack(anchor="w", padx=10)

        self.cpu_current_label = tk.Label(self.cpu_info_frame, text="Current:")
        self.cpu_current_label.pack(anchor="w", padx=10)

        self.cpu_min_label = tk.Label(self.cpu_info_frame, text="Min:")
        self.cpu_min_label.pack(anchor="w", padx=10)

        # OS Info Frame & Labels
        self.os_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Operating System",
        )
        self.os_label_frame.grid(
            column=0, row=1, rowspan=2, sticky="nesw"
        )  

        self.distro_label = tk.Label(self.os_label_frame, text="Distro:")
        self.distro_label.pack(anchor="w", padx=10)

        self.architecture_label = tk.Label(self.os_label_frame, text="Architecture:")
        self.architecture_label.pack(anchor="w", padx=10)

        self.kernel_label = tk.Label(self.os_label_frame, text="Kernel:")
        self.kernel_label.pack(anchor="w", padx=10)

        self.shell_label = tk.Label(self.os_label_frame, text="Shell:")
        self.shell_label.pack(anchor="w", padx=10)

        self.desktop_label = tk.Label(self.os_label_frame, text="Desktop:")
        self.desktop_label.pack(anchor="w", padx=10)

        self.window_manager_label = tk.Label(
            self.os_label_frame, text="Window Manager:"
        )
        self.window_manager_label.pack(anchor="w", padx=10)

        self.session_label = tk.Label(self.os_label_frame, text="Session:")
        self.session_label.pack(anchor="w", padx=10)

        self.resolution_label = tk.Label(self.os_label_frame, text="Resolution:")
        self.resolution_label.pack(anchor="w", padx=10)

        self.user_label = tk.Label(self.os_label_frame, text="User:")
        self.user_label.pack(anchor="w", padx=10)

        self.info_frame_column_2 = Frame(
            self.info_frame_container,
        )


        self.mem_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Memory",
        )
        self.mem_label_frame.grid(column=1, row=2, sticky="nesw", padx=5)

        self.ram_total_label = tk.Label(self.mem_label_frame, text="Ram Total:")
        self.ram_total_label.pack(anchor="w", padx=10)

        self.ram_available_label = tk.Label(self.mem_label_frame, text="Ram Available:")
        self.ram_available_label.pack(anchor="w", padx=10)

        self.ram_used_label = tk.Label(self.mem_label_frame, text="Ram Used:")
        self.ram_used_label.pack(anchor="w", padx=10)

        self.swap_total_label = tk.Label(self.mem_label_frame, text="Swap Total:")
        self.swap_total_label.pack(anchor="w", padx=10)

        self.swap_free_label = tk.Label(self.mem_label_frame, text="Swap Free:")
        self.swap_free_label.pack(anchor="w", padx=10)

        self.swap_used_label = tk.Label(self.mem_label_frame, text="Swap Used:")
        self.swap_used_label.pack(anchor="w", padx=10)

        self.net_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Network",
        )
        self.net_label_frame.grid(column=1, row=0, sticky="nesw", padx=5)

        self.hostname_label = tk.Label(self.net_label_frame, text="Hostname:")
        self.hostname_label.pack(anchor="w", padx=10)

        self.ip_label = tk.Label(self.net_label_frame, text="IP:")
        self.ip_label.pack(anchor="w", padx=10)

        self.web_label = tk.Label(self.net_label_frame, text="Web:")
        self.web_label.pack(anchor="w", padx=10)

        self.down_label = tk.Label(self.net_label_frame, text="Down:")
        self.down_label.pack(anchor="w", padx=10)

        self.up_label = tk.Label(self.net_label_frame, text="Up:")
        self.up_label.pack(anchor="w", padx=10)

        self.disk_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Disk",
        )
        self.disk_label_frame.grid(column=1, row=1, sticky="nesw", padx=5)

        self.total_size_label = tk.Label(self.disk_label_frame, text="Total Size:")
        self.total_size_label.pack(anchor="w", padx=10)

        self.used_label = tk.Label(self.disk_label_frame, text="Used:")
        self.used_label.pack(anchor="w", padx=10)

        self.free_label = tk.Label(self.disk_label_frame, text="Free:")
        self.free_label.pack(anchor="w", padx=10)

        self.pakage_count_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Packages Installed",
        )
        self.pakage_count_label_frame.grid(column=2, columnspan=2, row=0, sticky="nesw")

        self.debian_label = tk.Label(self.pakage_count_label_frame, text="Debian:")
        self.debian_label.pack(anchor="w", padx=10)

        self.flatpak_label = tk.Label(self.pakage_count_label_frame, text="Flatpak:")
        self.flatpak_label.pack(anchor="w", padx=10)

        self.snap_label = tk.Label(self.pakage_count_label_frame, text="Snap:")
        self.snap_label.pack(anchor="w", padx=10)

        self.distro_label_frame = ttk.LabelFrame(
            self.info_frame_container,
            text="Distro Logo",
        )
        self.distro_label_frame.grid(
            column=2, columnspan=2, row=1, rowspan=2, sticky="nesw"
        )  

        self.distro_logo_label = Label(
            self.distro_label_frame,
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
        # Screen dimensions
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # System information
        my_system = platform.uname()
        cpufreq = psutil.cpu_freq()
        swap = psutil.swap_memory()
        get_shell = os.environ["SHELL"]
        get_xdg_session = os.environ["XDG_SESSION_TYPE"]

        # CPU temperature retrieval
        cpu_temp = self.get_cpu_temperature()

        # Resource usage
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent
        hdd_usage = psutil.disk_usage("/").percent
        svmem = psutil.virtual_memory()

        # Update labels for CPU and memory
        self.update_cpu_labels(cpu_usage, cpu_temp, cpufreq)
        self.update_memory_labels(svmem, swap)

        # Network information
        lan_ip, down_rate, up_rate, web_state = self.get_network_info()

        # System hostname and IP
        self.hostname = socket.gethostname()
        self.IPAddr = socket.gethostbyname(self.hostname)
        self.hostname_label.configure(text=f"Hostname: {self.hostname}")
        self.ip_label.configure(text=f"IP: {lan_ip}")
        self.web_label.configure(text=f"Web: {web_state}")
        self.down_label.configure(text=f"Down: {down_rate} MB/s")
        self.up_label.configure(text=f"Up: {up_rate} MB/s")

        # Update OS information
        self.update_os_labels(my_system)

        # Update disk information
        self.update_disk_labels()

        # Update package information
        self.update_package_info()

        # Schedule the next update
        self.after(3000, self.update_labels)

    def get_cpu_temperature(self):
        """Get the CPU temperature."""
        try:
            cpu_temp = psutil.sensors_temperatures()
            return round(cpu_temp["cpu_thermal"][0][1])
        except:
            return "N/A"

    def update_cpu_labels(self, cpu_usage, cpu_temp, cpufreq):
        """Update CPU-related labels."""
        self.cpu_percent["text"] = f"{cpu_usage}%"
        self.cpu_temp_percent["text"] = f"{cpu_temp}°C"
        self.cpu_model_label.configure(text=f"Model: {self.get_cpu_model_name()}")
        self.cpu_max_label.configure(text=f"Max: {cpufreq.max:.0f} Mhz")
        self.cpu_current_label.configure(text=f"Current: {cpufreq.current:.0f} Mhz")
        self.cpu_min_label.configure(text=f"Min: {cpufreq.min:.0f} Mhz")

    def update_memory_labels(self, svmem, swap):
        """Update memory-related labels."""
        self.ram_percent["text"] = f"{svmem.percent}%"
        self.ram_total_label.configure(text=f"Ram Total: {self.get_size(svmem.total)}")
        self.ram_available_label.configure(text=f"Ram Available: {self.get_size(svmem.available)}")
        self.ram_used_label.configure(text=f"Ram Used: {self.get_size(svmem.used)}")
        self.swap_total_label.configure(text=f"Swap Total: {self.get_size(swap.total)}")
        self.swap_free_label.configure(text=f"Swap Free: {self.get_size(swap.free)}")
        self.swap_used_label.configure(text=f"Swap Used: {self.get_size(swap.used)}")

    def update_disk_labels(self):
        """Update disk-related labels."""
        obj_Disk = psutil.disk_usage("/")
        hdd_usage = psutil.disk_usage("/").percent
        self.hdd_percent["text"] = f"{hdd_usage}%"
        self.total_size_label.configure(text=f"Total Size: {obj_Disk.total / (2**30):.2f} GB")
        self.used_label.configure(text=f"Used: {obj_Disk.used / (2**30):.2f} GB")
        self.free_label.configure(text=f"Free: {obj_Disk.free / (2**30):.2f} GB")
        
        
    def get_network_info(self):
        """Get network-related information."""
        try:
            local_ip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            local_ip.connect(("8.8.8.8", 80))
            lan_ip = local_ip.getsockname()[0]
            net_io_counters = psutil.net_io_counters()
            down_rate = round(net_io_counters.bytes_recv / 1024 / 1024, 2)
            up_rate = round(net_io_counters.bytes_sent / 1024 / 1024, 2)
            web_state = "Connected"
        except (socket.error, socket.gaierror) as e:
            print(f"[Info] Failed to determine local IP address: {e}")
            lan_ip = None
            down_rate = "-"
            up_rate = "-"
            web_state = "Disconnected"

        return lan_ip, down_rate, up_rate, web_state

    def update_os_labels(self, my_system):
        """Update OS-related labels."""
        self.distro_label.configure(text=f"Distro: {nice_name[13:-2]}")
        self.architecture_label.configure(text=f"Architecture: {os_arch_output}")
        self.kernel_label.configure(text=f"Kernel: {my_system.release}")
        self.shell_label.configure(text=f"Shell: {os.environ['SHELL']}")
        self.desktop_label.configure(text=f"Desktop: {get_desktop_environment()}")
        self.window_manager_label.configure(text=f"Window Manager: {self.get_window_manager()}")
        self.session_label.configure(text=f"Session: {os.environ['XDG_SESSION_TYPE']}")
        self.resolution_label.configure(text=f"Resolution: {self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.user_label.configure(text=f"User: {user}")

    def update_package_info(self):
        """Update package-related information."""
        self.debian_label.configure(text=f"Debian: {deb_counted[:-1]}")
        self.flatpak_label.configure(text=f"Flatpak: {count_flatpaks()}")
        self.snap_label.configure(text=f"Snap: {snap_package_count}")

    def get_size(self, bytes, suffix="B"):
        """Scale bytes to its proper format."""
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    def get_cpu_model_name(self):
        """Get the CPU model name."""
        command = "lscpu | grep -E 'Model name|Modellname' | awk -F ': ' '{gsub(/^[ \t]+|[ \t]+$/, \"\", $2); print $2}'"
        try:
            output = subprocess.check_output(command, shell=True, universal_newlines=True)
            return output.strip()
        except subprocess.CalledProcessError:
            return "N/A"

    def get_window_manager(self):
        """Get the name of the window manager."""
        try:
            result = subprocess.run(
                ["wmctrl", "-m"], capture_output=True, text=True, check=True
            )
            output_lines = result.stdout.strip().split("\n")
            for line in output_lines:
                if line.startswith("Name: "):
                    return line.split("Name: ")[1]
        except subprocess.CalledProcessError as e:
            print(f"Error running wmctrl: {e}")
        
        return None
