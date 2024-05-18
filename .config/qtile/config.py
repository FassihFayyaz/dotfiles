#   ___ _____ ___ _     _____    ____             __ _       
#  / _ \_   _|_ _| |   | ____|  / ___|___  _ __  / _(_) __ _ 
# | | | || |  | || |   |  _|   | |   / _ \| '_ \| |_| |/ _` |
# | |_| || |  | || |___| |___  | |__| (_) | | | |  _| | (_| |
#  \__\_\|_| |___|_____|_____|  \____\___/|_| |_|_| |_|\__, |
#                                                      |___/  

import os
import re
import socket
import subprocess
import psutil
import json
from libqtile import hook
from libqtile import qtile
from typing import List  
from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.widget import Spacer, Backlight
from libqtile.widget.image import Image
from libqtile.dgroups import simple_key_binder
from pathlib import Path
from libqtile.log_utils import logger

from qtile_extras import widget
from qtile_extras.widget import StatusNotifier
from qtile_extras.widget.decorations import BorderDecoration



# --------------------------------------------------------
# Your configuration
# --------------------------------------------------------

# Keyboard layout in autostart.sh

# Show wlan status bar widget (set to False if wired network)
# show_wlan = True
show_wlan = False

# Show bluetooth status bar widget
# show_bluetooth = True
show_bluetooth = False

# --------------------------------------------------------
# General Variables
# --------------------------------------------------------

# Get home path
home = str(Path.home())

# --------------------------------------------------------
# Check for Desktop/Laptop
# --------------------------------------------------------

# 3 = Desktop
platform = int(os.popen("cat /sys/class/dmi/id/chassis_type").read())

# --------------------------------------------------------
# Set default apps
# --------------------------------------------------------

terminal = "alacritty"
browser = "firefox"
scrathpad_browser = "thorium-browser"
screenshot = "flameshot gui" 
wl_paste_selection_menu = "/bin/bash -c '$HOME/dotfiles/.config/qtile/scripts/ClipManager.sh'"
x11_paste_selection_menu = "copyq menu" 
file_manager = "thunar"
code_editor = "codium"

# --------------------------------------------------------
# Keybindings
# --------------------------------------------------------

mod = "mod4" # SUPER KEY

keys = [

    # Focus
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left (Vim)"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right (Vim)"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down (Vim)"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up (Vim)"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window around"),
    
    # Move
    Key([mod, "control"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "control"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.shuffle_left(), desc="Move window to the left (Vim)"),
    Key([mod, "control"], "l", lazy.layout.shuffle_right(), desc="Move window to the right (Vim)"),
    Key([mod, "control"], "j", lazy.layout.shuffle_down(), desc="Move window down (Vim)"),
    Key([mod, "control"], "k", lazy.layout.shuffle_up(), desc="Move window up (Vim)"),

    Key([mod, "shift"], "s", lazy.spawn(screenshot), desc="Take Screenshot"),
    # Size
    Key([mod, "shift"], "Left", lazy.layout.shrink(), desc="Shrink window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.grow(), desc="Grow window to the right"),
    Key([mod, "shift"], "h", lazy.layout.shrink(), desc="Shrink window to the left (Vim)"),
    Key([mod, "shift"], "l", lazy.layout.grow(), desc="Grow window to the right (Vim)"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Floating
    Key([mod], "t", lazy.window.toggle_floating(), desc='Toggle floating'),
    
    # Split
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle Layouts
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),

    # Rofi Keys/Shortcuts

    Key([mod, "control"], "Return", lazy.spawn("rofi -show drun"), desc="Run Launcher"),
    Key([mod, "shift"], "e", lazy.spawn("rofi -show emoji"), desc="Rofi Emoji"),
    Key([mod, "control"], "c", lazy.spawn("rofi -show calc"), desc="Rofi Calc"),

    # Fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    #System
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),

    # Apps
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "x", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Launch File Manager"),
    Key([mod], "o", lazy.spawn("obsidian"), desc="Launch Obsidian"),
    Key([mod], "c", lazy.spawn(code_editor), desc="Launch Code Editor"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch Browser"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle"), desc="Mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-"), desc="Lower Volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+"), desc="Raise Volume"),

    # Media Keys
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause"), desc="Play/Pause"),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop"), desc="Stop"),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next"), desc="Next"),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl prev"), desc="Previous"),

    # Misc
    Key([mod, "shift"], "w", lazy.spawn("/home/fassih/.config/qtile/scripts/wal.sh"), desc="Update Wallpaper"),
    Key([mod], "v", lazy.spawn(wl_paste_selection_menu), desc="Spawns Clipboard Manager"),
    Key([mod], "v", lazy.spawn(x11_paste_selection_menu), desc="Spawns Clipboard Manager"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("brightnessctl -q s +20%")),
    Key([], "XF86MonBrightnessDown", lazy.spawn("brightnessctl -q s 20%-"))        
]

