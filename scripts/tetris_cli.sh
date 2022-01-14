cd
sudo apt install libncursesw5-dev

git clone 'https://github.com/k-vernooy/tetris' && cd tetris

make

sudo make install

clear

echo "taken from:https://github.com/k-vernooy/tetris"

echo "Controles in the link"

echo "Start game by: tetris"

echo '                                                                     
    ____  _ ______              ____           __        ____         
   / __ \(_) ____/________     /  _/___  _____/ /_____ _/ / /__  _____
  / /_/ / / / __/ ___/ __ \    / // __ \/ ___/ __/ __ `/ / / _ \/ ___/
 / ____/ / /_/ / /  / /_/ /  _/ // / / (__  ) /_/ /_/ / / /  __/ /    
/_/   /_/\____/_/   \____/  /___/_/ /_/____/\__/\__,_/_/_/\___/_/     
                                                                      '

echo  '
 ____ ____ ____ ____ _________ ____ 
||D |||O |||N |||E |||       |||! ||
||__|||__|||__|||__|||_______|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|'

printf '\e[38;5;46m You can close this window now\n'

read -p "......Press Enter"