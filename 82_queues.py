"""
Queues

Example and comments for Queues.
"""

# Queues
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
print(queue.popleft())
