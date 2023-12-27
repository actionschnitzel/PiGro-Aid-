import os
import json
import subprocess
import socket
import platform

from resorcess import home


def count_flatpaks():
    if flatpak_path:
        flat_count = os.popen("flatpak list | wc --lines")
        flat_counted = flat_count.read()
        flat_count.close()
        flat_counted = flat_counted[:-1]
    else:
        flat_counted = "-"
    return flat_counted


def is_internet_available():
    try:
        host = socket.gethostbyname("www.github.com")
        socket.create_connection((host, 80), 2)
        return True
    except socket.error:
        pass
    return False


def refresh_flatpak_installs():
    command = "flatpak list --columns=name --columns=application --app"
    output = subprocess.check_output(command, shell=True, text=True)
    # print(output)

    lines = output.strip().split("\n")
    data = {}

    for line in lines:
        if not line.startswith("Name\tApplication"):
            split_values = line.split("\t")
            if len(split_values) == 2:
                name, application = split_values
                data[name] = application
            elif line.strip():
                print(f"Warnung: Unerwartetes Format in Zeile '{line}'")

    json_file_path = f"{home}/.pigro/flatpak_installed.json"
    expanded_json_file_path = os.path.expanduser(json_file_path)

    with open(expanded_json_file_path, "w") as json_file:
        json.dump(data, json_file, indent=2)

    with open(expanded_json_file_path, "r") as json_file:
        flat_uninstalled_dict = json.load(json_file)

    # print(flat_uninstalled_dict)
    return flat_uninstalled_dict


# Check ob Flatpak installiert ist
flatpak_path = os.path.exists("/bin/flatpak")


if flatpak_path:
    print("[Info] Flatpak is installed. List will be added")

    home = os.path.expanduser("~")
    json_file_path = f"{home}/.pigro/flat_remote_data.json"
    expanded_json_file_path = os.path.expanduser(json_file_path)

    if is_internet_available():
        command = f"flatpak remote-ls --columns=name --columns=application --app --arch={platform.machine()}"
        output = subprocess.check_output(command, shell=True, text=True)

        lines = output.strip().split("\n")
        flat_remote_data = {}

        for line in lines[1:]:
            name, application = line.split("\t")
            flat_remote_data[name] = application

        if os.path.exists(expanded_json_file_path):
            with open(expanded_json_file_path, "r") as json_file:
                flat_remote_dict = json.load(json_file)
        else:
            flat_remote_dict = {}

        flat_remote_dict.update(flat_remote_data)

        with open(expanded_json_file_path, "w") as json_file:
            json.dump(flat_remote_dict, json_file, indent=2)

        Flat_remote_dict = flat_remote_dict
        print(f"Added Flatpak cache.")
    else:
        if os.path.exists(expanded_json_file_path):
            with open(expanded_json_file_path, "r") as json_file:
                Flat_remote_dict = json.load(json_file)
        else:
            Flat_remote_dict = {}

    refresh_flatpak_installs()
else:
    print("[Info] Flatpak is not installed")
    Flat_remote_dict = {}
    flat_counted = "-"
