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
