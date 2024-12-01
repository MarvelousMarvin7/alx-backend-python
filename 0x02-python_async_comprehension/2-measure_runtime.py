#!/usr/bin/env python3
""" Measure runtime for four parallel comprehensions """

import asyncio
import time

async_comprehen = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """ measure runtime"""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehen() for _ in range(4)))
    end_time = time.perf_counter()
    total_runtime = end_time - start_time
    return total_runtime
