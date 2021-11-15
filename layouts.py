from libqtile import layout
from libqtile.config import Match
from function import colors
from settings import margin

# Default layout values
layouts_default = dict(
        border_normal = colors[4],
        border_focus = colors[2],
        border_width = 6,
        margin = margin
)

# Layouts
layouts = [
    layout.MonadTall(
        **layouts_default
    ),
    layout.MonadWide(**layouts_default),
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
