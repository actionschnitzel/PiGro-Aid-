<p align="center">
    <a href="https://github.com/actionschnitzel/PiGro-Aid-/tree/main">
        <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/9/proglogo.png" alt="PiGro logo">
    </a>
</p>

![HEADER2](https://github.com/actionschnitzel/tingsandstuff/blob/main/23_02/23_02_header.png?raw=true)
[![yt](https://github.com/actionschnitzel/tingsandstuff/blob/main/23_02/pigro_youtube.png?raw=true)](https://www.youtube.com/watch?v=QuPMnwFemoE)
---

# :bento: All Settings In One Place!

#### :heavy_check_mark: System Monitoring :heavy_check_mark: System Configuration :heavy_check_mark: Autostarts :heavy_check_mark: Process Monitor & Killer

#### :heavy_check_mark: Update & Upgrade GUI :heavy_check_mark:Multi Install GUI :heavy_check_mark: Change & Customize DE :heavy_check_mark: Overclocking

#### :heavy_check_mark: Link Collection

PiGro - Just Click it! is an all-inclusive graphical user interface (GUI) software that streamlines the process of managing all your Raspberry Pi settings from one convenient location. With PiGro, you can easily keep your software up-to-date, oversee the APT installer, Pi-Apps App Store, and Flatpak, configure autostarts, overclock your Pi, monitor the system's performance, back up your applications, install desktop environments, and customize your OS theme.

Designed with user-friendliness in mind, PiGro is easily accessible to users of all levels of expertise. Its intuitive interface and straightforward controls make it effortless to access and modify any settings you require.

---

# :floppy_disk: Installation

[![badge](https://github.com/Botspot/pi-apps/blob/master/icons/badge-light.png?raw=true)](https://github.com/Botspot/pi-apps)    
    
### Via Script:
```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash
```   
   
### Via APT:

Via [Debian Package](https://github.com/actionschnitzel/PiGro-Aid-/releases) Download

If you have already installed Pigro via the script, remove: `~/-PiGro-Aid-` and `~/.local/Share/Applications/Pigro.Desktop`. Then Install the Debian Package.



### Supported systems:

- [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (32-bit/64-bit) (Buster/Bullseye)(PIXEL & XFCE4)
- [Ubuntu](https://ubuntu.com/download/raspberry-pi) (64-bit) (All & XFCE4)
- [Ubuntu Mate](https://ubuntu-mate.org/download/) (All)
- [Diet-Pi](https://dietpi.com/#downloadinfo) (Scroll down to Important!)
- Debian based distros for Raspberry Pi in general

#### :exclamation: Installation Process & Updates

- If you have installed PiGro via Pi-Apps, you will automatically receive an update notification.
- If you have installed PiGro via Package you can check for updates in the About TAB.
- If you have installed PiGro via the official Repo APT will handle the updates.

#### Work on the next major update takes more time than expected.
-Many backend changes    
-Comfortable and simpler UI    
-More functions    
    
#### Hope in January '24 everything is done. As always, bug fixes & smaller patches for the latest version come as soon as possible.


---

# :exclamation: Important

#### `Pigro will install xterm`. For some reason, Xterm is then selected as default terminal emulator. You can change that by:

Open the Terminal and type `sudo update-alternatives --config x-terminal-emulator`. All available terminal emulators are listed. `lxterminal` is the default.

#### `Diet-Pi`: PiGro wouln't start because Wifi adapter is not set up:

`dietpi-config` > 7:Network Adapters > Wifi (This enables Wifi adapter)

---

# :hamburger: Latest Changes

[Changelog](https://github.com/actionschnitzel/PiGro-Aid-/wiki/Change-Log)

---

# :doughnut: Showcase

![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/9/showcase_9.png)

---

### :two_hearts: You want support me?

PiGro is completely free. I put up to three hours into improvements and updates every day. Not to forget the countless hours I spend reading manuals and reference books. If you like my work, you can support me

[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/PayPal_donation.png?raw=true)](https://www.paypal.com/paypalme/actionschnitzel)
