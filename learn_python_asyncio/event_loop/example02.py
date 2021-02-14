from example01 import loop, print_now


# Each call registers another callback
def trampoline(name: str = "") -> None:
    print(name, end=" ")
    print_now()
    loop.call_later(0.5, trampoline, name)


if __name__ == "__main__":
    loop.call_soon(trampoline)
    loop.call_later(6, loop.stop)
    loop.run_forever()
