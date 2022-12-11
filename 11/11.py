import os
import sys
import time
import re
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Monkey import Monkey
from Game import Game

monkeys = list()

start = time.time()
with open('11.input') as f:
    line = f.readline()
    while line:
        if "Monkey" in line:
            _id = re.search("([0-9]+)", line).group()
            items = list(map(int, re.findall("([0-9]+)", f.readline())))
            operation_template = f.readline().replace("  Operation: new = ", "").replace("\n", "")
            test = int(re.search("([0-9]+)", f.readline()).group())
            test_true = int(re.search("([0-9]+)", f.readline()).group())
            test_false = int(re.search("([0-9]+)", f.readline()).group())

            monkey = Monkey(_id=_id, operation_template=operation_template, test=test, test_true=test_true, test_false=test_false)
            monkey.add_items(items)
    
            monkeys.append(monkey)
        
        line = f.readline()

game = Game(monkeys=monkeys)
game.play(rounds=10000)
monkey_business = game.get_monkey_business()
game.print_mb()

part_one = monkey_business
print(f"Part 1: {part_one}")

part_two = "WIP"
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")