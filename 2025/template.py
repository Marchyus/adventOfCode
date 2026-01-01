from config import get_inputs, timer

# Get input data
inputs = get_inputs(__file__)


# Part A
@timer
def first(input):
    print(input)



# Part B
@timer
def second(input):
    pass

# Run tests
first(inputs["input"])
# second(inputs["input"])

