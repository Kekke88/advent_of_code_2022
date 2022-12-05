import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

duplicate_paths = 0
overlapping_paths = 0

start = time.time()
with open('04.input') as f:
    for line in f.readlines():
        paths = line.replace("\n", "").split(",")
        range_1 = paths[0].split("-")
        range_2 = paths[1].split("-")

        if int(range_1[0]) >= int(range_2[0]) and int(range_1[1]) <= int(range_2[1]):
            duplicate_paths += 1
        elif int(range_2[0]) >= int(range_1[0]) and int(range_2[1]) <= int(range_1[1]):
            duplicate_paths += 1

        if int(range_1[0]) <= int(range_2[1]) and int(range_2[0]) <= int(range_1[1]):
            overlapping_paths += 1

part_one = duplicate_paths
print(f"Part 1: {part_one}")

part_two = overlapping_paths
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")