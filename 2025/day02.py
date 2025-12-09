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
    input = input[0].split(",")
    #print(input)

    invalid_id_sum = 0

    for id_set in input:
        id1 = int(id_set.split('-')[0])
        id2 = int(id_set.split('-')[1])
        for i in range(id1, id2+1):
            #print(i)
            if len(str(i)) % 2 != 0:
                continue
            if (i // 10 ** (len(str(i)) // 2)) == (i % 10 ** (len(str(i)) // 2)):
                #print(f'invalid ID: {i}')
                invalid_id_sum += i
            #print(f'i = {i}, len(str(id)): {(i // 10 ** (len(str(i)) // 2)) == (i % 10 ** (len(str(i)) // 2))}')
    print(f'Invalid ID sum: {invalid_id_sum}')
    return(invalid_id_sum)

#first(part_a)


# Part B
def second(input):
    input = input[0].split(",")
    #print(input)

    invalid_id_sum = 0

    for id_set in input:
        # use as strings
        id1 = id_set.split('-')[0]
        id2 = id_set.split('-')[1]
        # check all IDs
        for i in range(int(id1), int(id2)+1):
            i_length = len(str(i))
            i_value = str(i)
            
            #print(f'I will check numbers: {i_value}')
            # check all numbers in range
            for pattern_length in range (1, (i_length//2)+1):
                #print(f'number {i_value} has {i_value.count(i_value[:pattern_length])} repeated pattern_lengths of {i_value[:pattern_length]}.', end=' ')
                #print(f'to invalidate, it must repeat this much: {i_length // pattern_length}')

                if (i_value.count(i_value[:pattern_length]) * i_value[:pattern_length] == i_value):
                    #print(f'Invalid number: {i_value}')
                    invalid_id_sum += int(i_value)
                    break
                

                # if (i_value.count(i_value[:pattern_length]) == i_length // pattern_length) and (i_length // pattern_length) != 1:
                #     invalid_id_sum += int(i_value)
                #     print(f'Invalid number: {i_value}')


    print(f'Invalid ID sum: {invalid_id_sum}')
    return(invalid_id_sum)


second(part_a)

