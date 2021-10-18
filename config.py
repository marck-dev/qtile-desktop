# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
# Copyright (c) 2021 Marck C. Guzman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
from pathlib import Path
from libqtile import backend, bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile.config import Group, Match
import os
import subprocess
import json

file = open("{}/.config/qtile/config.json".format(Path.home()), "r")
text = file.readlines()
text = "\n".join(text)
CONFIG = json.loads(text)
file.close()

SEP = "\ue0ba"
mod = "mod4"  # windows
terminal = guess_terminal()

groups = [
    Group("term"),  # ,matches=Match(title=['Alacritty'])
    Group("code", spawn="code", matches=Match(
        title=['Visual Studio Code', 'Idea', 'Intellij', 'Pycharm'])),  #
    Group("music", spawn="spotify", matches=Match(
        title=['Spotify', 'spotify', 'Youtube'])),  #
    Group("web", matches=Match(
        title=["Mozilla Firefox", "Chrome", "Chromium"]))
]

vol_wid = widget.Volume(**CONFIG["top_bar"]["volume"])
sep = widget.TextBox(SEP,
                     padding=0,
                     fontsize=20,
                     foreground=CONFIG["top_bar"]["windowName"]['background'])


def showPrompt():
    sep = widget.TextBox(SEP,
                         padding=0,
                         fontsize=20,
                         background=CONFIG["top_bar"]["prompt"]['background'],
                         foreground=CONFIG["top_bar"]["windowName"]['background'])


keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

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
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),

    # Sound
    Key([], "XF86AudioMute", lazy.spawn('amixer -D pulse set Master 1+ toggle')),
    Key([], "XF86AudioLowerVolume", lazy.spawn(
        'amixer -D pulse set Master 2%- ')),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(
        'amixer -D pulse set Master 2%+ ')),

    #     APPS


    Key([mod], "space", lazy.widget["keyboardlayout"].next_keyboard(),
        desc="Next keyboard layout."),
    Key([mod], "f", lazy.window.toggle_floating())
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

