import json
from pathlib import Path

def load_config(file_path: str, default_config: dict) -> dict:
    config_path = Path(file_path)
    if config_path.is_file():
        with config_path.open('r') as config_file:
            try:
                return json.load(config_file)
            except json.JSONDecodeError:
                print('Error decoding JSON, loading defaults.')
    else:
        print('Config file not found, loading defaults.')
    return default_config

if __name__ == '__main__':
    defaults = {'setting1': 'default_value1', 'setting2': 'default_value2'}
    config = load_config('config.json', defaults)
    print(config)