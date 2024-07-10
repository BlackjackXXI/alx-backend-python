#!/usr/bin/env python3
'''W4353654687587
'''
import asyncio
import random
from typing import Generator
async def async_generator() -> Generator[float, None, None]:
    '''SA24536537
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
