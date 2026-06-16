"""
Threading Example 13: Daemon Thread

Concept:
A daemon thread runs in the background.
It automatically stops when the main program exits.

Real-time Use Case:
Background monitoring, heartbeat check, auto-save, lightweight logging.
"""

import threading
import time


def background_monitor():
    while True:
        print("Background monitor is running...")
        time.sleep(1)


# daemon=True means this thread will not block program exit.
thread = threading.Thread(target=background_monitor, daemon=True)
thread.start()

# Main program sleeps for 3 seconds and then exits.
time.sleep(3)
print("Main program exiting. Daemon thread will stop automatically.")
