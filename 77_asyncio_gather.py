"""
Asyncio Gather

Example and comments for Asyncio Gather.
"""

# Asyncio Gather
import asyncio

async def say(value):
    return value

async def main():
    results = await asyncio.gather(say(1), say(2))
    print(results)

asyncio.run(main())
