### cpu_pendown.py ###
#====================#

import multiprocessing
import time
import math
import sys
from datetime import datetime

# psutil is required for temperature + CPU usage readings
try:
    import psutil
except ImportError:
    psutil = None


def cpu_stress():
    # Busy loop doing floating‑point work
    x = 0.0001
    while True:
        x = math.sqrt(x * x + 1)


def clear_line():
    sys.stdout.write("\r" + " " * 120 + "\r")
    sys.stdout.flush()


def get_cpu_temp():
    """Returns CPU temperature in °C if available, otherwise None."""
    if psutil is None:
        return None

    try:
        temps = psutil.sensors_temperatures()
        if not temps:
            return None

        for name in temps:
            for entry in temps[name]:
                if entry.current is not None:
                    return entry.current
    except Exception:
        return None

    return None


if __name__ == "__main__":
    print("CPU Stress Test")
    print("----------------")

    # Ask user how long to run the test
    while True:
        try:
            duration = int(input("Enter test duration in seconds: "))
            if duration > 0:
                break
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Please enter a valid integer.")

    core_count = multiprocessing.cpu_count()
    print(f"Detected CPU cores: {core_count}")

    start_timestamp = datetime.now()
    print("Starting stress test...")

    # Start worker processes
    processes = []
    for _ in range(core_count):
        p = multiprocessing.Process(target=cpu_stress)
        p.start()
        processes.append(p)

    print("CPU stress test running. Press Ctrl+C to stop early.")

    start_time = time.time()
    stopped_early = False

    # Logs: list of (timestamp, temperature, cpu_usage)
    telemetry_log = []

    # Initialize psutil CPU usage measurement
    if psutil:
        psutil.cpu_percent(interval=None)

    try:
        while True:
            elapsed = int(time.time() - start_time)
            remaining = duration - elapsed

            # Read CPU temperature
            temp = get_cpu_temp()

            # Read CPU usage percentage
            cpu_usage = psutil.cpu_percent(interval=None) if psutil else None

            # Store telemetry
            telemetry_log.append((datetime.now(), temp, cpu_usage))

            if remaining <= 0:
                break

            clear_line()
            if temp is not None and cpu_usage is not None:
                sys.stdout.write(
                    f"Running... {elapsed}s elapsed | {remaining}s remaining | "
                    f"Temp: {temp:.1f}°C | CPU Usage: {cpu_usage:.1f}%"
                )
            elif cpu_usage is not None:
                sys.stdout.write(
                    f"Running... {elapsed}s elapsed | {remaining}s remaining | "
                    f"Temp: N/A | CPU Usage: {cpu_usage:.1f}%"
                )
            else:
                sys.stdout.write(
                    f"Running... {elapsed}s elapsed | {remaining}s remaining | "
                    f"Temp: N/A | CPU Usage: N/A"
                )

            sys.stdout.flush()
            time.sleep(1)

    except KeyboardInterrupt:
        stopped_early = True
        print("\nStopping early...")

    # Stop all processes
    for p in processes:
        p.terminate()

    clear_line()
    print("CPU stress test completed.")

    end_timestamp = datetime.now()
    actual_runtime = int(time.time() - start_time)

    # Save results to a file
    filename = f"cpu_test_results_{start_timestamp.strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(filename, "w") as f:
        f.write("CPU Stress Test Results\n")
        f.write("-----------------------\n")
        f.write(f"Start time: {start_timestamp}\n")
        f.write(f"End time:   {end_timestamp}\n")
        f.write(f"CPU cores used: {core_count}\n")
        f.write(f"Requested duration: {duration} seconds\n")
        f.write(f"Actual runtime: {actual_runtime} seconds\n")
        f.write(f"Stopped early: {stopped_early}\n\n")

        f.write("Telemetry Log (timestamp | temp °C | CPU %):\n")
        for ts, t, usage in telemetry_log:
            t_str = f"{t:.1f}°C" if t is not None else "N/A"
            u_str = f"{usage:.1f}%" if usage is not None else "N/A"
            f.write(f"{ts} | {t_str} | {u_str}\n")

    print(f"Results saved to: {filename}")
