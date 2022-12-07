import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Terminal import Terminal

terminal = Terminal()

start = time.time()
with open('07.input') as f:
    for line in f.readlines():
        terminal.parse(line.replace("\n", ""))

part_one = terminal.get_total_sum()
print(f"Part 1: {part_one}")

part_two = terminal.get_deletion_size()
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")