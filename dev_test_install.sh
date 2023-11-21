YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

printf "${YELLOW}
██████╗ ██╗ ██████╗ ██████╗  █████╗  
██╔══██╗██║██╔════╝ ██╔══██╗██╔══██╗ 
██████╔╝██║██║  ██╗ ██████╔╝██║  ██║ 
██╔═══╝ ██║██║  ╚██╗██╔══██╗██║  ██║ 
██║     ██║╚██████╔╝██║  ██║╚█████╔╝ 
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚════╝  
${NC}"
printf "${RED}
░░█ █░█ █▀ ▀█▀   █▀▀ █░░ █ █▀▀ █▄▀   █ ▀█▀ █
█▄█ █▄█ ▄█ ░█░   █▄▄ █▄▄ █ █▄▄ █░█   █ ░█░ ▄
${NC}\n\n"
sleep 2
clear
sleep 2
printf "${RED}
█▀▄ █▀▀ █▀█ █▀▀ █▄░█ █▀▄ █▀▀ █▄░█ █▀▀ █ █▀▀ █▀
█▄▀ ██▄ █▀▀ ██▄ █░▀█ █▄▀ ██▄ █░▀█ █▄▄ █ ██▄ ▄█
${NC}\n\n"
echo  -e "\033[33;5mInstalling...\033[0m"
echo "git xterm python3-pil python3-pil.imagetk python3-pip python3-psutil python3-distro python3-bs4 python3-dev python3-requests mpg123 lolcat wmctrl gdebi mousepad"
> /dev/null 2>&1 sudo apt-get update
> /dev/null 2>&1 sudo apt-get install git xterm python3-pil python3-pil.imagetk python3-pip python3-psutil python3-distro python3-bs4 python3-dev python3-requests mpg123 lolcat wmctrl gdebi mousepad -y 





clear

cd


if [ -d "$HOME/PiGro-Aid-" ] 
then
    printf "${YELLOW}
█░█ █▀█ █▀▄ ▄▀█ ▀█▀ █▀▀
█▄█ █▀▀ █▄▀ █▀█ ░█░ ██▄
${GREEN}I will install the newest version.\n\n${NC}"
    echo  -e "\033[33;5mInstalling...\033[0m" 
    > /dev/null 2>&1 rm -rf $HOME/PiGro-Aid-
    > /dev/null 2>&1 git clone -b dev https://github.com/actionschnitzel/PiGro-Aid-.git
    > /dev/null 2>&1 cd PiGro-Aid-
else
    printf "${YELLOW}
█▄░█ █▀▀ █░█░█   █ █▄░█ █▀ ▀█▀ ▄▀█ █░░ █░░
█░▀█ ██▄ ▀▄▀▄▀   █ █░▀█ ▄█ ░█░ █▀█ █▄▄ █▄▄
${GREEN}I will now install PiGro\n\n${NC}"
    echo  -e "\033[33;5mInstalling...\033[0m"
    > /dev/null 2>&1 git clone -b dev https://github.com/actionschnitzel/PiGro-Aid-.git
    > /dev/null 2>&1 cd PiGro-Aid-
fi

clear

sudo chmod +x start.sh

DIRECTORY="$(readlink -f "$(dirname "$0")")"
if [ -z "$DIRECTORY" ] || [ "$DIRECTORY" == "$HOME" ] || [ "$DIRECTORY" == bash ];then
  DIRECTORY="$HOME/PiGro-Aid-"
fi

echo "[Desktop Entry]
Version=2.1
Exec=${DIRECTORY}/start.sh
Name=PiGro
GenericName=PiGro
Encoding=UTF-8
Terminal=false
Type=Application
Categories=System
Icon=${DIRECTORY}/images/icons/logo.png
Path=${DIRECTORY}/" > ~/Desktop/pigro.desktop

sudo chmod +x ~/Desktop/pigro.desktop


echo "[Desktop Entry]
Version=2.1
Exec=${DIRECTORY}/start.sh
Name=PiGro
GenericName=PiGro
Encoding=UTF-8
Terminal=false
Type=Application
Categories=System
Icon=${DIRECTORY}/images/icons/logo.png
Path=${DIRECTORY}/" > ~/.local/share/applications/pigro.desktop

cd
clear

printf "${YELLOW}
██████╗ ██╗ ██████╗ ██████╗  █████╗  
██╔══██╗██║██╔════╝ ██╔══██╗██╔══██╗ 
██████╔╝██║██║  ██╗ ██████╔╝██║  ██║ 
██╔═══╝ ██║██║  ╚██╗██╔══██╗██║  ██║ 
██║     ██║╚██████╔╝██║  ██║╚█████╔╝ 
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚════╝  
${NC}"
printf "${RED}
█ █▄░█ █▀ ▀█▀ ▄▀█ █░░ █░░ ▄▀█ ▀█▀ █ █▀█ █▄░█   █ █▀   █▀▄ █▀█ █▄░█ █▀▀
█ █░▀█ ▄█ ░█░ █▀█ █▄▄ █▄▄ █▀█ ░█░ █ █▄█ █░▀█   █ ▄█   █▄▀ █▄█ █░▀█ ██▄
${NC}"
echo  -e "\033[33;5mYou can close this window now\n\033[0m"
