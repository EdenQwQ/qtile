import os
from libqtile.command import lazy
from settings import theme

# load colors
colors = []

def load_colors(cache):
    with open(cache, 'r') as file:
        for i in range(16):
            colors.append(file.readline().strip())
    colors.append('#ffffff')

if theme == "pywal":
    cache = os.path.expanduser('~')+'/.cache/wal/colors'
else:
    cache = os.path.expanduser('~')+'/.config/qtile/themes/'+theme

load_colors(cache)


class Functions:
    @staticmethod
    def kill_all_windows():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                window.kill()

        return __inner

    @staticmethod
    def kill_all_windows_minus_current():
        @lazy.function
        def __inner(qtile):
            for window in qtile.current_group.windows:
                if window != qtile.current_window:
                    window.kill()

        return __inner
