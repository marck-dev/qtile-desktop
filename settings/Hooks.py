import os
import subprocess
from .Loader import CONFIG
from libqtile import hook


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~')
    os.system("feh --bg-fill {}".format(CONFIG["background"]))
    subprocess.call(home + '/.config/qtile/autostart.sh')


@hook.subscribe.client_new
def dialogs(window):
    if (window.window.get_wm_type() == 'dialog'
            or window.window.get_wm_transient_for()):
        window.floating = True
