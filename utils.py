import json
import os

class DataHandler:
    def __init__(self, directory='autoclicker_data'):
        self.directory = directory
        self._create_directory()

    def _create_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def save_data(self, filename, data):
        filepath = os.path.join(self.directory, f'{filename}.json')
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self, filename):
        filepath = os.path.join(self.directory, f'{filename}.json')
        if os.path.exists(filepath):
            with open(filepath, 'r') as f:
                return json.load(f)
        return None

    def list_files(self):
        return [f for f in os.listdir(self.directory) if f.endswith('.json')]

handler = DataHandler()