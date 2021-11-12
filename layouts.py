from libqtile import layout
from libqtile.config import Match
from function import colors
import os
from settings import margin

# Default layout values
layouts_default = dict(
        border_normal = colors[0],
        border_focus = colors[5],
        border_width = 6,
        margin = margin
)

# Layouts
layouts = [
    # layout.Bsp(
    #     **layouts_default
    # ),
    layout.MonadTall(
        **layouts_default
        # ratio = 0.70,
        # single_border_width = 4
    ),
    layout.MonadWide(**layouts_default),
    # layout.Stack(stack = 3,**layouts_default),
    # layout.Columns(),
    # layout.RatioTile(**layouts_default),
    # layout.Tile(**layouts_default),
    # layout.VerticalTile(),
    # layout.Matrix(),
    # layout.Zoomy(),
    # layout.Max(**layouts_default),
    layout.Floating(**layouts_default)
]

# Floating layout
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="Nitrogen"),
        Match(wm_class="pcmanfm"),
        Match(wm_class="GParted"),
    ],
    **layouts_default
)
