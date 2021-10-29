
echo '                                                                     
    ____  _ ______              ____           __        ____         
   / __ \(_) ____/________     /  _/___  _____/ /_____ _/ / /__  _____
  / /_/ / / / __/ ___/ __ \    / // __ \/ ___/ __/ __ `/ / / _ \/ ___/
 / ____/ / /_/ / /  / /_/ /  _/ // / / (__  ) /_/ /_/ / / /  __/ /    
/_/   /_/\____/_/   \____/  /___/_/ /_/____/\__/\__,_/_/_/\___/_/     
                                                                      '


echo "Thanks for installing Pigro!
Pigro is a system tool and is inspired by YaST (OpenSuse). Let's go!!!"
read -p "Install PiGro - Just Click It! ...... Agree (y/n)? " option
case "$option" in
    y*) sudo apt-get update ;;
    n*) exit ;;
esac
clear

echo 'Now I install dependencies'

sudo apt-get install xterm -y
sudo apt-get install python3-pil -y 
sudo apt-get install python3-pil.imagetk -y
sudo apt install python3-pip -y
sudo apt install mpg123 -y
sudo apt install lolcat -y
pip3 install psutil
pip3 install distro

git clone -b bullseye_testing_ https://github.com/actionschnitzel/PiGro-Aid-.git
cd PiGro-Aid-

sudo chmod +x start.sh
sudo cp pigro.desktop  /home/pi/Desktop
sudo cp pigro.desktop /usr/share/applications/
sudo chmod +x /home/pi/Desktop/pigro.desktop
cd
clear

echo '                                                                     
    ____  _ ______              ____           __        ____         
   / __ \(_) ____/________     /  _/___  _____/ /_____ _/ / /__  _____
  / /_/ / / / __/ ___/ __ \    / // __ \/ ___/ __/ __ `/ / / _ \/ ___/
 / ____/ / /_/ / /  / /_/ /  _/ // / / (__  ) /_/ /_/ / / /  __/ /    
/_/   /_/\____/_/   \____/  /___/_/ /_/____/\__/\__,_/_/_/\___/_/     
                                                                      '

echo  '
 ____ ____ ____ ____ _________ ____ 
||D |||O |||N |||E |||       |||! ||
||__|||__|||__|||__|||_______|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|'

printf '\e[38;5;46m You can close this window now\n'
