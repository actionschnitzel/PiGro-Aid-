echo "

██████╗░██╗░██████╗░██████╗░░█████╗░░
██╔══██╗██║██╔════╝░██╔══██╗██╔══██╗░
██████╔╝██║██║░░██╗░██████╔╝██║░░██║░
██╔═══╝░██║██║░░╚██╗██╔══██╗██║░░██║░
██║░░░░░██║╚██████╔╝██║░░██║╚█████╔╝░
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░
         🅹🆄🆂🆃 🅲🅻🅸🅲🅺 🅸🆃"

YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

printf "${GREEN}I now install dependencies${NC}\n\n"

sudo apt-get install -y xterm python3-pil python3-pil.imagetk python3-pip python3-dev python3-distro python3-psutil libnotify-bin mpg123 lolcat



clear

cd


if [ -d "$HOME/PiGro-Aid-" ] 
then
    printf "${YELLOW}[UPDATE]${NC}I will install the newest version.\n\n" 
    rm -rf $HOME/PiGro-Aid-
    git clone -b dev https://github.com/actionschnitzel/PiGro-Aid-.git
    cd PiGro-Aid-
else
    printf "${YELLOW}[NEW INSTALL]${NC}I will now install PiGro\n\n"
    git clone -b dev https://github.com/actionschnitzel/PiGro-Aid-.git
    cd PiGro-Aid-
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

echo "

██████╗░██╗░██████╗░██████╗░░█████╗░░
██╔══██╗██║██╔════╝░██╔══██╗██╔══██╗░
██████╔╝██║██║░░██╗░██████╔╝██║░░██║░
██╔═══╝░██║██║░░╚██╗██╔══██╗██║░░██║░
██║░░░░░██║╚██████╔╝██║░░██║╚█████╔╝░
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝░╚════╝░░
         🆃🅷🅴 🆃🅰🆂🅺 🅸🆂 🅲🅾🅼🅿🅻🅴🆃🅴"
printf "\n${GREEN}You can close this window now\n${NC}"
