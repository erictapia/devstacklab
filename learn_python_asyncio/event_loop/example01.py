import asyncio
import datetime


def print_now():
    print(datetime.datetime.now())


loop = asyncio.get_event_loop()


if __name__ == "__main__":
    
    loop.call_soon(print_now)
    loop.call_soon(print_now)
    loop.run_until_complete(asyncio.sleep(5))
