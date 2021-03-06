from libqtile import widget, bar
from libqtile.config import Screen
from .Loader import CONFIG
from .Globals import SEP
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
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               foreground=CONFIG["top_bar"]["windowName"]['background']),
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                widget.Volume(**CONFIG["top_bar"]["volume"]),
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
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               foreground=CONFIG["top_bar"]["windowName"]['background']),
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                widget.Volume(**CONFIG["top_bar"]["volume"]),
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
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               foreground=CONFIG["top_bar"]["windowName"]['background']),
                widget.WindowName(**CONFIG["top_bar"]["windowName"]),
                widget.TextBox(SEP,
                               padding=0,
                               fontsize=20,
                               background=CONFIG["top_bar"]["windowName"]['background'],
                               foreground=CONFIG["top_bar"]["volume"]['background']),
                widget.Volume(**CONFIG["top_bar"]["volume"]),
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
        ],
            CONFIG["bottom_bar"]["size"],
            opacity=CONFIG["bottom_bar"]["opacity"]
        ),
        wallpaper=CONFIG['background'],
        wallpaper_mode='fill'
    )
]
