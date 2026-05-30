"""
Performance Profiling

Example and comments for Performance Profiling.
"""

# Performance Profiling
import cProfile

def work():
    sum(range(1000))

cProfile.run("work()")
