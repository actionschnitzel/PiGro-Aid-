

# :floppy_disk: Install

#### DEV_TEST Branch Installer:

```
cd ~
sudo apt install git python3-dev python3-psutil python3-distro python3-bs4 python3-requests python3-pil python3-pil.imagetk xterm mpg123 lolcat wmctrl gdebi mousepad pkexec

git clone -b dev https://github.com/actionschnitzel/PiGro-Aid-.git

find ~/PiGro-Aid-/PiGro-JCI/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;


python3 ~/PiGro-Aid-/PiGro-JCI/src/main.py
```
