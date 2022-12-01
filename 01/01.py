import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Elf import ElfInventory

elves = list()

start = time.time()
with open('01.input') as f:
    elf = ElfInventory(total_calories=0)

    for line in f.readlines():
        if line != '\n':
            elf.add_food(int(line))
        else:
            elves.append(elf)
            elf = ElfInventory(total_calories=0)

elves.append(elf)
elves.sort()

part_one = elves.pop().total_calories
part_one_time_in_ms = (time.time() - start) * 1000
print(f"Part 1: {part_one}, execution time: {part_one_time_in_ms}ms")

part_two = part_one + elves.pop().total_calories + elves.pop().total_calories
part_two_time_in_ms = (time.time() - start) * 1000
print(f"Part 2: {part_two}, execution time: {part_two_time_in_ms}ms")