#!/usr/bin/env python3
'''2556787890
'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random
def task_wait_random(max_delay: int) -> asyncio.Task:
    '''123436557896789
    '''
    return asyncio.create_task(wait_random(max_delay))
