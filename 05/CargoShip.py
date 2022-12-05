from dataclasses import dataclass

@dataclass
class CargoShip:
    crate_stacks: dict

    def parse_crate_input(self, input: str):
        index = 0
        real_index = 0

        for c in input:
            if index % 4 == 0:
                real_index += 1

            if c.isalpha():
                if not real_index in self.crate_stacks:
                    self.crate_stacks[real_index] = list()
                self.crate_stacks[real_index].append(c)
            index += 1
