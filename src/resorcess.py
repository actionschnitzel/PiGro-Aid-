#!/usr/bin/python3

import os
from os import popen
from os import listdir
import os.path
from os.path import isfile, join
import distro
from pathlib import Path

# #global current_version
current_version = "23.02"

# Get User Name
# global user
user = os.environ["USER"]
print(f"[Info]: Hi,{user} waz uuuuup?!")


# Get Home Path
# global home
home = os.environ["HOME"]  # str(Path.home())
print(f"[Info]: {home} is your home directory!")

# set the directory autostart path
autostart_dir_path = f"{home}/.config/autostart/"

# check if the directory exists
if not os.path.exists(autostart_dir_path):
    # create the directory if it doesn't exist
    os.makedirs(autostart_dir_path)
    print(f"{autostart_dir_path} created successfully.")
else:
    print(f"{autostart_dir_path} already exists.")

# Gets path to PiGro
# global Application_path
Application_path = str(os.getcwd())
print(f"[Info]: PiGro directory is {Application_path}")


# Define paths to create
pigro_config_dir = f"{home}/.pigro"
pigro_config_file = f"{pigro_config_dir}/pigro.conf"

# Check if pigro directory exists
if not os.path.exists(pigro_config_dir):
    # Create pigro directory
    os.mkdir(pigro_config_dir)

    # Create pigro.conf file
    with open(pigro_config_file, 'w') as f:
        f.write("[PiGro - Just Click It! Configs]\n\n")
        f.write("first_run = true\n")
        f.write("theme = dark\n")
        f.write("perm = true\n")


# Check if Application_path is equal to f"{home}/PiGro-Aid-"
if Application_path == f"{home}/PiGro-Aid-":
    # Define path to scripts directory
    scripts_path = f"{Application_path}/scripts/"

    # Loop through all files in the scripts directory
    for filename in os.listdir(scripts_path):
        # Check if file extension is .sh
        if filename.endswith(".sh"):
            # Make file executable
            filepath = os.path.join(scripts_path, filename)
            os.chmod(filepath, 0o755)

# Check if perm var exsists
sudo_perm = open(f"{home}/.pigro/pigro.conf", "r")
read_sudo = sudo_perm.readlines()
sudo_perm.close()
found = False
for line in read_sudo:
    if str("perm = ") in line:
        found = True

if not found:
    sudo_perm = open(f"{home}/.pigro/pigro.conf", "a")
    sudo_perm.write(str("perm = true"))
    sudo_perm.close()

legit_check = open(f"{home}/.pigro/pigro.conf", "r")
read_check = legit_check.readlines()
legit_check.close()
for line in read_check:
    if str("perm = true") in line:
        # global legit
        legit = "pkexec"
    else:
        legit = "sudo"

# get Distro name
# global distro_get
distro_get = distro.id()
print("[Info]: Your Distro is: " + str(distro_get))


# Gets nice Distro name
# global nice_name
nice_name = popen("egrep '^(PRETTY_NAME)=' /etc/os-release")
nice_name = nice_name.read()


# Location of config.txt
# global config_path
if os.path.exists("/boot/config.txt"):
    config_path = "/boot/config.txt"
elif os.path.exists("/boot/firmware/usercfg.txt"):
    config_path = "/boot/firmware/usercfg.txt"
elif os.path.exists("/boot/firmware/config.txt"):
    config_path = "/boot/firmware/config.txt"
else:
    print("[Info]: Can't find config.txt")


# Get Desktop Environment
# global get_de
get_de = os.environ.get("XDG_CURRENT_DESKTOP")
print("[Info]: Your DE is: " + str(get_de))


# Checks if pi-apps is installed an imports the app list
open(f"{home}/.pigro/pi-apps_installed.list", "w").close()
# global piapps_path
piapps_path = os.path.exists(f"{home}/pi-apps")
if piapps_path == False:
    print("[Info]: Pi-Apps not found")
if piapps_path == True:
    print("[Info]: Pi-Apps is installed list will be added")
    # global pi_apps_installed_list
    pi_apps_installed_list = []
    for installed_pi_apps in os.listdir(f"{home}/pi-apps/data/status"):
        pi_apps_status = open(
            f"/home/{user}/pi-apps/data/status/{installed_pi_apps}", "r"
        )
        status = pi_apps_status.read()
        pi_apps_status.close()
        if status.strip() == "installed":
            pi_apps_installed_list.append(installed_pi_apps)


