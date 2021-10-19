from libqtile import layout, layout
from libqtile.config import Match
from .Loader import CONFIG

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])

layouts = [
    layout.Columns(
        border_focus=CONFIG["border_focus"], border_width=1, margin=5),
    layout.Max(),
    layout.Stack(
        num_stacks=2, border_focus=CONFIG["border_focus"], border_width=1,
        margin=5),
    layout.Matrix(
        border_focus=CONFIG["border_focus"], margin=5, border_width=1),
    layout.MonadTall(
        border_focus=CONFIG["border_focus"], margin=5, border_width=1)
]
