import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

start = time.time()
test = [0, 0, 0]
with open('01.input') as f:
    c = 0
    for line in f.readlines():
        if line != '\n':
            c += float(line)
        else:
            if test[0] < c:
                test[0] = c
                test.sort()
            c = 0
test.sort(reverse=True)

part_one = test[0]
part_one_time_in_ms = (time.time() - start) * 1000
print(f"Part 1: {part_one}, execution time: {part_one_time_in_ms} ms")

part_two = sum(test)
part_two_time_in_ms = (time.time() - start) * 1000 - part_one_time_in_ms
print(f"Part 2: {part_two}, execution time: {part_two_time_in_ms} ms")

print(f"Total execution time: {(time.time() - start) * 1000} ms")