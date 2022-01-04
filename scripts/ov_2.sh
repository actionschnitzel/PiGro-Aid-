#!/bin/bash

sudo cp /boot/config.txt{,.bak} && sudo sh -c 'echo "\narm_freq=2147\ngpu_freq=750\nover_voltage=8\ndisable_splash=1\nforce_turbo=1" >> /boot/config.txt'

#read -p "Done! You should reboot, C YA!......Press Enter"


