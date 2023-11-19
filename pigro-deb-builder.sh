#!/bin/bash



# Define the package name and version
PACKAGE_NAME="pigro-jci"
VERSION="24.01"

# Define the dependencies
DEPENDENCIES="xterm, python3-pil, python3-pil.imagetk, python3-pip, python3-psutil, python3-distro, python3-bs4, python3-dev, python3-requests, mpg123, lolcat, wmctrl, gdebi, mousepad"

# Create the necessary directories
mkdir -p ~/debian/DEBIAN
mkdir -p ~/debian/opt/PiGro-Aid-

rsync -av --exclude='.git' --exclude='.github' --exclude='start.sh' --exclude='.vscode' ~/PiGro-Aid-/ ~/debian/opt/PiGro-Aid-





# Create the control file
cat > debian/DEBIAN/control << EOF
Package: $PACKAGE_NAME
Version: $VERSION
Architecture: all
Maintainer: Timo Westphal <pigroxtrmo@gmail.com>
Depends: $DEPENDENCIES
Description: A system control tool for Raspberry Pi
EOF


# Create the post-installation script
cat > debian/DEBIAN/postinst << EOF
#!/bin/bash

# Source debconf library.
. /usr/share/debconf/confmodule

chmod +x /opt/PiGro-Aid-/src/main.py

# Create /bin/pigro with content "/opt/PiGro-Aid-/src/main.py"
echo "#!/bin/bash" > /bin/pigro
echo '/opt/PiGro-Aid-/src/main.py "$@"' >> /bin/pigro
chmod +x /bin/pigro

cp -f /opt/PiGro-Aid-/images/icons/logo.png /local/share/icons/pigro.png

# Create the desktop file
cat > /usr/share/applications/pigro.desktop << EOL
[Desktop Entry]
Version=2.1
Exec=pigro
Name=PiGro
GenericName=PiGro
Encoding=UTF-8
Terminal=false
Type=Application
Categories=System
Icon=/opt/PiGro-Aid-/images/icons/logo.png
Path=/opt/PiGro-Aid-/
EOL

find /opt/PiGro-Aid-/scripts/ -type f -iname "*.sh" -exec chmod +x {} \;

db_stop
EOF

# Create the pre-removal script
cat > debian/DEBIAN/prerm << EOF
#!/bin/bash
echo "Removing $PACKAGE_NAME..."
EOF

# Create the post-removal script
cat > debian/DEBIAN/postrm << EOF
#!/bin/bash

rm -rf /usr/share/applications/pigro.desktop
rm -rf /bin/pigro 
EOF

# Make the scripts executable
chmod +x debian/DEBIAN/postinst debian/DEBIAN/prerm debian/DEBIAN/postrm

# Build the package
dpkg-deb --build debian

# Move the package to the current directory
mv debian.deb $PACKAGE_NAME-$VERSION.deb

# Clean up the temporary files
rm -rf debian
