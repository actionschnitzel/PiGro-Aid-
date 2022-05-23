#!/bin/bash

if grep -Fxq "First_Run = True" $HOME/PiGro-Aid-/scripts/PiGro.conf
then
	python3 ~/PiGro-Aid-/splash.py
	python3 ~/PiGro-Aid-/pigro_main.py
	print "First_Run = True"

else
	python3 ~/PiGro-Aid-/pigro_main.py
	print "First_Run = False"
# code if not found
fi

# Needs to be implemented
#sudo $(python3 ~/PiGro-Aid-/pigro_main.py)