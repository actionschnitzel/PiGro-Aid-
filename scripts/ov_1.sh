#!/bin/bash

if  grep -q 'NAME="Ubuntu"' "/etc/os-release" ; then
         echo 'Using Ubuntu Config Path' ;
         cp /boot/firmware/config.txt{,.bak} && sudo sh -c 'echo "#Pigro_Overclocking1\narm_freq=2000\ngpu_freq=750\nover_voltage=6\ndisable_splash=1\nforce_turbo=1" >> /boot/firmware/config.txt' ; 
else
         echo 'Using Debian Config Path' ; 
         cp /boot/config.txt{,.bak} && sudo sh -c 'echo "#Pigro_Overclocking1\narm_freq=2000\ngpu_freq=750\nover_voltage=6\ndisable_splash=1\nforce_turbo=1" >> /boot/config.txt';
fi