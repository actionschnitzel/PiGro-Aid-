import os
from resorcess import home
from resorcess import user


def refresh_piapps_installs():
    print("[Info] Pi-Apps is installed. List will be added")
    pi_apps_installed_list = []
    for installed_pi_apps in os.listdir(f"{home}/pi-apps/data/status"):
        pi_apps_status = open(
            f"/home/{user}/pi-apps/data/status/{installed_pi_apps}", "r"
        )
        status = pi_apps_status.read()
        pi_apps_status.close()
        if status.strip() == "installed":
            pi_apps_installed_list.append(installed_pi_apps)
    # print(pi_apps_installed_list)

    piapps_installed = pi_apps_installed_list
    piapps_installed_content = piapps_installed
    for i, s in enumerate(piapps_installed_content):
        piapps_installed_content[i] = s.strip()
    return piapps_installed_content


# Checks if pi-apps is installed an imports the app list
piapps_path = os.path.exists(f"{home}/pi-apps")
if piapps_path == False:
    print("[Info] Pi-Apps is not installed")
    pi_apps_installed_list = []
    piapps_cache_content = []

if piapps_path == True:
    piapps_cache = os.popen(f"ls ~/pi-apps/apps/ ")
    piapps_cache_content = piapps_cache.readlines()
    for i, s in enumerate(piapps_cache_content):
        piapps_cache_content[i] = s.strip()

    refresh_piapps_installs()
    # print(piapps_cache_content)
