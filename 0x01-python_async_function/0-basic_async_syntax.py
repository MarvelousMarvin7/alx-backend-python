#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that
waits for a random delay between 0 and max_delay
(included and float value) secondsand eventually returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """return a wait_time that waits for a random delay
    between 0 and max_delay (included and float value) seconds
    """
    wait_time = random.uniform(0, max_delay)
    await asyncio.sleep(wait_time)
    return wait_time
