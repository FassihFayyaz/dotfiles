#!/bin/bash
#   ___ _____ ___ _     _____   ____  _             _
#  / _ \_   _|_ _| |   | ____| / ___|| |_ __ _ _ __| |_
# | | | || |  | || |   |  _|   \___ \| __/ _` | '__| __|
# | |_| || |  | || |___| |___   ___) | || (_| | |  | |_
#  \__\_\|_| |___|_____|_____| |____/ \__\__,_|_|   \__|
#

# My screen resolution
# xrandr --rate 120

# For Virtual Machine
# xrandr --output Virtual-1 --mode 1920x1080

# Start Polkit
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

# Nitrogen
nitrogen --restore &

# Load swww daemon
#swww-daemon &

# Load picom
picom &

# Start Blue light Filter
redshift -l 55.7:12.6 -t 6000:3500 -g 0.8 -m randr -v &

# Load power manager
#xfce4-power-manager &
corectrl --toggle-manual-profile Gaming --minimize-systray &

# Load notification service
dunst &

# Setup Wallpaper and update colors
sh ~/.config/qtile/scripts/wal.sh

# Start NoiseTorch on Collar Mic
# noisetorch -i alsa_input.pci-0000_07_00.6.analog-stereo &

# Start Vesktop
vesktop &

# Load espanso
#espanso &

# Launch NM Applet
nm-applet &

# Launch copyq
copyq &

# Launch Flameshot
flameshot &
