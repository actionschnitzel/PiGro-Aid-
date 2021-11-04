#!/bin/bash

sudo apt install -y xfce4 xfce4-goodies
clear

sudo dpkg-reconfigure lightdm
clear

echo "Please select the number with option >>startxfce4<<"

sudo update-alternatives --config x-session-manager
clear

echo "Please select the number with option >>xfwm4<<"

sudo update-alternatives --config x-window-manager
clear

echo "Now Bluetooth Stuff"

sudo apt install bluetooth pulseaudio-module-bluetooth blueman bluez-firmware


echo "Now WiFi Stuff"


sudo apt install network-manager-gnome -y
sudo systemctl disable dhcpcd
sudo /etc/init.d/dhcpcd stop


read -p "Done! C YA!......Press Enter and it will Sudo Rebooto"

sudo reboot