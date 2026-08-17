from typing import Final

# Constants for the autoclicker module
auto_click_interval: Final[float] = 0.1  # Interval between clicks in seconds
max_clicks: Final[int] = 1000  # Maximum number of clicks
mouse_button: Final[str] = 'left'  # Mouse button to be used for clicking
click_location: Final[tuple[int, int]] = (500, 500)  # Default click location


def get_click_params() -> dict[str, float | int | str | tuple[int, int]]:
    """Retrieve the parameters for clicking.
    
    Returns a dictionary containing the click parameters:
    - auto_click_interval: The interval between clicks.
    - max_clicks: The maximum number of clicks that can be performed.
    - mouse_button: The mouse button designated for clicking.
    - click_location: The tuple representing the x and y coordinates for the click.
    """
    return {
        'auto_click_interval': auto_click_interval,
        'max_clicks': max_clicks,
        'mouse_button': mouse_button,
        'click_location': click_location,
    }


if __name__ == '__main__':
    params = get_click_params()
    print(params)  # Example usage of the function