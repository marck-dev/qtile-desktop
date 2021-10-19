from libqtile.config import DropDown, Group, Match, ScratchPad

groups = [
    Group("term"),
    ScratchPad('menu', [
        DropDown('terminal', 'alacritty', opacity=0.7, height=0.15, y=0.1),
        DropDown('find', 'rofi -show filebrowser -theme slut -show-icons',
                 opacity=0.7),
    ]),
    Group("code", spawn="code",  exclusive=True, label="Prog",
          matches=Match(title=['Visual Studio Code',
                               'Idea',
                               'Intellij',
                               'Pycharm'])),
    Group("music", exclusive=True, label="Spoti",
          spawn="spotify", matches=Match(
              title=['Spotify',
                     'spotify',
                     'Youtube'])),
    Group("web", exclusive=True, label="Web",
          matches=Match(title=["Mozilla Firefox",
                               "Chrome",
                               "Chromium"]))
]
