from config import *

inputs_file = os.path.join(inputs_path, 'day03.txt')

# Build list of rucksacks
rucksacks = []
with open(inputs_file, 'r') as inputs:
    for line in inputs:
        rucksacks.append(line.strip())


# function to calculate sum of priorities
def calculate_prio(item_list):
    priority = list(string.ascii_letters)
    sum_of_priorities = 0
    for item in item_list:
        sum_of_priorities += (priority.index(item) + 1)
    return sum_of_priorities


# find matching item in every single backpack
matching_items = []
for rucksack in rucksacks:
    first_half, second_half = rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:]
    for i in range(0, len(first_half)):
        if first_half[i] in second_half:
            matching_items.append(first_half[i])
            break

# Find matching item in sets of 3
matching_badges = []
for i in range(0, len(rucksacks), 3):
    set_of_elfs = rucksacks[i: i+3]

    for i in range(0, len(set_of_elfs[0])):
        if set_of_elfs[0][i] in set_of_elfs[1] and set_of_elfs[0][i] in set_of_elfs[2]:
            matching_badges.append(set_of_elfs[0][i])
            break


print(f'Sum of priorities are: {calculate_prio(matching_items)}')
print(f'Sum of badges are: {calculate_prio(matching_badges)}')

