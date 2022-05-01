[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![forthebadge made-with-coffee](https://github.com/actionschnitzel/tingsandstuff/blob/main/powered_by_coffee.png)

![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/header_SM.png)

---

## All settings in one place! :key: :mag: :hammer: :toilet:

#### PiGro - Just Click It! is a control panel that bundles the most important options.

Due to the reduced desktop, Raspberry Pi OS lacks a control center that makes all options accessible at a glance. I started using opensuse when I was young and still do. I love the possibilities of its control center YaST.

And that's exactly what PiGro is, a tool inspired by the possibilities of YaST.

With a clear and graphically appealing GUI you can access the system deeply, overclock the Pi or replace the entire desktop environment. Everything you need to use the Pi as a desktop computer.

PiGro does many commands that have to be entered via the terminal with one or two clicks of a button.

##### :wrench: Sudo apt-get update/upgrade

##### :wrench: Sudo apt-get install ...

##### :wrench: Sudo nano boot / config.txt

##### :wrench: Overclocking

##### :wrench: Install and change the DE

### And there is a lot more!


With the latest release (codename: Stupida Medusa) PiGro - Just Click It! also works on Ubuntu.


---

# :doughnut: Showcase (Click 2 Enlage)


<img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/1.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/2.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/3.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/4.png" width="200">  <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/6.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/7.png" width="200">  <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/9.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/10.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/8.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/5.png" width="200">

<img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/welcome.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/system.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/update.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/installer.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/tuning.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/link.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/pigro_pix/tuning.png" width="200">

---

# :question: Pigro [Wiki](https://github.com/actionschnitzel/PiGro-Aid-/wiki)

Documentation + Manual /// Still in work

---

# :zap: Latest Improvements

#ADDED# xdg-open /etc/apt/sources.list.d/ Button in Update      
#ADDED# Installer uses now APT in a background process     
#ADDED# High Quality Welcome Tab Background  
#ADDED# XFCE Options are disabled when using other desktop  
#ADDED# Gparted & Neofetch Button disabled when not installed  
#ADDED# Shop is better structured  
#ADDED# Overclocking buttons are disabled immediately after clicking  
#ADDED# APT install funktion + combobox  
#ADDED# APT search function + combobox  
#ADDED# APT remove function + combobox  
#ADDED# Tuning specifications can be viewed via the map button  
#ADDED# VisualTk added to Links  
#ADDED# NEW OVERCLOCKING OPTION:  
 arm_freq=2300  
 gpu_freq=700  
 over_voltage=14  
 force_turbo=1  
#ADDED# VisualTk added to Links  
#ADDED# Bash History on System Tab  
#ADDED# Cron Job in System  
#ADDED# SD Copier in System  
#ADDED# Screen Settings  
#ADDED# Desktop Settings  
#ADDED# Desktop Session Settings  
#ADDED# Printer  
#ADDED# Menu Settings  
#ADDED# Pakage Sources  
#ADDED# Mous & Keyboard

#FIXED# Temperature rounded to one number after the decimal point  
#FIXED# Folder structure improved  
#FIXED# Icon & PNG improvements

#CHANGED# Old and useless code has been deleted  
#CHANGED# Image.open has been almost completely replaced by PhotoImage  
#CHANGED# Installer Renamed to Software  
#CHANGED# Fast Installer command "sudo apt-get install/remove" has now \*option "-y"  
#CHANGED# 64 Bit Mode removed due to it's no more avaleble in repo

---

# :rocket: To do [NEXT UPDATE]

- [ ] Check Back rutines
- [x] [Order Pizza with Steak, Cheese , Jalapeño , Bacon & Hollandaise Sauce :goberserk:]


---

# :floppy_disk: Install

Open a terminal and run this command:

```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/main/install.sh |bash
```

(Extra easy for LTT employees)

OR:

[![badge](https://github.com/Botspot/pi-apps/blob/master/icons/badge.png?raw=true)](https://github.com/Botspot/pi-apps)

#### Supported systems:

- [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (32-bit/64-bit) (Buster/Bullseye): fully supported.
- [Twister OS](https://twisteros.com/download.html): fully supported.
- [Ubuntu](https://ubuntu.com/download): fully supported.

#### :exclamation: Installation Process & Updates

If you install PiGro via Pi-Apps, you will automatically receive an update notification.  
If you install PiGro using the script, you can simply use:

```
"wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/main/install.sh |bash".
```

#### For more infos visit: [Behavior in the different distributors](https://github.com/actionschnitzel/PiGro-Aid-/wiki/Behavior-in-the-different-distributors)

---

# :question: Pigro [Wiki](https://github.com/actionschnitzel/PiGro-Aid-/wiki)

Documentation + Manual /// Still in work

---

# :zap: Latest Improvements

#ADDED I added a Pi Camera Tab just for fun. Never saw an App
that does Pi Cam stuff in a GUI ...
So maybe it stay in PiGro maby not... time will tell.

#ADDED Rename user option for old pi installations

#ADDED Expert Mode for Tuning

#ADDED Cute Tux greets you with your user name

#CHANGED User Pi said goodbye! PiGro now full supports user names

#CHANGED Rearranged Software tab

#FIXED If Snap/Pi-Apps/Flatpak is not installed the buttons
are disabled

#FIXED As always there are code improvements

#APT-GET Installer shows now terminal output due to transperency reasons

---

# :rocket: To do

- [ ] Add fully fuctional tkinter rip-off of raspi-config :partying_face: :imp:
- [x] [Order Pizza with Steak, Cheese , Jalapeño , Bacon & Hollandaise Sauce :goberserk:]

---

[![Actionschnitzel's GitHub stats](https://github-readme-stats.vercel.app/api?username=actionschnitzel)](https://github.com/actionschnitzel/github-readme-stats)

#### You want support me?

[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/kisspng-donation-computer-icons-portable-network-graphics-5b972c7ded3449.9709889315366339819716.png)](https://paypal.me/actionschnitzel?locale.x=de_DE)
