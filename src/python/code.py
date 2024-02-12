import time


class Timer:
    def __init__(self):
        self.start_time = None
        self.end_time = None

    def start(self):
        """Start the timer."""
        self.start_time = time.time()
        self.end_time = None
        print("Timer started.")

    def stop(self):
        """Stop the timer and report the elapsed time."""
        if self.start_time is None:
            print("Timer was not started.")
            return None

        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time
        print(f"Timer stopped. Elapsed time: {elapsed_time:.2f} seconds.")
        return elapsed_time


# Example usage
timer = Timer()
timer.start()
time.sleep(5)  # Simulate some operations or tasks taking 5 seconds
elapsed_time = timer.stop()
print(f"Total elapsed time: {elapsed_time:.2f} seconds.")
