
read -p "You are about to install PiGro - Just Click It! ...... Agree (y/n)? " option
case "$option" in
	y*) sudo apt-get update ;;
	n*) exit ;;
esac

read -p "There are some really cool "Tool-Must-Haves" like: NeoFetch ...... install (y/n)? " option
case "$option" in
	y*) sudo apt-get install neofetch ;;
esac

read -p "Gparted ...... install (y/n)? " option
case "$option" in
	y*) sudo apt-get install gparted ;;
esac
sudo apt-get install xterm
sudo chmod +x start.sh
sudo chmod +x scripts/raspiconfiginstall.sh
sudo chmod +x scripts/autoremove.sh
sudo chmod +x scripts/addunsignedrepo.sh
sudo chmod +x scripts/update.sh
sudo chmod +x scripts/upgrade.sh
sudo chmod +x scripts/lxappearance.sh
sudo chmod +x scripts/rmlxde.sh
sudo chmod +x scripts/terminal.sh
sudo chmod +x scripts/xfce4fix.sh
sudo chmod +x scripts/uninstall.sh
sudo cp pigro.desktop  /home/pi/Desktop
sudo cp pigro.desktop /usr/share/applications/
sudo chmod +x /home/pi/Desktop/pigro.desktop



