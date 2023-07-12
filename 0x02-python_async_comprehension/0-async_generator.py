#!/usr/env/ python3
"""
Async Generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    coroutine that loops 10 times, each time asynchronously
    wait 1 second and yield a random number
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
