# QtileConfig
## **My qtile config with a fresh-looking bar and pywal support.**

>_Note: This is my first rice. Please excuse my poor coding style and poor
English._
Based on the official example config  
Using [void linux](https://voidlinux.org) with glibc and runnit

### Dependences
* [qtile](http://www.qtile.org)
* [pywal](https://github.com/dylanaraps/pywal)
* [rofi](https://github.com/davatorium/rofi)
* [kitty](https://sw.kovidgoyal.net/kitty/)
* [nitrogen](http://projects.l3ib.org/nitrogen/)

```sh
# Replace 'xbps-install -S' with 'apt install' 'pacman -S' etc.
sudo xbps-install -S rofi kitty nitrogen

pip install qtile

pip install pywal pywalfox python-mpd2
```

### Getting started

1. Clone this repo
```sh
git clone https://github.com/EdenQwQ/qtile.git
```

2. Copy the config files
```sh
cp -r ~/qtile ~/.config/
```

3. Make sure you've checked the keybindings in keys.py, widgets in widgets.py,
   settings in settings.py.

### Etc

To generate pywal colorscheme, set your wallpaper with nitrogen and run <code>~/.config/qtile/pywal.sh</code>
