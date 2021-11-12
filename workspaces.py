from libqtile.config import Group, Key
from libqtile.command import lazy
from keys import keys, mod0, mod2
from settings import workspaces, rooms

# Workspaces and rooms
# The basic idea behind Workspaces and Rooms is to control
# DIFFERENT subsets of groups with the SAME hotkeys.
# So we can have multiple 'qwerasdf' rooms in a different workspaces.
#
# Qtile Groups are used behind the scenes, but their visibility
# is set dynamically.

def get_group_name(workspace, room):
    ''' Calculate Group name based on (workspace,room) combination.
    '''
    return '%s%s' % (room, workspace)

# Oops, time for a little hack there.
# This is a global object with information about current workspace.
# (viable as config code, not sure about client-server though)
wsp = {
    'current': workspaces[0][0], # first workspace is active by default
}
# ... and information about active group in the each workspace.
for w, _ in workspaces:
    wsp[w] = {
        'active_group': get_group_name(w, rooms[0]) # first room is active by default
    }

def get_workspace_groups(workspace):
    ''' Get list of Groups that belongs to workspace.
    '''
    return [ get_group_name(workspace, room) for room in rooms]

def to_workspace(workspace):
    ''' Change current workspace to another one.
    '''
    def f(qtile):
        global wsp

        # we need to save current active room(group) somewhere
        # to return to it later
        wsp[wsp['current']]['active_group'] = qtile.current_group.name

        # now we can change current workspace to the new one
        # (no actual switch there)
        wsp['current'] = workspace
        # and navigate to the active group from the workspace
        # (actual switch)
        qtile.groups_map[
            wsp[workspace]['active_group']
        ].cmd_toscreen(toggle = False)

        # we also need to change subset of visible groups in the GroupBox widget
        qtile.widgets_map['groupbox'].visible_groups = get_workspace_groups(workspace)
        qtile.widgets_map['groupbox'].draw()
        # You can do some other cosmetic stuff here.
        # For example, change Bar background depending on the current workspace.
        # # qtile.widgetMap['groupbox'].bar.background = 'ff0000'
    return f

def to_room(room):
    ''' Change active room to another within the current workspace.
    '''
    def f(qtile):
        global wsp
        qtile.groups_map[get_group_name(wsp['current'], room)].cmd_toscreen(toggle = False)
    return f

def window_to_workspace(workspace, room = rooms[0]):
    ''' Move active window to another workspace.
    '''
    def f(qtile):
        global wsp
        qtile.current_window.togroup(wsp[workspace]['active_group'])
    return f

def window_to_room(room):
    ''' Move active window to another room within the current workspace.
    '''
    def f(qtile):
        global wsp
        qtile.current_window.togroup(get_group_name(wsp['current'], room))
    return f

# Create individual Group for each (workspace,room) combination we have
groups = []
for workspace, hotkey in workspaces:
    for room in rooms:
        groups.append(Group(get_group_name(workspace, room)))

# Assign individual hotkeys for each workspace we have
for workspace, hotkey in workspaces:
    keys.append(Key(mod0, hotkey, lazy.function(
        to_workspace(workspace))))
    keys.append(Key(mod2, hotkey, lazy.function(
        window_to_workspace(workspace))))

# Assign shared hotkeys for each room we have.
# Decision about actual group to open is made dynamically.
for room in rooms:
    keys.append(Key(mod0, room, lazy.function(
        to_room(room))))
    keys.append(Key(mod2, room, lazy.function(
        window_to_room(room))))
