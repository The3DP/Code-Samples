import time
from functools import wraps

def timer(label="Execution Time"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            print(f"{label}: {end - start:.4f}s")
            return result
        return wrapper
    return decorator

@timer("Sleep Function")
def slow_function():
    time.sleep(1.5)
    return "Done"

print(slow_function())
