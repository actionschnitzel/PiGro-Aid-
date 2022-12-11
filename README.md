<p align="center">
    <a href="https://github.com/actionschnitzel/PiGro-Aid-/tree/main">
        <img src="https://github.com/actionschnitzel/tingsandstuff/blob/main/9/proglogo.png" alt="PiGro logo">
    </a>
</p>

![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/9/header_SM9_2.png)

---

# :bento: All Settings In One Place!

#### :heavy_check_mark: System Monitoring :heavy_check_mark: System Configuration :heavy_check_mark: Autostarts :heavy_check_mark: Process Monitor & Killer

#### :heavy_check_mark: Update & Upgrade GUI :heavy_check_mark:Multi Install GUI :heavy_check_mark: Change & Customize DE :heavy_check_mark: Overclocking

#### :heavy_check_mark: Link Collection

PiGro does many commands that have to be entered via the terminal with one or two clicks of a button.

PiGro – Just Click It! Is based on Python's Tkinter module. Due to its greatly reduced LXDE/PIXEL desktop, Raspberry Pi OS lacks some setting options. Pigro centralizes all important settings for the Raspberry Pi desktop and adds a GUI for overclocking to the desktop.

---

[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/youtube.png?raw=true)](https://www.youtube.com/watch?v=Wp6U14VW4G8)

---

# :floppy_disk: Install

Open a terminal and run this command:

```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash
```

OR:

[![badge](https://github.com/Botspot/pi-apps/blob/master/icons/badge-light.png?raw=true)](https://github.com/Botspot/pi-apps)

#### Supported systems:

- [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (32-bit/64-bit) (Buster/Bullseye)
- Debian based distros in general

#### :exclamation: Installation Process & Updates

If you install PiGro via Pi-Apps, you will automatically receive an update notification.  
If you install PiGro using the script, you can simply use:

```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash
```

---

# :hamburger: Latest Changes

[Changelog](https://github.com/actionschnitzel/PiGro-Aid-/wiki/Change-Log)

---

# :exclamation: Important

#### Pigro will install xterm. For some reason, Xterm is then selected as default terminal emulator. You can change that by:

Open the Terminal and type `sudo update-alternatives --config x-terminal-emulator`. All available terminal emulators are listed. `lxterminal` is the default.

#### By default "Authentication Mode" is set to pkexec (Only Raspberry Pi OS allows Passwordless-SUDO).

If you like to switch to `Passwordless` go to `Look & Feel` and under `PiGro Tweaks` you cann select `Passwordless-SUDO` or `pkexec`.

---

# :doughnut: Showcase

![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/9/showcase_9.png)

---

### :two_hearts: You want support me?

PiGro is completely free. I put up to three hours into improvements and updates every day. Not to forget the countless hours I spend reading manuals and reference books. If you like my work, you can support me

[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/PayPal_donation.png?raw=true)](https://www.paypal.com/paypalme/actionschnitzel)
