#!/bin/bash

cd /boot/

sudo sed -i '/arm_freq=2000/d' config.txt
sudo sed -i '/gpu_freq=750/d' config.txt
sudo sed -i '/over_voltage=6/d' config.txt
sudo sed -i '/force_turbo=1/d' config.txt
sudo sed -i '/disable_splash=1/d' config.txt

sudo sed -i '/arm_freq=2147/d' config.txt
sudo sed -i '/gpu_freq=750/d' config.txt
sudo sed -i '/over_voltage=8/d' config.txt
sudo sed -i '/force_turbo=1/d' config.txt

sudo sed -i '/arm_freq=2200/d' config.txt
sudo sed -i '/gpu_freq=750/d' config.txt
sudo sed -i '/over_voltage=6/d' config.txt
sudo sed -i '/force_turbo=1/d' config.txt
sudo sed -i '/disable_splash=1/d' config.txt

clear

#read -p "Done! You should reboot, C YA!......Press Enter"

