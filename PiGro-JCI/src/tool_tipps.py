#!/usr/bin/python3

import tkinter as tk


class CreateToolTip(object):
    """create a tooltip for a given widget"""

    def __init__(self, widget, text="widget info"):
        self.waittime = 500
        self.wraplength = 400
        self.widget = widget
        self.text = text
        self.widget.bind("<Enter>", self.enter)
        self.widget.bind("<Leave>", self.leave)
        self.widget.bind("<ButtonPress>", self.leave)
        self.id = None
        self.tw = None

    def enter(self, event=None):
        self.schedule()

    def leave(self, event=None):
        self.unschedule()
        self.hidetip()

    def schedule(self):
        self.unschedule()
        self.id = self.widget.after(self.waittime, self.showtip)

    def unschedule(self):
        id = self.id
        self.id = None
        if id:
            self.widget.after_cancel(id)

    def showtip(self, event=None):
        x = y = 0
        x, y, cx, cy = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 20
        # creates a toplevel window
        self.tw = tk.Toplevel(self.widget)
        # Leaves only the label and removes the app window
        self.tw.wm_overrideredirect(True)
        self.tw.wm_geometry("+%d+%d" % (x, y))
        label = tk.Label(
            self.tw,
            text=self.text,
            justify="left",
            background="#333333",
            foreground="white",
            relief="solid",
            borderwidth=1,
            wraplength=self.wraplength,
            padx=20,
            pady=20,
        )
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tw
        self.tw = None
        if tw:
            tw.destroy()


class TipsText:
    ttip_update = "apt update is a command in Debian-based Linux systems that refreshes the package list on your system by downloading information about available packages and their versions from the configured repositories. It ensures that your package manager has the latest information about software packages, allowing you to install or update them."

    ttip_upgrade = "The apt list --upgradeable command in Debian-based Linux systems provides a list of packages that have newer versions available for upgrade. It shows the packages that can be updated to a newer version, allowing users to see which software on their system has pending updates."

    ttip_fix_missing = "The apt install --fix-missing command in Debian-based Linux systems attempts to fix missing dependencies by downloading and installing any required packages that are not currently present on the system. This can be useful when there are broken dependencies preventing the successful installation of a package."

    ttip_fix_boken = "The apt --fix-broken install command in Debian-based Linux systems is used to fix broken dependencies by resolving any issues that might be preventing the successful installation or configuration of packages. It attempts to automatically correct and install any missing or broken dependencies for the packages that are in an inconsistent or broken state on the system."

    ttip_gdebi = "The gdebi-gtk command in Linux is used to install Debian (.deb) packages along with their dependencies. When you run gdebi-gtk followed by a file path, such as gdebi-gtk file.deb, it opens the graphical user interface of GDebi, a package installer. GDebi resolves and installs dependencies for the specified Debian package, providing a user-friendly way to handle installations outside of the package manager."

    ttip_autoremove = "The apt autoremove command in Debian-based Linux systems is used to remove packages that were automatically installed as dependencies for other packages but are no longer required. This helps to clean up the system by uninstalling orphaned packages, freeing up disk space and improving system efficiency."

    ttip_upgrade_list = "The apt list --upgradable command in Debian-based Linux systems is used to display a list of packages that have newer versions available for upgrade. It provides information about the packages that have updates ready to be installed, allowing you to see which software on your system can be updated to the latest versions."

    ttip_recon_a = "The dpkg --configure -a command in Debian-based Linux systems is used to configure any pending or partially configured packages on your system. This command is helpful when there are packages that were not properly configured during the initial installation or when an upgrade process was interrupted. Running this command attempts to configure all installed packages, ensuring that they are in a fully operational state."

    ttip_allow = "This Linux command updates the package lists and suppresses output, then identifies and fetches missing GPG keys for repositories to resolve NO_PUBKEY errors during the update process. It utilizes a loop to handle multiple keys, ensuring they are retrieved and added to the system."

    ttip_nala_update = "Which brings us to our next standout feature, nala fetch.This command works similar to how most people use netselect and netselect-apt.nala fetch will check if your distro is either Debian or Ubuntu.Nala will then go get all the mirrors from the respective master list.Once done we test the latency and score each mirror.Nala will choose the fastest 3 mirrors (configurable) and write them to a file."

    ttip_flatpak_update = "The flatpak update command is used to update all installed Flatpak applications on a Linux system. When executed, it checks for updates to the installed Flatpak packages and installs the latest versions available from the respective repositories. This command helps ensure that your Flatpak applications are running the most up-to-date versions with the latest features and security patches."

    ttip_flatpak_unused = "The flatpak uninstall --unused command is used to remove Flatpak runtimes and extensions that are no longer associated with any installed applications. When executed, it identifies and uninstalls runtime and extension packages that are not currently in use by any Flatpak applications, helping to free up disk space by removing components that are no longer needed."

    ttip_dmesg = "The sudo dmesg command in Linux displays the kernel ring buffer, providing a detailed log of system messages and events. By using sudo, the command is executed with elevated privileges, allowing access to system logs that might be restricted to regular users. This command is commonly used for troubleshooting hardware, device, and system-related issues, offering insights into the recent activities and events within the kernel."

    ttip_dmesg_follow = "The sudo dmesg --follow command in Linux is used to continuously display new kernel messages in real-time as they occur. The --follow option acts like a tail command, allowing you to monitor the kernel log dynamically. This can be useful for tracking system events, debugging hardware issues, or observing changes in real-time as they are logged by the kernel."

    ttip_crontab = "The crontab command in Linux is used to create, edit, and manage scheduled tasks, also known as cron jobs. By running crontab -e, you can open the crontab file for editing, allowing you to specify commands and their scheduling intervals. Each line in the crontab file represents a scheduled task, and the syntax for specifying the schedule is based on minute, hour, day of the month, month, and day of the week. This command is commonly used for automating repetitive tasks or scripts at specified times."
