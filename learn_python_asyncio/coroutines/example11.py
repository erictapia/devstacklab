import asyncio
import time
from typing import Callable, Coroutine

import httpx


addr = "https://langa.pl/crawl"
todo = set()


async def crawl2(prefix: str, url: str = "") -> None:
    url = url or prefix

    client = httpx.AsyncClient()

    try:
        response = await client.get(url)
    
    finally:
        await client.aclose()
    
    for line in response.text.splitlines():
        if line.startswith(prefix):
            task = asyncio.create_task(crawl2(prefix, line), name=line)
            todo.add(task)


async def progress(url: str, algo: Callable[..., Coroutine]) -> None:
    # report in an elegant way

    # tells asyncio to run task in the background
    # it runs only when there is an await
    task = asyncio.create_task(algo(url), name=url)

    # A collection of tasks
    todo.add(task)

    start = time.time()

    while len(todo):
        # await on todo tasks, will not raise exception instead returns:
        # - done: completed tasks
        # - _pending: tasks yet to complete
        done, _pending = await asyncio.wait(todo, timeout=0.5)

        # Update the todo by removing what is already done
        todo.difference_update(done)
        urls = (t.get_name() for t in todo)

        print(f"{len(todo)}: " + ", ".join(sorted(urls))[-75:])
    
    end = time.time()
    print(f"Took {int(end-start)} seconds")


async def async_main() -> None:
    try:
        await progress(addr, crawl2)
    
    except asyncio.CancelledError:
        for task in todo:
            task.cancel()
        
        done, pending = await asyncio.wait(todo, timeout=1.0)

        # remove done tasks from the todo collection
        todo.difference_update(done)

        # remove pending tasks from the todo collection
        todo.difference_update(pending)

        if todo:
            print("warning: new tasks added while we were cancelling")


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    task = loop.create_task(async_main())

    loop.call_later(5, task.cancel)

    loop.run_until_complete(task)
