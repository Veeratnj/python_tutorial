"""
Asyncio Tasks

Example and comments for Asyncio Tasks.
"""

# Asyncio Tasks
import asyncio

async def worker(name):
    print(name)

async def main():
    task = asyncio.create_task(worker("Task 1"))
    await task

asyncio.run(main())