# --------------------------------------------------------
# Groups
# --------------------------------------------------------

groups = [
    Group("1", layout='monadtall'),
    Group("2", layout='monadtall'),
    Group("3", layout='monadtall'),
    Group("4", layout='monadtall'),
    Group("5", layout='monadtall'),
    Group("6", layout='monadtall'),
    Group("7", layout='monadtall'),
    Group("8", layout='monadtall'),
    Group("9", layout='monadtall'),
]

dgroups_key_binder = simple_key_binder(mod)

# --------------------------------------------------------
# Scratchpads
# --------------------------------------------------------

groups.append(ScratchPad("6", [
    DropDown("chatgpt", scrathpad_browser+" --app=https://chat.openai.com", x=0.1, y=0.1, width=0.80, height=0.8),
    DropDown("mousepad", "mousepad", x=0.3, y=0.1, width=0.40, height=0.4, on_focus_lost_hide=False ),
    DropDown("terminal", "alacritty", x=0.3, y=0.1, width=0.40, height=0.4, on_focus_lost_hide=False ),
    DropDown("todoist", scrathpad_browser+" --app=https://todoist.com/", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
]))

keys.extend([
    Key([mod], 'F9', lazy.group["6"].dropdown_toggle("chatgpt")),
    Key([mod], 'F10', lazy.group["6"].dropdown_toggle("mousepad")),
    Key([mod], 'F11', lazy.group["6"].dropdown_toggle("terminal")),
    Key([mod, "shift"], "t", lazy.group["6"].dropdown_toggle("todoist"))
])

# --------------------------------------------------------
# Pywal Colors
# --------------------------------------------------------

colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
Color0=(colordict['colors']['color0'])
Color1=(colordict['colors']['color1'])
Color2=(colordict['colors']['color2'])
Color3=(colordict['colors']['color3'])
Color4=(colordict['colors']['color4'])
Color5=(colordict['colors']['color5'])
Color6=(colordict['colors']['color6'])
Color7=(colordict['colors']['color7'])
Color8=(colordict['colors']['color8'])
Color9=(colordict['colors']['color9'])
Color10=(colordict['colors']['color10'])
Color11=(colordict['colors']['color11'])
Color12=(colordict['colors']['color12'])
Color13=(colordict['colors']['color13'])
Color14=(colordict['colors']['color14'])
Color15=(colordict['colors']['color15'])

# --------------------------------------------------------
# Setup Layout Theme
# --------------------------------------------------------

layout_theme = { 
    "border_width": 3,
    "margin": 5,
    "border_focus": Color2,
    "border_normal": "FFFFFF",
    "single_border_width": 3
}

# --------------------------------------------------------
# Layouts
# --------------------------------------------------------

layouts = [
    layout.Max(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Floating()
]

# --------------------------------------------------------
# Setup Widget Defaults
# --------------------------------------------------------

widget_defaults = dict(
    font="JetBrainsMono Nerd Font Bold",
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

# --------------------------------------------------------
# Widgets
# --------------------------------------------------------

widget_list = [
    widget.TextBox(
        text='',
        font_size=14,
        foreground='ffffff',
        desc='',
        padding=10,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("rofi -show drun")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 0,
        fontsize = 12
    ),
    widget.GroupBox(
        highlight_method='block',
        highlight='ffffff',
        block_border='ffffff',
        highlight_color=['ffffff','ffffff'],
        block_highlight_text_color='000000',
        foreground='ffffff',
        rounded=False,
        this_current_screen_border='ffffff',
        active='ffffff'
    ),
    widget.TextBox(
                text = '|',
                foreground ='ffffff',
                padding = 2,
                fontsize = 12,
                ),
    widget.TextBox(
        text="  ",
        foreground="ffffff",
        fontsize=12,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn(browser)},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text=" ",
        foreground="ffffff",
        fontsize=12,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("thunar")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
        ),
    widget.WindowName(
        max_chars=120,
        width=800,
        padding=12,
    ),
    widget.Spacer(),
    widget.TextBox(
                text = '|',
                foreground ='ffffff',
                padding = 2,
                fontsize = 12,
    ),
    widget.Systray(
        icon_size = 12,
        padding = 8,
    ),
    # widget.StatusNotifier(
    #     icon_size = 12,
    #     padding = 8,
    # ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
    ),
    widget.Spacer(),
    widget.Spacer(),
    widget.CPU(
        padding=6,        
        measure_mem='G',
        format='  CPU: {load_percent}%',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e btop")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
        ),
    widget.Memory(
        padding=6,        
        measure_mem='G',
        format='{MemUsed: .0f}{mm}',
        fmt = '  Mem: {} used',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("alacritty -e btop")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.Spacer(length=8),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
        ),
    widget.Volume(
        padding=6, 
        fmt='  Volume: {}',
        mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("pavucontrol")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
        ),
    # widget.DF(
    #     padding=10, 
    #     background=Color8+".4",        
    #     visible_on_warn=False,
    #     format="{p} {uf}{m} ({r:.0f}%)"
    # ),
    # widget.Bluetooth(
    #     background=Color2+".4",
    #     padding=10,
    #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("blueman-manager")},
    # ),
    # widget.Wlan(
    #     background=Color2+".4",
    #     padding=10,
    #     format='{essid} {percent:2.0%}',
    #     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("alacritty -e nmtui")},
    # ),
    # widget.TextBox(
    #             text = '|',
    #             background=Color2+".4",
    #             foreground ='ffffff',
    #             padding = 2,
    #             fontsize = 14
    #             ),
    widget.Clock(
        padding=6,      
        format="  %a, %b %d - %I:%M %p",
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.TextBox(
        text = '|',
        foreground ='ffffff',
        padding = 2,
        fontsize = 12,
        ),
    widget.TextBox(
        padding=5,    
        text="",
        fontsize=12,
        mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("/bin/bash -c '$HOME/.config/qtile/scripts/powermenu.sh'")},
        decorations=[
            BorderDecoration(
                colour = Color12+".8",
                border_width = [0, 0, 2, 0],
            )
        ]
    ),
    widget.Spacer(
        length=8,
        background=Color2+".4",
        ),   
]

# Hide Modules if not on laptop
if (show_wlan == False):
    del widget_list[13:14]

if (show_bluetooth == False):
    del widget_list[12:13]

# --------------------------------------------------------
# Screens
# --------------------------------------------------------

screens = [
    Screen(
        #wallpaper='~/wallpaper/wallhaven1.jpg',
        top=bar.Bar(
            widget_list,
            30,
            padding=20,
            opacity=1.0,
            border_width=[0, 0, 0, 0],
            margin=[0,0,0,0],
            background=Color2+".4",
        ),
    ),
]

# --------------------------------------------------------
# Drag floating layouts
# --------------------------------------------------------

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

# --------------------------------------------------------
# Define floating layouts
# --------------------------------------------------------

floating_layout = layout.Floating(
    border_width=3,
    border_focus=Color2,
    border_normal="FFFFFF",
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

# --------------------------------------------------------
# General Setup
# --------------------------------------------------------

dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.

# --------------------------------------------------------
# Windows Manager Name
# --------------------------------------------------------

wmname = "QTILE"

# --------------------------------------------------------
# Hooks
# --------------------------------------------------------

# HOOK startup
@hook.subscribe.startup_once
def autostart():
    autostartscript = "~/.config/qtile/autostart.sh"
    home = os.path.expanduser(autostartscript)
    subprocess.Popen([home])

