import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Rope import Rope

rope = Rope(tails=9)

start = time.time()
with open('09.input') as f:
    for line in f.readlines():
        direction, amount = line.split(" ")
        rope.move(direction, int(amount))

part_one = len(rope.tail_log)
print(f"Part 1: {part_one}")

part_two = len(rope.tail_log)
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")