#!/bin/bash

sudo apt autoremove -y && sudo apt clean && sudo apt-get purge -y $(dpkg -l | grep '^rc' | awk '{print $2}') |lolcat

read -p "Done! C YA!......Press Enter"
