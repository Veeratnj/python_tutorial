"""
Async and Await

Example and comments for Async and Await.
"""

# Async and Await
import asyncio

async def say(message):
    print(message)

async def main():
    await say("Hello async")

asyncio.run(main())
