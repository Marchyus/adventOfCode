from config import *

# Read input file
inputs_file = os.path.join(inputs_path, 'day06.txt')
with open(inputs_file, 'r') as inputs:
    full_input = inputs.read()

# find index after any ammount of unique characters
def find_index_after_non_repeating(unique_char_count, full_input):
    index = unique_char_count - 1 # counting from 0
    for i in range(index, len(full_input)):
        unique_string = ''.join(full_input[i - index:i + 1])
        if len(set(unique_string)) == unique_char_count:
            return (i + 1) # return +1 because it's index of next character


# Part 1: find index after 4 unique characters
print(f"Index after 4 unique characters in a row: {find_index_after_non_repeating(4, full_input)}")
# Part 2: find index after 14 unique characters
print(f"Index after 14 unique characters in a row: {find_index_after_non_repeating(14, full_input)}")