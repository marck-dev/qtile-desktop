from typing import List  # noqa: F401
from settings import keys, groups, layouts, mouse, autostart, dialogs, screens, floating_layout
from settings.Globals import auto_minimize, auto_fullscreen, extension_defaults, bring_front_click, focus_on_window_activation, terminal, cursor_warp, reconfigure_screens, widget_defaults

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
