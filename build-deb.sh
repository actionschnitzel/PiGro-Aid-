#!/bin/bash



# Define the package name and version
PACKAGE_NAME="pigro-jci"
VERSION="24.04"

# Define the dependencies
DEPENDENCIES="python3-dev, python3-psutil, python3-distro, python3-bs4, python3-requests, python3-pil, python3-pil.imagetk, xterm, mpg123, lolcat, wmctrl, gdebi, mousepad, appstream, pkexec | policykit-1"

# Create the necessary directories
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/DEBIAN
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/opt/PiGro-JCI
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/bin
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/applications
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/icons/hicolor/256x256/apps
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/icons/hicolor/scalable/apps
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/metainfo
mkdir -p ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/doc/pigro-jci/

#Copy necessary files
rsync -av --exclude='start.sh' --exclude='.vscode' --exclude='src/__pycache__' --exclude='src/tabs/__pycache__' ~/PiGro-Aid-/PiGro-JCI/* ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/opt/PiGro-JCI/




# Copy files to location
cp ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/icon/pigro-logo.png ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/icons/hicolor/256x256/apps/pigro-logo.png
cp ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/icon/pigro-logo.svg ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/icons/hicolor/scalable/apps/pigro-logo.svg
cp ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/io.github.actionschnitzel.PiGro-Aid-.appdata.xml ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/metainfo/io.github.actionschnitzel.PiGro-JCI.appdata.xml
cp ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/LICENSE ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/doc/pigro-jci/LICENSE


# Create the copyright file
cat > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/copyright << EOF
Format: https://www.debian.org/doc/packaging-manuals/copyright-format/1.0/
Upstream-Name: PiGro - Just Click It!
Source: https://github.com/actionschnitzel/PiGro-JCI

Files: *
Copyright: 2023 Timo Westphal
License: GPL-3
 This package is free software; you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, version 3.
 .
 This package is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 .
 You should have received a copy of the GNU General Public License
 along with this program. If not, see <https://www.gnu.org/licenses/>
 .
 On Debian systems, the complete text of the GNU General
 Public License version 3 can be found in "/usr/share/common-licenses/GPL-3".
EOF


# Create the control file
cat > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/DEBIAN/control << EOF
Package: $PACKAGE_NAME
Version: $VERSION
Architecture: all
Maintainer: Timo Westphal <pigroxtrmo@gmail.com>
Depends: $DEPENDENCIES
Section: misc
Priority: optional
Homepage: https://zestful-pigroxtrmo.wordpress.com/
License: GPL-3.0
Description: A system control tool for Raspberry Pi
 PiGro is a system configuration tool inspired by openSUSE's YaST
 but designed with the user-friendliness of Linux Mint in mind.
 It equips Raspberry Pi OS with graphical interfaces for tasks 
 that would otherwise require the terminal.
 PiGro is also optimized for Ubuntu, Ubuntu Mate, and MX Linux.
EOF

# Create the preinst file
cat > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/DEBIAN/preinst << 'EOF'
#!/bin/bash

# preinst script

# Save the path of the standard terminal in a temporary file
default_terminal=$(readlink -f /usr/bin/x-terminal-emulator)
echo "$default_terminal" > /tmp/default_terminal_path

# Perform further tasks here before the installation
EOF

# Create the postinst file
cat > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/DEBIAN/postinst << 'EOF'
#!/bin/bash

# postinst script

# Read the saved path from the temporary file
default_terminal_path=$(cat /tmp/default_terminal_path)

# Check and restore the path
if [ ! -z "$default_terminal_path" ] && [ "$(readlink -f /usr/bin/x-terminal-emulator)" != "$default_terminal_path" ]; then
   # Restore the previous selection
   update-alternatives --set x-terminal-emulator "$default_terminal_path"
fi

# Clean up: Remove temporary file
rm -f /tmp/default_terminal_path

# Check if /opt/PiGro-Aid-/ exists and delete it
if [ -d "/opt/PiGro-Aid-/" ]; then
    echo "Deleting directory /opt/PiGro-Aid-/"
    rm -rf "/opt/PiGro-Aid-/"
fi
EOF

# Create the .desktop file
cat > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/applications/pigro.desktop << EOL
[Desktop Entry]
Version=2.1
Exec=pigro-jci
Name=PiGro
GenericName=PiGro
Encoding=UTF-8
Terminal=false
StartupWMClass=PiGro
Type=Application
Categories=System
Icon=pigro-logo
Path=/opt/PiGro-JCI/
EOL

chmod +x ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/opt/PiGro-JCI/src/main.py

chmod +x ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/DEBIAN/preinst

find ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/opt/PiGro-JCI/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;

# Create the /bin/pigro-jci file
echo "#!/bin/bash" > ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/bin/pigro-jci
echo '/opt/PiGro-JCI/src/main.py "$@"' >>  ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/bin/pigro-jci
chmod +x ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/bin/pigro-jci


# Build the package
cd ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/
chmod -R 755 debian
chmod 644 ~/PiGro-Aid-/PIGRO-DEBIAN-BUILD-BOX/debian/usr/share/applications/pigro.desktop
sudo chown -R root:root debian

dpkg-deb --build -Zxz debian


# Move the package to the current directory
mv debian.deb ~/PiGro-Aid-/$PACKAGE_NAME-$VERSION.deb

# Clean up the temporary files
sudo rm -rf debian
