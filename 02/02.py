import os
import sys
import time
 
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

hand_scores = {
    'X': 1,
    'Y': 2,
    'Z': 3
}

outcomes = {
    'AX': 3,
    'AY': 6,
    'AZ': 0,
    'BX': 0,
    'BY': 3,
    'BZ': 6,
    'CX': 6,
    'CY': 0,
    'CZ': 3
}

outcome_map = {
    'AX': 'Z',
    'AY': 'X',
    'AZ': 'Y',
    'BX': 'X',
    'BY': 'Y',
    'BZ': 'Z',
    'CX': 'Y',
    'CY': 'Z',
    'CZ': 'X'
}

def calculate_score(opponent_hand: str, my_hand: str) -> list:
    my_optimal_hand = outcome_map[opponent_hand + my_hand]
    return [outcomes[opponent_hand + my_hand] + hand_scores[my_hand], outcomes[opponent_hand + my_optimal_hand] + hand_scores[my_optimal_hand]]

start = time.time()
total_score = 0
total_score_part_2 = 0
with open('02.input') as f:
    for line in f.readlines():
        opponent_hand, my_hand = line.strip().split(" ", 2)
        score, score_2 = calculate_score(opponent_hand=opponent_hand, my_hand=my_hand)
        total_score += score
        total_score_part_2 += score_2

part_one = total_score
print(f"Part 1: {part_one}")

part_two = total_score_part_2
print(f"Part 2: {part_two}")

print(f"Total execution time: {(time.time() - start) * 1000} ms")