from example01 import loop, print_now
from example02 import trampoline


if __name__ == "__main__":
    loop.call_soon(trampoline, "First")
    loop.call_soon(trampoline, "Second")
    loop.call_soon(trampoline, "Third")

    loop.call_later(8, loop.stop)
    loop.run_forever()
