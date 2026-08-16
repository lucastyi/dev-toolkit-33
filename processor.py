import time

class ClickProcessor:
    def __init__(self, click_interval=0.1):
        self.click_interval = click_interval
        self.is_running = False

    def start(self):
        self.is_running = True
        while self.is_running:
            self.perform_click()
            time.sleep(self.click_interval)

    def stop(self):
        self.is_running = False

    def perform_click(self):
        # Simulate a mouse click here
        print('Click!')  # Replace with actual click implementation

    def set_click_interval(self, interval):
        if interval > 0:
            self.click_interval = interval
        else:
            raise ValueError('Interval must be greater than 0')

# Example usage:
if __name__ == '__main__':
    processor = ClickProcessor(0.05)
    try:
        processor.start()
    except KeyboardInterrupt:
        processor.stop()