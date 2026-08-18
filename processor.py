import time
import random

class Clicker:
    def __init__(self, click_delay=0.1):
        self.click_delay = click_delay
        self.running = False

    def start(self):
        self.running = True
        self._process_loop()

    def stop(self):
        self.running = False

    def _process_loop(self):
        while self.running:
            position = self.get_click_position()
            if self.validate_position(position):
                self.simulate_click(position)
                time.sleep(self.click_delay)
            else:
                print('Invalid click position: {}'.format(position))

    def get_click_position(self):
        # Simulate obtaining a random position
        return (random.randint(0, 1920), random.randint(0, 1080))

    def validate_position(self, position):
        x, y = position
        return isinstance(x, int) and isinstance(y, int) and 0 <= x <= 1920 and 0 <= y <= 1080

    def simulate_click(self, position):
        print(f'Simulated click at {position}')

if __name__ == '__main__':
    clicker = Clicker(click_delay=0.5)
    try:
        clicker.start()
    except KeyboardInterrupt:
        clicker.stop()  # Ensures graceful stop after an interrupt