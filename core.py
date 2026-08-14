import time
import random
import threading

class AutoClicker:
    def __init__(self, interval, duration):
        self.interval = interval
        self.duration = duration
        self.is_running = False

    def start(self):
        if self.interval <= 0:
            raise ValueError("Interval must be positive")
        if self.duration <= 0:
            raise ValueError("Duration must be positive")
        self.is_running = True
        threading.Thread(target=self._click).start()

    def _click(self):
        end_time = time.time() + self.duration
        while self.is_running and time.time() < end_time:
            self._perform_click()
            time.sleep(self.interval)
        self.is_running = False

    def _perform_click(self):
        # Simulating a mouse click
        print(f"Click performed at: {time.time()}")

    def stop(self):
        self.is_running = False

if __name__ == '__main__':
    clicker = AutoClicker(1, 5)
    try:
        clicker.start()
    except ValueError as e:
        print(f'Error: {e}')
    time.sleep(10)
    clicker.stop()
    print('AutoClicker stopped')