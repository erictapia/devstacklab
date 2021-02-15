import asyncio

import httpx


addr = "https://langa.pl/crawl"


# Initial version, very slow
#
# Issues:
# - backend tasks reporting status, print, not great ideas
# - recursive calls
# - await call is creating a blocking environment and does not take advantage
#   asyncio that allows concurrency
# - AsyncClient should be using a context manager
async def crawl0(prefix: str, url: str = "") -> None:
    url = url or prefix
    print(f"Crawling {url}")

    client = httpx.AsyncClient()

    try:
        response = await client.get(url)
    
    finally:
        await client.aclose()
    
    for line in response.text.splitlines():
        if line.startswith(prefix):
            await crawl0(prefix, line)


if __name__ == "__main__":
    asyncio.run(crawl0(addr))
