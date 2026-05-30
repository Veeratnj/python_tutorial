"""
Network Programming

Example and comments for Network Programming.
"""

# Network Programming
import socket
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print("Socket created", s.family, s.type)
