import time

class AutoClicker:
    def __init__(self, delay: float):
        self.delay = delay
        self.running = False

    def start(self):
        self.running = True
        while self.running:
            self.click()
            time.sleep(self.delay)

    def stop(self):
        self.running = False

    def click(self):
        # Here the actual clicking logic will be implemented
        pass

    def set_delay(self, new_delay: float):
        if new_delay > 0:
            self.delay = new_delay

    def toggle(self):
        self.running = not self.running

if __name__ == "__main__":
    clicker = AutoClicker(0.1)
    try:
        clicker.start()
    except KeyboardInterrupt:
        clicker.stop()