from example01 import loop, print_now
from example02 import trampoline


# This function takes long to complete thus hog
# Its intentional to see how the async event loop executes callbacks
# it runs callbacks one at a time
def hog():
    sum = 0
    print("Hog is running")
    for i in range(10_000):
        for j in range(10_000):
            sum += j
    
    return sum

if __name__ == "__main__":
    loop.call_soon(trampoline, "First")
    loop.call_soon(trampoline, "Second")
    loop.call_soon(trampoline, "Third")

    # Scheduling the hog to run 15 seconds later
    loop.call_later(15, hog)
    loop.call_later(20, loop.stop)

    # The async event loop has a debug mode that will print time lapsed and
    # code block location information for callbacks taking too long to
    # complete.  Not intended in production.  uvloop is recommended for
    # production
    loop.set_debug(True)

    loop.run_forever()