layouts = [
    layout.Columns(
        border_focus=CONFIG["border_focus"], border_width=1, margin=5),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    layout.Stack(
        num_stacks=2, border_focus=CONFIG["border_focus"], border_width=1, margin=5),
    layout.Matrix(
        border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    layout.MonadTall(
        border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    # layout.MonadWide(border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    layout.RatioTile(
        border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    #layout.Tile(border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    #layout.TreeTab(border_focus=CONFIG["border_focus"], margin=5, border_width=1, background=CONFIG["border_focus"]),
    # layout.VerticalTile(),
    #layout.Zoomy(border_focus=CONFIG["border_focus"], margin=5, border_width=1),
]

widget_defaults = dict(
    font=CONFIG["font"],
    fontsize=CONFIG["fontSize"],
    padding=3,
    foreground=CONFIG["default_foreground"]
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(background=CONFIG["top_bar"]["windowName"]['background'],
                                     padding=10,
                                     foreground="#000000"),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["groupBox"]['background']),
                widget.Spacer(length=20),
                widget.GroupBox(**CONFIG["top_bar"]["groupBox"]),
                widget.Prompt(**CONFIG["top_bar"]["prompt"]),
                widget.Spacer(length=20),
                sep,
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                vol_wid,
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["volume"]['background'],
                               foreground=CONFIG["top_bar"]["clock"]['background']),
                widget.Clock(**CONFIG["top_bar"]["clock"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["clock"]['background'],
                               foreground=CONFIG["top_bar"]["quickExit"]['background']),
                widget.QuickExit(**CONFIG["top_bar"]["quickExit"]),
            ],
            CONFIG["top_bar"]["size"],
            opacity=CONFIG["top_bar"]["opacity"]
        ),
        bottom=bar.Bar([
            widget.KeyboardLayout(**CONFIG["bottom_bar"]["keyboard"]),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["keyboard"]['background'],
                           foreground=CONFIG['bottom_bar']['battery']['background']),
            widget.Battery(**CONFIG["bottom_bar"]["battery"]),
            widget.Spacer(length=40),
            widget.Memory(**CONFIG["bottom_bar"]["memory"]),
            widget.Spacer(length=40),

            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["memory"]['background'],
                           foreground=CONFIG['bottom_bar']['tasklist']['background']),
            widget.TaskList(**CONFIG['bottom_bar']['tasklist']),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["tasklist"]['background'],
                           foreground="#000000"),
            widget.Moc(),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background="#000000",
                           foreground=CONFIG['bottom_bar']['cpu']['background']),
            widget.CPU(**CONFIG["bottom_bar"]["cpu"]),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["cpu"]['background'],
                           foreground="#000000"),
            widget.TextBox("\uf011",
                           padding=10,
                           fontsize=13,
                           margin=10,
                           mouse_callback={"Button1": lazy.spawn('poweroff')},
                           foreground=CONFIG["bottom_bar"]["tasklist"]['background'],
                           background="#000000"),
            # widget.LaunchBar(progs=[("firefox", "firefox", 'Mozilla Firefox'),
            #                                              ('code', 'code', 'Visual Studio Code')])
        ],
            CONFIG["bottom_bar"]["size"],
            opacity=CONFIG["bottom_bar"]["opacity"]
        ),
        wallpaper=CONFIG['background'],
        wallpaper_mode='fill'
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(background=CONFIG["top_bar"]["windowName"]['background'],
                                     padding=10,
                                     foreground="#000000"),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["groupBox"]['background']),
                widget.Spacer(length=20),
                widget.GroupBox(**CONFIG["top_bar"]["groupBox"]),
                widget.Spacer(length=20),
                sep,
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                vol_wid,
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["volume"]['background'],
                               foreground=CONFIG["top_bar"]["clock"]['background']),
                widget.Clock(**CONFIG["top_bar"]["clock"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["clock"]['background'],
                               foreground=CONFIG["top_bar"]["quickExit"]['background']),
                widget.QuickExit(**CONFIG["top_bar"]["quickExit"]),
            ],
            CONFIG["top_bar"]["size"],
            opacity=CONFIG["top_bar"]["opacity"]
        ),
        bottom=bar.Bar([
            widget.KeyboardLayout(**CONFIG["bottom_bar"]["keyboard"]),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["keyboard"]['background'],
                           foreground=CONFIG['bottom_bar']['battery']['background']),
            widget.Battery(**CONFIG["bottom_bar"]["battery"]),
            widget.Spacer(length=40),
            widget.Memory(**CONFIG["bottom_bar"]["memory"]),
            widget.Spacer(length=40),

            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["memory"]['background'],
                           foreground=CONFIG['bottom_bar']['tasklist']['background']),
            widget.TaskList(**CONFIG['bottom_bar']['tasklist']),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["tasklist"]['background'],
                           foreground=CONFIG['bottom_bar']['cpu']['background']),
            widget.CPU(**CONFIG["bottom_bar"]["cpu"]),
            # widget.LaunchBar(progs=[("firefox", "firefox", 'Mozilla Firefox'),
            #                                              ('code', 'code', 'Visual Studio Code')])
        ],
            CONFIG["bottom_bar"]["size"],
            opacity=CONFIG["bottom_bar"]["opacity"]
        ),
        wallpaper=CONFIG['background'],
        wallpaper_mode='fill'
    ),
    Screen(
        top=bar.Bar(
            [
                widget.CurrentLayout(background=CONFIG["top_bar"]["windowName"]['background'],
                                     padding=10,
                                     foreground="#000000"),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["groupBox"]['background']),
                widget.Spacer(length=20),
                widget.GroupBox(**CONFIG["top_bar"]["groupBox"]),
                widget.Spacer(length=20),
                sep,
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                vol_wid,
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["volume"]['background'],
                               foreground=CONFIG["top_bar"]["clock"]['background']),
                widget.Clock(**CONFIG["top_bar"]["clock"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["clock"]['background'],
                               foreground=CONFIG["top_bar"]["quickExit"]['background']),
                widget.QuickExit(**CONFIG["top_bar"]["quickExit"]),
            ],
            CONFIG["top_bar"]["size"],
            opacity=CONFIG["top_bar"]["opacity"]
        ),
        bottom=bar.Bar([
            widget.KeyboardLayout(**CONFIG["bottom_bar"]["keyboard"]),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["keyboard"]['background'],
                           foreground=CONFIG['bottom_bar']['battery']['background']),
            widget.Battery(**CONFIG["bottom_bar"]["battery"]),
            widget.Spacer(length=40),
            widget.Memory(**CONFIG["bottom_bar"]["memory"]),
            widget.Spacer(length=40),

            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["memory"]['background'],
                           foreground=CONFIG['bottom_bar']['tasklist']['background']),
            widget.TaskList(**CONFIG['bottom_bar']['tasklist']),
            widget.TextBox(SEP,
                           padding=0,
                           fontsize=25,
                           margin=0,
                           background=CONFIG["bottom_bar"]["tasklist"]['background'],
                           foreground=CONFIG['bottom_bar']['cpu']['background']),
            widget.CPU(**CONFIG["bottom_bar"]["cpu"]),
            # widget.LaunchBar(progs=[("firefox", "firefox", 'Mozilla Firefox'),
            #                                              ('code', 'code', 'Visual Studio Code')])
        ],
            CONFIG["bottom_bar"]["size"],
            opacity=CONFIG["bottom_bar"]["opacity"]
        ),
        wallpaper=CONFIG['background'],
        wallpaper_mode='fill'
    )
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
# floating_layout = layout.Floating(float_rules=[
#     # Run the utility of `xprop` to see the wm class and name of an X client.
#     *layout.Floating.default_float_rules,
#     Match(wm_class='confirmreset'),  # gitk
#     Match(wm_class='makebranch'),  # gitk
#     Match(wm_class='maketag'),  # gitk
#     Match(wm_class='ssh-askpass'),  # ssh-askpass
#     Match(title='branchdialog'),  # gitk
#     Match(title='pinentry'),  # GPG key password entry
# ])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"


@hook.subscribe.startup
def autostart():
    home = os.path.expanduser('~')
    os.system("feh --bg-fill {}".format(CONFIG["background"]))
    subprocess.call(home + '/.config/qtile/autostart.sh')


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog'
            or window.window.get_wm_transient_for()):
        window.floating = True
