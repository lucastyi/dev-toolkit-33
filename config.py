from typing import Dict, Any

class Config:
    """
    Configuration class to manage settings for the autoclicker.
    """
    def __init__(self, settings: Dict[str, Any]) -> None:
        """
        Initialize the configuration with provided settings.
        
        :param settings: A dictionary containing configuration settings.
        """
        self.settings = settings

    def get(self, key: str, default: Any = None) -> Any:
        """
        Retrieve a value from the settings dictionary.
        
        :param key: The key to look for in the settings.
        :param default: The value to return if the key is not found.
        :return: The value associated with the key, or default if not found.
        """
        return self.settings.get(key, default)

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the settings dictionary.
        
        :param key: The key to set in the settings.
        :param value: The value to associate with the key.
        """
        self.settings[key] = value

    def load_from_file(self, file_path: str) -> None:
        """
        Load configuration settings from a file.
        
        :param file_path: The path to the configuration file.
        """
        import json
        with open(file_path, 'r') as file:
            self.settings = json.load(file)

    def save_to_file(self, file_path: str) -> None:
        """
        Save the current settings to a file.
        
        :param file_path: The path to save the configuration file.
        """
        import json
        with open(file_path, 'w') as file:
            json.dump(self.settings, file, indent=4)