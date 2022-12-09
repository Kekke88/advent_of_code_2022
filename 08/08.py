import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

tree_matrix = list()

def is_visible(trees: list, x: int, y: int) -> bool:
    is_blocked_south = False
    for i in range(x+1, len(trees)):
        if trees[i][y] >= trees[x][y]:
            is_blocked_south = True
    
    is_blocked_west = False
    for i in range(y-1, -1, -1):
        if trees[x][i] >= trees[x][y]:
            is_blocked_west = True

    is_blocked_north = False
    for i in range(x-1, -1, -1):
        
        if trees[i][y] >= trees[x][y]:
            is_blocked_north = True

    is_blocked_east = False
    for i in range(y+1, len(trees)):
        if trees[x][i] >= trees[x][y]:
            is_blocked_east = True

    return not (is_blocked_east and is_blocked_north and is_blocked_south and is_blocked_west)

def get_visible_trees(trees: list, x: int, y: int) -> int:
    south_sum = 0
    for i in range(x+1, len(trees)):
        if trees[i][y] < trees[x][y]:
            south_sum += 1
        elif trees[i][y] >= trees[x][y]:
            south_sum += 1 
            break
        else:
            break
    
    west_sum = 0
    for i in range(y-1, -1, -1):
        if trees[x][i] < trees[x][y]:
            west_sum += 1
        elif trees[x][i] >= trees[x][y]:
            west_sum += 1
            break
        else:
            break

    north_sum = 0
    for i in range(x-1, -1, -1):
        if trees[i][y] < trees[x][y]:
            north_sum += 1
        elif trees[i][y] >= trees[x][y]:
            north_sum += 1
            break
        else:
            break

    east_sum = 0
    for i in range(y+1, len(trees)):
        if trees[x][i] < trees[x][y]:
            east_sum += 1
        elif trees[x][i] >= trees[x][y]:
            east_sum += 1
            break
        else:
            break
        
    return south_sum * west_sum * north_sum * east_sum

def find_top_scenic_score(trees: list) -> int:
    scenic_score = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees) - 1):
            tmp = get_visible_trees(trees, i, j)
            if tmp > scenic_score:
                scenic_score = tmp
    return scenic_score 

def find_visible_trees(trees: list) -> int:
    visible_trees = 0
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees) - 1):
            print(end=trees[i][j])
            if is_visible(trees, i, j): 
                visible_trees += 1
        print("")
    return visible_trees

start = time.time()
with open('08.input') as f:
    for line in f.readlines():
        tree_matrix += line.split()

visible_trees = find_visible_trees(trees=tree_matrix)

part_one = visible_trees + len(tree_matrix) * 4 - 4
print(f"Part 1: {part_one}")

scenic_score = find_top_scenic_score(trees=tree_matrix)
part_two = scenic_score
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")