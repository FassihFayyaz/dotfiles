# Dotfiles

Personal dotfiles for my Arch Linux + niri + Noctalia setup.

## What's included

- **niri** — compositor config (split into `cfg/*.kdl`)
- **alacritty** — terminal config + Noctalia theme
- **fastfetch** — system info config + Noctalia theme
- **bash** — `.bashrc`
- **starship** — prompt config
- **Thunar** — file manager settings
- **gtk-3.0 / gtk-4.0** — GTK theming (Noctalia)
- **qt5ct / qt6ct** — Qt theming (Noctalia)
- **nwg-look** — GTK appearance settings
- **mpv** — media player config
- **xfce4** — Thunar helper settings

## Install

Clone and symlink with GNU Stow:

```bash
git clone https://github.com/FassihFayyaz/dotfiles.git ~/dotfiles
cd ~/dotfiles
stow -t ~ */
```

Each subdirectory mirrors the home directory layout. Stow symlinks them into `~`.

## Related

- [ArchFassih](https://github.com/FassihFayyaz/ArchFassih) — install script for the full system
