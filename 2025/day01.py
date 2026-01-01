from config import get_inputs, timer

# Get input data
inputs = get_inputs(__file__)


# Part A
@timer
def first(input):
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

        #print(f'rotated {turn}, points at {pointing_at}')       
    print(f"Part 1 '0' count: {zero_count}")


# Part B
def second(input):
    pointing_at = 50
    zero_count = 0

    for turn in input:
        previous = pointing_at
        # turn
        #print(f'Start at: {previous}', end= ' ')
        if turn.startswith("L"):
            pointing_at -= int(turn.lstrip("L"))
        else:
            pointing_at += int(turn.lstrip("R"))

        #print(f'rotated {turn} to {pointing_at}', end=' ')

        if previous == 0: zero_count -= 1

        if previous <= pointing_at:
            zero_count += max(0, (pointing_at // 100) - ((previous - 1) // 100))
            #print(f'[#{zero_count}]', end=' ')
        else:
            zero_count += max(0, (previous // 100) - ((pointing_at - 1) // 100))
            #print(f'[#{zero_count}]', end=' ')

        pointing_at %= 100

        #print(f'now pointing at: {pointing_at}')        
    print(f"Part 2 '0' count: {zero_count}")


# run tests
first(inputs["input"])
timed_second = timer(second) #Closure, not decorator
timed_second(inputs["input"]) #Closure, not decorator

