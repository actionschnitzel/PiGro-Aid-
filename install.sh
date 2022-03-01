echo '                                                                     
    ____  _ ______              ____           __        ____         
   / __ \(_) ____/________     /  _/___  _____/ /_____ _/ / /__  _____
  / /_/ / / / __/ ___/ __ \    / // __ \/ ___/ __/ __ `/ / / _ \/ ___/
 / ____/ / /_/ / /  / /_/ /  _/ // / / (__  ) /_/ /_/ / / /  __/ /    
/_/   /_/\____/_/   \____/  /___/_/ /_/____/\__/\__,_/_/_/\___/_/     
                                                                      '

echo 'Now I install dependencies'

sudo apt-get install xterm python3-pil python3-pil.imagetk python3-pip mpg123 lolcat -y

pip3 install psutil distro

clear

git clone https://github.com/actionschnitzel/PiGro-Aid-.git
cd PiGro-Aid-

sudo chmod +x start.sh
sudo cp pigro.desktop  $HOME/Desktop
sudo cp pigro.desktop /usr/share/applications/
sudo chmod +x $HOME/Desktop/pigro.desktop
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