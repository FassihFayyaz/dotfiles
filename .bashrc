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
PS1='[\u@\h \W]\$ '

# -----------------------------------------------------
# SETTING UP XDG and Other Environment Variable
# -----------------------------------------------------

export EDITOR="micro"
export BROWSER="firefox"
export XDG_CONFIG_HOME=$HOME/.config
export XDG_CACHE_HOME=$HOME/.cache
export XDG_DATA_HOME=$HOME/.local/share
export XDG_STATE_HOME=$HOME/.local/state
export KODI_DATA=$XDG_DATA_HOME/kodi
export OLLAMA_MODELS=$XDG_DATA_HOME/ollama/models
export QT_QPA_PLATFORMTHEME="qt5ct"
export NPM_CONFIG_USERCONFIG=$XDG_CONFIG_HOME/npm/npmrc
export NODE_REPL_HISTORY="$XDG_DATA_HOME"/node_repl_history

# -----------------------------------------------------
# Aliases
# -----------------------------------------------------

alias bashrc="micro ~/.bashrc"
alias update="paru -Syu"
alias count="ls * | wc -l"
alias sumi="sudo micro"
alias c='clear'
alias ff='fastfetch'
alias shutdown='systemctl poweroff'
alias matrix='cmatrix'
alias mi='micro'
alias update-mirrors='rate-mirrors arch | sudo tee /etc/pacman.d/mirrorlist'
alias update-grub='sudo grub-mkconfig -o /boot/grub/grub.cfg'
alias Qtile='startx'

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
# Sudo last command
# -----------------------------------------------------

s() { # do sudo, or sudo the last command if no argument given
    if [[ $# == 0 ]]; then
        sudo $(history -p '!!')
    else
        sudo "$@"
    fi
}

alias lutris="gamescope -w 1920 -h 1080 /bin/lutris & /usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 & corectrl --toggle-manual-profile Gaming --minimize-systray &"


# -----------------------------------------------------
# Added conda to path
# -----------------------------------------------------

[ -f /opt/miniconda3/etc/profile.d/conda.sh ] && source /opt/miniconda3/etc/profile.d/conda.sh

# -----------------------------------------------------
# Zoxide - Replacing cd
# -----------------------------------------------------

eval "$(zoxide init --cmd cd bash)"

# -----------------------------------------------------
# START STARSHIP
# -----------------------------------------------------

eval "$(starship init bash)"

# -----------------------------------------------------
# PYWAL
# -----------------------------------------------------

cat ~/.cache/wal/sequences

# -----------------------------------------------------
# Easy extract
# -----------------------------------------------------
function extract {
    if [ $# -eq 0 ]; then
        # display usage if no parameters given
        echo "Usage: extract <path/file_name>.<zip|rar|bz2|gz|tar|tbz2|tgz|Z|7z|xz|ex|tar.bz2|tar.gz|tar.xz|.zlib|.cso|.zst>"
        echo "       extract <path/file_name_1.ext> [path/file_name_2.ext] [path/file_name_3.ext]"
    fi
    for n in "$@"; do
        if [ ! -f "$n" ]; then
            echo "'$n' - file doesn't exist"
            return 1
        fi

        case "${n%,}" in
        *.cbt | *.tar.bz2 | *.tar.gz | *.tar.xz | *.tbz2 | *.tgz | *.txz | *.tar)
            tar zxvf "$n"
            ;;
        *.lzma) unlzma ./"$n" ;;
        *.bz2) bunzip2 ./"$n" ;;
        *.cbr | *.rar) unrar x -ad ./"$n" ;;
        *.gz) gunzip ./"$n" ;;
        *.cbz | *.epub | *.zip) unzip ./"$n" ;;
        *.z) uncompress ./"$n" ;;
        *.7z | *.apk | *.arj | *.cab | *.cb7 | *.chm | *.deb | *.iso | *.lzh | *.msi | *.pkg | *.rpm | *.udf | *.wim | *.xar | *.vhd)
            7z x ./"$n"
            ;;
        *.xz) unxz ./"$n" ;;
        *.exe) cabextract ./"$n" ;;
        *.cpio) cpio -id <./"$n" ;;
        *.cba | *.ace) unace x ./"$n" ;;
        *.zpaq) zpaq x ./"$n" ;;
        *.arc) arc e ./"$n" ;;
        *.cso) ciso 0 ./"$n" ./"$n.iso" &&
            extract "$n.iso" && \rm -f "$n" ;;
        *.zlib) zlib-flate -uncompress <./"$n" >./"$n.tmp" &&
            mv ./"$n.tmp" ./"${n%.*zlib}" && rm -f "$n" ;;
        *.dmg)
            hdiutil mount ./"$n" -mountpoint "./$n.mounted"
            ;;
        *.tar.zst) tar -I zstd -xvf ./"$n" ;;
        *.zst) zstd -d ./"$n" ;;
        *)
            echo "extract: '$n' - unknown archive method"
            return 1
            ;;
        esac
    done
}

# -----------------------------------------------------
# Check if in a direct TTY (e.g., /dev/tty1) and Xorg is not running
# -----------------------------------------------------

if [[ "$(tty)" = "/dev/tty1" ]]; then
    startx
else
    fastfetch
fi

# -----------------------------------------------------
# END
# -----------------------------------------------------
