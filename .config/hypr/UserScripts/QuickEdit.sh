#!/bin/bash
# Rofi menu for Quick Edit / View of Settings (SUPER E)

configs="$HOME/.config/hypr/configs"
UserConfigs="$HOME/.config/hypr/UserConfigs"

menu(){
  printf "1. view Env-variables\n"
  printf "2. view Window-Rules\n"
  printf "3. view Startup_Apps\n"
  printf "4. view User-Keybinds\n"
  printf "5. view Monitors\n"
  printf "6. view Laptop-Keybinds\n"
  printf "7. view User-Settings\n"
  printf "8. view Workspace-Rules\n"
  printf "9. view Default-Settings\n"
  printf "10. view Default-Keybinds\n"
}

main() {
    choice=$(menu | rofi -i -dmenu -config ~/.config/rofi/config.rasi | cut -d. -f1)
    case $choice in
        1)
            kitty -e micro "$UserConfigs/ENVariables.conf"
            ;;
        2)
            kitty -e micro "$UserConfigs/WindowRules.conf"
            ;;
        3)
            kitty -e micro "$UserConfigs/Startup_Apps.conf"
            ;;
        4)
            kitty -e micro "$UserConfigs/UserKeybinds.conf"
            ;;
        5)
            kitty -e micro "$UserConfigs/Monitors.conf"
            ;;
        6)
            kitty -e micro "$UserConfigs/Laptops.conf"
            ;;
        7)
            kitty -e micro "$UserConfigs/UserSettings.conf"
            ;;
        8)
            kitty -e micro "$UserConfigs/WorkspaceRules.conf"
            ;;
		9)
            kitty -e micro "$configs/Settings.conf"
            ;;
        10)
            kitty -e micro "$configs/Keybinds.conf"
            ;;
        *)
            ;;
    esac
}

main