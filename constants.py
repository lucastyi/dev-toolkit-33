CLICK_INTERVAL = 0.01
DEFAULT_DURATION = 60
CLICK_COUNT_LIMIT = 1000

KEYBOARD_KEYS = {
    'start': 'F9',
    'stop': 'F10',
    'pause': 'F11',
    'resume': 'F12',
}

MOUSE_BUTTONS = {
    'left': 'left_button',
    'right': 'right_button',
    'middle': 'middle_button',
}

# This dictionary holds the settings for the autoclicker.
AUTOD_SETTINGS = {
    'click_interval': CLICK_INTERVAL,
    'duration': DEFAULT_DURATION,
    'max_clicks': CLICK_COUNT_LIMIT,
    'keyboard_keys': KEYBOARD_KEYS,
    'mouse_buttons': MOUSE_BUTTONS,
}

def get_setting(setting_name):
    return AUTOD_SETTINGS.get(setting_name, None)

def set_setting(setting_name, value):
    if setting_name in AUTOD_SETTINGS:
        AUTOD_SETTINGS[setting_name] = value
