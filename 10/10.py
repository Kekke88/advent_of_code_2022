import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from CPU import CPU

cpu = CPU()

start = time.time()
with open('10.input') as f:
    for line in f.readlines():
        cpu.parse_instruction(line.replace("\n", ""))

#sum = 0
#cpu.run(cycles=19)
#sum += cpu.x * 20
#cpu.run(cycles=40)
#sum += cpu.x * 60
#cpu.run(cycles=40)
#sum += cpu.x * 100
#cpu.run(cycles=40)
#sum += cpu.x * 140
#cpu.run(cycles=40)
#sum += cpu.x * 180
#cpu.run(cycles=40)
#sum += cpu.x * 220

part_one = 100
print(f"Part 1: {part_one}")

cpu.reset()
cpu.run(cycles=240)

part_two = "WIP"
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")