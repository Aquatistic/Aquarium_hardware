# Aquarium_hardware

## How to auto start Project
To start project automatically after RPI boot you need to input this command *sudo crontab -e*, then choose editor of your choice. After file opens place this line at the end:
*@reboot /bin/sleep 10; . /home/\<user\>/\<Project destination\>/AquariumLauncher.sh >> \<log file name\>*.

Now you need to file project destination info in the AquariumLauncher.sh file. After that auarium should start automatically on boot.
