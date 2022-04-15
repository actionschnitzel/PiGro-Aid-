
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color


sudo apt update && upgrade

sudo apt install -y xfce4 xfce4-terminal xfce4-goodies lightdm slick-greeter bluetooth pulseaudio-module-bluetooth blueman bluez-firmware network-manager-gnome

sudo apt remove lxde* --purge -y
    
sudo apt remove pipanel --purge -y 
    
sudo apt remove lxpanel --purge -y 
    
sudo apt remove openbox* --purge -y
    
sudo apt remove obconf --purge -y
    
sudo apt autoremove -y    

sudo systemctl disable dhcpcd
    
sudo /etc/init.d/dhcpcd stop

clear
printf "\n${GREEN}Sodo Rebooto in:\n${NC}"
sleep 2
clear
printf "\n${GREEN}Sodo Rebooto in: 3\n${NC}"
sleep 2
clear
printf "\n${GREEN}Sodo Rebooto in: 2\n${NC}"
sleep 2
clear
printf "\n${GREEN}Sodo Rebooto in: 1\n${NC}"
sleep 2
#sudo reboot                   
   
