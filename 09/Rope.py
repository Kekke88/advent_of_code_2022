from dataclasses import dataclass
import math

@dataclass
class Point:
    x: int = 0
    y: int = 0

@dataclass
class Rope:
    head: Point
    tails: list
    tail_log: dict
    head_log: dict

    def __init__(self, tails = 1):
        self.head = Point()
        self.tails = list()

        for i in range(0, tails):
            self.tails.append(Point())

        self.tail_log = dict()
        self.head_log = dict()
        self.log_path()

    def follow(self, part_to_follow: Point, tail_index: int):
        part = self.tails[tail_index]

        if self.get_distance_between_parts(part_to_follow, part) < 2:
            return

        move_vector = Point()

        if part_to_follow.x > part.x:
            move_vector.x = 1
        if part_to_follow.y > part.y:
            move_vector.y = 1
        if part_to_follow.y < part.y:
            move_vector.y = -1
        if part_to_follow.x < part.x:
            move_vector.x = -1

        part.x += move_vector.x
        part.y += move_vector.y

        tail_index += 1

        if len(self.tails) > tail_index:
            self.follow(part_to_follow=part, tail_index=tail_index)

    def log_path(self, tail=9):
        self.head_log[str(self.head.x) + ":" + str(self.head.y)] = True
        self.tail_log[str(self.tails[tail-1].x) + ":" + str(self.tails[tail-1].y)] = True
        
    def get_distance_between_parts(self, part_to_follow: Point, part: Point) -> int:
        return math.sqrt(math.pow(part_to_follow.x - part.x, 2) + math.pow(part_to_follow.y - part.y, 2))


    def move(self, direction: str, amount: int):
        move_vector = Point()
        if direction == "R":
            move_vector.x = 1
        elif direction == "U":
            move_vector.y = -1
        elif direction == "L":
            move_vector.x = -1
        else:
            move_vector.y = 1
        
        for i in range(0, amount):
            self.head.x += move_vector.x
            self.head.y += move_vector.y
            if len(self.tails) > 0:
                self.follow(part_to_follow=self.head, tail_index=0)
            self.log_path()
