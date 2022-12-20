import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from DistressSignal import Packet, DistressSignal

distress_signal = DistressSignal()

start = time.time()
with open('13.input') as f:
    while True:
        packet_1_data = f.readline().replace("\n", "")
        packet_2_data = f.readline().replace("\n", "")

        packet = Packet()
        packet.parse(packet_1_data=packet_1_data, packet_2_data=packet_2_data)
        distress_signal.add_packet(packet)

        newline = f.readline()

        if not newline:
            break

part_one = distress_signal.validate_packets()
print(f"Part 1: {part_one}")

distress_signal.add_packet(packet=Packet(packet_1=[[2]], packet_2=[[6]]))
part_two = distress_signal.get_decoder_key()
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")