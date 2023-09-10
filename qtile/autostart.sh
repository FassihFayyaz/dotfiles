#!/usr/bin/env bash 

if [[ $(systemd-detect-virt) = "none" ]]; then
    echo "Not running in a Virtual Machine";
elif xrandr | grep "1366x768"; then
    xrandr -s 1366x768 || echo "Cannot set 1366x768 resolution.";
elif xrandr | grep "1920x1080"; then
    xrandr -s 1920x1080 || echo "Cannot set 1920x1080 resolution.";
else echo "Could not set a resolution."
fi

/home/fassih/.local/bin/rnnoise activate
flameshot &
picom &
copyq &
dunst &
psensor &
nitrogen --restore &
flatpak run org.qbittorrent.qBittorrent &
flatpak run com.discordapp.Discord &