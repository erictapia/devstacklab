import asyncio
import time
from typing import Callable, Coroutine

import httpx


addr = "https://langa.pl/crawl"
todo = set()


async def crawl1(prefix: str, url: str = "") -> None:
    url = url or prefix

    client = httpx.AsyncClient()

    try:
        response = await client.get(url)
    
    finally:
        await client.aclose()
    
    for line in response.text.splitlines():
        if line.startswith(prefix):
            todo.add(line)
            await crawl1(prefix, line)
    
    todo.discard(url)



async def progress(url: str, algo: Callable[..., Coroutine]) -> None:
    # report in an elegant way

    # tells asyncio to run task in the background
    # it runs only when there is an await
    asyncio.create_task(algo(url), name=url)

    todo.add(url)

    start = time.time()

    while len(todo):
        print(
            f"{len(todo)}: "
            + ", ".join(sorted(todo))[-38:]
        )

        await asyncio.sleep(0.5)
    
    end = time.time()
    print(
        f"Took {int(end-start)}"
        + " seconds"
    )


if __name__ == "__main__":
    asyncio.run(progress(addr, crawl1))