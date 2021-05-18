#!/bin/bash



if [ -f /usr/bin/thunar ];then
  sudo thunar

elif [ -f /usr/bin/pcmanfm ];then
  sudo pcmanfm
else
  echo "Failed to locate FM!!!"
  exit 1
fi 
