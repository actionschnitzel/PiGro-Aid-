ds64-shell
sudo systemctl restart systemd-binfmt
git clone https://github.com/ptitSeb/box64
cd box64
mkdir build; cd build; cmake .. -DRPI4ARM64=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo
make -j4
sudo make install

read -p "Done!, C YA!......Press Enter"