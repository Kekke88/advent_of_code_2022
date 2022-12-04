from dataclasses import dataclass
from typing import List

@dataclass
class Rucksack:
    compartment_1: List
    compartment_2: List

    def get_common_item(self) -> str:
        return ''.join(set(self.compartment_1).intersection(self.compartment_2))
    
    def get_common_item_priority(self) -> int:
        item = self.get_common_item()
        return ord(item) - 64 + 26 if item.isupper() else ord(item) - 96

    def get_badge(self, rucksack2, rucksack3) -> str:
        

    def add_items(self, items: str):
        self.compartment_1 = items[:len(items)//2]
        self.compartment_2 = items[len(items)//2:]