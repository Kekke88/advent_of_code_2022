from dataclasses import dataclass

@dataclass
class Operation:
    amount: int
    _from: int
    to: int
