from resorcess import *



class SoftwareSys:
    # Descriptions by ????????????
    sys_dict = {
        # Browser
        "sys_0": {
            "Name": "Bash History",
            "Description": "Öffnet die Datei bash_history in deinem HOME-Verzeichnis. Es wird eine Auflisting aller ausgeführen Befehle angezeigt.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/bash.png",
            "Action": f"xdg-open {home}/.bash_history",
            "Path": "Bash History",
        },
        "sys_1": {
            "Name": "Cron Job",
            "Description": "Ein Cron Job ist ein geplanter Task, der auf Unix- oder Linux-Systemen automatisch zu festgelegten Zeiten oder Intervallen ausgeführt wird. Cron Jobs werden mithilfe des `cron`-Dienstes und der `crontab`-Datei eingerichtet und sind nützlich für regelmäßige Aufgaben wie Backups, Updates oder das Ausführen von Skripten.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/mousepad.png",
            "Action": f"{permit} mousepad /etc/crontab",
            "Path": "Bash History",
        },
        "sys_2": {
            "Name": "dmesg --follow",
            "Description": "'dmesg --follow' zeigt neue Kernel-Meldungen in Echtzeit an. Es ist nützlich, um laufend aktuelle Systemereignisse oder Fehler direkt zu überwachen.",            
            "Icon": f"{application_path}/images/icons/papirus/48x48/deepin-log-viewer.png",
            "Action": "x-terminal-emulator -e 'bash -c \"pkexec dmesg --follow; exec bash\"'",
            "Path": "Bash History",
        },
        "sys_3": {
            "Name": "dmesg",
            "Description": "'dmesg' zeigt die Systemmeldungen des Kernels an, die beim Hochfahren und während des Betriebs gesammelt werden. Diese Meldungen helfen, Probleme mit der Hardware oder dem System zu diagnostizieren und geben Einblick in den aktuellen Systemstatus.",            
            "Icon": f"{application_path}/images/icons/papirus/48x48/deepin-log-viewer.png",
            "Action": "x-terminal-emulator -e 'bash -c \"pkexec dmesg; exec bash\"'",
            "Path": "Bash History",
        },
        "sys_4": {
            "Name": "FM God Mode",
            "Description": "Öffnet den File-Browser mit erhöhten Rechten.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/folder-yellow.png",
            "Action": f"{permit} nemo",
            "Path": "Bash History",
        },
        "sys_5": {
            "Name": "Gparted",
            "Description": "Ein schneller, sicherheitsorientierter Browser, der Werbung blockiert und Tracker blockiert. Basiert auf Chromium und fokussiert auf Datenschutz. Unterstützt eine Vielzahl an Erweiterungen.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/bash.png",
            "Action": "",
            "Path": "Bash History",
        },
        # E-Mail und Messaging
        "sys_6": {
            "Name": "Reconfigure Keyboard",
            "Description": "Es wird der befehlt 'dpkg-reconfigure keyboard-configuration' ausgeführt. Hiermit lässt sich die Tastaturbelegung anpassen.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/gnome-settings-keybinding.png",
            "Action": "x-terminal-emulator -e 'bash -c \"pkexec dpkg-reconfigure keyboard-configuration; exec bash\"'",
            "Path": "Bash History",
        },
        "sys_7": {
            "Name": "Reconfigure Locales",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/papirus/48x48/desktop-effects.png",
            "Action": "x-terminal-emulator -e 'bash -c \"pkexec dpkg-reconfigure locales; exec bash\"'",
            "Path": "Bash History",
        },
        "sys_8": {
            "Name": "Raspi Bookshelf",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "rp-bookshelf",
            "Path": "rp-bookshelf",
        },
        "sys_9": {
            "Name": "Raspi-Config GUI",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "env SUDO_ASKPASS=/usr/lib/rc-gui/pwdrcg.sh sudo -AE rc_gui",
            "Path": "rc_gui",
        },
        "sys_10": {
            "Name": "Raspi-Config CLI",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "x-terminal-emulator -e 'bash -c \"sudo raspi-config; exec bash\"'",
            "Path": "raspi-config",
        },
        "sys_11": {
            "Name": "Edit Config.txt",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": f"{permit} mousepad {config_path}",
            "Path": "raspi-config",
        },
        "sys_12": {
            "Name": "Raspi Diagnostics",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "agnostics",
            "Path": "agnostics",
        },
        "sys_13": {
            "Name": "Raspi Printer Settings",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "system-config-printer",
            "Path": "system-config-printer",
        },
        "sys_14": {
            "Name": "Raspi Mouse & Keyboard",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": f"lxinput",
            "Path": "lxinput",
        },
        "sys_15": {
            "Name": "Raspi SD Card Copier",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "env SUDO_ASKPASS=/usr/lib/piclone/pwdpic.sh sudo -AE dbus-launch piclone",
            "Path": "piclone",
        },
        "sys_16": {
            "Name": "Raspi Desktop Settings",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "pcmanfm --desktop-pref",
            "Path": "pcmanfm --desktop-pref",
        },
        "sys_17": {
            "Name": "Raspi Screen Settings",
            "Description": "Es wird der befehlt 'dpkg-reconfigure locales' ausgeführt. Hiermit lässt sich die System-Sprache ändern.",
            "Icon": f"{application_path}/images/icons/PiXflat/bookshelf.png",
            "Action": "lxrandr",
            "Path": "lxrandr",
        },
    }
    