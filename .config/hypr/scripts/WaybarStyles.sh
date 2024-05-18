#!/bin/bash
# /* ---- 💫 https://github.com/FassihFayyaz 💫 ---- */  ##
# Script for waybar styles

set -euo pipefail
IFS=$'\n\t'

# Define directories
waybar_styles="$HOME/.config/waybar/style"
waybar_style="$HOME/.config/waybar/style.css"
SCRIPTSDIR="$HOME/.config/hypr/scripts"
wofi_config="$HOME/.config/wofi/config"

# Function to display menu options
menu() {
    options=()
    while IFS= read -r file; do
        if [ -f "$waybar_styles/$file" ]; then
            options+=("$(basename "$file" .css)")
        fi
    done < <(find "$waybar_styles" -maxdepth 1 -type f -name '*.css' -exec basename {} \; | sort)
    
    printf '%s\n' "${options[@]}"
}

# Apply selected style
apply_style() {
    ln -sf "$waybar_styles/$1.css" "$waybar_style"
    restart_waybar_if_needed
}

# Restart Waybar if it's running
restart_waybar_if_needed() {
    if pgrep -x "waybar" >/dev/null; then
        pkill waybar
        sleep 0.1  # Delay for Waybar to completely terminate
    fi
    "${SCRIPTSDIR}/Refresh.sh" &
}

# Main function
main() {
    choice=$(menu | wofi -i -dmenu -config "$wofi_config")

    if [[ -z "$choice" ]]; then
        echo "No option selected. Exiting."
        exit 0
    fi

    apply_style "$choice"
}

# Kill Wofi if already running before execution
if pgrep -x "wofi" >/dev/null; then
    pkill wofi
    exit 0
fi

main
