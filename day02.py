# input - number of Calories each Elf is carrying: https://adventofcode.com/2022/day/2/input
from config import *

inputs_file = os.path.join(inputs_path, 'day02.txt')
# Rock - A, X, Paper - B, Y, Scissors - C, Z

# Match points
# Win - 6, Draw - 3, Lose - 0
# Points for shape
# Rock - 1, Paper - 2, Scissors - 3

games = []
with open(inputs_file, 'r') as inputs:
    for line in inputs:
        games.append(line.strip().replace(' ', ''))


def calculate_points(games):
    points_won = 0
    winning_combinations = ['AY', 'BZ', 'CX']
    draw_combinations = ['AX', 'BY', 'CZ']

    for game in games:
        if game[1] == 'X':
            points_won += 1
        elif game[1] == 'Y':
            points_won += 2
        else:
            points_won += 3

        if game in winning_combinations:
            points_won += 6
        elif game in draw_combinations:
            points_won += 3
    return points_won

print(f"First round points: {calculate_points(games)} ")

# 2nd round
# X - lose, Y - draw, Z - win

games2 = []
for game in games:
    if game[1] == 'X':
        if game[0] == 'A': games2.append('AZ')
        if game[0] == 'B': games2.append('BX')
        if game[0] == 'C': games2.append('CY')

    if game[1] == 'Y':
        if game[0] == 'A': games2.append('AX')
        if game[0] == 'B': games2.append('BY')
        if game[0] == 'C': games2.append('CZ')

    if game[1] == 'Z':
        if game[0] == 'A': games2.append('AY')
        if game[0] == 'B': games2.append('BZ')
        if game[0] == 'C': games2.append('CX')


print(f"Second round points: {calculate_points(games2)} ")