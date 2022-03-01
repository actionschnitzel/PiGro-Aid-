#!/bin/bash

sudo cp /boot/config.txt{,.bak} && sudo sh -c 'echo "#Pigro_Overclocking4\narm_freq=2300\ngpu_freq=500\nover_voltage=14\ndisable_splash=1\nforce_turbo=1" >> /boot/config.txt'

#read -p "Done! You should reboot, C YA!......Press Enter"