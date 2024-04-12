#! /bin/sh

chosen=$(printf "Power Off\nReboot\nLog Out\nSuspend" | rofi -dmenu -i -p "Power Menu")
case $chosen in
    "Power Off") poweroff ;;
    "Reboot") reboot ;;
    "Log Out") qtile cmd-obj -o cmd -f shutdown ;;
    "Suspend") systemctl suspend ;;
esac