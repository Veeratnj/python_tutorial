"""
Threads

Example and comments for Threads.
"""

# Threads
import threading

def worker():
    print("Worker thread")

thread = threading.Thread(target=worker)
thread.start()
thread.join()
