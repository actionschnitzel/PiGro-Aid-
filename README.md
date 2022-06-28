[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
![forthebadge made-with-coffee](https://github.com/actionschnitzel/tingsandstuff/blob/main/powered_by_coffee.png)
![forthebadge for-rpi](https://github.com/actionschnitzel/tingsandstuff/blob/main/4rpi.png)

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
##### :wrench: Add Autostart on DE Login
### And there is a lot more!

---
### :two_hearts: You want support me?

PiGro is completely free. I put up to three hours into improvements and updates every day. Not to forget the countless hours I spend reading manuals and reference books. If you like my work, you can support me. The easiest way is to buy a sticker or something from RedBubble so you get something and so do I ;-)

[RedBubble](https://www.redbubble.com/de/people/Actionschnitzel/shop?anchor=profile&asc=u)    
    
or:    
    
[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/PayPal_donation.png?raw=true)](https://www.paypal.com/paypalme/actionschnitzel)    
---
# :doughnut: Showcase (Click 2 Enlage)

<img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/1.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/2.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/3.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/4.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/6.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/7.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/9.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/10.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/8.png" width="200"> <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/Stupida_Medusa_Release/5.png" width="200">

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

# :exclamation: Important

#### Pigro will install xterm. For some reason, Xterm is then selected as default terminal emulator. You can change that by:
     
Open the Terminal and type `sudo update-alternatives --config x-terminal-emulator`. All available terminal emulators are listed. `lxterminal` is the default.
     
---

# :question: Pigro [Wiki](https://github.com/actionschnitzel/PiGro-Aid-/wiki)

Documentation + Manual /// Still in work

---

# :zap: Latest Improvements


#ADDED: Process Viewer/ Killer

#ADDED: ask:yes/no/cancel popups to critikal options

#ADDED: Disk space usage on Welcome tab

#ADDED: Autostart tab

#ADDED: Change Wallpaper for PIXEL Desktop

#CHANGED: straighter visual appearance

- bigger icons     
- main color #222222    
- removed tab decoration    
    
#CHANGED: *.list,*conf files moved to ~/.pigro
(./pigro is a hidden config folder that stores cache files and pigro configs. This way git pull works again)

#CHANGED: Bye Splash Screen(PiGro starts now faster)    
    
#FIXED: #arm_freq=800 bug on Tuning Display fixed    

---

# :rocket: To do

- [ ] Add fully fuctional tkinter rip-off of raspi-config :partying_face: :imp:
- [x] [Order Pizza with Steak, Cheese , Jalapeño , Bacon & Hollandaise Sauce :goberserk:]

---

[![Actionschnitzel's GitHub stats](https://github-readme-stats.vercel.app/api?username=actionschnitzel)](https://github.com/actionschnitzel/github-readme-stats)

