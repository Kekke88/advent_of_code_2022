from dataclasses import dataclass, field
import math

@dataclass
class Instruction:
    command: str
    parameters: list
    time_needed: int
    time_passed: int = 0

@dataclass
class CPU:
    x: int = 1
    instructions: list = field(default_factory=list)
    iterator: int = 0
    pixel_pos: int = 0

    def parse_instruction(self, instruction: str):
        command = instruction.split(" ")[0]
        parameters = instruction.split(" ")[1:]
        i = Instruction(command=command, parameters=parameters, time_needed=1 if command == "noop" else 2)
        self.instructions.append(i)

    def execute(self, instruction: Instruction):
        if instruction.command == "noop":
            return
        
        if instruction.command == "addx":
            self.x += int(instruction.parameters[0])

    def reset(self):
        self.iterator = 0
        self.x = 1
        self.pixel_pos = 0

    def draw(self):
        if self.x == self.pixel_pos - 1 or self.x == self.pixel_pos or self.x == self.pixel_pos + 1:
            print(end="#")
        else:
            print(end=".")

        self.pixel_pos += 1

        if self.pixel_pos == 40:
            print("")
            self.pixel_pos = 0

    def run(self, cycles=1):
        for i in range(0, cycles):
            instruction = self.instructions[self.iterator]
            
            instruction.time_passed += 1

            self.draw()

            if instruction.time_passed >= instruction.time_needed:
                self.execute(instruction)
                self.iterator += 1

            if self.iterator >= len(self.instructions):
                self.iterator = 0
