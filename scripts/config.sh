#!/bin/bash

# Yup, this is lazy coding ;-)

if [ -f /usr/bin/thunar ];then
  sudo xdg-open /boot/firmware/config.txt

elif [ -f /usr/bin/nemo ];then
  sudo sudo xdg-open ~/test.txt
else
  echo "Failed to locate FM!!!"
  exit 1
fi 
