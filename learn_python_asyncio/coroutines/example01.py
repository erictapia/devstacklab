import asyncio
import datetime


def print_now():
    print(datetime.datetime.now())


async def keep_printing(name: str = "") -> None:
    while True:
        print(name, end=" ")
        print_now()
        await asyncio.sleep(0.50)


# A async function to try/catch exceptions, the main entry
async def async_main() -> None:
    try:
        await asyncio.wait_for(keep_printing("Hey"), 10)
    
    except asyncio.TimeoutError:
        print("oops, time's up")


if __name__ == "__main__":
    asyncio.run(async_main())
