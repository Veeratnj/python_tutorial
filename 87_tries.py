"""
Tries

Example and comments for Tries.
"""

# Tries
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

root = TrieNode()
root.children["a"] = TrieNode()
print("Trie node added")
