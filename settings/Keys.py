from libqtile.command import lazy as Lazy
from libqtile.config import Key, KeyChord
from libqtile.lazy import lazy
from .Globals import mod, terminal

keys = [
    #            -| WINDOWS SWITCHING |-
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    #                 -| MOVE WINDOW IN COLS |-
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    #               -| RESIZING WINDOWS |-
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

    # Toggle between different layouts as defined below
    Key([mod, "shift"], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn(
        'rofi -show drun -combi-modi drun,filebrowser -show-icons')),

    #               -| SOUND |-
    Key([], "XF86AudioMute", lazy.spawn('amixer -D pulse set Master 1+ toggle')),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        'amixer -D pulse set Master 2%- ')),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        'amixer -D pulse set Master 2%+ ')),


    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
    Key([mod], "f", lazy.window.toggle_floating()),
    Key([mod, "shift"], "f", lazy.window.toggle_fulscreen())
]

keys.extend([
    KeyChord([mod], "p", [
        Key([], "p", lazy.spawn('pycharm'), desc='Open pycharm'),
        Key([], "c", lazy.spawn('code'), desc='Open VS Code'),
        Key([], "i", lazy.spawn('idea'), desc='Open Idea'),
        Key([], "s", lazy.spawn('spotify'), desc='Open Spotify'),
    ])

])

keys.extend([
    KeyChord([mod], "s", [
        Key([], "w", lazy.group["web"].toscreen()),
        Key([], "c", lazy.group["code"].toscreen()),
        Key([], "t", lazy.group["term"].toscreen()),
        Key([], "m", lazy.group["music"].toscreen()),
    ])

])

#               -| MOVE TO OTHER DESKTOP |-
keys.extend([
    KeyChord([mod], 'm', [
        Key([], 'm', Lazy.window.togroup('music')),
        Key([], 't', Lazy.window.togroup('term')),
        Key([], 'w', Lazy.window.togroup('web')),
        Key([], 'c', Lazy.window.togroup('code')),
    ])
])

keys.extend([
    Key([mod], 'F2', lazy.group['menu'].dropdown_toggle('terminal')),
    Key([mod], 'F3', lazy.group['menu'].dropdown_toggle('find')),
])
