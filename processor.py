import time
import random

class AutoClicker:
    def __init__(self, interval: float, click_count: int):
        self.interval = interval
        self.click_count = click_count
        self.start_time = None

    def start(self):
        print("AutoClicker started.")
        self.start_time = time.time()
        for _ in range(self.click_count):
            self.perform_click()
            time.sleep(self.interval)
        print("AutoClicker completed.")

    def perform_click(self):
        print(f"Click at {time.time() - self.start_time:.2f} seconds")

if __name__ == '__main__':
    clicker = AutoClicker(interval=random.uniform(0.1, 0.5), click_count=10)
    clicker.start()