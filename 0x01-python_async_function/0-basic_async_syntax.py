#!/usr/bin/env python3
'''T123567
'''
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    '''12345678
    '''
    wait_time = random.random() * max_delay
    await asyncio.sleep(wait_time)
    return wait_time
