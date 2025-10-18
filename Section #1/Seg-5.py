import threading

class SafeCounter:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        for _ in range(100000):
            with self.lock:
                self.count += 1

counter = SafeCounter()
t1 = threading.Thread(target=counter.increment)
t2 = threading.Thread(target=counter.increment)

t1.start()
t2.start()
t1.join()
t2.join()

print("Final count:", counter.count)
