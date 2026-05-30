"""
Project: Task Scheduler

Example and comments for Project: Task Scheduler.
"""

# Project: Task Scheduler
import schedule
import time

def job():
    print("Running scheduled task")

# schedule.every(1).minutes.do(job)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
