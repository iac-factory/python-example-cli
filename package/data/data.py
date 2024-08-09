import json

from importlib.resources import files

metadata = json.loads(files("package.data").joinpath("metadata.json").read_text())
