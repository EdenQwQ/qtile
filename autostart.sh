#!/usr/bin/env bash

## Autostart Programs

# Kill already running process
_ps=(mpd, clash)
for _prs in "${_ps[@]}"; do
	if [[ `pidof ${_prs}` ]]; then
		pkill -9 ${_prs}
	fi
done

# Restore wallpaper
exec nitrogen --restore &

# Lauch compositor
# exec picom &

# Start mpd
exec mpd &

xrdb .Xresources

xinput set-prop "SYNA1D31:00 06CB:CD48 Touchpad" "Synaptics Tap Action" 0, 0, 0, 0, 1, 3, 2 &

sxhkd &

startup &
