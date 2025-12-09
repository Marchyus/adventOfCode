from config import get_inputs # get and/or create input files

# Get file names
all_inputs = get_inputs(__file__)
part_a, part_b, part_a_test, part_b_test = [], [], [], []
if all_inputs["success"] == True:
    part_a, part_b = all_inputs["part_a"], all_inputs["part_b"]
    part_a_test, part_b_test = all_inputs["part_a_test"], all_inputs["part_b_test"]
else:
    print(f'Input file(s) are missing: {all_inputs}')



# Part A
def part_one(input):
    pointing_at = 50
    zero_count = 0
    for turn in input:
        # turn
        if turn.startswith("L"):
            pointing_at -= int(turn.lstrip("L"))
        else:
            pointing_at += int(turn.lstrip("R"))

        # adjust for <0 or >99
        while pointing_at < 0:
            pointing_at += 100
        while pointing_at > 99:
            pointing_at -= 100

        # count 0
        if pointing_at == 0:
            zero_count += 1

        print(f'rotated {turn}, points at {pointing_at}')
        
    print(f"0 count: {zero_count}")



# run test
#part_one(part_a)

# Part B
def part_two(input):
    pointing_at = 50
    zero_count = 0

    for turn in input:
        previous = pointing_at
        # turn
        print(f'Start at: {previous}', end= ' ')
        if turn.startswith("L"):
            pointing_at -= int(turn.lstrip("L"))
        else:
            pointing_at += int(turn.lstrip("R"))

        print(f'rotated {turn} to {pointing_at}', end=' ')

        if previous == 0: zero_count -= 1

        if previous <= pointing_at:
            zero_count += max(0, (pointing_at // 100) - ((previous - 1) // 100))
            print(f'[#{zero_count}]', end=' ')
        else:
            zero_count += max(0, (previous // 100) - ((pointing_at - 1) // 100))
            print(f'[#{zero_count}]', end=' ')

        pointing_at %= 100

        print(f'now pointing at: {pointing_at}')
        


        

        
        
    print(f"0 count: {zero_count}")

# same input
part_two(part_a)

