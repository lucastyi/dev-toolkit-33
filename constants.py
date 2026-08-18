import json
import os

DEFAULTS = {
    'click_interval': 0.1,
    'max_clicks': 1000,
    'sensitivity': 0.5,
    'click_type': 'left',
}

CONFIG_FILE = 'config.json'

def load_config(file_path=CONFIG_FILE):
    if not os.path.exists(file_path):
        return DEFAULTS
    with open(file_path, 'r') as file:
        try:
            config = json.load(file)
            return {**DEFAULTS, **config}
        except json.JSONDecodeError:
            print('Error reading configuration, using defaults.')
            return DEFAULTS

if __name__ == '__main__':
    config = load_config()
    print(config)