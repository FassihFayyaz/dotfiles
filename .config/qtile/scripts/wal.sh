#!/bin/bash

wallDIR="$HOME/wallpaper/"

# Get Random wallpaper name

PICS=($(find ${wallDIR} -type f \( -name "*.jpg" -o -name "*.jpeg" -o -name "*.png" -o -name "*.gif" \)))
RANDOMPICS=${PICS[ $RANDOM % ${#PICS[@]} ]}


# Transition config
FPS=60
TYPE="random"
DURATION=1
BEZIER=".43,1.19,1,.4"
SWWW_PARAMS="--transition-fps $FPS --transition-type $TYPE --transition-duration $DURATION --transition-bezier $BEZIER"


# Set wallpaper
swww query || swww-daemon --format xrgb && swww img ${RANDOMPICS} $SWWW_PARAMS

wal -i ${RANDOMPICS}

qtile cmd-obj -o cmd -f reload_config

pywalfox update