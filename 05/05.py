import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from CargoShip import CargoShip
from CargoCrane import CargoCrane

is_parsing_crate_data = True
is_parsing_op_data = False

cargo_ship = CargoShip(crate_stacks=dict())
mirrored_cargo_ship = CargoShip(crate_stacks=dict())
cargo_crane = CargoCrane(operations=list(), version=9000)

start = time.time()
with open('05.input') as f:
    for line in f.readlines():
        if line == "\n":
            is_parsing_op_data = True
            is_parsing_crate_data = False
            continue

        if is_parsing_crate_data:
            cargo_ship.parse_crate_input(line)
            mirrored_cargo_ship.parse_crate_input(line)

        if is_parsing_op_data:
            cargo_crane.parse_op_input(line)

cargo_crane.execute(cargo_ship=cargo_ship)

top_crates = ""
for key in sorted(cargo_ship.crate_stacks):
    top_crates += cargo_ship.crate_stacks.get(key).pop(0)

part_one = top_crates
print(f"Part 1: {part_one}")

cargo_crane.version = 9001
cargo_crane.execute(cargo_ship=mirrored_cargo_ship)

top_crates = ""
for key in sorted(mirrored_cargo_ship.crate_stacks):
    top_crates += mirrored_cargo_ship.crate_stacks.get(key).pop(0)

part_two = top_crates
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")