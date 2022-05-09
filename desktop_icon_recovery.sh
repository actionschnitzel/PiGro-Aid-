#Only for DEV use 

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
Icon=${DIRECTORY}/images/icons/pigro_icons/96x96.png
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
Icon=${DIRECTORY}/images/icons/pigro_icons/96x96.png
Path=${DIRECTORY}/" > ~/.local/share/applications/pigro.desktop

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

printf "\n${GREEN}You can close this window now\n${NC}"