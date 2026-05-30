"""
Concurrent Futures

Example and comments for Concurrent Futures.
"""

# Concurrent Futures
from concurrent.futures import ThreadPoolExecutor

def task(n):
    return n * n

with ThreadPoolExecutor() as executor:
    results = executor.map(task, [1, 2, 3])
    print(list(results))
