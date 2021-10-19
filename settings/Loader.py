from pathlib import Path
import json
file = open("{}/.config/qtile/config.json".format(Path.home()), "r")
text = file.readlines()
text = "\n".join(text)
CONFIG = json.loads(text)
file.close()
