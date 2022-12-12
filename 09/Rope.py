from dataclasses import dataclass
import math
import time
import curses

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
    commands: list
    scr: any
    offset_x: int = 75
    offset_y: int = 150

    def __init__(self, tails = 1, scr = None):
        self.head = Point()
        self.tails = list()
        self.commands = list()

        for i in range(0, tails):
            self.tails.append(Point())

        self.tail_log = dict()
        self.head_log = dict()
        self.log_path()
        self.scr = scr

    def visualize(self):
        for command in self.commands:
            self.move(command[0], command[1])

    def store_command(self, direction: str, amount: int):
        self.commands.append([direction, amount])

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

        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

        # Draw
        self.scr.erase()
        for i in range(len(self.tails) - 1, -1, -1):
            self.scr.addstr(abs(self.tails[i].x + 100), abs(self.tails[i].y + 200), "█", curses.color_pair(3))#str(i+1))
        self.scr.addstr(self.head.x + 100, self.head.y + 200, "█", curses.color_pair(2))
        if self.head.x + 100 > (self.offset_x + 25):
            self.offset_x += 1
        if self.head.y + 200 > (self.offset_y + 75):
            self.offset_y += 1
        if self.head.x + 100 < (self.offset_x):
            self.offset_x -= 1
        if self.head.y + 200 < (self.offset_y):
            self.offset_y -= 1

        self.scr.addstr(self.offset_x, self.offset_y, f"Screen Offset x: {self.offset_x}, y: {self.offset_y}")
        self.scr.addstr(self.offset_x+1, self.offset_y, f"Tail visits: {len(self.tail_log)}", curses.color_pair(1))
        self.scr.box()
        self.scr.refresh(self.offset_x, self.offset_y, 5, 10, 50, 150)
        time.sleep(0.005)

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
