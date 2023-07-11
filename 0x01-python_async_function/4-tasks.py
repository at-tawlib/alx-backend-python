#!/usr/bin/env python3
"""
Basics
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawn task_wait_random n times with the specified max_delay
    return listof all the delays in ascending order
    """
    tasks = []
    delays = []

    for _ in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
