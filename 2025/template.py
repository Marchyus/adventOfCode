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
def first(input):
    print(input)


first(part_a_test)


# Part B
def second(input):
    print(input)


#second(part_b_test)

