import json
from typing import Any, Dict, List

def load_json(file_path: str) -> Any:
    with open(file_path, 'r') as file:
        return json.load(file)


def save_json(file_path: str, data: Any) -> None:
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def filter_items_by_key(data: List[Dict[str, Any]], key: str, value: Any) -> List[Dict[str, Any]]:
    return [item for item in data if item.get(key) == value]


def enrich_data(data: List[Dict[str, Any]], enrichment: Dict[str, Any]) -> List[Dict[str, Any]]:
    for item in data:
        item.update(enrichment)
    return data


def data_summary(data: List[Dict[str, Any]]) -> Dict[str, int]:
    return { 'total_items': len(data), 'keys': list(data[0].keys()) if data else [] }