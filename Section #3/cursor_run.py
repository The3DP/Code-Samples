import time

while True:
    for char in "/-\|":
        # \r moves the cursor back to the start of the line
        print(f"\r{char} Loading...", end="", flush=True)
        time.sleep(0.1)
