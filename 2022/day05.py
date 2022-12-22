from config import *

inputs_file = os.path.join(inputs_path, 'day05.txt')

# Build list of
shipping = {}
with open(inputs_file, 'r') as inputs:
    full_input = inputs.read().split('\n\n')
    initial_load = full_input[0].splitlines()
    instructions = full_input[1].splitlines()


# Generate dictionary with stack lists
for stack in range(0, int(initial_load[-1].strip().split(' ')[-1])):
    shipping.update({stack: []})

# Load crates into columns
for load in initial_load[:-1]:
    load = load.replace('    ', ' [] ').replace('  ', ' ').strip().replace('[', '').replace(']', '').split(' ')
    for stack in range(0, int(initial_load[-1].strip().split(' ')[-1])):
        if len(load[stack]) > 0:
            shipping[stack].append(load[stack])

# Reverse crates in columns
for column in shipping:
    listas2 = shipping[column]
    listas2.reverse()
    shipping.update({column: listas2})

#########################
# Read instructions


for instruction in instructions:
    take_from = int(instruction.split(' ')[3])-1
    take_to = int(instruction.split(' ')[5])-1
    take_count = int(instruction.split(' ')[1])

    took_what = shipping[take_from][-take_count:]
    tmp_list = shipping[take_from][:-take_count]

    # Do actual manipulation here
    shipping[take_from] = tmp_list
    # # Move one at a time
    # took_what.reverse()
    # for crate in took_what:
    #     shipping[take_to].append(crate)

    # Move all at once
    shipping[take_to] = shipping[take_to] + took_what



top_crates = []
for key in sorted(shipping.keys()):
    top_crates.append(shipping[key][-1])

print(''.join(top_crates))


