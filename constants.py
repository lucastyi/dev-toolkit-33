import os

DEFAULT_CLICK_INTERVAL = 0.01
DEFAULT_CLICK_COUNT = 100
DEFAULT_MOUSE_BUTTON = 'left'
DEFAULT_SCREEN_RESOLUTION = (1920, 1080)
DEFAULT_LOG_LEVEL = 'INFO'

# Performance tuning constants
MAX_CONCURRENT_CLICKS = os.cpu_count() or 1
MOUSE_MOVEMENT_SMOOTHNESS = 0.1
AUTO_CLICKER_VERSION = '1.0.0'

# Predefined color codes for UI elements
COLOR_PRIMARY = '#3498db'
COLOR_SECONDARY = '#2ecc71'
COLOR_ERROR = '#e74c3c'
COLOR_WARNING = '#f39c12'
COLOR_SUCCESS = '#27ae60'

# Configuration file paths
CONFIG_DIR = os.path.join(os.getenv('APPDATA'), 'dev-toolkit-33')
CONFIG_FILE = os.path.join(CONFIG_DIR, 'settings.json')

# Timeout settings
GUI_TIMEOUT = 5
API_TIMEOUT = 10
