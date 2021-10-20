#!/bin/bash



if [ -f /usr/local/bin/pigro ];then
  echo "goood!"

else
  sudo cp /home/pi/PiGro-Aid-/scripts/pigro /usr/local/bin/ 
  

  sudo chmod +x /usr/local/bin/pigro
  exit 1
fi 
