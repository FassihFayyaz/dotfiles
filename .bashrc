#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

# Zoxide changing cd as zoxide
eval "$(zoxide init --cmd cd bash)"

# 4. More ls aliases
alias ll='ls -l'
alias la='ls -Al'
alias lt='ls -ltrh'