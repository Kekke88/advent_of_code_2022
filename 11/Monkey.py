from dataclasses import dataclass, field
import math

@dataclass
class Monkey:
    _id: int
    operation_template: str
    test: int
    test_true: int
    test_false: int

    inspected_items: int = 0
    items: list = field(default_factory=list)

    def add_items(self, items: list):
        self.items += items

    def do_action(self, mod) -> dict:
        thrown_items = dict()
        for i in range(len(self.items) - 1, -1, -1):
            self.inspected_items += 1
            old = self.items[i]
            new = eval(self.operation_template)
            self.items[i] = new % mod

            if self.items[i] % self.test == 0:
                if not self.test_true in thrown_items:
                    thrown_items[self.test_true] = list()

                thrown_items[self.test_true].append(self.items[i])
                del self.items[i]
            else:
                if not self.test_false in thrown_items:
                    thrown_items[self.test_false] = list()

                thrown_items[self.test_false].append(self.items[i])
                del self.items[i]
        
        return thrown_items