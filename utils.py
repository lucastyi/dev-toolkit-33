import json
import os

class DataHandler:
    def __init__(self, file_path):
        self.file_path = file_path
        self.ensure_file_exists()

    def ensure_file_exists(self):
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as f:
                json.dump([], f)

    def read_data(self):
        with open(self.file_path, 'r') as f:
            return json.load(f)

    def write_data(self, data):
        with open(self.file_path, 'w') as f:
            json.dump(data, f)

    def append_data(self, new_entry):
        data = self.read_data()
        data.append(new_entry)
        self.write_data(data)

    def clear_data(self):
        self.write_data([])