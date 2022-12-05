from dataclasses import dataclass
from Operation import Operation
from CargoShip import CargoShip
import re

@dataclass
class CargoCrane:
    operations: list
    version: int

    def parse_op_input(self, line: str):
        line = re.sub(r'[^0-9 ]', '', line)
        values = list(filter(None, line.split(" ")))

        op = Operation(amount=values[0], _from=values[1], to=values[2])
        self.operations.append(op)

    def execute(self, cargo_ship: CargoShip):
        for op in self.operations:

            if self.version == 9000:
                for i in range(0, int(op.amount)):
                    crate = cargo_ship.crate_stacks.get(int(op._from)).pop(0)
                    cargo_ship.crate_stacks.get(int(op.to)).insert(0, crate)
            elif self.version == 9001:
                crates = list()
                for i in range(0, int(op.amount)):
                    crates.append(cargo_ship.crate_stacks.get(int(op._from)).pop(0))

                for crate in reversed(crates):
                    cargo_ship.crate_stacks.get(int(op.to)).insert(0, crate)
