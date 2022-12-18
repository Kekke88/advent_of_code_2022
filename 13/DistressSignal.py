from dataclasses import dataclass, field

@dataclass
class Packet:
    packet_1: list = field(default_factory=list)
    packet_2: list = field(default_factory=list)

    def parse(self, packet_1_data: str, packet_2_data: str):
        self.packet_1 = eval(packet_1_data)
        self.packet_2 = eval(packet_2_data)

    def validate(self) -> bool:
        for i in range(len(self.packet_1)):
            self.compare(self.packet_1[i], self.packet_2[i])

@dataclass
class DistressSignal:
    packets: list = field(default_factory=list)

    def add_packet(self, packet: Packet):
        self.packets.append(packet)