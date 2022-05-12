YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color


FILE=/bin/stress
printf  "Searching for stress\n"

if [ -f "$FILE" ]; then
    printf "${GREEN} $FILE exists.${NC}\n\n"
    clear
    printf "${GREEN}This will take a bit\n${YELLOW}To cancel press CTRL+C\n${RED}The Plot popes up atomaticly\nafter the Test has finished${NC}\n\n"

    export PATH=$PATH:/home/pi/.local/bin

    stressberry-run out.dat
else 
    printf "${YELLOW} $FILE does not exist an must be installed.${NC}\n\n"
    sudo apt install stress
    python3 -m pip install stressberry
    clear
    read -p "You need to reboot for Stressberry to work! Reboot?" yn
    case $yn in
        [Yy]* ) sudo reboot;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
fi

# 
# 


