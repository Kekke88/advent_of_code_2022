import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from lib.Vector2d import Vector2d

height_map = list()


def is_available(from_pos: Vector2d, to_pos: Vector2d, visited: dict) -> bool:
    print(
        f"Checking {height_map[from_pos.y][from_pos.x]} -> {height_map[to_pos.y][to_pos.x]} ({ord(height_map[from_pos.y][from_pos.x])} -> {ord(height_map[to_pos.y][to_pos.x])})"
    )

    check_char = height_map[to_pos.y][to_pos.x]
    if check_char == "E":
        check_char = "z"

    return (
        ord(height_map[from_pos.y][from_pos.x]) + 1 >= ord(check_char) + 1
        and not f"{to_pos.x}:{to_pos.y}" in visited
    )


def find_start_pos(height_map: list) -> Vector2d:
    search_pos = Vector2d()

    for i in range(0, len(height_map)):
        found = height_map[i].find("S")
        if found != -1:
            search_pos.x = found
            search_pos.y = i

    return search_pos


def find_paths(height_map: list, visited: dict, position: Vector2d) -> dict:
    print("--- VISITED ---")
    print(visited)
    print(f"Current position: {height_map[position.y][position.x]}")
    if height_map[position.y][position.x] == "E":
        print("Returning")
        return visited
    test_pos = Vector2d()
    # North
    test_pos.x = position.x
    test_pos.y = position.y - 1
    if position.y > 0 and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        visited[f"{position.x}:{position.y - 1}"] = True
        find_paths(height_map=height_map, visited=visited, position=test_pos)

    # East
    test_pos.x = position.x + 1
    test_pos.y = position.y
    if len(height_map[test_pos.y]) > test_pos.x and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        visited[f"{position.x + 1}:{position.y}"] = True
        find_paths(height_map=height_map, visited=visited, position=test_pos)

    # South
    test_pos.x = position.x
    test_pos.y = position.y + 1
    if len(height_map) > test_pos.y and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        visited[f"{position.x}:{position.y + 1}"] = True
        find_paths(height_map=height_map, visited=visited, position=test_pos)

    # West
    test_pos.x = position.x - 1
    test_pos.y = position.y
    if test_pos.x > 0 and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        visited[f"{position.x + 1}:{position.y}"] = True
        find_paths(height_map=height_map, visited=visited, position=test_pos)


start = time.time()
with open("12.example.input") as f:
    for line in f.readlines():
        height_map.append(line.replace("\n", ""))

start_pos = find_start_pos(height_map=height_map)
print(f"Start pos: {start_pos.x}:{start_pos.y}")
height_map[start_pos.y] = height_map[start_pos.y].replace("S", "a")
print(height_map)
find_paths(height_map=height_map, visited={f"{start_pos.x}:{start_pos.y}": True}, position=start_pos)

part_one = "WIP"
print(f"Part 1: {part_one}")

part_two = "WIP"
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
