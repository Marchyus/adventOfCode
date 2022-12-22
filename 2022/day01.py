# input - number of Calories each Elf is carrying: https://adventofcode.com/2022/day/1/input
from config import *

inputs_file = os.path.join(inputs_path, 'day01.txt')


top_3_calories = [0, 0, 0]
this_elf_calories = 0

with open(inputs_file, 'r') as inputs:
    for line in inputs:
        # If line is blank - check calorie max
        if len(line.strip()) < 1:
            if this_elf_calories > min(top_3_calories):
                # replace smallest number in the list
                index = top_3_calories.index(min(top_3_calories))
                top_3_calories[index] = this_elf_calories
            this_elf_calories = 0
        else:
            this_elf_calories += int(line)

    print(f'Most calories carried by singe dude: {max(top_3_calories)}')
    print(f'Calories carried by top 3 elfs: {sum(top_3_calories)}')
