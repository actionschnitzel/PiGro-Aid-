#!/bin/bash

read -p "Hmmm....XFCE4......NICE! Dude.....No WIFI???!!!!! I'm gonna help you out ;-)......Press Enter"

sudo systemctl disable dhcpcd
sudo /etc/init.d/dhcpcd stop
read -p "Done! C YA!......Press Enter"

sudo reboot