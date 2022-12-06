import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

LENGTH_OF_MARKER = 4
LENGTH_OF_MESSAGE_START = 14

marker = 0
start_of_message = 0

start = time.time()
with open('06.input') as f:
    for line in f.readlines():
        for i in range(0, len(line)-1):
            if marker != 0 and start_of_message != 0:
                break
            if len(set(line[i:i+LENGTH_OF_MARKER])) == LENGTH_OF_MARKER and marker == 0:
                marker = i + LENGTH_OF_MARKER
            if len(set(line[i:i+LENGTH_OF_MESSAGE_START])) == LENGTH_OF_MESSAGE_START and start_of_message == 0:
                start_of_message = i + LENGTH_OF_MESSAGE_START


part_one = marker
print(f"Part 1: {part_one}")

part_two = start_of_message
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")