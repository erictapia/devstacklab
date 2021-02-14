import asyncio

from example01 import keep_printing


async def async_main() -> None:
    await keep_printing("First"),
    await keep_printing("Second"),
    await keep_printing("Third")



async def async_main_gather() -> None:
    await asyncio.gather(
        keep_printing("First"),
        keep_printing("Second"),
        keep_printing("Third")
    )


if __name__ == "__main__":
    # This will only run the "First" since its an infinite loop
    print("Without gather")
    print("-" * 80)
    coroutine = async_main()
    
    try:
        asyncio.run(asyncio.wait_for(coroutine, 5))

    except asyncio.TimeoutError:
        print("oops, time's up!")
        print("-" * 80)

    # This will run all three
    print("With gather")
    print("-" * 80)
    coroutine = async_main_gather()
    try:
        asyncio.run(asyncio.wait_for(coroutine, 5))

    except asyncio.TimeoutError:
        print("oops, time's up!")
        print("-" * 80)
