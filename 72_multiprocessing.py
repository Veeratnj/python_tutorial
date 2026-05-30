"""
Multiprocessing

Example and comments for Multiprocessing.
"""

# Multiprocessing
from multiprocessing import Process

def f():
    print("Process started")

if __name__ == "__main__":
    p = Process(target=f)
    p.start()
    p.join()
