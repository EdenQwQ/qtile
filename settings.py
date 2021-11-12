# Global margin for windows and the bar
margin = 40

## BAR SETTINGS ##

size = 100
opacity = 0.6
# Determine the bar color style. Choose from 'none', 'full', 'compact'
colored = 'compact'
# Arrange the widget order
mywidgets = ['currentlayout', 'chord','decor', 'mpd2', 'decor', 'groupbox', 'windowname', 'decor', 'volume_icon', 'volume', 'decor', 'clock', 'decor', 'battery']
mywidgets = ['currentlayout', 'chord','decor', 'mpd2', 'decor', 'groupbox', 'windowname', 'decor', 'volume_icon', 'volume', 'decor', 'clock', 'decor', 'battery']
# Widgets to be showed in a reversed bg and fg in compact mode
reverse = ['currentlayout', 'chord', 'battery', 'windowtabs']
# The seprator on the bar
# 
# decor = '  '
decor = '  '
# decor = ' || '
decor_size = 30
font = 'FantasqueSansMono Nerd Font Regular'
# font = 'DMMono Nerd Font'
# font = 'Noto Sans Sc Bold'


default_apps = {
  'browser' : 'firefox',
  'terminal' : 'kitty',
  'editor' : 'kitty nvim',
  'file' : 'pcmanfm',
  'file' : 'nemo',
}

# List of available workspaces.
# Each workspace has its own prefix and hotkey.
workspaces = [
  #name hotkey
  ('a', 'a'),
  ('b', 'b'),
  ('c', 'c'),
  ('d', 'd'),
  ('e', 'e'),
]

# List of available rooms.
# Rooms are identical between workspaces, but they can
# be changed to different ones as well. Minor changes required.
rooms = '123456'
