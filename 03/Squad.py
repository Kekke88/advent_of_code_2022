from dataclasses import dataclass
from Rucksack import Rucksack


@dataclass
class Squad:
    rucksack_one: Rucksack
    rucksack_two: Rucksack
    rucksack_three: Rucksack

    def get_badge_priority(self) -> int:
        item = self.get_badge()
        return ord(item) - 64 + 26 if item.isupper() else ord(item) - 96

    def get_badge(self) -> str:
        return ''.join(set(self.rucksack_one.get_all_items()) & set(self.rucksack_two.get_all_items()) & set(self.rucksack_three.get_all_items()))

    def is_full(self) -> bool:
        if self.rucksack_one and self.rucksack_two and self.rucksack_three:
            return True
        return False

    def add_rucksack(self, rucksack: Rucksack) -> bool:
        if not self.rucksack_one:
            self.rucksack_one = rucksack
        elif not self.rucksack_two:
            self.rucksack_two = rucksack
        elif not self.rucksack_three:
            self.rucksack_three = rucksack
        else:
            return False
        
        return True