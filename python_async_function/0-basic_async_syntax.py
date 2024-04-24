#!/usr/bin/env python3
""" This async function takes an int that waits for a random delay. """
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    delay = random.randrange(0, max_delay)
    await asyncio.sleep(delay)
    return delay
