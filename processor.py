import time
import random

def validate_input(value):
    if not isinstance(value, int) or value < 0:
        raise ValueError('Input must be a non-negative integer')

class AutoClicker:
    def __init__(self, interval, clicks):
        validate_input(interval)
        validate_input(clicks)
        self.interval = interval
        self.clicks = clicks

    def start(self):
        print('Starting autoclicker...')
        for _ in range(self.clicks):
            self.click()
            time.sleep(self.interval)

    def click(self):
        print('Click!')  # Simulate a click

if __name__ == '__main__':
    click_interval = random.randint(1, 3)
    total_clicks = random.randint(5, 10)
    autoclicker = AutoClicker(click_interval, total_clicks)
    autoclicker.start()