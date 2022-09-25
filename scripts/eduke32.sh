#DUKE.RTS & DUKE3D.GRP not included
#https://www.eduke32.com/
YELLOW='\033[0;33m'
GREEN='\033[0;32m'
RED='\033[0;31m'
NC='\033[0m' # No Color

sudo apt-get install build-essential nasm libgl1-mesa-dev libglu1-mesa-dev libsdl1.2-dev libsdl-mixer1.2-dev libsdl2-dev libsdl2-mixer-dev flac libflac-dev libvorbis-dev libvpx-dev libgtk2.0-dev freepats git 


cd $HOME 
wget https://voidpoint.io/terminx/eduke32/-/archive/master/eduke32-master.tar.gz
tar -xf eduke32-master.tar.gz
mv eduke32-master eduke32

cd ~/eduke32

make

clear

printf "\n\n\nDone! DUKE.RTS & DUKE3D.GRP not included. Move the to files to ~/.config/eduke32/ manually ;-)"
