#!/bin/bash
rm -f ${HOME}/patcher/src/latest.txt
rm -f ${HOME}/patcher/install.sh
if [ "$1" == "--remove" ]; then
	cd ${HOME}
	./patcher/uninstall.sh
fi

if [ "$1" == "--update" ]; then
	cd ${HOME}
	./patcher/upgradepatcher.sh
fi

if [ "$1" == "--nogui" ]; then
	cd ${HOME}/patcher/src/
	python3 main.py ${HOME} 1 1
fi

if [ "$1" == "" ]; then
	cd ${HOME}/patcher/src/
	python3 main.py ${HOME} 0 0 > log.txt
fi


read -p "Done! C YA!......Press Enter after update is finished"