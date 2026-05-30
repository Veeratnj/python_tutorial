"""
Linked Lists

Example and comments for Linked Lists.
"""

# Linked Lists
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

head = Node(1)
head.next = Node(2)
print(head.value, head.next.value)
