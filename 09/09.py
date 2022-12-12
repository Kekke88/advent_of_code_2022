import os
import sys
import time
import curses

from curses import wrapper
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from Rope import Rope



def main(stdscr):
    pad = curses.newpad(200, 400)
    stdscr.refresh()

    for i in range(1000):
        for j in range(26):
            pad.addstr(".")

    pad.box()
    pad.refresh(0, 0, 5, 10, 50, 150)

    stdscr.refresh()

    rope = Rope(tails=9, scr = pad)

    with open('09.input') as f:
        for line in f.readlines():
            direction, amount = line.split(" ")
            rope.store_command(direction, int(amount))
    rope.visualize()
    stdscr.getch()

wrapper(main)

#start = time.time()
#with open('09.input') as f:
#    for line in f.readlines():
#        direction, amount = line.split(" ")
#        rope.store_command(direction, int(amount))

#part_one = len(rope.tail_log)
#print(f"Part 1: {part_one}")

#part_two = len(rope.tail_log)
#print(f"Part 2: {part_two}")

#print(f"Total execution time: {(time.time() - start) * 1000} ms")