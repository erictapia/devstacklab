import asyncio

from example01 import print_now


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()

        try:
            await asyncio.sleep(0.50)
        
        except asyncio.CancelledError:
            # Catching cancellation
            print(name, "was cancelled")
            break


async def async_main_gather() -> None:
    try:
        await asyncio.wait_for(
            asyncio.gather(
                keep_printing("First"),
                keep_printing("Second"),
                keep_printing("Third")
            ),
            5
        )

    except asyncio.TimeoutError:
        print("oops, time's up!")


if __name__ == "__main__":
    asyncio.run(async_main_gather())
