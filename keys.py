from libqtile.command import lazy
from libqtile.config import Key, KeyChord
from settings import default_apps
from function import Functions

# Default mod keys
mod0 = ['mod4']
mod1 = ['mod1']
mod2 = ['mod4', 'shift']
mod3 = ['mod4', 'control']

# Default applications
mybrowser = default_apps['browser']
myterminal = default_apps['terminal']
myeditor = default_apps['editor']
myfm = default_apps['file']

# Keys
keys = [

    # Keychord
    KeyChord(mod0, 't', [
        Key([], 'h', lazy.layout.swap_left()),
        Key([], 'l', lazy.layout.swap_right()),
        Key([], 'j', lazy.layout.shuffle_down()),
        Key([], 'k', lazy.layout.shuffle_up()),
    ],
             mode = 'move'
             ),
    KeyChord(mod0, 'r', [
        Key([], 'w', lazy.spawn(mybrowser)),
        Key([], 'e', lazy.spawn(myeditor)),
        Key([], 'f', lazy.spawn(myfm)),
        Key([], 'n', lazy.spawn('nitrogen')),
        Key([], 't', lazy.spawn('thunar admin:/')),
    ],
             mode = 'run'
             ),
    KeyChord(mod0, 'o', [
        Key([], 'q', lazy.spawn('kitty .config/qtile')),
        Key([], 'c', lazy.spawn('kitty .config')),
    ],
             mode = 'open'
             ),

    # Layout hotkeys
    Key(mod0, 'h', lazy.layout.shrink_main()),
    Key(mod0, 'l', lazy.layout.grow_main()),
    Key(mod0, 'j', lazy.layout.down()),
    Key(mod0, 'k', lazy.layout.up()),
    Key(mod2, 'h', lazy.layout.swap_left()),
    Key(mod2, 'l', lazy.layout.swap_right()),
    Key(mod2, 'j', lazy.layout.shuffle_down()),
    Key(mod2, 'k', lazy.layout.shuffle_up()),
    Key(mod0, 'f', lazy.layout.maximize()),
    Key(mod2, 'n', lazy.layout.normalize()),
    Key(mod2, 'space', lazy.layout.flip()),

    # Window hotkeys
    Key(mod0, 'space', lazy.next_layout()),
    Key(mod0, 'q', lazy.window.kill()),
    Key(mod2, 'q', Functions.kill_all_windows()),
    Key(mod2, 'o', Functions.kill_all_windows_minus_current()),
    Key(mod2, 'space', lazy.window.toggle_floating()),

    # Spec hotkeys
    Key(mod0, 'Return', lazy.spawn(myterminal)),
    Key(mod3, 'r', lazy.restart()),
    Key(mod3, 'q', lazy.shutdown()),

    # Apps hotkeys
    Key(mod2, 'f', lazy.spawn(myfm)),
    Key(mod2, 'w', lazy.spawn(mybrowser)),

    # Rofi
    Key(mod0, 'p', lazy.spawn('.config/qtile/rofi/bin/launcher')),
    Key(mod0, 's', lazy.spawn('.config/qtile/rofi/bin/screenshot')),
    Key(mod0, 'w', lazy.spawn('.config/qtile/rofi/bin/windows')),
    Key(mod0, 'x', lazy.spawn('.config/qtile/rofi/bin/powermenu')),

]
