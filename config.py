'''
     QQQQQQQQQ              tttt            iiii  lllllll
   QQ:::::::::QQ         ttt:::t           i::::i l:::::l
 QQ:::::::::::::QQ       t:::::t            iiii  l:::::l
Q:::::::QQQ:::::::Q      t:::::t                  l:::::l
Q::::::O   Q::::::Qttttttt:::::ttttttt    iiiiiii  l::::l     eeeeeeeeeeee
Q:::::O     Q:::::Qt:::::::::::::::::t    i:::::i  l::::l   ee::::::::::::ee
Q:::::O     Q:::::Qt:::::::::::::::::t     i::::i  l::::l  e::::::eeeee:::::ee
Q:::::O     Q:::::Qtttttt:::::::tttttt     i::::i  l::::l e::::::e     e:::::e
Q:::::O     Q:::::Q      t:::::t           i::::i  l::::l e:::::::eeeee::::::e
Q:::::O     Q:::::Q      t:::::t           i::::i  l::::l e:::::::::::::::::e
Q:::::O  QQQQ:::::Q      t:::::t           i::::i  l::::l e::::::eeeeeeeeeee
Q::::::O Q::::::::Q      t:::::t    tttttt i::::i  l::::l e:::::::e
Q:::::::QQ::::::::Q      t::::::tttt:::::ti::::::il::::::le::::::::e
 QQ::::::::::::::Q       tt::::::::::::::ti::::::il::::::l e::::::::eeeeeeee
   QQ:::::::::::Q          tt:::::::::::tti::::::il::::::l  ee:::::::::::::e
     QQQQQQQQ::::QQ          ttttttttttt  iiiiiiiillllllll    eeeeeeeeeeeeee
             Q:::::Q
              QQQQQQ
'''

from libqtile import hook
import os, subprocess
import widgets, keys, workspaces, layouts, mouse

# Load
widget_defaults = widgets.widget_defaults
screens = widgets.screens
keys = keys.keys
groups = workspaces.groups
floating_layout = layouts.floating_layout
layouts = layouts.layouts
mouse = mouse.mouse

# Misc
dgroups_key_binder = None
dgroups_app_rules = []
main = None
follow_mouse_focus = True
bring_front_click = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
extentions = []
wmname = 'LG3D'

auto_fullscreen = True
focus_on_window_activation = "smart"

# Startup
@hook.subscribe.startup_once
def autostart():
  home = os.path.expanduser('~/.config/qtile/autostart.sh')
  subprocess.call([home])
