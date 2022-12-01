import os
import sys
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from lib.misc import is_integer
from Elf import ElfInventory

elves = list()

with open('01.input') as f:
    elf = ElfInventory(total_calories=0)

    for line in f.readlines():
        if is_integer(line):
            elf.add_food(int(line))
        else:
            elves.append(elf)
            elf = ElfInventory(total_calories=0)

elves.append(elf)
elves.sort()

part_one = elves.pop().total_calories
part_two = part_one + elves.pop().total_calories + elves.pop().total_calories

print(f"Part 1: {part_one}")
print(f"Part 2: {part_two}")