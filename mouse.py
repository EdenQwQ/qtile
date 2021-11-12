from libqtile.command import lazy
from libqtile.config import Drag, Click
from keys import mod0, mod1
# Mouse
mouse = [
    Drag(mod0, 'Button1', lazy.window.set_position_floating(),
        start = lazy.window.get_position()),
    Drag(mod0, 'Button3', lazy.window.set_size_floating(),
        start = lazy.window.get_size()),
]
