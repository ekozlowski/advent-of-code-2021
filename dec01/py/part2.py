"""
There are much simpler ways to solve this, but I wanted to experiment with some deques and coroutines in Python.

"""
from collections import deque
depths = deque([int(x.strip()) for x in open('../input.txt', 'r').readlines()])


def process(stream, next_coroutine):
    while(len(stream) >= 3):
        vals = stream[0], stream[1], stream[2]
        next_coroutine.send(vals)
        stream.popleft()
    next_coroutine.close()


def get_depth_increases():
    increases = 0
    previous = None
    try:
        while True:
            current = (yield)
            if previous is None:
                previous = current
                continue # can't compare b/c we don't have a previous value.
            else:
                if sum(current) > sum(previous):
                    increases += 1
            previous = current
    except GeneratorExit:
        print("Done with depth increases!")
        print(f"There were {increases} depth increases")


gdi = get_depth_increases()
gdi.__next__()  # initialize coroutine (run to 'current = (yield)')
process(depths, gdi)
