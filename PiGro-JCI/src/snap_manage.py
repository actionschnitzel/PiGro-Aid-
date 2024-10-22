import os
import subprocess


def is_snap_installed():
    return os.path.exists("/bin/snap")

 
def count_installed_snap_packages():
    try:
        output = subprocess.check_output(["snap", "list"]).decode("utf-8")
        packages = output.strip().split("\n")[1:]  # Skip the header line
        return len(packages)
    except subprocess.CalledProcessError:
        return -1


if is_snap_installed():
    snap_package_count = count_installed_snap_packages()
    if snap_package_count != -1:
        print(
            f"[Info] Snap is installed, and there are {snap_package_count} packages installed."
        )
    else:
        print("[Info] Failed to list installed packages using Snap.")
        snap_package_count = "-"
else:
    print("[Info] Snap is not installed on your system.")
    snap_package_count = "-"


import subprocess

def get_installed_snaps():
    command = "snap list"
    output = subprocess.check_output(command, shell=True, text=True)

    lines = output.strip().split("\n")

    lines = lines[1:]

    snap_names = []

    for line in lines:
        snap_name = line.split()[0]
        snap_names.append(snap_name)

    #print(snap_names)
    return snap_names

#get_installed_snaps()

