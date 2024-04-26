#!/usr/bin/env python3
""" The regular function syntax task 3. """
import asyncio
random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    """ Task wait random. """
    return asyncio.create_task(randwait(max_delay))
