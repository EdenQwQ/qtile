from libqtile import bar, widget
from libqtile.config import Screen
from workspaces import get_workspace_groups, wsp
from function import colors
from settings import decor, colored, margin, reverse, font, mywidgets, opacity, size, decor_size, position, border_width
import iwlib

widget_defaults = dict(
        font = font,
        fontsize = 28,
        padding = 3,
)


decor = widget.TextBox(
        text = decor,
        fontsize = decor_size,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'decor' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'decor' in reverse else colors[0],
)

battery = widget.Battery(
        low_foreground = colors[0] if colored == 'full' or colored == 'compact' and 'battery' in reverse else colors[7],
        format = '{percent:2.0%} {hour:d}:{min:02d}',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'battery' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'battery' in reverse else colors[0],
        padding = 40
        )

mpd2 = widget.Mpd2(
        status_format = '{play_status}  {artist}-{title}',
        play_states = {'pause': '', 'play': '', 'stop': ''},
        max_chars = 20,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'mpd2' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'mpd2' in reverse else colors[0],
        )

groupbox = widget.GroupBox(
        hide_unused = True,
        border_width = 2,
        disable_drag = True,
        highlight_method = 'block',
        inactive = colors[8],
        active = colors[0] if colored == 'full' or colored == 'compact' and 'groupbox' in reverse else colors[7],
        highlight_color = colors[1],
        # highlight_method = 'line',
        this_current_screen_border = colors[0] if colored == 'full' or colored == 'compact' and 'groupbox' in reverse else colors[7],
        # this_screen_border = colors [4],
        # other_current_screen_border = colors[6],
        # other_screen_border = colors[4],
        padding = 10,
        margin_x = 20,
        block_highlight_text_color = colors[7] if colored == 'full' or colored == 'compact' and 'groupbox' in reverse else colors[0],
        visible_groups = get_workspace_groups(wsp['current']),
        spacing = 0,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'groupbox' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'groupbox' in reverse else colors[0],
        )

windowname = widget.WindowName(
        max_chars = 20,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'windowname' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'windowname' in reverse else colors[0],
        )

volume_icon = widget.TextBox(
       text = '墳 ',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'volume_icon' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'volume_icon' in reverse else colors[0],
        )

volume = widget.Volume(
        update_interval = 0,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'volume' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'volume' in reverse else colors[0],
        )

wlan_icon = widget.TextBox(
        text = ' 直 ',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'wlan_icon' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'wlan_icon' in reverse else colors[0],
        )

wlan = widget.Wlan(
        format = '{essid}',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'wlan' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'wlan' in reverse else colors[0],
        )

net = widget.Net(
        interface = 'wlan0',
        format = '{down} ↓↑{up} ',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'net' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'net' in reverse else colors[0],
        )

clock = widget.Clock(
        format = '%a %b %d, %H:%M',
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'clock' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'clock' in reverse else colors[0],
        )

chord = widget.Chord(
        padding = 20,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'chord' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'chord' in reverse else colors[0],
        )

currentlayout = widget.CurrentLayout(
        padding = 40,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'currentlayout' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'currentlayout' in reverse else colors[0],
        )
net_fold = widget.WidgetBox(
        widgets = [
                widget.Net(
                        interface = 'wlan0',
                        format = '{down} ↓↑{up} ',
                        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'net' in reverse else colors[7],
                        background = colors[7] if colored == 'full' or colored == 'compact' and 'net' in reverse else colors[0],
                )
        ],
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'net_fold' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'net_fold' in reverse else colors[0],
        text_closed = ' [<] ',
        text_open = ' [>] '
)
weather = widget.Wttr(
        location={
                'Ningbo': 'Ningbo',
        },
        format = '%l %c %t %m',
        padding = 20,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'weather' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'weather' in reverse else colors[0],
)
windowtabs = widget.WindowTabs(
        max_chars = 65,
        padding = 20,
        foreground = colors[0] if colored == 'full' or colored == 'compact' and 'windowtabs' in reverse else colors[7],
        background = colors[7] if colored == 'full' or colored == 'compact' and 'windowtabs' in reverse else colors[0],
)

# Load widgets from settings
widgets = []
for wid in mywidgets:
        widgets.append(eval(wid))

screen = Screen(
        top = bar.Bar(
                widgets,
                size = size,
                background = colors[0],
                opacity = opacity,
                border_width = border_width,
                margin = [margin,margin,0,margin],
                border_color = colors[7]
        ),
)

if position == "bottom" :
        screen = Screen(
                bottom = bar.Bar(
                        widgets,
                        size = size,
                        background = colors[0],
                        opacity = opacity,
                        border_width = border_width,
                        margin = [0,margin,margin,margin],
                        border_color = colors[7]
                ),
        )
screens = [
        screen
]

