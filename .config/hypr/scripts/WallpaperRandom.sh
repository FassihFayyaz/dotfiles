#!/bin/bash
# /* ---- 💫 https://github.com/FassihFayyaz 💫 ---- */  ##
# Script for Random Wallpaper ( CTRL ALT W)

wallDIR="$HOME/Pictures/wallpaper/"
scriptsDir="$HOME/.config/hypr/scripts"

PICS=($(find ${wallDIR} -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" \)))
RANDOMPICS=${PICS[ $RANDOM % ${#PICS[@]} ]}


# Transition config
FPS=60
TYPE="random"
DURATION=1
BEZIER=".43,1.19,1,.4"
SWWW_PARAMS="--transition-fps $FPS --transition-type $TYPE --transition-duration $DURATION --transition-bezier $BEZIER"


swww query || swww-daemon --format xrgb && swww img ${RANDOMPICS} $SWWW_PARAMS


# ${scriptsDir}/PywalSwww.sh
wal -i ${RANDOMPICS}
sleep 1
pywalfox update
${scriptsDir}/Refresh.sh 