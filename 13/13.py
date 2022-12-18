import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from DistressSignal import Packet, DistressSignal

distress_signal = DistressSignal()

start = time.time()
with open('13.example.input') as f:
    while True:
        packet_1_data = f.readline().replace("\n", "")
        packet_2_data = f.readline().replace("\n", "")

        packet = Packet()
        packet.parse(packet_1_data=packet_1_data, packet_2_data=packet_2_data)
        distress_signal.add_packet(packet)

        newline = f.readline()

        if not newline:
            break

print(distress_signal)

part_one = "WIP"
print(f"Part 1: {part_one}")

part_two = "WIP"
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")