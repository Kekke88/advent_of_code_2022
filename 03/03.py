import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Rucksack import Rucksack
from Squad import Squad

start = time.time()
total_priority = 0
badge_priority = 0
s = Squad(rucksack_one=None, rucksack_two=None, rucksack_three=None)

with open('03.input') as f:
    for line in f.readlines():
        r = Rucksack(compartment_1=list(), compartment_2=list())
        r.add_items(line.replace("\n", ""))
        total_priority += r.get_common_item_priority()
        s.add_rucksack(r)

        if s.is_full():
            badge_priority += s.get_badge_priority()
            s = Squad(rucksack_one=None, rucksack_two=None, rucksack_three=None)


part_one = total_priority
print(f"Part 1: {part_one}")

part_two = badge_priority
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")