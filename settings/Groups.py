from libqtile.config import DropDown, Group, Match, ScratchPad

groups = [
    Group("term"),
    ScratchPad('menu', [
        DropDown('terminal', 'alacritty', opacity=1, height=0.15, y=0.1),
        DropDown('find', 'rofi -show filebrowser -theme slut -show-icons',
                 opacity=0.9),
    ]),
    Group("code", spawn="code",  exclusive=False, label="Prog",
          matches=Match(title=['Visual Studio Code',
                               'jetbrains-idea-ce',
                               'jetbrains*',
                               'jetbrains-pycharm-ce'])),
    Group("music", exclusive=False, label="Spoti",
          spawn="spotify", matches=Match(
              title=['Spotify',
                     'spotify',
                     'Youtube'])),
    Group("web", exclusive=True, label="Web",
          matches=Match(title=["Mozilla Firefox",
                               "Google Chrome",
                               "Google-chrome",
                               "google-chrome-stable",
                               "chrome",
                               "Chromium"]))
]
