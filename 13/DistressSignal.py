from dataclasses import dataclass, field
from functools import cmp_to_key

@dataclass
class Packet:
    packet_1: list = field(default_factory=list)
    packet_2: list = field(default_factory=list)

    def parse(self, packet_1_data: str, packet_2_data: str):
        self.packet_1 = eval(packet_1_data)
        self.packet_2 = eval(packet_2_data)

    def validate(self) -> bool:
        return self.compare(self.packet_1, self.packet_2)

    def compare(self, list_1, list_2) -> bool:
        for i in range(len(list_1)):
            if len(list_2) == i:
                return False

            if isinstance(list_1[i], int) and isinstance(list_2[i], int):
                if list_1[i] < list_2[i]:
                    return True
                if list_1[i] > list_2[i]:
                    return False

            if isinstance(list_1[i], list) and isinstance(list_2[i], int):
                v = self.compare(list_1[i], [list_2[i]])
                if isinstance(v, bool):
                    return v

            if isinstance(list_1[i], int) and isinstance(list_2[i], list):
                v = self.compare([list_1[i]], list_2[i])
                if isinstance(v, bool):
                    return v

            if isinstance(list_1[i], list) and isinstance(list_2[i], list):
                v = self.compare(list_1[i], list_2[i])
                if isinstance(v, bool):
                    return v

        if len(list_2) > len(list_1):
            return True

def compare(list_1, list_2) -> int:
    for i in range(len(list_1)):
        if len(list_2) == i:
            return 1

        if isinstance(list_1[i], int) and isinstance(list_2[i], int):
            if list_1[i] < list_2[i]:
                return -1
            if list_1[i] > list_2[i]:
                return 1

        if isinstance(list_1[i], list) and isinstance(list_2[i], int):
            v = compare(list_1[i], [list_2[i]])
            if isinstance(v, int):
                return v

        if isinstance(list_1[i], int) and isinstance(list_2[i], list):
            v = compare([list_1[i]], list_2[i])
            if isinstance(v, int):
                return v

        if isinstance(list_1[i], list) and isinstance(list_2[i], list):
            v = compare(list_1[i], list_2[i])
            if isinstance(v, int):
                return v

    if len(list_2) > len(list_1):
        return -1

@dataclass
class DistressSignal:
    packets: list[Packet] = field(default_factory=list)

    def add_packet(self, packet: Packet):
        self.packets.append(packet)

    def get_decoder_key(self) -> int:
        packets = list()

        for packet in self.packets:
            packets.append(packet.packet_1)
            packets.append(packet.packet_2)

        packets = sorted(packets, key=cmp_to_key(compare))

        i = 1
        decoder_key = 0
        for packet in packets:
            if packet == [[2]]:
                decoder_key = i
            
            if packet == [[6]]:
                decoder_key *= i

            i += 1

        return decoder_key

    def validate_packets(self):
        i = 1
        sum = 0
        for packet in self.packets:
            if packet.validate():
                sum += i
            i += 1

        return sum