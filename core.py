import json
import time
from typing import Any, Dict

class AutoClickerDataHandler:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = self.load_data()

    def load_data(self) -> Dict[str, Any]:
        try:
            with open(self.filepath, 'r') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return self.handle_error(e)

    def handle_error(self, error: Exception) -> Dict[str, Any]:
        print(f'Error loading data: {error}')
        return {}

    def save_data(self) -> None:
        with open(self.filepath, 'w') as file:
            json.dump(self.data, file, indent=4)

    def update_click_data(self, clicks: int) -> None:
        self.data['clicks'] = self.data.get('clicks', 0) + clicks
        self.save_data()

    def reset_click_data(self) -> None:
        self.data['clicks'] = 0
        self.save_data()

    def get_click_data(self) -> int:
        return self.data.get('clicks', 0)

if __name__ == '__main__':
    handler = AutoClickerDataHandler('click_data.json')
    handler.update_click_data(5)
    print(f'Total clicks: {handler.get_click_data()}')