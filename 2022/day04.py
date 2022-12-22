from config import *

inputs_file = os.path.join(inputs_path, 'day04.txt')

# Build list of rucksacks
pairs = []
with open(inputs_file, 'r') as inputs:
    for line in inputs:
        pairs.append(line.strip().split(','))


fully_contain = 0
overlap = 0

for pair in pairs:
    elf_a = [int(i) for i in pair[0].split('-')]
    elf_b = [int(i) for i in pair[1].split('-')]

    # Count full contains
    if elf_a[0] >= elf_b[0] and elf_a[1] <= elf_b[1]:
        fully_contain += 1
    elif elf_b[0] >= elf_a[0] and elf_b[1] <= elf_a[1]:
        fully_contain += 1

    # Count Overlaps
    if elf_a[1] >= elf_b[0] and elf_a[1] <= elf_b[1]:
        overlap += 1

    elif elf_b[1] >= elf_a[0] and elf_b[1] <= elf_a[1]:
        overlap += 1



print(f"Fully contains: {fully_contain}")
print(f"Overlaps: {overlap}")

