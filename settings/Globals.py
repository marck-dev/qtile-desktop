from libqtile.utils import guess_terminal
from .Loader import CONFIG

mod = "mod4"  # windows key
terminal = guess_terminal()
SEP = "\ue0ba"
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True

widget_defaults = dict(
    font=CONFIG["font"],
    fontsize=CONFIG["fontSize"],
    padding=3,
    foreground=CONFIG["default_foreground"]
)
extension_defaults = widget_defaults.copy()
