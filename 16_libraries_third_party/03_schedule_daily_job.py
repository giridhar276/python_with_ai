# Topic: Third-party Libraries
# Example: Schedule repeated job

try:
    import schedule
except ImportError:
    print("Please install schedule: pip install schedule")
    raise SystemExit

import time

def job():
    print("Running scheduled report job")

# every().seconds.do() schedules a function to run repeatedly.
schedule.every(2).seconds.do(job)

for _ in range(5):
    # run_pending() runs jobs that are due.
    schedule.run_pending()
    time.sleep(1)
