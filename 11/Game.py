from Monkey import Monkey
import math

class Game:
    monkeys: list[Monkey]

    def __init__(self, monkeys: list):
        self.monkeys = monkeys

    def get_monkey_business(self) -> int:
        top_monkeys = [0, 0]
        
        for monkey in self.monkeys:
            if top_monkeys[0] < monkey.inspected_items:
                top_monkeys[0] = monkey.inspected_items
                top_monkeys.sort()
        
        return top_monkeys[0] * top_monkeys[1]
    
    def print_mb(self):
        for monkey in self.monkeys:
            print(f"Monkey #{monkey._id} inspected items {monkey.inspected_items} times.")

    def play(self, rounds: int = 1):
        for i in range(0, rounds):
            mod = math.prod(m.test for m in self.monkeys)
            for monkey in self.monkeys:
                thrown_items = monkey.do_action(mod)

                for k, v in thrown_items.items():
                    self.monkeys[k].add_items(v)