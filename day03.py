from config import *

inputs_file = os.path.join(inputs_path, 'day03.txt')

rucksacks = []
with open(inputs_file, 'r') as inputs:
    for line in inputs:
        rucksacks.append(line.strip())


priority = list(string.ascii_letters)



matching_letters = []
for rucksack in rucksacks:
    first_half, second_half = rucksack[0:len(rucksack)//2], rucksack[len(rucksack)//2:]
    #print (len(first_half), second_half)


    for i in range(0, len(first_half)):
        if first_half[i] in second_half:
            #print("matching letter", first_half[i])
            matching_letters.append(first_half[i])
            break

print (matching_letters)
print (priority)
print(priority.index('A')+1)

sum_of_priorities = 0
for letter in matching_letters:
    sum_of_priorities += (priority.index(letter) + 1)

print(sum_of_priorities)

########################
# second part
###########

matching_letters2 = []
for i in range(0, len(rucksacks), 3):
    set_of_elfs = rucksacks[i: i+3]

    for i in range(0, len(set_of_elfs[0])):
        if set_of_elfs[0][i] in set_of_elfs[1] and set_of_elfs[0][i] in set_of_elfs[2]:
            matching_letters2.append(set_of_elfs[0][i])
            break

print(matching_letters2)

sum_of_priorities2 = 0
for letter in matching_letters2:
    sum_of_priorities2 += (priority.index(letter) + 1)

print(sum_of_priorities2)