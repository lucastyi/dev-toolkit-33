import json
from typing import Any, Dict, List

class AutoClickerData:
    def __init__(self):
        self.clicks: List[Dict[str, Any]] = []

    def add_click(self, x: int, y: int, timestamp: float) -> None:
        click_info = {'x': x, 'y': y, 'timestamp': timestamp}
        self.clicks.append(click_info)

    def to_json(self) -> str:
        return json.dumps(self.clicks)

    def from_json(self, data: str) -> None:
        self.clicks = json.loads(data)

    def clear_clicks(self) -> None:
        self.clicks.clear()

    def get_click_count(self) -> int:
        return len(self.clicks)


# Example of usage:
auto_clicker_data = AutoClickerData()
auto_clicker_data.add_click(100, 200, 1630454400.0)
auto_clicker_data.add_click(150, 250, 1630454410.0)
json_data = auto_clicker_data.to_json()
auto_clicker_data.clear_clicks()  # Clear clicks after processing
