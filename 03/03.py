import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Rucksack import Rucksack

start = time.time()
total_priority = 0
badge_priority = 0

with open('03.input') as f:
    for line in f.readlines():
        r = Rucksack(compartment_1=list(), compartment_2=list())
        r.add_items(line)
        total_priority += r.get_common_item_priority()


part_one = total_priority
print(f"Part 1: {part_one}")

part_two = "WIP"
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")