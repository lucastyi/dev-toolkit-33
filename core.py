from typing import Optional, Callable

class AutoClicker:
    """A class to represent an autoclicker."""
    def __init__(self, interval: float, click_function: Callable[[], None]) -> None:
        """Initialize the AutoClicker.

        Args:
            interval (float): The time interval between clicks in seconds.
            click_function (Callable[[], None]): The function to be called for each click.
        """
        self.interval = interval
        self.click_function = click_function
        self.running = False

    def start(self) -> None:
        """Start the autoclicker."""
        self.running = True
        while self.running:
            self.click_function()
            time.sleep(self.interval)

    def stop(self) -> None:
        """Stop the autoclicker."""
        self.running = False

# Example usage:
if __name__ == '__main__':
    import time

    def simple_click():
        print("Clicked!")

    autoclicker = AutoClicker(1.0, simple_click)  # Click every second
    try:
        autoclicker.start()
    except KeyboardInterrupt:
        autoclicker.stop()
        print("AutoClicker stopped.")