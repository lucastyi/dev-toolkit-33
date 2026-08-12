import json

DEFAULTS = {
    'click_interval': 0.1,
    'max_clicks': 1000,
    'click_button': 'left',
    'activate_hotkey': 'F6'
}

class ConfigLoader:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = DEFAULTS.copy()  # Start with defaults

    def load(self):
        try:
            with open(self.config_file, 'r') as file:
                user_config = json.load(file)
                self.config.update(user_config)  # Merge with user config
        except FileNotFoundError:
            print(f'Config file {self.config_file} not found, using defaults.')  
        except json.JSONDecodeError:
            print('Error decoding JSON, using defaults.')  

    def get(self, key):
        return self.config.get(key, DEFAULTS.get(key))

    def set(self, key, value):
        self.config[key] = value  

if __name__ == '__main__':
    loader = ConfigLoader('config.json')
    loader.load()
    print(loader.get('click_interval'))  # Example usage
