import asyncio
import random
import time

async def async_range(n):
    for i in range(n):
        yield i

async def print_a(n):
    async for i in async_range(10):
        print('A')
        await asyncio.sleep(random.randint(1, 100) / 50)


async def print_b(n):
    async for i in async_range(10):
        print('B')
        await asyncio.sleep(random.randint(1, 100) / 50)
    await print_c()


async def print_c():
    print('C')


async def main():
    await asyncio.gather(print_a(10), print_b(10))


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
