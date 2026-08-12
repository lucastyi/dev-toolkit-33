from typing import Tuple, Any


def calculate_click_interval(clicks_per_second: float) -> float:
    """
    Calculate the interval between clicks in seconds.

    Args:
        clicks_per_second (float): The number of clicks desired per second.

    Returns:
        float: The interval between clicks, in seconds.
    """
    return 1.0 / clicks_per_second


def validate_click_position(position: Tuple[int, int]) -> bool:
    """
    Validate that the click position is within screen bounds.

    Args:
        position (Tuple[int, int]): The x and y coordinates of the click position.

    Returns:
        bool: True if valid, False otherwise.
    """
    x, y = position
    return 0 <= x <= 1920 and 0 <= y <= 1080


def perform_click(position: Tuple[int, int], button: str = 'left') -> None:
    """
    Simulate a mouse click at the given position.

    Args:
        position (Tuple[int, int]): The x and y coordinates of the click position.
        button (str): The button to click ('left' or 'right').
    """
    if not validate_click_position(position):
        raise ValueError('Click position is out of bounds.')
    # Simulated click functionality
    print(f'Performing {button} click at {position}.')


def setup_autoclicker(clicks_per_second: float, position: Tuple[int, int]) -> None:
    """
    Setup and start the autoclicker with specified parameters.

    Args:
        clicks_per_second (float): The desired clicks per second.
        position (Tuple[int, int]): The x and y coordinates for clicking.
    """
    interval = calculate_click_interval(clicks_per_second)
    print(f'Set up autoclicker at {position} for {clicks_per_second} clicks/second, interval: {interval}s.')
    # Here would be the loop to click at interval, not implemented for brevity
