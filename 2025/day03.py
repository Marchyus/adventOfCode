from config import get_inputs, timer

# Get input data
inputs = get_inputs(__file__)



# Part A
@timer
def first(banks):
    total_joltage = 0
    for bank in banks:
        #print(bank)
        #print(bank[:len(bank)-1])
        max1 = max(bank[:len(bank)-1])
        max1_index = bank.index(max1)
        #print("max1:", max1)
        #print(max1_index)
        max2 = max(bank[max1_index+1:])
        #print("max2:", max2)
        total_joltage += int(max1+max2)
        
    print(f"Total joltage: {total_joltage}")
    return total_joltage



# Part B
@timer
def second(banks):
    total_joltage = 0
    for bank in banks:
        bank_joltage = '' # string, cause input is string
        battery_count = 12
        #max_index = 0
        while battery_count > 0:

            largest = max(bank[0:len(bank)-battery_count+1])
            # print(f'I grab {bank[0:len(bank)-battery_count]} and max from it is {largest}', end=" ")
            
            bank_joltage += largest
            # print(f"append largest to bank_joltage: [{bank_joltage}]", end= ' ')
            
            bank = bank[bank.index(largest)+1:]
            # print(f"and trim bank to {bank}")



            battery_count -= 1

        total_joltage += int(bank_joltage)
        
        
    print(f"Total joltage: {total_joltage}")
    return total_joltage


# Run tests
first(inputs["input"])
second(inputs["input"])