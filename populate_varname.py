import os
import yaml
import shutil
from pathlib import Path
import requests


def load_data(data_file):
    res = None
    with open(data_file, 'r') as stream:
        try:
            res = yaml.load(stream, Loader=yaml.Loader)
        except yaml.YAMLError as exc:
            print(exc)
    return res


settings_data = load_data('settings.yaml')
if settings_data is None:
    print("No settings.yaml file found")
    exit(1)

if not "plugins" in settings_data:
    print("No plugins section in settings.yaml file")
    exit(1)

data = {}
for item in settings_data["plugins"]:
    print(item, settings_data["plugins"][item])
    url = settings_data["plugins"][item]
    
    if url is None:
        data[item] = None
        continue
    else:
        r = requests.get(url)
        resp = r.json()
        tmp = {}
        for key, value in resp["value"].items():
            tmp[key] = {
                "source": value,
                "type": "data"
            }
    data[item] = tmp


with open('varname.yaml', 'w') as outfile:
    yaml.dump(data, outfile, default_flow_style=False)
