from dataclasses import dataclass
from typing import Dict

@dataclass
class ElfInventory:
    total_calories: int

    def add_food(self, calories: int):
        self.total_calories += calories
    
    def __lt__(self, other):
         return self.total_calories < other.total_calories
