import os
import sys
import time

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from lib.Vector2d import Vector2d

height_map = list()
visited = []

def get_available_nodes(height_map: list, position: Vector2d):
    test_pos = Vector2d()
    return_nodes = list()
    # North
    test_pos.x = position.x
    test_pos.y = position.y - 1
    if position.y > 0 and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        return_nodes.append(Vector2d(test_pos.x, test_pos.y))

    # East
    test_pos.x = position.x + 1
    test_pos.y = position.y
    if len(height_map[test_pos.y]) > test_pos.x and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        return_nodes.append(Vector2d(test_pos.x, test_pos.y))

    # South
    test_pos.x = position.x
    test_pos.y = position.y + 1
    if len(height_map) > test_pos.y and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        return_nodes.append(Vector2d(test_pos.x, test_pos.y))

    # West
    test_pos.x = position.x - 1
    test_pos.y = position.y
    if test_pos.x > 0 and is_available(
        from_pos=position, to_pos=test_pos, visited=visited
    ):
        return_nodes.append(Vector2d(test_pos.x, test_pos.y))

    return return_nodes


def shortest_path(height_map: list, position: Vector2d, end: Vector2d):
    path_list = [[position]]
    path_index = 0

    previous_nodes = {f"{position.x}:{position.y}"}
    if position == end:
        return path_list[0]
        
    while path_index < len(path_list):
        current_path = path_list[path_index]
        last_node = current_path[-1]
        next_nodes = get_available_nodes(height_map, last_node)

        if end in next_nodes:
            current_path.append(end)
            return current_path

        for next_node in next_nodes:
            if not f"{next_node.x}:{next_node.y}" in previous_nodes:
                new_path = current_path[:]
                new_path.append(next_node)
                path_list.append(new_path)
                previous_nodes.add(f"{next_node.x}:{next_node.y}")
        path_index += 1
    return []


def is_available(from_pos: Vector2d, to_pos: Vector2d, visited: dict) -> bool:
    check_char = height_map[to_pos.y][to_pos.x]
    if check_char == "E":
        check_char = "z"

    return ord(height_map[from_pos.y][from_pos.x]) + 1 >= ord(check_char)


def find_pos(height_map: list, character: str) -> Vector2d:
    search_pos = Vector2d()

    for i in range(0, len(height_map)):
        found = height_map[i].find(character)
        if found != -1:
            search_pos.x = found
            search_pos.y = i

    return search_pos

def find_start_positions(height_map: list) -> list:
    start_positions = list()

    for i in range(0, len(height_map)):
        for j in range(0, len(height_map[i])):
            if height_map[i][j] == "a":
                start_positions.append(Vector2d(j, i))

    return start_positions

start = time.time()
with open("12.input") as f:
    for line in f.readlines():
        height_map.append(line.replace("\n", ""))

start_pos = find_pos(height_map=height_map, character="S")
end_pos = find_pos(height_map=height_map, character="E")
height_map[start_pos.y] = height_map[start_pos.y].replace("S", "a")

solution = shortest_path(height_map=height_map, position=start_pos, end=end_pos)

part_one = len(solution) - 1
print(f"Part 1: {part_one}")

solutions = list()
start_positions = find_start_positions(height_map=height_map)
for start_pos in start_positions:
    path_length = len(shortest_path(height_map=height_map, position=start_pos, end=end_pos))
    if path_length > 0: 
        solutions.append(path_length)

solutions.sort()

part_two = solutions[0] - 1
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")
