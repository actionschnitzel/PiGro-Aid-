![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/9/header_SM9.png)

---

# :bento: All Settings In One Place!

#### :heavy_check_mark: System Monitoring :heavy_check_mark: System Configuration :heavy_check_mark: Autostarts :heavy_check_mark: Process Monitor & Killer

#### :heavy_check_mark: Update & Upgrade GUI :heavy_check_mark:Multi Install GUI :heavy_check_mark: Change & Customize DE :heavy_check_mark: Overclocking

#### :heavy_check_mark: Link Collection

PiGro does many commands that have to be entered via the terminal with one or two clicks of a button.

PiGro – Just Click It! Is based on Python's Tkinter module. Due to its greatly reduced LXDE/PIXEL desktop, Raspberry Pi OS lacks some setting options. Pigro centralizes all important settings for the Raspberry Pi desktop and adds a GUI for overclocking to the desktop.

---

# :hamburger: Latest Changes

So what's new? For a long time I made all the backgrounds and icons myself. Since this is very time-consuming, I have mostly switched to using the Papirus icon theme.
PiGro should feel like a system native application, so I reduced some things visually, such as the backgrounds. You can now choose between dark and light theme in the LOOK & FEEL tab.
The dark theme is the default. The Light Theme is based on the standard colors of Raspberry Pi OS. The transparency can now also be switched on and off separately. I've also done my best to make everything clearer and better structured.

I've read a lot on forums that people have deleted their taskbar/panel and don't know how to get it back. In LOOK & FEEL there is now a button that resets the taskbar to default.

As always, there are many code improvements.
[Changelog](https://github.com/actionschnitzel/PiGro-Aid-/wiki/Change-Log)

---

# :dart: Next Update

- [x] Nothin' to do at the moment

---

# :floppy_disk: Install

Open a terminal and run this command:

```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash
```

OR:

[![badge](https://github.com/Botspot/pi-apps/blob/master/icons/badge-light.png?raw=true)](https://github.com/Botspot/pi-apps)

#### Supported systems:

- [Raspberry Pi OS](https://www.raspberrypi.com/software/operating-systems/) (32-bit/64-bit) (Buster/Bullseye): fully supported.
- [Twister OS](https://twisteros.com/download.html): fully supported.


#### :exclamation: Installation Process & Updates

If you install PiGro via Pi-Apps, you will automatically receive an update notification.  
If you install PiGro using the script, you can simply use:

```
wget -qO- https://raw.githubusercontent.com/actionschnitzel/PiGro-Aid-/installer/install.sh |bash
```

#### For more infos visit: [Behavior in the different distributors](https://github.com/actionschnitzel/PiGro-Aid-/wiki/Behavior-in-the-different-distributors)

---

# :exclamation: Important



#### Pigro will install xterm. For some reason, Xterm is then selected as default terminal emulator. You can change that by:

Open the Terminal and type `sudo update-alternatives --config x-terminal-emulator`. All available terminal emulators are listed. `lxterminal` is the default.

#### :exclamation: For the time being, PiGro no longer has Ubuntu support. With every new Ubuntu release, more and more dependencies are missing and I have to work on work-arounds almost constantly. That's not fun.

---

# :doughnut: Showcase

![GUI](https://github.com/actionschnitzel/tingsandstuff/blob/main/9/showcase_9.png)



---

### :two_hearts: You want support me?

PiGro is completely free. I put up to three hours into improvements and updates every day. Not to forget the countless hours I spend reading manuals and reference books. If you like my work, you can support me    
    
[![badge](https://github.com/actionschnitzel/tingsandstuff/blob/main/PayPal_donation.png?raw=true)](https://www.paypal.com/paypalme/actionschnitzel)
