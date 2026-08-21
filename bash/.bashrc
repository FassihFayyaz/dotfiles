#    _               _
#   | |__   __ _ ___| |__  _ __ ___
#   | '_ \ / _` / __| '_ \| '__/ __|
#  _| |_) | (_| \__ \ | | | | | (__
# (_)_.__/ \__,_|___/_| |_|_|  \___|
#
# by FassihFayyaz
# -----------------------------------------------------
# ~/.bashrc
# -----------------------------------------------------

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

# -----------------------------------------------------
# System
# -----------------------------------------------------
# Source global definitions
if [ -f /etc/bashrc ]; then
    . /etc/bashrc
fi

# -----------------------------------------------------
# Environment
# -----------------------------------------------------
# User specific environment
if ! [[ "$PATH" =~ "$HOME/.local/bin:$HOME/bin:" ]]; then
    PATH="$HOME/.local/bin:$HOME/bin:$PATH"
fi
export PATH

# OpenCode
export PATH=/home/fassih/.opencode/bin:$PATH

# -----------------------------------------------------
# XDG Base Directory
# -----------------------------------------------------
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share
export XDG_STATE_HOME=$HOME/.local/state
export KODI_DATA=$XDG_DATA_HOME/kodi
export OLLAMA_MODELS=$XDG_DATA_HOME/ollama/models
export QT_QPA_PLATFORMTHEME="qt5ct"

# Uncomment the following line if you don't like systemctl's auto-paging feature:
# export SYSTEMD_PAGER=

# -----------------------------------------------------
# Aliases & Functions
# -----------------------------------------------------
# Aliases
alias bashrc="micro ~/.bashrc"
alias update="sudo dnf upgrade"
alias count="ls * | wc -l"
alias sumi="sudo micro"
alias c='clear'
alias ff='fastfetch'
alias shutdown='systemctl poweroff'
alias matrix='cmatrix'
alias mi='micro'
alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'

# -----------------------------------------------------
# More ls aliases
# -----------------------------------------------------
alias ls='eza -a --icons'
alias ll='eza -al --icons'
alias lt='eza -a --tree --level=1 --icons'

# -----------------------------------------------------
# GIT
# -----------------------------------------------------
alias gs="git status"
alias ga="git add"
alias gc="git commit -m"
alias gp="git push"
alias gpl="git pull"
alias gst="git stash"
alias gsp="git stash; git pull"
alias gcheck="git checkout"
alias gcredential="git config credential.helper store"

# -----------------------------------------------------
# Functions
# -----------------------------------------------------
# Sudo last command
s() { # do sudo, or sudo the last command if no argument given
    if [[ $# == 0 ]]; then
        sudo $(history -p '!!')
    else
        sudo "$@"
    fi
}

# User specific aliases and functions
if [ -d ~/.bashrc.d ]; then
    for rc in ~/.bashrc.d/*; do
        if [ -f "$rc" ]; then
            . "$rc"
        fi
    done
fi
unset rc

# -----------------------------------------------------
# Prompt
# -----------------------------------------------------
# Starship prompt (overrides PS1 below)
eval "$(starship init bash)"

# Default PS1 (unused when Starship is active)
PS1='[\u@\h \W]\$ '
# -----------------------------------------------------
# Check if in a direct TTY (e.g., /dev/tty1) and Xorg is not running
# -----------------------------------------------------

if [[ "$(tty)" = "/dev/tty1" ]]; then
    startx
else
    fastfetch
fi

# -----------------------------------------------------
# Zoxide - Init & Replacing cd
# -----------------------------------------------------

eval "$(zoxide init --cmd cd bash)"

. "$HOME/.local/share/../bin/env"
