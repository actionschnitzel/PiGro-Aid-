#xpad-neo
#https://github.com/atar-axis/xpadneo
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color



sudo apt-get install dkms raspberrypi-kernel-headers

git clone https://github.com/atar-axis/xpadneo.git

cd xpadneo

sudo ./install.sh

clear

printf "\n\n\nDone!"