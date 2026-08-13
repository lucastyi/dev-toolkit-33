import json
import os

class Config:
    def __init__(self, filename='config.json'):
        self.filename = filename
        self.data = self.load_config()

    def load_config(self):
        if not os.path.exists(self.filename):
            return {}
        with open(self.filename, 'r') as file:
            return json.load(file)

    def get(self, key):
        return self.data.get(key, None)

    def set(self, key, value):
        self.data[key] = value
        self.save_config()

    def save_config(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file, indent=4)

config = Config()