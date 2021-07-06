
echo  '\e[92mPigro Installer\n\nI recently switched from Mint to MX and was blown away by the "MX Tools GUI". In the spirit of this, PiGro has now become an all-in-one control center.Hope you like it.\e[39m'
read -p "You are about to install PiGro - Just Click It! ...... Agree (y/n)? " option
case "$option" in
	y*) sudo apt-get update ;;
	n*) exit ;;
esac

clear

read -p "There are some really cool "Tool-Must-Haves" like: NeoFetch ...... install (y/n)? " option
case "$option" in
	y*) sudo apt-get install neofetch ;;
esac

clear

read -p "Gparted ...... install (y/n)? " option
case "$option" in
	y*) sudo apt-get install gparted ;;
esac

clear


sudo apt-get install xterm -y
sudo apt-get install python3-pil python3-pil.imagetk -y


sudo chmod +x start.sh
sudo chmod +x start1.sh
sudo chmod +x scripts/raspiconfiginstall.sh
sudo chmod +x scripts/ov_1.sh
sudo chmod +x scripts/ov_2.sh
sudo chmod +x scripts/autoremove.sh
sudo chmod +x scripts/addunsignedrepo.sh
sudo chmod +x scripts/update.sh
sudo chmod +x scripts/fmsudo.sh
sudo chmod +x scripts/upgrade.sh
sudo chmod +x scripts/lxappearance.sh
sudo chmod +x scripts/rmlxde.sh
sudo chmod +x scripts/terminal.sh
sudo chmod +x scripts/xfce4fix.sh
sudo chmod +x scripts/uninstall.sh
sudo chmod +x scripts/rm_ov.sh
sudo chmod +x scripts/lutris.sh
sudo cp pigro.desktop  /home/pi/Desktop
sudo cp pigro.desktop /usr/share/applications/
sudo chmod +x /home/pi/Desktop/pigro.desktop


echo  '\e[92mDone! You can close this window now.\e[39m'

