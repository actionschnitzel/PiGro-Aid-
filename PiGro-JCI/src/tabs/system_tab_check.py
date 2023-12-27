import os


def check_file_exists(file_path):
    return os.path.exists(file_path)


def check_gnome_tweaks():
    return check_file_exists("/bin/gnome-tweaks")


def check_gnome_control_center():
    return check_file_exists("/bin/gnome-control-center")


def check_alacarte():
    return check_file_exists("/bin/alacarte")


def check_update_manager():
    return check_file_exists("/bin/update-manager")


def check_software_properties_gtk():
    return check_file_exists("/bin/software-properties-gtk")


def check_xfce4_settings_manager():
    return check_file_exists("/bin/xfce4-settings-manager")


def check_pcmanfm():
    return check_file_exists("/bin/pcmanfm")


def check_piclone():
    return check_file_exists("/bin/piclone")


def check_deskpi_config():
    return check_file_exists("/bin/deskpi-config")


def check_rp_prefapps():
    return check_file_exists("/bin/rp-prefapps")


def check_rc_gui():
    return check_file_exists("/bin/rc_gui")


def check_raspi_config():
    return check_file_exists("/bin/raspi-config")


def check_agnostics():
    return check_file_exists("/bin/agnostics")


def check_preload_state():
    return check_file_exists("/var/lib/preload/preload.state")


def check_dselect():
    return check_file_exists("/bin/dselect")


def check_dselect():
    return check_file_exists("/bin/dselect")


def check_papirus():
    return check_file_exists("/bin/papirus-folders")


def check_bookshelf():
    return check_file_exists("/bin/rp-bookshelf")


def check_pipanel():
    return check_file_exists("/bin/pipanel")


def check_zram():
    return check_file_exists("/bin/zram.sh")
