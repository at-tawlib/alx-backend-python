#!/usr/bin/env python3
"""
The basics of async
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """waits for random max_delay and returns it"""
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
