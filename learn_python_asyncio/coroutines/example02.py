import asyncio

from example01 import keep_printing, print_now


async def async_main() -> None:
    kp = keep_printing("Hey")

    # setup doesn't run until it has been awaited
    waiter = asyncio.wait_for(kp, 3)

    try:
        # Now that it has been awaited, the waiter will run thus keep printing
        await waiter
    except asyncio.TimeoutError:
        print("oops, time's up!")


async def async_main_without_await() -> None:
    kp = keep_printing("Hey")

    # setup doesn't run until it has been awaited
    waiter = asyncio.wait_for(kp, 3)

    try:
        # Without the await, the waiter will never run
        waiter
    except asyncio.TimeoutError:
        print("oops, time's up!")


if __name__ == "__main__":
    asyncio.run(async_main())

    # On purpose, without the await, will not run and an Exception will be
    # thrown
    asyncio.run(async_main_without_await())
