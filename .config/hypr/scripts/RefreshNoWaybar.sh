#!/bin/bash
# /* ---- 💫 https://github.com/FassihFayyaz 💫 ---- */  ##

SCRIPTSDIR=$HOME/.config/hypr/scripts

# Define file_exists function
file_exists() {
    if [ -e "$1" ]; then
        return 0  # File exists
    else
        return 1  # File does not exist
    fi
}


# for cava-pywal (note, need to manually restart cava once wallpaper changes)
ln -sf "$HOME/.cache/wal/cava-colors" "$HOME/.config/cava/config" || true

exit 0