# Get Achitecture Of OS
arch_bash = """#determine if host system is 64 bit arm64 or 32 bit armhf
if [ "$(od -An -t x1 -j 4 -N 1 "$(readlink -f /sbin/init)")" = ' 02' ];then
arch=64
printf "arm64"
elif [ "$(od -An -t x1 -j 4 -N 1 "$(readlink -f /sbin/init)")" = ' 01' ];then
arch=32
printf "armhf"
else
error "Failed to detect OS CPU architecture! Something is very wrong."
fi"""

# #global os_arch_output
os_arch = popen(arch_bash)
os_arch_output = os_arch.read()


# Checks if flatpak exists

# global flatpak_path
flatpak_path = os.path.exists("/bin/flatpak")
if flatpak_path == True:
    print("[Info]: Flatpak is installed")
    # global flat_counted
    flat_count = popen("flatpak list | wc --lines")
    flat_counted = flat_count.read()
    flat_count.close()
    print(f"[Info]: {flat_counted[:-1]} Flatpaks are installed")
else:
    print("[Info]: Flatpak is not installed")
    flatpak_path = False


# Checks if pigro.conf exists
if os.path.isfile(f"{home}/.pigro/pigro.conf"):
    print("[Info]: pigro.conf exists")
else:
    print("[Info]: pigro.conf not found")
    with open(f"{home}/.pigro/pigro.conf", "a") as pigro_config_f:
        pigro_config_f.write(
            "[PiGro - Just Click It! Configs]\n\nfirst_run = true\ntheme = dark"
        )
        print("[Info]: pigro.conf was created")


# Counts installed .DEBs
deb_count = popen("dpkg --list | wc --lines")
# global deb_counted
deb_counted = deb_count.read()
deb_count.close()
print(f"[Info]: {deb_counted[:-1]} .deb Packages Installed")


# Color Theme Identifier
conf_file = open(f"{home}/.pigro/pigro.conf", "r")
read_conf = conf_file.readlines()
conf_file.close()


for line in read_conf:
    # Dark Theme Settings
    if str("theme = dark") in line:
        print("[Info]: Dark Theme")
        # global maincolor
        maincolor = "#404040"
        # global nav_color
        nav_color = "#2b2b2b"
        # global frame_color
        frame_color = "#383838"
        # global main_font
        main_font = "white"
        # global info_color
        info_color = "yellow"
        # global ext_btn
        ext_btn = "#007acc"
        # global label_frame_color
        label_frame_color = "#d4244d"
        if distro_get == "ubuntu":
            maincolor = "#333333"
            nav_color = "#272727"
            frame_color = "#333333"
            main_font = "white"
            info_color = "yellow"
            ext_btn = "#333333"

    # Light Theme Settings
    if str("theme = light") in line:
        print("[Info]: Light Theme")
        maincolor = "#f5f5f5"
        nav_color = "#e8e8e8"
        frame_color = "#f5f5f5"
        main_font = "black"
        info_color = "#0075b7"
        ext_btn = "#c5c5c5"
        label_frame_color = "#0075b7"
        if distro_get == "ubuntu":
            maincolor = "#fafafa"
            nav_color = "#ffffff"
            frame_color = "#fafafa"
            main_font = "black"
            info_color = "#0075b7"
            ext_btn = "#fafafa"

# Font Definition Vars
# global font_20
font_20 = ("Sans", 20)
# global font_16
font_16 = ("Sans", 16)
# global font_14
font_14 = ("Sans", 14)
# global font_12_b
font_12_b = ("Sans", 12, "bold")
# global font_12
font_12 = ("Sans", 12)
# global font_10
font_10 = ("Sans", 10)
# global font_10_b
font_10_b = ("Sans", 10, "bold")
# global font_9_b
font_9_b = ("Sans", 9, "bold")
# global font_9
font_9 = ("Sans", 9)
# global font_8_b
font_8_b = ("Sans", 8, "bold")
# global font_8
font_8 = ("Sans", 8)
