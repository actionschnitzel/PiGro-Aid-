#!/bin/bash

if  grep -q 'NAME="Ubuntu"' "/etc/os-release" ; then
	echo 'Using Ubuntu Config Path' ; 
	cd /boot/firmware/

	sed -i '/arm_freq/d' config.txt
	sed -i '/gpu_freq/d' config.txt
	sed -i '/over_voltage/d' config.txt
	sed -i '/force_turbo/d' config.txt
	sed -i '/disable_splash/d' config.txt

	sed -i '/#Pigro_Overclocking1/d' config.txt
	sed -i '/#Pigro_Overclocking2/d' config.txt
	sed -i '/#Pigro_Overclocking3/d' config.txt
	sed -i '/#Pigro_Overclocking4/d' config.txt
	sed -i '/#Pigro_Custom/d' config.txt

else
	echo 'Using Debian Config Path' ; 
	cd /boot/

	sed -i '/arm_freq/d' config.txt
	sed -i '/gpu_freq/d' config.txt
	sed -i '/over_voltage/d' config.txt
	sed -i '/force_turbo/d' config.txt
	sed -i '/disable_splash/d' config.txt

	sed -i '/#Pigro_Overclocking1/d' config.txt
	sed -i '/#Pigro_Overclocking2/d' config.txt
	sed -i '/#Pigro_Overclocking3/d' config.txt
	sed -i '/#Pigro_Overclocking4/d' config.txt
	sed -i '/#Pigro_Custom/d' config.txt
	
fi


