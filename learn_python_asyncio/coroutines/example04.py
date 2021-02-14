import asyncio
import inspect

from example01 import keep_printing


async def async_function() -> None:
    await keep_printing()


if __name__ == "__main__":
    coroutine = async_function()
    
    print(f"type(async_function) = {type(async_function)}")
    print(f"type(coroutine) = {type(coroutine)}")
    print(f"inspect.isawaitable(async_funcition) = {inspect.isawaitable(async_function)}")
    print(f"inspect.isawaitable(coroutine) = {inspect.isawaitable(coroutine)}")
