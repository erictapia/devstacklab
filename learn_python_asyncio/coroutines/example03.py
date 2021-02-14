import asyncio

from example01 import print_now


async def print3times() -> None:
    for _ in range(3):
        print_now()
        await asyncio.sleep(0.1)


if __name__ == "__main__":

    coro1 = print3times()
    coro2 = print3times()

    print(f"type(print3times) = {type(print3times)}")
    print(f"type(coro1) = {type(coro1)}")
    print(f"type(coro2) = {type(coro2)}")

    print("-" * 80)
    asyncio.run(coro1)
    
    print("-" * 80)
    asyncio.run(coro2)
    
    print("-" * 80)
    # This will throw a ValueError exception because its not a coroutine object
    # - Python 3.9.1 did not throw an exception and ran it
    asyncio.run(print3times())

    print("-" * 80)
    # Re-running a coroutine will throw a RuntimeError exception because
    # coroutines can only be awaited on once
    asyncio.run(coro1)
