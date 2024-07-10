#!/usr/bin/env python3
'''12343544867
'''
import asyncio
import time
from importlib import import_module as using

async_comprehension = using('1-async_comprehension').async_comprehension
async def measure_runtime() -> float:
    '''3145245635646797859
    '''
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - start_time
