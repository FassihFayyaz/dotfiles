#! /bin/sh

chosen=$(printf "Power Off\nReboot\nLog Out\nSuspend" | rofi -dmenu -i -p "Power Menu")
case $chosen in
    "Power Off") poweroff ;;
    "Reboot") reboot ;;
    "Log Out") i3-msg exit ;;
    "Suspend") systemctl suspend ;;
esac